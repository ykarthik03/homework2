# commands/base_command.py (Commands Branch)
from abc import ABC, abstractmethod

class BaseCommand(ABC):
    """Abstract base class for all commands in the commands branch."""

    @abstractmethod
    def name(self) -> str:
        """Return the command name as used in the REPL."""
        pass

    @abstractmethod
    def execute(self, *args) -> None:
        """Execute the command logic (with debugging in the commands branch)."""
        pass
