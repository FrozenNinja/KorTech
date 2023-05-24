# This init is required for each cog.
# Import your main class from the cog's folder.
from .report import Report


async def setup(bot):
    await bot.add_cog(Report(bot))