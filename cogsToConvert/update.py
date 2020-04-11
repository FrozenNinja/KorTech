from discord.ext import commands
import discord
import os
from .utils import checks


class Update:
    """Written for Hame"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(administrator=True)
    async def update(self, ctx):
	
        await self.bot.say("All available <@&323631110997147659> type !here to report in for Update! :bell:")

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(administrator=True)
    async def updoot(self, ctx):
	
        await self.bot.say("Whurrr iss youu attt <@&323631110997147659> ??? UPDOOT!")


def setup(bot):
    bot.add_cog(Update(bot))