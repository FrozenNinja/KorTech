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
        users = ctx.message.author
        self.nsapi = self.bot.get_cog('NSApi')
        
        #Checks that previous nation is no longer WA
        oldnation = await self.config.user(users).userwa()
        if oldnation != "Null":
            wa = await self._isinwa(wanation=oldnation)
            if "non-member" in wa.lower():
                #Checks that new nation is WA
                newwa = await self._isinwa(wanation=newnation)
                if "non-member" not in newwa.lower():
                    #Saves new WA in Roster
                    await self.config.user(users).userwa.set(newnation)
                    async with self.config.roster() as user:
                        user[users.display_name] = newnation
                        await ctx.send("Your WA Nation has been set!")
                else:
                    await ctx.send("Make sure Nation given is in the WA")
            else:
                await ctx.send("Make sure your old WA nation has successfully resigned")
        else:
            #Checks that new nation is WA
            newwa = await self._isinwa(wanation=newnation)
            if "non-member" not in newwa.lower():
                #Saves new WA in Roster
                await self.config.user(users).userwa.set(newnation)
                async with self.config.roster() as user:
                   user[users.display_name] = newnation
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

        rosterdict = await self.config.roster()
        tostring = json.dumps(rosterdict, sort_keys=True indent=0)

        nav = pag.EmbedNavigatorFactory(max_lines=16, prefix="__**TITO Roster**__", enable_truncation=True)
        nav += tostring.strip('{}').replace('":',"\n").replace('",','\n').replace('"',"**").rstrip('\n').rstrip('*')

        nav.start(ctx)

    async def _isinwa(self, wanation):
        """Check if Nation is in the WA"""
        Api.agent = "10000 Islands Discord Bot contact Kortexia"
        request = Api(
            "wa",
            nation=wanation,
        )
        root = await request
        pretty = pretty_string(root)
        return pretty