import discord
import nationstates
import os
from .utils.dataIO import fileIO
from .utils.dataIO import dataIO
from .utils.chat_formatting import *
from .utils import checks
from discord.ext import commands
from datetime import timedelta
from collections import deque, defaultdict
from __main__ import send_cmd_help, settings
from time import gmtime, strftime, localtime
import urllib.request
import json
from discord.utils import get

fdasfsg
def id_from_args(*args):
        return '_'.join(args).lower()

default_settings = {
        "updating_role"  : "",
        "soldier_role"   : "",
        "commander_role" : "",
        "muted_role"     : "",
        "allied_role"    : ""
}

class HunterPrime:
        """Hunter Prime"""

        def __init__(self, bot):
                self._settings = dataIO.load_json("data/hunterprime/settings.json")
                self.bot = bot

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def approx(self, ctx, *args):
                """Show approximate update time of region."""

                server = ctx.message.server
                author = ctx.message.author
                region = id_from_args(*args)

                role_cmd = self._get_commander_role(server)
                if not role_cmd in ctx.message.author.roles:
                        await self.bot.say("Not authorized to use this command.")
                        return

                url = "http://localhost:6264/region/{}/q=region__update_starts".format(region);
                datas = urllib.request.urlopen(url).read()
                data = json.loads(datas.decode('utf-8'))
                if isinstance(data, list):
                        data = data[1]
                stamp = strftime("%H:%M:%S", localtime(int(data)))
                await self.bot.say(stamp);

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def pdc(self, ctx):
                """Show pending delegate changes."""

                server = ctx.message.server
                author = ctx.message.author

                role_cmd = self._get_commander_role(server)
                if not role_cmd in ctx.message.author.roles:
                        await self.bot.say("Not authorized to use this command.")
                        return

                datas = urllib.request.urlopen("http://localhost:6264/world/q=world__regions+region__name+region__update_starts+region__delegate+region__most_endorsed+nation__name+nation__endorsement_count/region_filter=delegate_change_pending").read()
                data = json.loads(datas.decode('utf-8'))
                for i, s in enumerate(data):
                        if isinstance(data[i]["update_starts"], list):
                                data[i]["update_starts"] = data[i]["update_starts"][1]
                data.sort(key=lambda r: r["update_starts"] if r["update_starts"] is not None else 0)
                def nstr(n):
                        if n is None:
                                return "_none_";
                        else:
                                return n;
                def fmt(r):
                        if r["update_starts"] is None:
                                stamp = "??:??:??"
                        else:
                                stamp = strftime("%H:%M:%S", localtime(int(r["update_starts"])))
                        delfrom = nstr(r["delegate"])
                        delto = nstr(r["most_endorsed"])
                        return "{}: https://www.nationstates.net/region={} ({} --> {})".format(stamp, r["name"], delfrom, delto)

                data = map(fmt, data)
                out = "**Pending delegate changes:**\n" + "\n".join(data)
                while len(out) >= 2000:
                        i = out.rfind("\n", 0, 2000)
                        await self.bot.say(out[:i])
                        out = "**Pending delegate changes (cont.):**\n" + out[i+1:]
                await self.bot.say(out)


        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def im_here(self, ctx):
                """Mark that the user is present for update."""

                server = ctx.message.server
                author = ctx.message.author

                role_upd = self._get_updating_role(server)

                ss = self._get_server_settings(server.id)
                roles_lib = list(map(lambda r: self._role_from_string(server, r), ss["soldier_role"].split(",")))
                if not any(True for i in author.roles if i in roles_lib):
                        await self.bot.say("You're not masked, {}. Please ask a {}.".format(author.mention, self._get_commander_role(server).name))
                        return

                try:
                        await self.bot.add_roles(author, role_upd)
                except discord.errors.Forbidden as err:
                        await self.bot.say("I don't have permissions to mark you, {}: {}.".format(author.mention, err))
                except AttributeError:  # role_to_add is NoneType
                        await self.bot.say("That role isn't user settable, {}.".format(author.mention))
                else:
                        await self.bot.say("Marked {} as present for this update.".format(author.mention))

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def allied_here(self, ctx):
                """Mark that the user is present for update."""

                server = ctx.message.server
                author = ctx.message.author

                role_upd = self._get_updating_role(server)

                ss = self._get_server_settings(server.id)
                roles_lib = list(map(lambda r: self._role_from_string(server, r), ss["allied_role"].split(",")))
                if not any(True for i in author.roles if i in roles_lib):
                        await self.bot.say("You're not masked, {}. Please ask a {}.".format(author.mention, self._get_commander_role(server).name))
                        return

                try:
                        await self.bot.add_roles(author, role_upd)
                except discord.errors.Forbidden as err:
                        await self.bot.say("I don't have permissions to mark you, {}: {}.".format(author.mention, err))
                except AttributeError:  # role_to_add is NoneType
                        await self.bot.say("That role isn't user settable, {}.".format(author.mention))
                else:
                        await self.bot.say("Marked {} as present for this update.".format(author.mention))

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def im_not_here(self, ctx):
                """Mark that the user is no longer present for update."""

                server = ctx.message.server
                author = ctx.message.author

                role_upd = self._get_updating_role(server)

                try:
                        await self.bot.remove_roles(author, role_upd)
                except discord.errors.Forbidden as err:
                        await self.bot.say("I don't have permissions to unmark you, {}: {}.".format(author.mention, err))
                else:
                        await self.bot.say("{} is no longer marked as present for this update.".format(author.mention))

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def update_over(self, ctx):
                """Mark that update is finished."""
                server = ctx.message.server
                ss = self._get_server_settings(server.id)

                role_upd = self._get_updating_role(server)
                role_cmd = self._get_commander_role(server)
                if not role_cmd in ctx.message.author.roles:
                        await self.bot.say("Not authorized to use this command.")
                        return

                for member in server.members:
                        if not role_upd in member.roles:
                                continue

                        try:
                                await self.bot.remove_roles(member, role_upd)
                        except discord.errors.Forbidden:
                                await self.bot.say("%s: Failed to unmask - I don't have permissions to do that." % member.name)
                        except AttributeError:  # role_to_add is NoneType
                                await self.bot.say("%s: Failed to unmask - That role isn't user settable." % member.name)
                        else:
                                await self.bot.say("%s: Unmasked." % member.mention)

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def radio_silence(self, ctx):
                """Silence peeps."""
                server = ctx.message.server
                ss = self._get_server_settings(server.id)

                role_mute = self._get_muted_role(server)
                role_upd = self._get_updating_role(server)
                role_cmd = self._get_commander_role(server)
                if not role_cmd in ctx.message.author.roles:
                        await self.bot.say("Not authorized to use this command.")
                        return

                for member in server.members:
                        if not role_upd in member.roles:
                                continue

                        try:
                                await self.bot.add_roles(member, role_mute)
                        except discord.errors.Forbidden:
                                await self.bot.say("%s: Failed to mask - I don't have permissions to do that." % member.name)
                        except AttributeError:  # role_to_add is NoneType
                                await self.bot.say("%s: Failed to mask - That role isn't user settable." % member.name)
                        else:
                                await self.bot.say("%s: Muted." % member.mention)

        @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
        async def silence_over(self, ctx):
                """Silence is over."""
                server = ctx.message.server
                ss = self._get_server_settings(server.id)

                role_mute = self._get_muted_role(server)
                role_upd = self._get_updating_role(server)
                role_cmd = self._get_commander_role(server)
                if not role_cmd in ctx.message.author.roles:
                        await self.bot.say("Not authorized to use this command.")
                        return

                for member in server.members:
                        if not role_mute in member.roles:
                                continue

                        try:
                                await self.bot.remove_roles(member, role_mute)
                        except discord.errors.Forbidden:
                                await self.bot.say("%s: Failed to unmask - I don't have permissions to do that." % member.name)
                        except AttributeError:  # role_to_add is NoneType
                                await self.bot.say("%s: Failed to unmask - That role isn't user settable." % member.name)
                        else:
                                await self.bot.say("%s: Unmuted." % member.mention)


        def _get_updating_role(self, server):
                return self._get_role(server, "updating_role")
        def _get_soldier_role(self, server):
                return self._get_role(server, "soldier_role")
        def _get_commander_role(self, server):
                return self._get_role(server, "commander_role")
        def _get_muted_role(self, server):
                return self._get_role(server, "muted_role")
        def _get_allied_role(self, server):
                return self._get_role(server, "allied_role")
        def _get_role(self, server, role):
                ss = self._get_server_settings(server.id)
                return self._role_from_string(server, ss[role])

        @commands.group(pass_context=True, no_pm=True)
        @checks.serverowner_or_permissions(administrator=True)
        async def hunterprimeset(self, ctx):
                """Manages HunterPrime settings."""
                if ctx.invoked_subcommand is None:
                        server = ctx.message.server
                        await send_cmd_help(ctx)
                        roles = settings.get_server(server).copy()
                        ss = self._get_server_settings(server.id)
                        _settings = {**ss, **roles}
                        msg = ("Updating role: {updating_role}\n"
                                   "Soldier role: {soldier_role}\n"
                                   "Commander role: {commander_role}\n"
                                   "Muted role: {muted_role}\n"
                                   "Allied role: {allied_role}\n"
                                   "".format(**_settings))
                        await self.bot.say(box(msg))

        @hunterprimeset.command(pass_context=True, name="updatingrole", no_pm=True)
        async def _hunterprimeset_updatingrole(self, ctx, role_name: str):
                """Sets the updating role for this server, case insensitive."""
                await self._set_role(ctx.message.server, "updating_role", "Updating", role_name)

        @hunterprimeset.command(pass_context=True, name="soldierrole", no_pm=True)
        async def _hunterprimeset_soldierrole(self, ctx, role_name: str):
                """Sets the soldier role for this server, case insensitive."""
                await self._set_role(ctx.message.server, "soldier_role", "Soldier", role_name)

        @hunterprimeset.command(pass_context=True, name="commanderrole", no_pm=True)
        async def _hunterprimeset_commanderrole(self, ctx, role_name: str):
                """Sets the commander role for this server, case insensitive."""
                await self._set_role(ctx.message.server, "commander_role", "Commander", role_name)

        @hunterprimeset.command(pass_context=True, name="mutedrole", no_pm=True)
        async def _hunterprimeset_mutedrole(self, ctx, role_name: str):
                """Sets the updating role for this server, case insensitive."""
                await self._set_role(ctx.message.server, "muted_role", "Muted", role_name)

        @hunterprimeset.command(pass_context=True, name="alliedrole", no_pm=True)
        async def _hunterprimeset_alliedrole(self, ctx, role_name: str):
                """Sets the updating role for this server, case insensitive."""
                await self._set_role(ctx.message.server, "allied_role", "Allied", role_name)

        async def _set_role(self, server, setting_name, display_name, newval):
                ss = self._get_server_settings(server.id)
                ss[setting_name] = newval
                self._set_server_settings(server.id, ss)
                await self.bot.say("{} role set to '{}'".format(display_name, newval))

        def _role_from_string(self, server, rolename, roles=None):
                if roles is None:
                        roles = server.roles

                roles = [r for r in roles if r is not None]
                role = discord.utils.find(lambda r: r.name.lower() == rolename.lower(),
                                                                  roles)
                return role

        def _get_server_settings(self, sid):
                if sid not in self._settings:
                        self._settings[sid] = default_settings.copy()
                return self._settings[sid]

        def _set_server_settings(self, sid, ss):
                self._settings[sid] = ss
                dataIO.save_json('data/hunterprime/settings.json', self._settings)

def check_folders():
        folders = ("data", "data/hunterprime/")
        for folder in folders:
                if not os.path.exists(folder):
                        print("Creating " + folder + " folder...")
                        os.makedirs(folder)


def check_files():
        ignore_list = {"SERVERS": [], "CHANNELS": []}

        files = {
                #"blacklist.json"      : [],
                #"whitelist.json"      : [],
                #"ignorelist.json"     : ignore_list,
                #"filter.json"         : {},
                #"past_names.json"     : {},
                #"past_nicknames.json" : {},
                "settings.json"       : {},
                #"modlog.json"         : {},
                #"perms_cache.json"    : {}
        }

        for filename, value in files.items():
                if not os.path.isfile("data/hunterprime/{}".format(filename)):
                        print("Creating empty {}".format(filename))
                        dataIO.save_json("data/hunterprime/{}".format(filename), value)

def setup(bot):
        check_folders()
        check_files()
        bot.add_cog(HunterPrime(bot))