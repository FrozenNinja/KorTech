import discord
import asyncio
import sans
from sans.api import Api
from sans.errors import HTTPException, NotFound
from sans.utils import pretty_string
from redbot.core import checks, commands, Config
from redbot.core.utils.chat_formatting import pagify, escape, box
from lxml import etree as ET

class Roster(commands.Cog):

    def __init__(self, bot):
        Api.loop = bot.loop
        self.bot = bot
        self.delim = ', '
        self.config = Config.get_conf(self, identifier=31415926535)
        self.config.register_global(
            roster ={}
        )
        self.config.register_user(
            userwa=""
        )

    @commands.command()
    async def setwa(self, ctx, newnation, user : discord.User=None):
        user = ctx.message.author
        self.nsapi = self.bot.get_cog('NSApi')
        self.nsapi.check_agent()
        
        #Checks that previous nation is no longer WA
        oldnation = await self.config.user.userwa()
        if oldnation != "":
            wa = await self._isinwa(wanation=oldnation)
            if "non-member" in wa.lower():
                #Checks that new nation is WA
                newwa = await self._isinwa(wanation=newnation)
                if "non-member" not in newwa.lower():
                    #Saves new WA in Roster
                    await self.config.user.userwa.set(newnation)
                else:
                    await ctx.send("Make sure Nation given is in the WA")
            else:
                await ctx.send("Make sure your old WA nation has successfully resigned")
        else:
            #Checks that new nation is WA
            newwa = await self._isinwa(wanation=newnation)
            if "non-member" not in newwa.lower():
                #Saves new WA in Roster
                await self.config.user.userwa.set(newnation)    
            else:
                await ctx.send("Make sure Nation given is in the WA")

    @commands.command()            
    async def checkwa(self, ctx, user : discord.User=None):
        user = ctx.message.author
        
        #Lists current WA nation for self
        currentwa = await self.config.user.userwa()
        await ctx.send(currentwa)
    
    #async def roster(self, ctx):
    
        #Display current WA roster in flippable format
        
    @commands.command()
    async def _isinwa(self, wanation):
        """Check if Nation is in the WA"""
        Api.agent = "Kortexia"
        request = Api(
            "wa",
            nation=wanation,
        )
        root = await request
        pretty = pretty_string(root)
        return pretty