import discord
from discord.ext import commands
from cogs.utils import checks
import re
import os
from .utils.dataIO import dataIO

try:
    import pycountry
except:
    pycountry = None

class CountryCode:
    def __init__(self, bot):
        self.countries = dataIO.load_json("data/countrycode/countries.json")
        self.subregions = dataIO.load_json("data/countrycode/subregions.json")
        self.bot = bot
        


    @commands.command(pass_context=True, no_pm=True)
    async def addcountry(self, ctx, country: str):
        """Example: [p]addcountry GB"""
        server = ctx.message.server
        user = ctx.message.author

        re1 = '((?:[a-z][a-z]+))'  # Word 1
        re2 = '.*?'  # Non-greedy match on filler
        re3 = '((?:[a-z][a-z]+))'  # Word 2
        rg = re.compile(re1 + re2 + re3, re.IGNORECASE | re.DOTALL)

        m = rg.search(country)
        if(country.upper() == 'NA'):
            country = 'US'
        subregionobj = None
        try:
            if m:
                word1 = m.group(1)
                countryobj = pycountry.countries.get(alpha_2=word1.upper())
                subregionobj = pycountry.subdivisions.get(code=country.upper())
            else:
                countryobj = pycountry.countries.get(alpha_2=country.upper())
        except:
            countryobj= None

        if countryobj is not None:
            #try:
            if subregionobj is not None:
                try:
                    if user.id not in self.subregions[subregionobj.code]:
                        self.subregions[subregionobj.code][user.id] = {}
                        await self.bot.say(
                            "Greetings from " + countryobj.name + ": " + subregionobj.name + " :flag_" + countryobj.alpha_2.lower() + ": by " + user.mention)
                        dataIO.save_json("data/countrycode/subregions.json", self.subregions)
                    else:
                        await self.bot.say("You already set your countryorigin to that country!")
                except KeyError:
                    self.subregions[subregionobj.code] = {}
                    self.subregions[subregionobj.code][user.id] = {}
                    await self.bot.say(
                            "Greetings from " + countryobj.name + ": " + subregionobj.name + " :flag_" + countryobj.alpha_2.lower() + ": by " + user.mention)
                    dataIO.save_json("data/countrycode/subregions.json", self.subregions)
            else:
                try:
                    if user.id not in self.countries[countryobj.name]:
                        self.countries[countryobj.name][user.id] = {}
                        await self.bot.say(
                            "Greetings from " + countryobj.name + " :flag_" + countryobj.alpha_2.lower() + ": by " + user.mention)
                        dataIO.save_json("data/countrycode/countries.json", self.countries)
                    else:
                        await self.bot.say("You already set your countryorigin to that country!")
                except KeyError:
                    self.countries[countryobj.name] = {}
                    self.countries[countryobj.name][user.id] = {}
                    await self.bot.say(
                            "Greetings from " + countryobj.name + " :flag_" + countryobj.alpha_2.lower() + ": by " + user.mention)
                    dataIO.save_json("data/countrycode/countries.json", self.countries)
            #except AttributeError:
                #await self.bot.say("w00ps, something went wrong! :( Please try again.")
        else:
            await self.bot.say(
                "Sorry I don't know your country! Did you use the correct ISO countrycode? \nExample: `-country GB` or `-country US-CA for california`")

    @commands.command(pass_context=True, no_pm=True)
    async def removecountry(self, ctx, country: str):

        server = ctx.message.server
        user = ctx.message.author

        re1 = '((?:[a-z][a-z]+))'  # Word 1
        re2 = '.*?'  # Non-greedy match on filler
        re3 = '((?:[a-z][a-z]+))'  # Word 2
        rg = re.compile(re1 + re2 + re3, re.IGNORECASE | re.DOTALL)

        m = rg.search(country)
        subregionobj = None
        try:
            if m:
                word1 = m.group(1)
                countryobj = pycountry.countries.get(alpha_2=word1.upper())
                subregionobj = pycountry.subdivisions.get(code=country.upper())
            else:
                countryobj = pycountry.countries.get(alpha_2=country.upper())
        except:
            countryobj= None
        if countryobj is not None:
            if subregionobj is not None:
                try:
                    if user.id in self.subregions[subregionobj.code]:
                        del(self.subregions[subregionobj.code][user.id])
                        await self.bot.say(
                            "The boys and girls from " + countryobj.name + ": " + subregionobj.name + " will miss you " + user.mention + "! :(")
                        dataIO.save_json("data/countrycode/subregions.json", self.subregions)
                    else:
                        await self.bot.say("You already removed that country as your countryorigin!")
                except KeyError:
                    await self.bot.say("You already removed that country as your countryorigin!")
            else:
                try:
                    if user.id in self.countries[countryobj.name]:
                        del(self.countries[countryobj.name][user.id])
                        await self.bot.say(
                            "The boys and girls from " + countryobj.name + " will miss you " + user.mention + "! :(")
                        dataIO.save_json("data/countrycode/countries.json", self.countries)
                    else:
                        await self.bot.say("You already removed that country as your countryorigin!")
                except:
                    await self.bot.say("You already removed that country as your countryorigin!")
        else:
            await self.bot.say("Sorry I don't know your country! Did you use the correct ISO countrycode?")


def check_folders():
    folders = ("data", "data/countrycode/")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)
            
def check_files():
    if not os.path.isfile("data/countrycode/countries.json"):
        print("Creating empty countries.json...")
        dataIO.save_json("data/countrycode/countries.json", {})
    if not os.path.isfile("data/countrycode/subregions.json"):
        print("Creating empty subregions.json...")
        dataIO.save_json("data/countrycode/subregions.json", {})
    if not os.path.isfile("data/countrycode/settings.json"):
        print("Creating empty settings.json...")
        dataIO.save_json("data/countrycode/settings.json", {})

def setup(bot):
    if pycountry is None:
        raise RuntimeError("You need to run pip3 install pycountry")
    check_folders()
    check_files()
    bot.add_cog(CountryCode(bot))
