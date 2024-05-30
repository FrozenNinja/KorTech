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
        elif user.id == 177403864369070080: #CEProtect
            await ctx.send("*" + user.mention + " laughs at " + author.mention + " for even trying to execute the CE" + "*")
        elif author.id == 277453509018779648: #Hame
            if user.id == 116329127732051974:
                await ctx.send("*" + user.mention + " dodges the bullet like a ninja" + "*")
            else:
                await ctx.send("*" + author.mention + " executes " + user.mention + " with Nagant M1895 Revolver" + "*")
        elif user.id == 116329127732051974: #KortProtect
            await ctx.send("*" + user.mention + " laughs at " + author.mention + "*" + " You can't turn my own bot against me. Fool!")
        elif author.id == 116329127732051974: #Kort
            if user.id == 177403864369070080:
                await ctx.send("*" + author.mention + " summons **MechaKorTech**!\n" + user.mention + " summons\n**MechaAschDroid**!\nThey start to battle and destroy everything around them!" + "*")
            else:
                await ctx.send("*" + author.mention + " summons **MechaKorTech** to blast " + user.mention + " into smithereens!" + "*")
        elif author.id == 313367342966898689: #Hakke
            await ctx.send("*" + author.mention + " hugs " + user.mention + " and smothers them to death" + "*")
        elif author.id == 304481265233559554: #Mark
            await ctx.send("*" + user.mention + " has failed our CE Emeritus " + author.mention + " and has thus forfeit their life." + "*")
        elif author.id == 177403864369070080: #Asche
            await ctx.send("*" + author.mention + " waves a dismissive hand and a bolt of lightning splits the sky, striking " + user.mention + " and reducing them to dust" + "*")
        elif author.id == 346447222222618624: #Pantso
            await ctx.send("*" + author.mention + " banishes " + user.mention + " to the Tasteless Isles, cursed forever to wear ugly sweaters, eat cold soggy tacos, and watch only Jersey Shore re-runs." + "*")
        elif author.id == 630608474023264267: #WH
            await ctx.send("*" + author.mention + " quickly unholsters his DL-44 and shoots first, killing " + user.mention + " instantly" + "*")
        elif author.id == 627094307706372097: #Val
            await ctx.send("*" + author.mention + " lifts up his radiant sword. " + "*" + " **" + "\"AND IT SHALL BE RETURNED!\"" + "** " + "*" + "With an elegant strike, " + user.mention + " is lying on the ground, the ether of whom absorbed back to it's rightful place" + "*")
        elif author.id == 505759332856496128: #FE
            await ctx.send("*" + author.mention + " calls on the mighty eagle battalion to dive from the sky delivering poop, crushing " + user.mention + " to death" + "*")
        elif author.id == 418631163310112768: #Astro
            await ctx.send("*" + user.mention + " has been strapped to " + author.mention + "'s rocketship! They are blasting off into space, never to be seen again!" + "*")
        elif author.id == 373240532509392906: #Onfande
            await ctx.send("*" + user.mention + " has instantly been evaporated by a beam of plasma striking their exact location!" + "*")
        else:
            await ctx.send("You aren't Häme!")