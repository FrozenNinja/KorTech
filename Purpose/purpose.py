import discord
from redbot.core import commands
from redbot.core.config import Config


class Purpose(commands.Cog):
    """What is my purpose?"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def testthis(self, ctx):
        await ctx.send("test successful")
        
    @commands.Cog.listener()
	@commands.cooldown(1, 10, commands.BucketType.guild)
    async def on_command(self, ctx):

        await ctx.send("test")