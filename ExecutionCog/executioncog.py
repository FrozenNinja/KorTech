import discord
from redbot.core import commands

class ExecutionCog(commands.Cog):
    """Written for Hame"""

    @commands.command()
    async def execute(self, ctx: commands.Context, user: discord.Member):

        author = ctx.message.author	
        #Text
        if user.id == 351596701913448449: #KorTech
            await ctx.send("Attempting to kill me with my own power? Foolish mortal.\n" + "*" + "Electrocutes " + author.mention + " until they turn into ash." + "*")
        elif user.id == 313367342966898689: #Hakke
            await ctx.send("*" + user.mention + " laughs at " + author.mention + " and proceeds to drain them of all their blood" + "*")
        elif author.id == 277453509018779648: #Hame
            if user.id == 116329127732051974:
                await ctx.send("*" + user.mention + " dodges the bullet like a ninja" + "*")
            else:
                await ctx.send("*" + author.mention + " executes " + user.mention + " with Nagant M1895 Revolver" + "*")
        elif author.id == 116329127732051974: #Kort
            if user.id == 177403864369070080:
                await ctx.send("*" + author.mention + " summons **MechaKorTech**!\n" + user.mention + " summons\n**MechaAschDroid**!\nThey start to battle and destroy everything around them!" + "*")
            else:
                await ctx.send("*" + author.mention + " summons **MechaKorTech** to blast " + user.mention + " into smithereens!" + "*")
        elif author.id == 313367342966898689: #Hakke
            await ctx.send("*" + author.mention + " hugs " + user.mention + " and smothers them to death" + "*")
        elif author.id == 700757718473900052: #Thed
            await ctx.send("*" + author.mention + " lights a match and watches " + user.mention + " burn at the stake. May the fire cleanse you of all your sins and failures." + "*")
        elif author.id == 304481265233559554: #Mark
            await ctx.send("*" + user.mention + " has failed our Glorious Leader " + author.mention + " and has thus forfeit their life." + "*")
        elif author.id == 200525863060635649: #SM
            await ctx.send("*" + author.mention + " needs to let Kort know what he wants as a command" + "*")
        elif author.id == 185944398217871360: #HN
            await ctx.send("*" + author.mention + " purges the heresy of " + user.mention + " with cleansing flame." + "*")
        elif author.id == 679023417315426344: #Sul
            await ctx.send("*" + author.mention + " stalks silently in shadows. " + user.mention + " has failed for the last time..." + "*")
        elif author.id == 143549673947398145: #Control
            await ctx.send("*" + author.mention + " crushes " + user.mention + " beneath the treads of his tank for failing the Mother Islands" + "*")
        elif author.id == 505759332856496128: #FE
            await ctx.send("*" + author.mention + " calls on the mighty eagle battalion to dive from the sky delivering poop, crushing " + user.mention + " to death" + "*")
        elif author.id == 198544671469731840: #Wisch
            await ctx.send("*" + author.mention + " sics an army of cats on " + user.mention + " who is promptly mauled to death!" + "*")
        elif author.id == 356510817094598658: #ENE
            await ctx.send("*" + author.mention + " assembles an army of snapping turtles, slowly enclosing " + user.mention + "  until they are reduced to a pile of bones" + "*")
        else:
            await ctx.send("You aren't Häme!")

    @commands.command()
    async def husband(self, ctx, user: discord.Member):

        author = ctx.message.author
        if author.id == 754524576670548049:
            await ctx.send("*Luna hugs FE and tells him how great a husband he is!*")
