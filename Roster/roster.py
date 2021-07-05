import dataclasses
import discord
import asyncio
import sans
import json
from sans.api import Api
from sans.errors import HTTPException, NotFound
from sans.utils import pretty_string
from redbot.core import checks, commands, Config
from redbot.core.utils.chat_formatting import pagify, escape, box
from lxml import etree as ET
from libneko import pag

@dataclasses.dataclass
class RosterEntry:
    """One entry of the roster."""

    name: str
    wa: str

class Roster(commands.Cog):

    def __init__(self, bot):
        Api.loop = bot.loop
        self.bot = bot
        self.delim = ', '
        self.config = Config.get_conf(self, identifier=31415926535)
        default_global = {
            "roster": {}
        }
        default_user = {
            "userwa": "Null"
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)

    @commands.command()
    @commands.has_role("TITO Member")
    async def setwa(self, ctx, newnation):
        """Set WA of a member in the roster."""

        user = ctx.message.author
        self.nsapi = self.bot.get_cog('NSApi')
        
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
                async with self.config.roster() as roster:
                    roster[user.id] = (user.display_name, newnation)
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
    
    @commands.command()
    @commands.has_role("KPCmd")
    async def roster(self, ctx):
        #Display current WA roster in flippable format

        rosterdict = {name: wa for name, wa in (await self.config.roster()).values()}
        tostring = json.dumps(rosterdict, sort_keys=True, indent=0)

        nav = pag.EmbedNavigatorFactory(max_lines=30, prefix="__**TITO Roster**__", enable_truncation=True)
        nav += tostring.strip('{}').replace('":',"\n").replace('",','\n').replace('"',"**").rstrip('\n').rstrip('*')

        nav.start(ctx)

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