import discord
import random
from redbot.core import commands
from redbot.core.config import Config


class Purpose(commands.Cog):
    """What is my purpose?"""

    def __init__(self, bot):
        self.bot = bot
        
    messages = 0

    @commands.Cog.listener()
    async def on_command(self, ctx):

        n = random.randint(2,5)
        
        if messages >= n:
            await ctx.send("test")
            global messages = 0
        else:
            global messages +=1