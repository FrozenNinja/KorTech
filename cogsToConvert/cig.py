import discord
from discord.ext import commands

class Cig:
    """Cigarette leaving"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def cig(self, ctx):
	
        author = ctx.message.author	
        #Text
        await self.bot.say(author.mention + " **has left for a cigarette :smoking:**")
        
def setup(bot):
    bot.add_cog(Cig(bot))