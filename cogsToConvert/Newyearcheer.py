import discord
from discord.ext import commands

class Newyearcheer:
    """Duel replace"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def Newyearcheer(self, ctx, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        await self.bot.say(author.mention + " *decides **not** to duel* " + user.mention + " but instead raises a mug of butter beer :beers: and wishes them a \n :sparkler: Happy New Year instead! :fireworks: ")
        
def setup(bot):
    bot.add_cog(Newyearcheer(bot))