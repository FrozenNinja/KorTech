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
        
    @commands.listener()
    async def on_message(self, message):
    
        #reply = "test"
    
        await ctx.send(message.content)
        #asyncio.sleep(10)