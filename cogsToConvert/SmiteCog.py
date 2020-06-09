import discord
from redbot.core import commands
from redbot.core import checks


class SmiteCog(commands.Cog):
    """Written for Hame"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.command()
    @commands.guild_only()
    @checks.mod_or_permissions(manage_messages=True)
    async def smite(self, ctx: commands.Context, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        await ctx.send("*" + author.mention + "\n**SMITES**\n" + user.mention + "\nwith The Holy Power of Lord Klopstock!!!" + "*")

def setup(bot):
    bot.add_cog(SmiteCog(bot))