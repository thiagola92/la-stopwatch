from abc import abstractmethod
from typing import Callable


class StopwatchABS:
    def __init__(self, callback: Callable[[int], None] = ..., *args, **kwargs):
        """"""

    @abstractmethod
    def __enter__(self):
        """Reset timer before enter context manager."""

    @abstractmethod
    def __exit__(self, type, value, traceback) -> bool:
        """Log before exit context manager."""

    @abstractmethod
    def __call__(self, func: Callable) -> Callable:
        """Time a function or method."""

    @abstractmethod
    def __str__(self) -> str:
        """Get the current timing as string."""

    @abstractmethod
    def __repr__(self) -> str:
        """Get the current timing as string."""

    @abstractmethod
    def reset(self):
        """Restart the timer."""

    @abstractmethod
    def get_record(self, name: int | str) -> int | None:
        """Get a record by name.

        Return None if no item is found.
        """

    @abstractmethod
    def get_records(self) -> dict[int | str, int]:
        """Get a dictionary with all records."""

    @abstractmethod
    def duration(self) -> int:
        """Get the elapsed time since start (or reset)."""

    @abstractmethod
    def record(self, name: str = ...):
        """Record current time.

        If a name is giving it'll use it as key, otherwise
        the quantity of nameless records will be used as key.
        """
