import builtins
import pprint


def replace_builtin_print():
    print("Replacing print with pprint")
    builtins.print = pprint.pprint
