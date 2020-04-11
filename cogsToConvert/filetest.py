import discord
import pathlib
import os
from discord.ext import commands

class filetest:
    def __init__(self, bot):
        self.bot = bot
#Code written by Kortexia for Lynxi

    @commands.command(pass_context=True, no_pm=True)
    async def test(self, ctx, *arg):
        list = os.listdir("data/filetest")
        formatted = [s.replace('.txt', '') for s in list]

        if len(arg) != 0:
            if pathlib.Path(r'data/filetest/{}.txt'.format(*arg)).exists():
                await self.bot.send_file(ctx.message.channel, r"data/filetest/{}.txt".format(*arg))
            else:
                await self.bot.say("**Select a Spellbook by using \">spellbook [filename]\"**\n")
                await self.bot.say('\n'.join(formatted))
        else:
            await self.bot.say("**Select a Spellbook by using \">spellbook [filename]\"**\n")
            await self.bot.say('\n'.join(formatted))

def setup(bot):
    bot.add_cog(filetest(bot))