# This init is required for each cog.
# Import your main class from the cog's folder.
from .tilapia import Tilapia


async def setup(bot):
    await bot.add_cog(Tilapia(bot))