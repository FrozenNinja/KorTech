import discord
from redbot.core import commands

class Slap(commands.Cog):
    """Slaps a user"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx: commands.Context, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        await ctx.send(author.mention + " *slaps* " + user.mention)
        
def setup(bot):
    bot.add_cog(Slap(bot))