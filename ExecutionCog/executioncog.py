import discord
from redbot.core import commands

class ExecutionCog(commands.Cog):
    """Written for Hame"""

    @commands.command()
    async def execute(self, ctx: commands.Context, user: discord.Member):

        author = ctx.message.author	
        #Text
        if author.id == 277453509018779648:
            if user.id == 116329127732051974:
                await ctx.send("*" + user.mention + " dodges the bullet like a ninja" + "*")
            else:
                await ctx.send("*" + author.mention + " executes " + user.mention + " with Nagant M1895 Revolver" + "*")
        elif author.id == 116329127732051974:
            if user.id == 177403864369070080:
                await ctx.send("*" + author.mention + " summons **MechaKorTech**!\n" + user.mention + " summons\n**MechaAschDroid**!\nThey start to battle and destroy everything around them!" + "*")
            else:
                await ctx.send("*" + author.mention + " summons **MechaKorTech** to blast " + user.mention + " into smithereens!" + "*")
        elif author.id == 177403864369070080:
            if user.id == 116329127732051974:
                await ctx.send("*" + user.mention + " and " + author.mention + " REEEEE at eachother until everyone else's heads explode" + "*")
            else:
                await ctx.send("*" + author.mention + " REEEEEs at" + user.mention + "until their head explodes" + "*")
        elif author.id == 313367342966898689:
            await ctx.send("*" + author.mention + " hugs " + user.mention + " and smothers them to death" + "*")
        elif author.id == 129537561101074433:
            await ctx.send("*" + author.mention + " reads The Wealth of Nations to " + user.mention + " until they die from boredom" + "*")
        elif author.id == 214367240991014912:
            await ctx.send("*" + author.mention + " throws a blue shell, sending " + user.mention + " straight to last place!" + "*")
        elif author.id == 277232149957050378:
            await ctx.send("*" + author.mention + " has a haiku for " + user.mention + "*" + "```My blade slices forth\nExecution comes at last\nDo not fail next time```")
        elif author.id == 304481265233559554:
            await ctx.send("*" + user.mention + " has failed our Glorious Leader " + author.mention + " and has thus forfeit their life." + "*")
        #elif author.id == 184369090150793216:
           # await ctx.send("*" + author.mention + " stares at " + user.mention + " with withering disapproval until they combust from shame" + "*")
        elif author.id == 200525863060635649:
            await ctx.send("*" + author.mention + " needs to let Kort know what he wants as a command" + "*")
        elif author.id == 143549673947398145:
            await ctx.send("*" + author.mention + " crushes " + user.mention + " beneath the treads of his tank for failing the Mother Islands" + "*")
        elif author.id == 198544671469731840:
            await ctx.send("*" + author.mention + " sics an army of cats on " + user.mention + " who is promptly mauled to death!" + "*")
        else:
            await ctx.send("You aren't Häme!")