# plugin_loader.py
import importlib
import pkgutil
import inspect
import os
from commands.base_command import BaseCommand
import logging

logger = logging.getLogger("appLogger")

def load_plugins(commands_package: str):
    """
    Dynamically load command classes.
    Returns a dictionary: {command_name: command_instance}.
    """
    commands_dict = {}
    try:
        package = importlib.import_module(commands_package)
    except ImportError as e:
        logger.error("Could not import package %s: %s", commands_package, e)
        return commands_dict

    package_path = os.path.dirname(package.__file__)

    for _, module_name, is_pkg in pkgutil.iter_modules([package_path]):
        if is_pkg or not module_name.endswith("_command"):
            continue
        try:
            module = importlib.import_module(f"{commands_package}.{module_name}")
        except Exception as e:
            logger.error("Failed to import module %s: %s", module_name, e)
            continue
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseCommand) and obj is not BaseCommand:
                try:
                    command_instance = obj()
                    logger.debug("Loaded command: %s", command_instance.name())
                    commands_dict[command_instance.name()] = command_instance
                except Exception as e:
                    logger.error("Error instantiating command %s: %s", name, e)
    return commands_dict
