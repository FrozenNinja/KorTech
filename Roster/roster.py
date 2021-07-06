import dataclasses
import discord
import asyncio
import sans
import io
import json
from sans.api import Api
from sans.errors import HTTPException, NotFound
from sans.utils import pretty_string
from redbot.core import checks, commands, Config
from redbot.core.utils.chat_formatting import pagify, escape, box
from lxml import etree as ET
from libneko import pag

class Roster(commands.Cog):

    def __init__(self, bot):
        Api.loop = bot.loop
        self.bot = bot
        self.delim = ', '
        self.config = Config.get_conf(self, identifier=31415926535)
        default_global = {
            "roster": set()
        }
        default_user = {
            "userwa": "Null",
            "name": "Null"
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)

    @commands.command()
    @commands.has_role("TITO Member")
    async def setwa(self, ctx, newnation):
        """Set WA of a member in the roster."""

        user = ctx.message.author
        
        #Checks that previous nation is no longer WA
        oldnation = await self.config.user(user).userwa()
        if oldnation == newnation:
            await ctx.send("This nation has already been recorded.")
        elif oldnation != "Null" and await self._isinwa(wanation=oldnation):
            await ctx.send("Make sure your old WA nation has successfully resigned.")
        else:
            # Only reach if old is null / not in WA
            #Checks that new nation is WA
            if await self._isinwa(wanation=newnation):
                #Saves new WA in Roster
                await self.config.user(user).userwa.set(newnation)
                await self.config.user(user).name.set(user.display_name)
                async with self.config.roster() as roster:
                    roster.add(user.id)
                await ctx.send("Your WA Nation has been set!")
            else:
                await ctx.send("Make sure Nation given is in the WA")
                
    @commands.command()
    async def removewa(self, ctx):
        user = ctx.message.author
        await self.config.user(user).clear()

    @commands.command()            
    async def checkwa(self, ctx):
        user = ctx.message.author
        
        #Lists current WA nation for self
        currentwa = await self.config.user(user).userwa()
        await ctx.send(currentwa)

    async def _roster_map(self):
        """Construct a name -> WA mapping of roster members."""
        return {
            (await self.config.user_from_id(user_id).name())
            : (await self.config.user_from_id(user_id).userwa()) 
            for user_id in (await self.config.roster())
        }
    
    @commands.command()
    @commands.has_role("KPCmd")
    async def roster(self, ctx):
        #Display current WA roster in flippable format

        tostring = json.dumps(self._roster_map(), sort_keys=True, indent=0)

        nav = pag.EmbedNavigatorFactory(max_lines=30, prefix="__**TITO Roster**__", enable_truncation=True)
        nav += tostring.strip('{}').replace('":',"\n").replace('",','\n').replace('"',"**").rstrip('\n').rstrip('*')

        nav.start(ctx)

    @commands.command()
    @commands.has_role("KPCmd")
    async def rawroster(self, ctx: commands.Context) -> None:
        """Output the roster in raw key-value format."""
        # rosteritems = "\n".join(f"{name}={wa}" for userid, (name, wa) in (await self.config.roster()).items())
        rosteritems = json.dumps(self._roster_map(), indent=4)
        await ctx.send("Roster", file=discord.File(io.BytesIO(rosteritems.encode("utf-8")), filename="roster.json"))

    @commands.command()
    @commands.has_role("KPCmd")
    async def clearroster(self, ctx: commands.Context) -> None:
        """Clear all data from the roster."""
        # Yes this wipes all config data for this Cog,
        # which should only be WA and roster list.
        await self.config.clear_all()
        await ctx.send("Roster cleared.")

    async def _isinwa(self, wanation: str) -> bool:
        """Check if Nation is in the WA"""
        Api.agent = "10000 Islands Discord Bot contact Kortexia"
        request = Api(
            "wa",
            nation=wanation,
        )
        root = await request
        pretty = pretty_string(root)
        return "wa" in pretty.lower()