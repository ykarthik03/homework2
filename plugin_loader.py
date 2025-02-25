import importlib
import pkgutil
import inspect
import os
from commands.base_command import BaseCommand

def load_plugins(commands_package: str):
    """
    Dynamically load command classes.
    Returns a dictionary: {command_name: command_instance}.
    """
    commands_dict = {}
    package = importlib.import_module(commands_package)
    package_path = os.path.dirname(package.__file__)

    for _, module_name, is_pkg in pkgutil.iter_modules([package_path]):
        if is_pkg or not module_name.endswith("_command"):
            continue
        module = importlib.import_module(f"{commands_package}.{module_name}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseCommand) and obj is not BaseCommand:
                command_instance = obj()
                print(f"Loaded command: {command_instance.name()}")  # optional debug message
                commands_dict[command_instance.name()] = command_instance

    return commands_dict
