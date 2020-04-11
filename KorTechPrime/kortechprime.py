import discord
from redbot.core import commands
from redbot.core.config import Config


class KorTechPrime(commands.Cog):
    """10KI Cog to facilitate Update Management"""

    @commands.command()
    async def im_here(self, ctx: commands.Context):
                """Mark that the user is present for update."""

                guild = ctx.message.guild
                author = ctx.message.author

                role_memb = discord.utils.get(ctx.guild.roles, name="TITO Member")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

                if role_memb not in ctx.author.roles:
                        await ctx.send("You are not masked as a TITO Member")
                        return

                try:
                        await ctx.author.add_roles(role_upd)
                except discord.errors.Forbidden as err:
                        await ctx.send("I don't have permissions to mark you, {}: {}.".format(author.mention, err))
                except AttributeError:  # role_to_add is NoneType
                        await ctx.send("That role isn't user settable, {}.".format(author.mention))
                else:
                        await ctx.send("Marked {} as present for this update.".format(author.mention))