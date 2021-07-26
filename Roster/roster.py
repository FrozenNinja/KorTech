"""Manage a WA roster."""

import asyncio
import io
import json
import typing as t

import discord
from libneko import pag
from redbot.core import commands, Config

import sans
from sans.api import Api
from sans.utils import pretty_string

# from lxml import etree as ET
# from redbot.core.utils.chat_formatting import pagify, escape, box
# from sans.errors import HTTPException, NotFound


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
        default_global = {"roster": {}}
        default_user = {"userwa": "Null", "name": "Null"}
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)

    @commands.command()
    @commands.has_role("TITO Member")
    async def setwa(self, ctx: commands.Context, newnation: str) -> None:
        """Set your WA in the roster."""

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
                roster[user.id] = True
            await ctx.send("Your WA Nation has been set!")

    @commands.command()
    @commands.has_role("TITO Member")
    async def removewa(self, ctx: commands.Context) -> None:
        """Remove your WA from the roster."""
        user = ctx.message.author
        await self.config.user(user).clear()
        async with self.config.roster() as roster:
            roster.pop(user.id, None)

    @commands.command()
    @commands.has_role("TITO Member")
    async def checkwa(self, ctx: commands.Context) -> None:
        """Check you WA in the roster."""
        user = ctx.message.author
        # Lists current WA nation for self
        currentwa = await self.config.user(user).userwa()
        await ctx.send(currentwa)

    async def _roster_map(self) -> t.Mapping[str, str]:
        """Construct a name -> WA mapping of roster members."""
        return {
            (await self.config.user_from_id(user_id).name())
            : (await self.config.user_from_id(user_id).userwa())
            for user_id in (await (self.config.roster())).keys()
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
        rosteritems = json.dumps(await self._roster_map(), indent=4)
        await ctx.send(
            "Roster",
            file=discord.File(
                io.BytesIO(rosteritems.encode("utf-8")), filename="roster.json"
            ),
        )

    @roster.command()
    async def clear(self, ctx: commands.Context) -> None:
        """Clear all data from the roster."""
        # Yes this wipes all config data for this Cog,
        # which should only be WA and roster list.
        timeout = 5
        await ctx.send(f"Confirmation required; type 'confirm' within {timeout} seconds.")
        try:
            await self.bot.wait_for(
                "message",
                check=(lambda msg: msg.channel == ctx.channel and msg.author == ctx.author and msg.content.strip().lower() == "confirm"),
                timeout=timeout
            )
            # checking for 'confirm' is done in the wait_for predicate
            # so at this point in code we can clear
            await self.config.clear_all()
            await ctx.send("Roster cleared.")
        except asyncio.TimeoutError:
            await ctx.send("Timeout passed, roster not cleared.")
       

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
            pretty = pretty_string(root)
            return "wa" in pretty.lower()
