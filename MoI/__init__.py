# This init is required for each cog.
# Import your main class from the cog's folder.
from .moi import MoI


def setup(bot):
    bot.add_cog(MoI(bot))
