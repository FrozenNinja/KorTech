import discord
from redbot.core import commands

class Newyearcheer(commands.Cog):
    """Duel replace"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def Newyearcheer(self, ctx: commands.Context, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        await ctx.send(author.mention + " *decides **not** to duel* " + user.mention + " but instead raises a mug of butter beer :beers: and wishes them a \n :sparkler: Happy New Year instead! :fireworks: ")
        
def setup(bot):
    bot.add_cog(Newyearcheer(bot))