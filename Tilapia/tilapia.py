import discord
from redbot.core import commands


class Tilapia(commands.Cog):
    """Tilapia"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        if message.channel.id == 748238663862845502:
            if ":tilapia:" not in message.content:
                await message.delete()
            elif "panda" in message.content:
                await message.delete()