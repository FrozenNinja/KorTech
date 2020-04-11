import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class Insult:

    """Airenkun's Insult Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.insults = fileIO("data/insult/insults.json","load")

    @commands.command(pass_context=True, no_pm=True)
    async def insult(self, ctx, user : discord.Member=None):
        """Insult the user"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "GET YOUR OWN PUNS!"
                await self.bot.say(user.mention + msg)
            else:
                await self.bot.say(msg + randchoice(self.insults))
        else:
            await self.bot.say(msg + randchoice(self.insults))


def setup(bot):
    bot.add_cog(Insult(bot))
