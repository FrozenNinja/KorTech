import discord
from redbot.core import commands

class Cig(commands.Cog):
    """Cigarette leaving"""

    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def cig(self, ctx: commands.Context):
	
        author = ctx.message.author	
        #Text
        await ctx.send(author.mention + " **has left for a cigarette :smoking:**")
        
def setup(bot):
    bot.add_cog(Cig(bot))