# This init is required for each cog.
# Import your main class from the cog's folder.
from .tilapia import Tilapia


def setup(bot):
    bot.add_cog(Tilapia(bot))