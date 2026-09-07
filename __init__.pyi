from typing import Optional, List, Set, Dict, Any

class RynArgsError(Exception):
    pass

class ModulesNotFounded(RynArgsError):
    pass

__version__: str
__author__: str

class RynParse:
    def __init__(
        self,
        utilcmd: str = "Write here the command to call your utility so that it is displayed correctly in the tooltips.",
        utilname: Optional[str] = "Here you can optionally write the official name of your utility for a more beautiful description",
        prefix: Optional[str] = "Enter a prefix for flags here. It will be automatically substituted, for example, "-", so you can write '-flag' later.",
        done: Optional[str] = "Here's the termination command for parent flags. For example, 'done' so you can later write '-flag <arg1> <arg2> -done'",
        useutilnameinlogs: Optional[bool] = "This is so that you can decide whether to display the 'utilname' in the logs or not.",
        exit_after_help: Optional[bool] = "If enabled, the script successfully terminates after displaying the help information."
    ) -> None: ...

    def parent_add(self, parents: Set[str] | List[str] = "Here, return a set or a list so that the parser understands that these flags end only at the \"done\" trigger.") -> None: ...

    def description(
        self,
        description: str = "Here you need to write a description of your utility. It will then be displayed when you type '-help.'",
        maincolor: Optional[str] = "The color of all text. It is the primary color. If not maincolor white by default",
        namecolor: Optional[str] = "The title color of your utility. If there is no default color, the main one",
        raw: Optional[bool] = "Allows you to write completely raw text without processing, color, or tabs. False by default",
        name_tabs: Optional[int] = "Tab before utility name. Default is 5",
        def_tabs: Optional[int] = "Tabs before the description itself, 2 by default",
        help_tabs: Optional[int] = "Tabs before tooltips with main flags, default 5",
        help_title: Optional[str] = "The header name before the key flags. Defaults to 'Flag Help'"
    ) -> str: "Returns a ready-made description that must then be inserted into the parsing function."

    def add_argument(
        self,
        argument: str = "The name of the flag under which it will be used",
        use_example: str = "Example of usage",
        what_is_do: str = "Specifies the value of the flag",
        cmdcol: Optional[str] = "Command for the color of your team specified during class initialization",
        argcolor: Optional[str] = "The color of the newly added flag",
        exmpcol: Optional[str] = "Color example of use",
        actcol: Optional[str] = "Flag color description and meaning",
        prefix: Optional[bool] = "Whether the prefix is included in the hint or not",
        mainset: Optional[bool] = "Mainset flags are displayed when typing the help command in any case.",
        raw: Optional[bool] = "Allows you to write your own colors via ACII codes"
    ) -> None: "Returns nothing but displays hints in the format '{utilcmd} {arg} {usage example} - {what it does}'"

    def parsing(self,
        descrip: Optional[str] = "Insert the variable here where “description” was returned so that the description works with the help flag."
        ) -> Dict[str, Any]: ...
    def log(self,
        message: str = "Your message",
        tipe: str = "Your type. For example, ERROR", 
        color: Optional[str] = "Colour. For example, red+bold",
        retur: Optional[bool] = "If enabled, it returns the ready log.",
        prt: Optional[bool] = "If enabled, it outputs the image to the terminal/console.",
        onlymsg: Optional[bool] = "If enabled, it removes absolutely everything except the message.",
        nocolor: Optional[bool] = "If enabled, it removes the colors.",
        noname: Optional[bool] = "If enabled, it removes the utility name from the log."
        ): ...