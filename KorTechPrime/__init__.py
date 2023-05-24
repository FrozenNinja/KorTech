# This init is required for each cog.
# Import your main class from the cog's folder.
from .kortechprime import KorTechPrime


async def setup(bot):
    await bot.add_cog(KorTechPrime(bot))
