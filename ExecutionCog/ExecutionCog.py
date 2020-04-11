import discord
from discord.ext import commands

class ExecutionCog:
    """Written for Hame"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def execute(self, ctx, user: discord.Member):
	
        author = ctx.message.author	
        #Text
        if author.id == "277453509018779648":
            if user.id == "116329127732051974":
                await self.bot.say("*" + user.mention + " dodges the bullet like a ninja" + "*")
            else:
                await self.bot.say("*" + author.mention + " executes " + user.mention + " with Nagant M1895 Revolver" + "*")
        elif author.id == "116329127732051974":
            if user.id == "177403864369070080":
                await self.bot.say("*" + author.mention + " summons **MechaKorTech**!\n" + user.mention + " summons\n**MechaAschDroid**!\nThey start to battle and destroy everything around them!" + "*")
            else:
                await self.bot.say("*" + author.mention + " summons **MechaKorTech** to blast " + user.mention + " into smithereens!" + "*")
        elif author.id == "177403864369070080":
            if user.id == "116329127732051974":
                await self.bot.say("*" + user.mention + " and " + author.mention + " REEEEE at eachother until everyone else's heads explode" + "*")
            else:
                await self.bot.say("*" + author.mention + " REEEEEs at" + user.mention + "until their head explodes" + "*")
        elif author.id == "313367342966898689":
            await self.bot.say("*" + author.mention + " hugs " + user.mention + " and smothers them to death" + "*")
        elif author.id == "129537561101074433":
            await self.bot.say("*" + author.mention + " reads The Wealth of Nations to " + user.mention + " until they die from boredom" + "*")
        elif author.id == "214367240991014912":
            await self.bot.say("*" + author.mention + " throws a blue shell, sending " + user.mention + " straight to last place!" + "*")
        elif author.id == "277232149957050378":
            await self.bot.say("*" + author.mention + " has a haiku for " + user.mention + "*" + "```My blade slices forth\nExecution comes at last\nDo not fail next time```")
        elif author.id == "304481265233559554":
            await self.bot.say("*" + user.mention + " has failed our Glorious Leader " + author.mention + " and has thus forfeit their life." + "*")
        elif author.id == "286367887168634882":
            await self.bot.say("*" + author.mention + " needs to let Kort know what she wants as a command" + "*")
        elif author.id == "200525863060635649":
            await self.bot.say("*" + author.mention + " needs to let Kort know what he wants as a command" + "*")
        else:
            await self.bot.say("You aren't Häme!")
