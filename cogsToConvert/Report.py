import os

import sys
import aiofiles
import discord
import asyncio
from asyncio import Lock
from discord.ext import commands

from __main__ import send_cmd_help
from cogs.utils import checks

from .utils.dataIO import dataIO
from .utils.chat_formatting import box, pagify

class Report:

    def __init__(self, bot):
        self.bot = bot
        self.nsapi = None
        self.delim = ', '
        self.locks = {"_ne": Lock(), "_nne": Lock()}

    @commands.command(pass_context=True)
    async def report(self, ctx, user : discord.User=None):
        author = ctx.message.author

        #Mission Summary
        await self.bot.say("Mission Summary?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                summary = message.content
                break
            except:
                await self.bot.say("Stop breaking things, try again")

        #RaidLead
		await self.bot.say("Is the raid leader in the WA?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                if "yes" in message.content.lower():
				    await self.bot.say("Who was the raid lead?")
					    while True:
                                   try:
                                       message = await self.bot.wait_for_message(author=author, timeout=30)

                                       if message is None:
                                           return await self.bot.say("You took too long to reply.")

                                       raidlead = message.content
									   raidmembers = "N/A"
									   rleadcount = 0
                                       break
                                    except:
                                        await self.bot.say("Stop breaking things, try again")
                elif "no" in message.content.lower():
                    await self.bot.say("Who was the raid lead?")

                    while True:
                        try:
                            message = await self.bot.wait_for_message(author=author, timeout=30)

                            if message is None:
                                return await self.bot.say("You took too long to reply.")

                            answer = message.content

                            raidlead = answer
                            qraidmembers = self._ne(wanation=answer)
                            raidmembers = await qraidmembers
                            qrleadcount = self._nec(wanation=answer)
                            rleadcount = await qrleadcount
                            break
                        except:
                            await self.bot.say("Please make sure the nation is spelled correctly and is currently in the WA")
                else:
                    await self.bot.say("Please answer yes or no")
            except:
                await self.bot.say("Stop breaking the command, try again")

        #DefenderLead
        await self.bot.say("Who was the Defender lead?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                answer = message.content

                defenderlead = answer
                qdefendermembers = self._ne(wanation=answer)
                defendermembers = await qdefendermembers
                qdleadcount = self._nec(wanation=answer)
                dleadcount = await qdleadcount
                break
            except:
                await self.bot.say("Please make sure the nation is spelled correctly and is currently in the WA")

        #TITO Nations Count
        await self.bot.say("How many TITO Members were involved?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                membercount = float(message.content)
                break
            except ValueError:
                await self.bot.say("Please enter a number")

        #TITO Nations
        await self.bot.say("Which TITO Members were involved?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                members = message.content
                break
            except:
                await self.bot.say("How did you mess that up? Try again")

        #Coast Watching Eagle
        await self.bot.say("Did anybody earn a Coast Watching Eagle?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                if "no" in message.content.lower():
                    cwe = "No CWE"
                    break
                elif "yes" in message.content.lower():
                    await self.bot.say("Who earned the CWE?")
                    message = await self.bot.wait_for_message(author=author, timeout=30)

                    cwe = message.content

                    if cwe is None:
                        return await self.bot.say("You took too long to reply.")
                    break
                else:
                    await self.bot.say("Please answer yes or no")

            except:
                await self.bot.say("Idk how you messed that up, try again")

        #Finalization
        await self.bot.say("Mission Finalized?")

        while True:
            try:
                message = await self.bot.wait_for_message(author=author, timeout=30)

                if message is None:
                    return await self.bot.say("You took too long to reply.")

                if "yes" in message.content.lower():
                    final = "Final"
                    break
                elif "no" in message.content.lower():
                    final = ""
                    break
                else:
                    await self.bot.say("Please answer yes or no")
            except:
                await self.bot.say("Stop breaking the command, try again")

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
            await self.bot.say(finalmsg)
        except:
            await self.bot.say("An error occured, please try again")

    async def _ne(self, *, wanation):
        """Nations Endorsing the specified WA nation"""
        self.nsapi = self.bot.get_cog('NSApi')
        self.nsapi.check_agent()
        origne = (self._endocheck(await self.nsapi.api(
            "endorsements", "wa", nation=wanation))["endorsements"].replace(",", self.delim))
        ne = origne.replace("_", " ")
        return ne

    async def _nec(self, *, wanation):
        """Number of Nations Endorsing (Count) the specified WA nation"""
        self.nsapi = self.bot.get_cog('NSApi')
        self.nsapi.check_agent()
        nec = (self._endocheck(await self.nsapi.api(
            "censusscore-66", "wa", nation=wanation))["censusscore"]["text"])
        return nec

    async def _region_wa(self, region):
        rnations = await self.nsapi.api("nations", region=region)
        wamembers = set((await self.nsapi.api(
            "members", council="1"))["members"].split(","))
        return wamembers.intersection(rnations["nations"].split(":"))

    def _endocheck(self, data):
        if data["unstatus"] == "Non-member":
            raise commands.BadArgument("Nation {} is not in the WA.".format(
                data["id"]))
        return data


def check_folders():
    fol = "data/Report"
    if not os.path.exists(fol):
        print("Creating {} folder...".format(fol))
        os.makedirs(fol)


def setup(bot):
    check_folders()
    bot.add_cog(Report(bot))
