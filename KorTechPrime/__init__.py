# This init is required for each cog.
# Import your main class from the cog's folder.
from .kortechprime import KorTechPrime


def setup(bot):
    bot.add_cog(KorTechPrime())