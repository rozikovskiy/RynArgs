import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def error(error: str, message: str, pythonerror: str):
    print(f"\033[35;1m{error}\033[0;35m: {message}\n\n\033[0;35;1mPython Error\033[0;35m: {pythonerror}")
    exit(1)
try:
    from .parser import RynParse, RynArgsParseError
    from . import ryndiff
except Exception as e:
    error("ModulesCannotBeImported", f"Modules not imported into {SCRIPT_DIR}.", e)
__version__ = "1.0.1-Early-Beta"
__author__ = "Ryn Corp."
__all__ = ["RynParse", "RynArgsParseError"]