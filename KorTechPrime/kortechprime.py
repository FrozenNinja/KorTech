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

                if (role_memb in ctx.author.roles) or (role_ally in ctx.author.roles):
                    await ctx.author.add_roles(role_upd)
                    emoji = '<:tito:351110740259897349>'
                    await ctx.message.add_reaction(emoji)
                else:
                        await ctx.send("You are not masked as TITO Member or Allied Military")

    @commands.command()
    async def not_here(self, ctx: commands.Context):
                """Mark that the user is not present for update."""

                guild = ctx.message.guild
                author = ctx.message.author

                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

                await ctx.author.remove_roles(role_upd)
                emoji = '<:oof:549276828158918656>'
                await ctx.message.add_reaction(emoji)

    @commands.command()
    async def update_over(self, ctx: commands.Context):
                """Mark that update is finished."""

                guild = ctx.message.guild

                role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
                role_memb = discord.utils.get(ctx.guild.roles, name="TITO Member")
                role_ally = discord.utils.get(ctx.guild.roles, name="Allied Military")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")
				
                if not role_cmd in ctx.author.roles:
                        await ctx.send("Not authorized to use this command.")
                        return

                for member in guild.members:
                        if not role_upd in member.roles:
                                continue

                        try:
                                await ctx.member.remove_roles(role_upd)
                        except discord.errors.Forbidden:
                                await ctx.send("%s: Failed to unmask - I don't have permissions to do that." % ctx.member.name)
                        except AttributeError:  # role_to_add is NoneType
                                await ctx.send("%s: Failed to unmask - That role isn't user settable." % ctx.member.name)
                        else:
                                await ctx.send("%s: Unmasked." % ctx.member.mention)