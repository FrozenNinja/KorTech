import sys
from .fifo import FIFO
# Applying fix from: https://github.com/Azure/azure-functions-python-worker/issues/640
# [Fix] Create a wrapper for importing imgres
from .date_trigger import *
from . import CustomDateTrigger
# [Fix] Register imgres into system modules
sys.modules["CustomDateTrigger"] = CustomDateTrigger

async def setup(bot):
    cog = FIFO(bot)
    bot.add_cog(cog)
    r = bot.add_cog(cog)
    if r is not None:
        await r
    await cog.initialize()


def teardown(bot):
    pass