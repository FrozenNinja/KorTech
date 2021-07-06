import discord
import random
from redbot.core import commands
from redbot.core.config import Config


class Tilapia(commands.Cog):
    """Tilapia"""

    def in_channel(channel_id)
    def predicate(ctx):
        return ctx.message.channel.id == channel_id
    return commands.check(predicate)

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @is_channel('748238663862845502')
    async def on_message_without_command(self, message):
 
        if ":tilapia:" not in message.content:
            await ctx.message.delete(message)