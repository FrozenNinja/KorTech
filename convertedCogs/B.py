import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import italics, pagify
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
import datetime
import time
import aiohttp
import asyncio
import re

class B(commands.Cog):
  
    def __init__(self, bot):
        self.bot = bot
		
    def replace(self, string, substitutions):

        substrings = sorted(substitutions, key=len, reverse=True)
        regex = re.compile('|'.join(map(re.escape, substrings)))
        return regex.sub(lambda match: substitutions[match.group(0)], string)

    @commands.command()
    async def B(self, ctx: commands.Context, arg):
        #Flips text to B

        string = arg
        substitutions = {"a" : ":regional_indicator_a:", 
		"b" : ":b:", 
		"c" : ":regional_indicator_c:", 
		"d" : ":regional_indicator_d:", 
		"e" : ":regional_indicator_e:", 
		"f" : ":regional_indicator_f:", 
		"g" : ":regional_indicator_g:", 
		"h" : ":regional_indicator_h:", 
		"i" : ":regional_indicator_i:", 
		"j" : ":regional_indicator_j:", 
		"k" : ":regional_indicator_k:", 
		"l" : ":regional_indicator_l:", 
		"m" : ":regional_indicator_m:", 
		"n" : ":regional_indicator_n:", 
		"o" : ":regional_indicator_o:", 
		"p" : ":regional_indicator_p:", 
		"q" : ":regional_indicator_q:", 
		"r" : ":regional_indicator_r:", 
		"s" : ":regional_indicator_s:", 
		"t" : ":regional_indicator_t:", 
		"u" : ":regional_indicator_u:", 
		"v" : ":regional_indicator_v:", 
		"w" : ":regional_indicator_w:", 
		"x" : ":regional_indicator_x:", 
		"y" : ":regional_indicator_y:", 
		"z" : ":regional_indicator_z:", 
		" " : '\n',
		"?" : ":question:",
		"!" : ":exclamation:"}
        stringlower = string.lower()
        output = self.replace(stringlower, substitutions)
		
        await ctx.send(output)
			
def setup(bot):
    bot.add_cog(B(bot))