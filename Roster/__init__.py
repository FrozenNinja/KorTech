# This init is required for each cog.
# Import your main class from the cog's folder.
from .roster import Roster


async def setup(bot):
    await bot.add_cog(Roster(bot))
