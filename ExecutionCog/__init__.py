from .executioncog import ExecutionCog


async def setup(bot):
    await bot.add_cog(ExecutionCog())
