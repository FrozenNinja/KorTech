import discord
import asyncio
from asyncio import Lock
import sans
from sans.api import Api
from sans.utils import pretty_string
from redbot.core import checks, commands
from redbot.core.utils.chat_formatting import pagify, escape, box

class Report(commands.Cog):

    @commands.command()
    async def startreport(self, ctx, user : discord.User=None):
        self.delim = ', '
        self.locks = {"_ne": Lock(), "_nne": Lock()}
        Api.agent = "Kortexia"

        #Mission Summary
        await ctx.send("Mission Summary?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                summary = message.content
                break
            except:
                await ctx.send("Stop breaking things, try again")
                break

        #RaidLead
        await ctx.send("Who was the raid lead?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                answer = message.content

                raidlead = answer
                qraidmembers = self._ne(wanation=answer)
                raidmembers = await qraidmembers
                qrleadcount = self._nec(wanation=answer)
                rleadcount = await qrleadcount
                break
            except:
                await ctx.send("Please make sure the nation is spelled correctly and is currently in the WA")
                break

        #DefenderLead
        await ctx.send("Who was the Defender lead?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                answer = message.content

                defenderlead = answer
                qdefendermembers = self._ne(wanation=answer)
                defendermembers = await qdefendermembers
                qdleadcount = self._nec(wanation=answer)
                dleadcount = await qdleadcount
                break
            except:
                await ctx.send("Please make sure the nation is spelled correctly and is currently in the WA")
                break

        #TITO Nations Count
        await ctx.send("How many TITO Members were involved?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                membercount = float(message.content)
                break
            except ValueError:
                await ctx.send("Please enter a number")
                break

        #TITO Nations
        await ctx.send("Which TITO Members were involved?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                members = message.content
                break
            except:
                await ctx.send("How did you mess that up? Try again")
                break

        #Coast Watching Eagle
        await ctx.send("Did anybody earn a Coast Watching Eagle?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                if "no" in message.content.lower():
                    cwe = "No CWE"
                    break
                elif "yes" in message.content.lower():
                    await ctx.send("Who earned the CWE?")
                    message = await client.wait_for(author=ctx.author, timeout=30)

                    cwe = message.content

                    if cwe is None:
                        return await ctx.send("You took too long to reply.")
                    break
                else:
                    await ctx.send("Please answer yes or no")

            except:
                await ctx.send("Idk how you messed that up, try again")
                break

        #Finalization
        await ctx.send("Mission Finalized?")

        while True:
            try:
                message = await client.wait_for(author=ctx.author, timeout=30)

                if message is None:
                    return await ctx.send("You took too long to reply.")

                if "yes" in message.content.lower():
                    final = "Final"
                    break
                elif "no" in message.content.lower():
                    final = ""
                    break
                else:
                    await ctx.send("Please answer yes or no")
            except:
                await ctx.send("Stop breaking the command, try again")
                break

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

    async def _ne(self, *, wanation: str):
        """Nations Endorsing the specified WA nation"""
        origne = (self._endocheck(await Api(
            "endorsements wa", nation=wanation))["endorsements"].replace(",", self.delim))
        ne = origne.replace("_", " ")
        return ne

    async def _nec(self, *, wanation: str):
        """Number of Nations Endorsing (Count) the specified WA nation"""
        nec = (self._endocheck(await Api("census wa", nation=wanation, scale="66", mode="score"))["censusscore"]["text"])
        return nec

    def _endocheck(self, data):
        if data["unstatus"] == "Non-member":
            raise commands.BadArgument("Nation {} is not in the WA.".format(data["id"]))
        return data