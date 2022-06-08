"""KorTechPrime"""

import discord
from redbot.core import commands


class MoI(commands.Cog):
    """10KI Cog for Minister of Immigration role management"""
        guild = ctx.message.guild

        role_monthlytop = discord.utils.get(ctx.guild.roles, name="Recruiter of the Month")
        role_weeklytop = discord.utils.get(ctx.guild.roles, name="Recruiter of the Week")
        role_2000tg = discord.utils.get(ctx.guild.roles, name="2000 Telegrams Sent Monthly!")
        role_1000tg = discord.utils.get(ctx.guild.roles, name="1000 Telegrams Sent Monthly!")
        role_500tg = discord.utils.get(ctx.guild.roles, name="500 Telegrams Sent Monthly!")
        role_250tg = discord.utils.get(ctx.guild.roles, name="250 Telegrams Sent Monthly!")

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group()
    @commands.has_role("MoI")
    async def moi(
        self, ctx: commands.Context) -> None:
        """Command group for MoI Role Management"""

    @moi.command()
    async def topmonth(
        self, ctx: commands.Context, user: discord.Member = None
        ) -> None:
        """Gives Recruiter of the Month role and takes it from previous"""
        for member in guild.members:
            try:
                await member.remove_roles(role_monthlytop)
            except discord.Forbidden:
                pass
        try:
            await user.add_roles(role_monthlytop)
        except discord.Forbidden:
            pass
    
    @moi.command()
    async def topweek(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives Recruiter of the Week role and takes it from previous"""
        for member in guild.members:
            try:
                await member.remove_roles(role_weeklytop)
            except discord.Forbidden:
                pass
        try:
            await user.add_roles(role_weeklytop)
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg2000(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 2000 Telegrams Sent Monthly! role"""
        try:
            await user.add_roles(role_2000tg)
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg1000(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 1000 Telegrams Sent Monthly! role"""
        try:
            await user.add_roles(role_1000tg)
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg500(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 500 Telegrams Sent Monthly! role"""
        try:
            await user.add_roles(role_500tg)
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg250(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 250 Telegrams Sent Monthly! role"""
        try:
            await user.add_roles(role_250tg)
        except discord.Forbidden:
            pass

    @commands.command()
    @commands.admin()
    async def remove_monthly_role(
        self, ctx: commands.Context
    ) -> None:
        """Removes all monthly roles from users"""
        for member in guild.members:
            try:
                await member.remove_roles(role_2000tg)
                await member.remove_roles(role_1000tg)
                await member.remove_roles(role_500tg)
                await member.remove_roles(role_250tg)
            except discord.Forbidden:
                pass