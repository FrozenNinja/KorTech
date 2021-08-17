import discord
from redbot.core import commands


class Tilapia(commands.Cog):
    """Tilapia"""

    def __init__(self, bot):
        self.bot = bot

    async def filter_message(self, message: discord.Message) -> bool:
        """Filter the given message based on channel and content.

        May delete the message depending on message content,
        and returns True if and only if the message was deleted.

        Specifically, if the message is in the tilapia channel
        and either does not have :tilapia: in it
        or does have panda in it,
        the message is deleted.
        """
        if message.channel.id == 748238663862845502:
            if ":tilapia:" not in message.content or "panda" in message.content:
                await message.delete()
                return True
        return False

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        await self.filter_message(message)

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        """Handle message edit.

        May not be called by discord.py
        if the edited message was not in cache,
        but usually edited messages are recent messages,
        which should be in the cache.
        """
        await self.filter_message(after)
