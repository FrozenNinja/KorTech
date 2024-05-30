from .ping import ping


async def setup(bot):
    await bot.add_cog(Ping())
