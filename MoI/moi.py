"""KorTechPrime"""

import discord
from redbot.core import commands
from datetime import date

class MoI(commands.Cog):
    """10KI Cog for Minister of Immigration role management"""

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
        guild = ctx.message.guild
        role_monthlytop = discord.utils.get(ctx.guild.roles, name="Recruiter of the Month")

        for member in guild.members:
            if role_monthlytop in member.roles:
                try:
                    await member.remove_roles(role_monthlytop)
                except discord.Forbidden:
                    await ctx.send("I can't do that")
                    pass
        try:
            await user.add_roles(role_monthlytop)
            await ctx.send("Role succesfully swapped to new Monthly Top Recruiter")
        except discord.Forbidden:
            await ctx.send("I can't do that")
            pass
    
    @moi.command()
    async def topweek(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives Recruiter of the Week role and takes it from previous"""
        guild = ctx.message.guild
        role_weeklytop = discord.utils.get(ctx.guild.roles, name="Recruiter of the Week")

        for member in guild.members:
            if role_weeklytop in member.roles:
                try:
                    await member.remove_roles(role_weeklytop)
                except discord.Forbidden:
                    await ctx.send("I can't do that")
                    pass
        try:
            await user.add_roles(role_weeklytop)
            await ctx.send("Role succesfully swapped to new Weekly Top Recruiter")
        except discord.Forbidden:
            await ctx.send("I can't do that")
            pass

    @moi.command()
    async def tg2000(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 2000 Telegrams Sent Monthly! role"""
        role_2000tg = discord.utils.get(ctx.guild.roles, name="2000 Telegrams Sent Monthly!")

        try:
            await user.add_roles(role_2000tg)
            await ctx.send("2000 TG role given")
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg1000(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 1000 Telegrams Sent Monthly! role"""
        role_1000tg = discord.utils.get(ctx.guild.roles, name="1000 Telegrams Sent Monthly!")

        try:
            await user.add_roles(role_1000tg)
            await ctx.send("1000 TG role given")
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg500(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 500 Telegrams Sent Monthly! role"""
        role_500tg = discord.utils.get(ctx.guild.roles, name="500 Telegrams Sent Monthly!")

        try:
            await user.add_roles(role_500tg)
            await ctx.send("500 TG role given")
        except discord.Forbidden:
            pass

    @moi.command()
    async def tg250(
        self, ctx: commands.Context, user: discord.Member = None
    ) -> None:
        """Gives 250 Telegrams Sent Monthly! role"""
        role_250tg = discord.utils.get(ctx.guild.roles, name="250 Telegrams Sent Monthly!")

        try:
            await user.add_roles(role_250tg)
            await ctx.send("250 TG role given")
        except discord.Forbidden:
            pass

    @commands.command()
    @commands.admin()
    async def remove_monthly_roles(
        self, ctx: commands.Context
    ) -> None:
        """Removes all monthly roles from users"""
        guild = ctx.message.guild
        role_2000tg = discord.utils.get(ctx.guild.roles, name="2000 Telegrams Sent Monthly!")
        role_1000tg = discord.utils.get(ctx.guild.roles, name="1000 Telegrams Sent Monthly!")
        role_500tg = discord.utils.get(ctx.guild.roles, name="500 Telegrams Sent Monthly!")
        role_250tg = discord.utils.get(ctx.guild.roles, name="250 Telegrams Sent Monthly!")

        if date.today().day !=9:
            await ctx.send("Sketchy date thing works")
            return
        else:
            for member in guild.members:
                if role_2000tg in member.roles:
                    try:
                        await member.remove_roles(role_2000tg)
                    except discord.Forbidden:
                        await ctx.send("Error resetting roles")
                        pass
                if role_1000tg in member.roles:
                    try:
                        await member.remove_roles(role_1000tg)
                    except discord.Forbidden:
                        await ctx.send("Error resetting roles")
                        pass
                if role_500tg in member.roles:
                    try:
                        await member.remove_roles(role_500tg)
                    except discord.Forbidden:
                        await ctx.send("Error resetting roles")
                        pass
                if role_250tg in member.roles:
                    try:
                        await member.remove_roles(role_250tg)
                    except discord.Forbidden:
                        await ctx.send("Error resetting roles")
                        pass
            await ctx.send("All Monthly roles reset")