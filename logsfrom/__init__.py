from .logsfrom import LogsFrom


async def setup(bot):
    await bot.add_cog(LogsFrom())
