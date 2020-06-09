from redbot.core import commands
from redbot.core.utils.chat_formatting import box

try:
    from pyfiglet import figlet_format
except:
    figlet_format = None


class Ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ascii")
    async def _ascii(self, ctx: commands.Context, *, text):
        msg = str(figlet_format(text, font='cybermedium'))
        if msg[0] == " ":
            msg = "." + msg[1:]
        error = figlet_format('LOL, that\'s a bit too long.',
                              font='cybermedium')
        if len(msg) > 2000:
            await ctx.send(box(error))
        else:
            await ctx.send(box(msg))


def setup(bot):
    if figlet_format is None:
        raise NameError("You need to run `pip3 install pyfiglet`")
    n = Ascii(bot)
    bot.add_cog(n)
