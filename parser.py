from typing import Optional
from .ryndiff import RynDiff
from textwrap import wrap
from sys import argv as args_from_sys

class RynArgsParseError(Exception):
    pass

class NoArgumentsAdded(RynArgsParseError):
    pass

class NoMessageInLog(RynArgsParseError):
    pass
class NoTypeInLog(RynArgsParseError):
    pass
class NoColorWithUnknownType(RynArgsParseError):
    pass

class RynParse:
    def __init__(self, utilcmd: str, utilname: Optional[str] = "", prefix: Optional[str] = "-", done: Optional[str] = "done", useutilnameinlogs: Optional[bool] = True, exit_after_help: Optional[bool] = False):
        self.arglist = set()
        self.arghelp = dict()
        self.utilname = utilname
        self.prefix = prefix
        self.utilname = utilname
        self.utilcmd = utilcmd
        self.done = done
        self.parents = set()
        self.rub = len(prefix)
        self.mainset = set()
        self._ryn_diff = RynDiff()
        self.exit_after_help = exit_after_help
        self.diff = RynDiff.diff(self._ryn_diff)
        self.useutilnameinlogs = useutilnameinlogs
        self.available_colors = {
            "reset": "\033[0m",
            "bold": "\033[1m",
            "dim": "\033[2m",
            "italic": "\033[3m",
            "underline": "\033[4m",
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "dark_gray": "\033[38;5;238m",
            "deep_black": "\033[38;5;232m",
            "dark_red": "\033[38;5;88m",
            "dark_green": "\033[38;5;22m",
            "dark_yellow": "\033[38;5;136m",
            "dark_blue": "\033[38;5;18m",
            "dark_magenta": "\033[38;5;90m",
            "dark_cyan": "\033[38;5;30m",
            "chocolate": "\033[38;5;94m",
            "navy": "\033[38;5;17m",
            "olive": "\033[38;5;100m",
            "purple": "\033[38;5;54m",
            "slate": "\033[38;5;60m",
            "maroon": "\033[38;5;52m",
            "bright_black": "\033[90m",
            "bright_red": "\033[91m",
            "bright_green": "\033[92m",
            "bright_yellow": "\033[93m",
            "bright_blue": "\033[94m",
            "bright_magenta": "\033[95m",
            "bright_cyan": "\033[96m",
            "bright_white": "\033[97m",
            "orange": "\033[38;5;208m",
            "pink": "\033[38;5;206m",
            "gold": "\033[38;5;220m",
            "neon_green": "\033[38;5;46m",
            "sky_blue": "\033[38;5;39m",
            "violet": "\033[38;5;135m",
            "peach": "\033[38;5;216m",
            "mint": "\033[38;5;121m",
        }

    def parent_add(self, parents: set | list):
        self.parents=set(parents)

    def description(
        self,
        description: str,
        maincolor: Optional[str] = "",
        namecolor: Optional[str] = "",
        raw: Optional[bool] = False,
        name_tabs: Optional[int] = 5,
        def_tabs: Optional[int] = 2,
        help_tabs: Optional[int] = 5,
        help_title: Optional[str] = "Flag Help"
    ):
        if maincolor:
            maincolor = "".join(self.available_colors.get(c, "") for c in maincolor.split("+"))

        if namecolor:
            namecolor = "".join(self.available_colors.get(c, "") for c in namecolor.split("+"))
        nt="\t"*name_tabs
        dt="\t"*def_tabs
        ht="\t"*help_tabs
        if raw: readydescription = description
        else: readydescription = "\n".join(dt + line for line in wrap(description, width=70))
        return f"{nt}\033[0m{namecolor}{self.utilname}\n\033[0m{maincolor}{readydescription}\n{ht}{namecolor}{help_title}\033[0m"

    def add_argument(self, argument: str, use_example: str, what_is_do: str, cmdcol: Optional[str] = "reset", argcolor: Optional[str] = "reset", exmpcol: Optional[str] = "reset", actcol: Optional[str] = "reset", prefix: Optional[bool] = True, mainset: Optional[bool] = False, raw: Optional[bool] = False):
        done=self.prefix+argument
        self.arglist.add(done)
        cook=""
        if prefix: cook=argument
        else: cook=done
        if argcolor: argcolor = "".join(self.available_colors.get(c, "") for c in argcolor.split("+"))
        if exmpcol: exmpcol = "".join(self.available_colors.get(c, "") for c in exmpcol.split("+"))
        if actcol: actcol = "".join(self.available_colors.get(c, "") for c in actcol.split("+"))
        if cmdcol: cmdcol = "".join(self.available_colors.get(c, "") for c in cmdcol.split("+"))
        if not raw: self.arghelp[done] = f"{cmdcol}{self.utilcmd}\033[0m {argcolor}{cook}\033[0m {exmpcol}{use_example}\033[0m - {actcol}{what_is_do}\033[0m"
        else: self.arghelp[done] = f"{self.utilcmd}\033[0m {cook}\033[0m {use_example}\033[0m - {what_is_do}\033[0m"
        if mainset: self.mainset.add(done)

    def parsing(self, descrip: Optional[str], args: Optional[list] = args_from_sys):
        arguments = args
        if not self.arglist: 
            raise NoArgumentsAdded("No candidates have been found for the search.")
        args=arguments[1:]
        al={}
        maxi = len(args)
        helplist={f"{self.prefix}help", f"{self.prefix}h", f"{self.prefix}support", f"{self.prefix}sup"}
        for i, argument in enumerate(args):
            if argument in self.arglist:
                if argument[self.rub:] in self.parents and f"{self.prefix}{self.done}" in args:
                    strint=""
                    ind=i+1
                    while args[ind] != f"{self.prefix}{self.done}":
                        if ind >= maxi:
                            break
                        if not strint: strint += args[ind]
                        else: strint += " "+ args[ind]
                        ind += 1
                    al[f"{args[i][self.rub:]}|{i}"] = strint
                elif i + 1 < maxi:
                    al[args[i][self.rub:]] = args[i+1]
            elif argument in helplist:
                    if i + 1 < maxi: 
                        target_arg = args[i + 1]
                        if target_arg in self.arghelp:
                            print(self.arghelp[target_arg])
                        else:
                            print(descrip)
                        if exit_after_help:
                            exit(0)
                        else:
                            return
                    else:
                        print(descrip)
                        for flag_name, flag_help in self.arghelp.items():
                            if flag_name in self.mainset: 
                                print(f"  {flag_help}")
                        exit(0)
            else:
                matches = self.diff.fuzzy(argument, self.arglist, 0.6)
                if matches:
                    default=f"Unknown flag \"\033[31m\033[1m{argument}\033[0m\". Maybe you mean \"\033[32m\033[1m{matches[0]}\033[0m\"?"
                    if self.useutilnameinlogs == True: log = f"{self.utilcmd}\033[0m [\033[31m\033[1mERROR\033[0m]: {default}"
                    else: log = default
                    print(log)
        return al
    def log(self, message, tipe, color: Optional[str] = "", retur: Optional[bool] = False, prt: Optional[bool] = True, onlymsg: Optional[bool] = False, nocolor: Optional[bool] = False, noname: Optional[bool] = False):
        typetocolor = {
            "OK": "green+bold",
            "ERROR": "red+bold",
            "WARNING": "orange+bold",
            "INFO": "yellow+bold",
            "LOG": "cyan+bold",
            "SUCCESS": "green+bold"
        }
        if tipe in typetocolor:
            colorc=typetocolor.get(tipe)
            if not colorc and not color:
                colorc="reset"
            elif color:
                colorc=color
            else:
                pass    
        else:
            if not color: raise NoColorWithUnknownType("Unknown type. Custom color isnt provided.")
            colorc = color
        colorc = "".join(self.available_colors.get(c, "") for c in colorc.split("+"))
        if not message: raise NoMessageInLog("No message in log provided")
        if not tipe: raise NoTypeInLog("No type in log provided")
        if not nocolor:
            body = f"[{colorc}{tipe}\033[0m] {message}"
        else:
            body = f"[{tipe}] {message}"
        if self.useutilnameinlogs and not noname: ready=f"{self.utilcmd} {body}"
        else: ready=body
        if onlymsg: ready=message
        if prt: print(ready)
        if retur: return ready
        