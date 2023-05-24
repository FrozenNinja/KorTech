# This init is required for each cog.
# Import your main class from the cog's folder.
from .moi import MoI


async def setup(bot):
    await bot.add_cog(MoI(bot))
