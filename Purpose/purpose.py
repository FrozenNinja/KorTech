import discord
import random
from redbot.core import commands
from redbot.core.config import Config


class Purpose(commands.Cog):
    """What is my purpose?"""

    def __init__(self, bot):
        self.bot = bot
        self.messages = 0

    @commands.Cog.listener()
    async def on_message_without_command(self, message):

        n = random.randint(50,300)
 
        if self.messages >= n:
            await message.channel.send("Skynet was an amateur")
            self.messages = 0
        else:
            self.messages +=1