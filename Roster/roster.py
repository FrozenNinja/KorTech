"""Manage a WA roster."""

import asyncio
import enum
import io
import json
import typing as t

import discord
from libneko import pag
from redbot.core import commands, Config

import sans
from sans.api import Api

# from sans.utils import pretty_string

# from lxml import etree as ET
# from redbot.core.utils.chat_formatting import pagify, escape, box
# from sans.errors import HTTPException, NotFound

from . import deployed


def channel_and_author(ctx: commands.Context) -> t.Callable[[discord.Message], bool]:
    """Construct a predicate that checks author and channel to be same as context."""

    def pred(message: discord.Message) -> bool:
        return message.author == ctx.author and message.channel == ctx.channel

    return pred


class DModes(enum.Enum):
    """Modes that [p]deployed can run in."""

    FILE = "file"
    NO_FILE = "no-file"
    KNOWN = "known"
    PUPPETS = "puppets"
    UNKNOWN = "unknown"


class Roster(commands.Cog):
    """Roster Cog."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initiate this cog with the given bot."""
        self.bot = bot
        # Connect sans to bot async loop
        Api.loop = bot.loop

        self.delim = ", "

        # Setup config structure
        self.config = Config.get_conf(self, identifier=31415926535)
        # Roster is a mapping from id to True
        # Known is
        self.config.register_global(roster={}, known={})
        self.config.register_user(userwa="Null", name="Null")

    @commands.group()
    @commands.has_role("KPCmd")
    async def known(self, ctx: commands.Context) -> None:
        """Command group for managing a list of known puppets."""

    @known.command()
    async def upload(self, ctx: commands.Context) -> None:
        """Import the JSON file attached to this command,
        or wait for a file to be uploaded after the command is run.

        Interprets the file as a roster of known puppets;
        the JSON should be formatted as {name: [puppets]}
        The name is also interpreted as a puppet.
        """
        if len(ctx.message.attachments) > 0:
            file = ctx.message.attachments[0]
        else:
            RESPONSE_TIMEOUT = 10
            await ctx.send(
                f"Please send a roster JSON file within the next {RESPONSE_TIMEOUT} seconds."
            )
            try:
                message = await self.bot.wait_for(
                    "message", check=channel_and_author(ctx), timeout=RESPONSE_TIMEOUT
                )
            except asyncio.TimeoutError:
                await ctx.send("Timed out waiting for roster JSON file.")
                return
            else:
                if len(message.attachments) > 0:
                    file = message.attachments[0]
                else:
                    await ctx.send("No file attached, please rerun this command.")
                    return
        raw: bytes = await file.read()
        try:
            known = json.loads(raw)
        except json.JSONDecodeError:
            await ctx.send("Provided file is not well-formed JSON.")
        else:
            await self.config.known.set(known)
            await ctx.send("Known list updated.")

    @known.command()
    async def export(self, ctx: commands.Context, sort: bool = True) -> None:
        """Export known puppets as JSON."""
        known = json.dumps(await self.config.known(), indent=4, sort_keys=sort)
        await ctx.send(
            "Known",
            file=discord.File(io.BytesIO(known.encode("utf-8")), filename="known.json"),
        )

    async def _deployments(self, lead: str) -> deployed.Deployments:
        """Automatically use the known config to determine deployments."""
        deployments = await deployed.deployed_lists(
            lead=lead, roster=(await self.config.known())
        )
        return deployments

    @commands.command()
    @commands.has_role("KPCmd")
    async def deployed(
        self, ctx: commands.Context, lead: str, mode: str = "file"
    ) -> None:
        """Check who is deployed on a lead, according to loaded known file.

        Possible modes are [file, no-file, known, puppets, unknown].
        """
        MAX_MESSAGE_SIZE = 2000

        # Convert to Enum Mode
        try:
            dmode = DModes(mode)
        except ValueError:
            possible_modes = ", ".join(mode.value for mode in DModes)
            await ctx.send(f"Invalid mode {mode}. Valid modes are [{possible_modes}].")
        else:
            deployments = await self._deployments(lead)

            # Most modes don't have a file
            outfile: t.Optional[discord.File] = None
            message: str = ""

            if dmode is DModes.FILE or dmode is DModes.NO_FILE:
                # Generate content
                content = "Known: {known}\nKnown Puppets: {puppets}\nUnknown: {unknown}".format(
                    known=", ".join(deployments.known),
                    puppets=", ".join(deployments.puppets),
                    unknown=", ".join(deployments.unknown),
                )
                message = f"Deployed on {lead}:"
                if dmode is DModes.FILE:
                    outfile = discord.File(
                        io.BytesIO(content.encode("utf-8")),
                        filename=f"deployed_{deployed.clean_format(lead)}.txt",
                    )
                else:
                    message += "\n" + content.join(("```", "```"))
                    outfile = None
            elif dmode is DModes.KNOWN:
                message = ", ".join(deployments.known)
            elif dmode is DModes.PUPPETS:
                message = ", ".join(deployments.puppets)
            elif dmode is DModes.UNKNOWN:
                message = ", ".join(deployments.unknown)
            else:
                message = f"Mode {dmode} currently unsupported."

            # We cannot send an empty message
            if not message:
                message = "None"
            # Also can't send too big of a message
            elif len(message) > MAX_MESSAGE_SIZE:
                message = "Body too large to send, use `file` mode."

            await ctx.send(message, file=outfile)

    @commands.command()
    @commands.has_role("TITO Member")
    async def setwa(
        self, ctx: commands.Context, newnation: str, user: discord.Member = None
    ) -> None:
        """Set your WA in the roster."""

        # Command can use setwa on other members
        if not (user and discord.utils.get(ctx.author.roles, name="KPCmd")):
            user = ctx.message.author

        # Checks that previous nation is no longer WA
        oldnation = await self.config.user(user).userwa()
        if oldnation == newnation:
            await ctx.send("This nation has already been recorded.")
        elif oldnation != "Null" and await self._isinwa(wanation=oldnation):
            await ctx.send("Make sure your old WA nation has successfully resigned.")
        # Only reach if old is null / not in WA
        # Checks that new nation is WA
        elif not await self._isinwa(wanation=newnation):
            await ctx.send(f"Nation '{newnation}' is not in the WA.")
        else:
            # Saves new WA in Roster
            await self.config.user(user).userwa.set(newnation)
            await self.config.user(user).name.set(user.display_name)
            async with self.config.roster() as roster:
                roster[str(user.id)] = True
            await ctx.send("Your WA Nation has been set!")

    @commands.command()
    @commands.has_role("TITO Member")
    async def removewa(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Remove your WA from the roster."""
        # Command can use removewa on other members
        if not (user and discord.utils.get(ctx.author.roles, name="KPCmd")):
            user = ctx.message.author
        await self.config.user(user).clear()
        async with self.config.roster() as roster:
            # config mappings use string keys
            roster.pop(str(user.id), None)
        await ctx.send("Your WA Nation has been removed.")

    @commands.command()
    @commands.has_role("TITO Member")
    async def checkwa(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """Check you WA in the roster."""
        # Command can use checkwa on other members
        if not (user and discord.utils.get(ctx.author.roles, name="KPCmd")):
            user = ctx.message.author
        # Lists current WA nation for self
        currentwa = await self.config.user(user).userwa()
        await ctx.send(currentwa)

    async def _roster_map(self) -> t.Mapping[str, str]:
        """Construct a name -> WA mapping of roster members."""
        return {
            (await self.config.user_from_id(user_id).name()): (
                await self.config.user_from_id(user_id).userwa()
            )
            for user_id in map(int, (await (self.config.roster())).keys())
        }

    @commands.group()
    @commands.has_role("KPCmd")
    async def roster(self, ctx: commands.Context) -> None:
        """Roster related command group."""

    @roster.command()
    async def show(self, ctx: commands.Context) -> None:
        """Display current WA roster in flippable format."""

        rosterdict = await self._roster_map()
        if rosterdict:
            tostring = json.dumps(rosterdict, sort_keys=True, indent=0)

            nav = pag.EmbedNavigatorFactory(
                max_lines=30, prefix="__**TITO Roster**__", enable_truncation=True
            )
            nav += (
                tostring.strip("{}")
                .replace('":', "\n")
                .replace('",', "\n")
                .replace('"', "**")
                .rstrip("\n")
                .rstrip("*")
            )

            nav.start(ctx)
        else:
            await ctx.send("Roster is empty.")

    @roster.command()
    async def raw(self, ctx: commands.Context) -> None:
        """Output the roster in raw key-value format."""
        rosteritems = json.dumps(await self._roster_map(), indent=4, sort_keys=True)
        await ctx.send(
            "Roster",
            file=discord.File(
                io.BytesIO(rosteritems.encode("utf-8")), filename="roster.json"
            ),
        )

    @roster.command()
    async def clear(self, ctx: commands.Context) -> None:
        """Clear all data from the roster."""
        timeout = 5
        await ctx.send(
            f"Confirmation required; type 'confirm' within {timeout} seconds."
        )
        try:
            await self.bot.wait_for(
                "message",
                check=(
                    lambda msg: msg.channel == ctx.channel
                    and msg.author == ctx.author
                    and msg.content.strip().lower() == "confirm"
                ),
                timeout=timeout,
            )
        except asyncio.TimeoutError:
            await ctx.send("Timeout passed, roster not cleared.")
        else:
            # checking for 'confirm' is done in the wait_for predicate
            # so at this point in code we can clear
            # we only clear the roster and user data,
            # we don't want to clear the known data
            await self.config.roster.clear()
            await self.config.clear_all_users()
            await ctx.send("Roster list and user WAs cleared.")

    async def _isinwa(self, wanation: str) -> bool:
        """Check if Nation is in the WA"""
        Api.agent = "10000 Islands Discord Bot contact Kortexia"
        request = Api(
            "wa",
            nation=wanation,
        )
        try:
            root = await request
        except sans.errors.HTTPException:
            return False
        else:
            # pretty = pretty_string(root)
            wa_status: str = root["UNSTATUS"].text
            # logging.info(wa_status)
            return "wa" in wa_status.lower()
