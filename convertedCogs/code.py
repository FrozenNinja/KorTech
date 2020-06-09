import discord
from redbot.core.utils.chat_formatting import box

from redbot.core import commands

class Code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=["language", "lng"])
    async def code(self, ctx: commands.Context, language, *, msg):
        """Makes your text in a codeblock in a certain language"""
        await ctx.send(box(msg, language))

def setup(bot):
    bot.add_cog(Code(bot))
