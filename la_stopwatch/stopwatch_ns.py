from copy import deepcopy
from time import time_ns
from typing import Callable

from la_stopwatch.abstraction import StopwatchABS


class StopwatchNS(StopwatchABS):
    def __init__(self, callback: Callable[[int], None] = ..., *args, **kwargs):
        self._records: dict[int | str, int] = {}
        self._nameless_records: int = 0

        self._callback = callback
        self._args = args
        self._kwargs = kwargs

        self.reset()

    def __enter__(self):
        return self.reset()

    def __exit__(self, type, value, traceback) -> bool:
        if isinstance(self._callback, Callable):
            self._callback(self.duration(), *self._args, **self._kwargs)

        return False

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapper

    def __str__(self) -> str:
        return str(self.duration())

    def __repr__(self) -> str:
        return str(self.duration())

    def reset(self):
        self._start = time_ns()
        return self

    def duration(self) -> int:
        return time_ns() - self._start

    def get_record(self, name: int | str) -> int | None:
        return self._records.get(name)

    def get_records(self) -> dict[int | str, int]:
        return deepcopy(self._records)

    def record(self, name: str = ...):
        if not isinstance(name, str):
            name = self._nameless_records
            self._nameless_records += 1

        self._records[name] = self.duration()

        return self
