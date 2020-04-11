import discord
from discord.ext import commands

class Slap:
    """Slaps a user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def slap(self, ctx, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        await self.bot.say(author.mention + " *slaps* " + user.mention)
        
def setup(bot):
    bot.add_cog(Slap(bot))