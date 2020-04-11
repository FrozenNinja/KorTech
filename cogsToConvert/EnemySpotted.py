import discord
from discord.ext import commands
from discord.utils import get
from .utils import checks


class EnemySpotted:
    """Assign Traitor"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions(administrator=True)
    async def enemyspotted(self, ctx, user: discord.Member):

        author = ctx.message.author
        role = get(user.server.roles, name="Enemy Faction")
        await self.bot.add_roles(user, role)
        await self.bot.say("*An enemy has been spotted!*")
	
def setup(bot):
    bot.add_cog(EnemySpotted(bot))
