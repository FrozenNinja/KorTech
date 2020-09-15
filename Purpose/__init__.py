# This init is required for each cog.
# Import your main class from the cog's folder.
from .purpose import Purpose


def setup(bot):
    bot.add_cog(Purpose(bot))
