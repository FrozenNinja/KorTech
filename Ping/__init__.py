from .ping import Ping


async def setup(bot):
    await bot.add_cog(Ping())
