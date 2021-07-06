import discord
from redbot.core import commands


class Tilapia(commands.Cog):
    """Tilapia"""

    def is_channel():
        def predicate(ctx):
            return ctx.message.channel.id == 748244385858322432
        return commands.check(predicate)

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @is_channel()
    async def on_message(message):
        if ":tilapia:" not in message.content:
            await ctx.message.delete()