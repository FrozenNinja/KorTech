import discord
import asyncio
from asyncio import Lock
import sans
from sans.api import Api
from sans.errors import HTTPException, NotFound
from sans.utils import pretty_string
from redbot.core import checks, commands, Config
from redbot.core.utils.chat_formatting import pagify, escape, box

class Report(commands.Cog):

    def __init__(self, bot):
        Api.loop = bot.loop
        self.bot = bot
        self.delim = ', '
        self.locks = {"_ne": Lock(), "_nne": Lock()}

    @commands.command()
    async def startreport(self, ctx, user : discord.User=None):
        #Mission Summary
        await ctx.send("Mission Summary?")
        summary = ""

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                summary = message.content
                break
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")
            except:
                await ctx.send("Stop breaking things, try again")

        #RaidLead
        await ctx.send("Who was the raid lead?")
        raidlead = ""
        rleadcount = 0
        raidmembers = ""

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                answer = message.content
                raidlead = answer
                qraidmembers = self._ne(wanation=answer)
                raidmembers = await qraidmembers
                qrleadcount = self._nec(wanation=answer)
                rleadcount = await qrleadcount
                break
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")
            except:
                await ctx.send("Please make sure the nation is spelled correctly and is currently in the WA")

        #DefenderLead
        await ctx.send("Who was the Defender lead?")
        defenderlead = ""
        dleadcount = 0
        defendermembers = ""

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                answer = message.content
                defenderlead = answer
                qdefendermembers = self._ne(wanation=answer)
                defendermembers = await qdefendermembers
                qdleadcount = self._nec(wanation=answer)
                dleadcount = await qdleadcount
                break
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")
            except:
                await ctx.send("Please make sure the nation is spelled correctly and is currently in the WA")

        #TITO Nations Count
        await ctx.send("How many TITO Members were involved?")
        membercount = 0

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                membercount = float(message.content)
                break
            except ValueError:
                await ctx.send("Please enter a number")

        #TITO Nations
        await ctx.send("Which TITO Members were involved?")

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                members = message.content
                break
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")
            except:
                await ctx.send("How did you mess that up? Try again")

        #Coast Watching Eagle
        await ctx.send("Did anybody earn a Coast Watching Eagle?")

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                if "no" in message.content.lower():
                    cwe = "No CWE"
                    break
                elif "yes" in message.content.lower():
                    await ctx.send("Who earned the CWE?")
                    while True:
                        try:
                            message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                            cwe = message.content
                            break

                        except asyncio.TimeoutError:
                            return await ctx.send("You took too long to reply.")

                else:
                    await ctx.send("Please answer yes or no")

            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")
            except:
                await ctx.send("Idk how you messed that up, try again")

        #Finalization
        await ctx.send("Mission Finalized?")

        while True:
            try:
                message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)

                if "yes" in message.content.lower():
                    final = "Final"
                    break
                elif "no" in message.content.lower():
                    final = ""
                    break
                else:
                    await ctx.send("Please answer yes or no")
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")
            except:
                await ctx.send("Stop breaking the command, try again")

        finalmsg = """{}

INVADER lead: [font color="#e61919"]{}[/font]
Endorsements Received: {} -- {}

DEFENDER lead: [font color="#00ff00"]{}[/font]
Endorsements Received: {} -- {}

[hr]TITO nations involved: {}
[font color="#ff9900"]{}[/font]

[font color="#ffff00"]{}[/font]

[font color="aqua"]{}[/font]""".format(summary, raidlead, int(float(rleadcount)), raidmembers, defenderlead, int(float(dleadcount)), defendermembers, int(membercount), members, cwe, final)

        try:
            await ctx.send(finalmsg)
        except:
            await ctx.send("An error occured, please try again")

    async def _ne(self, ctx, *, wanation):
        """Nations Endorsing the specified WA nation"""
        Api.agent = "Kortexia"
        root = await Api("wa", nation=wanation)
        if root.UNSTATUS.pyval.lower() == "non-member":
            return ctx.send("bleh")
        origne = await Api("endorsements wa", nation=wanation)["endorsements"].replace(",", self.delim)
        ne = origne.replace("_", " ")
        return ne

    async def _nec(self, ctx, *, wanation):
        """Number of Nations Endorsing (Count) the specified WA nation"""
        Api.agent = "Kortexia"
        root = await Api("wa", nation=wanation)
        if root.UNSTATUS.pyval.lower() == "non-member":
            return False
        nec = await Api("census wa", nation=wanation, scale="66", mode="score")["censusscore"]["text"]
        return nec