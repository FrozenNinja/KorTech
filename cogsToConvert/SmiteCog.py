import discord
from discord.ext import commands
from cogs.utils import checks


class SmiteCog:
    """Written for Hame"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions(manage_messages=True)
    async def smite(self, ctx, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        await self.bot.say("*" + author.mention + "\n**SMITES**\n" + user.mention + "\nwith The Holy Power of Lord Klopstock!!!" + "*")

def setup(bot):
    bot.add_cog(SmiteCog(bot))