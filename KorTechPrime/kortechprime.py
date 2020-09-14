import discord
from redbot.core import commands
from redbot.core.config import Config


class KorTechPrime(commands.Cog):
    """10KI Cog to facilitate Update Management"""

    global updatetime
    updatetime = False

    @commands.command()
    async def updatetime(self, ctx, arg):
                """Designate whether its UpdateTime or not, please use Yes or No"""

                if arg.lower() == "yes":
                   updatetime = True
                elif arg.lower() == "no":
                   updatetime = False
                else:
                    await ctx.send("Please answer Yes or No")

    @commands.command()
    async def imhere(self, ctx: commands.Context):
                """Mark that the user is present for update."""

                guild = ctx.message.guild
                author = ctx.message.author

                role_memb = discord.utils.get(ctx.guild.roles, name="TITO Member")
                role_ally = discord.utils.get(ctx.guild.roles, name="Allied Military")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

                if updatetime == True:
                    if (role_memb in ctx.author.roles) or (role_ally in ctx.author.roles):
                        await ctx.author.add_roles(role_upd)
                        emoji = '<:tito:351110740259897349>'
                        await ctx.message.add_reaction(emoji)
                    else:
                        await ctx.send("You are not masked as TITO Member or Allied Military")
                else:
                    await ctx.send("Try again when its time for Update!")

    @commands.command()
    async def nohere(self, ctx: commands.Context):
                """Mark that the user is not present for update."""

                guild = ctx.message.guild
                author = ctx.message.author

                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

                await ctx.author.remove_roles(role_upd)
                emoji = '<:oof:549276828158918656>'
                await ctx.message.add_reaction(emoji)

    @commands.command()
    async def rampage(self, ctx: commands.Context):
                """Mark that update is finished."""

                guild = ctx.message.guild

                role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")
				
                if not role_cmd in ctx.author.roles:
                        await ctx.send("Not authorized to use this command.")
                        return

                for Member in guild.members:
                        if not role_upd in Member.roles:
                                continue

                        try:
                                await Member.remove_roles(role_upd)
                        except discord.errors.Forbidden:
                                await ctx.send("Failed to unmask - I don't have permissions to do that.")
                        else:
                                await ctx.send("%s: Unmasked." % Member.mention)

    @commands.command()
    async def radio_silence(self, ctx: commands.Context):
                """Silence peeps."""

                guild = ctx.message.guild

                role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
                role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")
				
                if not role_cmd in ctx.author.roles:
                        await ctx.send("Not authorized to use this command.")
                        return

                for Member in guild.members:
                        if not role_upd in Member.roles:
                                continue

                        try:
                                await Member.add_roles(role_mute)
                        except discord.errors.Forbidden:
                                await ctx.send("Failed to unmask - I don't have permissions to do that.")
                        else:
                                await ctx.send("%s: Muted." % Member.mention)

    @commands.command()
    async def silence_over(self, ctx: commands.Context):
                """Un-Silence peeps."""

                guild = ctx.message.guild

                role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
                role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
                role_upd = discord.utils.get(ctx.guild.roles, name="Updating")
				
                if not role_cmd in ctx.author.roles:
                        await ctx.send("Not authorized to use this command.")
                        return

                for Member in guild.members:
                        if not role_mute in Member.roles:
                                continue

                        try:
                                await Member.remove_roles(role_mute)
                        except discord.errors.Forbidden:
                                await ctx.send("Failed to unmask - I don't have permissions to do that.")
                        else:
                                await ctx.send("%s: Unmuted." % Member.mention)