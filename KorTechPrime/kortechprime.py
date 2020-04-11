import discord
from redbot.core import commands
from redbot.core.config import Config


class KorTechPrime(commands.Cog):
    """10KI Cog to facilitate Update Management"""

    @commands.command()
    async def here(self, ctx: commands.Context):
                """Mark that the user is present for update."""

                guild = ctx.message.guild
                author = ctx.message.author

                role_memb = discord.utils.get(ctx.guild.roles, name="TITO Member")
                role_ally = discord.utils.get(ctx.guild.roles, name="Allied Military")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

                if role_memb or role_ally in ctx.author.roles:
                    await ctx.author.add_roles(role_upd)
                    emoji = '<:tito:351110740259897349>'
                    await message.add_reaction(emoji)
                else:
                        await ctx.send("You are not masked as TITO Member or Allied Military")