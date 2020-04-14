# This init is required for each cog.
# Import your main class from the cog's folder.
from .report import Report


def setup(bot):
    bot.add_cog(Report())