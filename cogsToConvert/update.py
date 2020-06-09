import discord
import os
from redbot.core import commands
from redbot.core import checks


class Update(commands.Cog):
    """Written for Hame"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def update(self, ctx: commands.Context):
	
        await ctx.send("All available <@&323631110997147659> type !here to report in for Update! :bell:")

    @commands.command()
    @commands.guild_only()
    @checks.admin_or_permissions(administrator=True)
    async def updoot(self, ctx: commands.Context):
	
        await ctx.send("Whurrr iss youu attt <@&323631110997147659> ??? UPDOOT!")


def setup(bot):
    bot.add_cog(Update(bot))