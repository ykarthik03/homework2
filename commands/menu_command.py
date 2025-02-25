from commands.base_command import BaseCommand

class MenuCommand(BaseCommand):
    def name(self) -> str:
        return "menu"

    def execute(self, *args) -> None:
        """
        Usage:
          menu

        Lists all available commands.
        """
        # Delay the import to break the circular dependency
        from plugin_loader import load_plugins
        commands = load_plugins("commands")
        print("Available commands:")
        for cmd_name in sorted(commands.keys()):
            print(f"  {cmd_name}")