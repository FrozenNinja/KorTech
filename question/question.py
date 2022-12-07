from redbot.core import commands
import time

class Question(commands.Cog):
    """Description of the cog visible with [p]help MyFirstCog"""

    @commands.command()
    async def question(self, ctx):
        """Counts down from 7"""
        i = 7
        while(i > 0):
            await ctx.send(i)
            time.sleep(1)
            i = i - 1
        await ctx.send("Answer Window closed")