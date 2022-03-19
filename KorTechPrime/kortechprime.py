"""KorTechPrime"""

import discord
from redbot.core import commands
from redbot.core.config import Config


class KorTechPrime(commands.Cog):
    """10KI Cog to facilitate Update Management"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.updatetime = False

    @commands.command()
    async def isupdate(self, ctx: commands.Context, arg: str) -> None:
        """Designate whether its UpdateTime or not, please use Yes or No"""

        role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")

        if role_cmd not in ctx.author.roles:
            await ctx.send("You are not authorized to use this command.")
            return

        if arg.lower() == "yes":
            self.updatetime = True
            await ctx.send("Update is running!")
        elif arg.lower() == "no":
            self.updatetime = False
            await ctx.send("It's no longer time for Update")
        else:
            await ctx.send("Please answer Yes or No")

    @commands.command()
    async def imhere(self, ctx: commands.Context) -> None:
        """Mark that the user is present for update."""

        role_memb = discord.utils.get(ctx.guild.roles, name="TITO Member")
        role_ally = discord.utils.get(ctx.guild.roles, name="Allied Military")
        role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

        if self.updatetime:
            if (role_memb in ctx.author.roles) or (role_ally in ctx.author.roles):
                await ctx.author.add_roles(role_upd)
                emoji = "<:tito:351110740259897349>"
                await ctx.message.add_reaction(emoji)
            else:
                await ctx.send("You are not masked as TITO Member or Allied Military")
        else:
            await ctx.send("Try again when its time for Update!")

    @commands.command()
    async def nohere(self, ctx: commands.Context) -> None:
        """Mark that the user is not present for update."""

        role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

        await ctx.author.remove_roles(role_upd)
        emoji = "<:oof:549276828158918656>"
        await ctx.message.add_reaction(emoji)

    @commands.command()
    async def rampage(self, ctx: commands.Context) -> None:
        """Mark that update is finished."""

        guild = ctx.message.guild

        role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
        role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

        if role_cmd not in ctx.author.roles:
            await ctx.send("You are not authorized to use this command.")
            return

        for Member in guild.members:
            if role_upd not in Member.roles:
                continue

            try:
                await Member.remove_roles(role_upd)
            except discord.errors.Forbidden:
                await ctx.send(
                    "Failed to unmask - I don't have permissions to do that."
                )
            else:
                await ctx.send(f"{Member.mention}: Unmasked.")

    @commands.command()
    async def radio_silence(self, ctx: commands.Context) -> None:
        """Silence peeps."""

        guild = ctx.message.guild

        role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
        role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
        role_upd = discord.utils.get(ctx.guild.roles, name="Updating")

        if role_cmd not in ctx.author.roles:
            await ctx.send("You are not authorized to use this command.")
            return
        else:
            await ctx.send(
                "Radio Silence has been enacted, pay attention to posted orders"
            )

        for Member in guild.members:
            if role_upd not in Member.roles:
                continue

            try:
                await Member.add_roles(role_mute)
            except discord.errors.Forbidden:
                await ctx.send(
                    "Failed to unmask - I don't have permissions to do that."
                )

    @commands.command()
    async def silence_over(self, ctx: commands.Context) -> None:
        """Un-Silence peeps."""

        guild = ctx.message.guild

        role_cmd = discord.utils.get(ctx.guild.roles, name="KPCmd")
        role_mute = discord.utils.get(ctx.guild.roles, name="Muted")

        if role_cmd not in ctx.author.roles:
            await ctx.send("You are not authorized to use this command.")
            return
        else:
            await ctx.send(
                "Radio Silence has been disabled, resume normal conversation"
            )

        for Member in guild.members:
            if role_mute not in Member.roles:
                continue

            try:
                await Member.remove_roles(role_mute)
            except discord.errors.Forbidden:
                await ctx.send(
                    "Failed to unmask - I don't have permissions to do that."
                )
