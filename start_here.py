import builtins
import importlib
import sys
from copy import deepcopy
from pprint import pprint

import settings
from edit_modules.replace_builtins import replace_builtin_print
from package__init__mechanics import *  # imports everything on __all__

if __name__ == "__main__":

    print(settings)  # prints module repr (with location of the module)
    settings_imported_module_content = settings.__dict__.keys()
    assert "HI_SETTING" in settings_imported_module_content, "Imported value in settings.__inti__ is available."
    assert (
        "base" in settings_imported_module_content
    ), "Because I imported HI_SETTINGS from `base`, the whole module is imported."

    assert "base" not in globals(), "Base is import "
    print(settings.base.HI_SETTING)
    print(settings.base.BASE_LOCAL_CONST)

    print("### importing cache")
    print("### importing cache")
    print("### importing cache")
    print("### importing cache")
    package__init__mechanics_function1()  # imported from package__init__mechanics import *

    print(settings.HI_SETTING)
    assert "settings" in sys.modules, "settings module should be cached"

    assert "math" in sys.modules, "math was imported in settings.__init__.py. Should also be cached"
    math_module_id = id(sys.modules["math"])
    settings_module_id = id(sys.modules["settings"])

    import math  # isort: skip
    import settings  # importing settings again doesnt run the module again. check prints. check   # isort: skip

    assert settings_module_id == id(sys.modules["settings"]), "Math module was already cached"
    assert math_module_id == id(sys.modules["math"]), "Math module was already cached imported in another module"

    print("###### Editing modules")
    print("###### Editing modules")
    print("###### Editing modules")

    print("Default print:", print, id(print))

    old_print = deepcopy(print)

    replace_builtin_print()

    assert old_print != print, "Expected builtin print to be replaced"

    print("Print Replacement:")
    print(print)
    print(id(print))

    assert print == pprint, "Expected replacement to be pprint"
    assert builtins.print == pprint, "Expected replacement to be pprint"

    print("Settings' module print")
    settings_module_builtins = getattr(settings, "__builtins__")
    assert settings_module_builtins["print"] == pprint, "pprint should be replaced everywhere"

    print("### Reseting module")
    print("### Reseting module")
    print("### Reseting module")

    importlib.reload(settings)  # doesnt work on builtin module

    settings_builtins = getattr(settings, "__builtins__")

    assert settings_builtins != builtins, "Module' builtins != the builtin module"
    assert isinstance(settings_builtins, dict), "modules' __builtins__ is a dict"
