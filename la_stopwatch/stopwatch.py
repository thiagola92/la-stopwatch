from time import time_ns
from copy import deepcopy
from datetime import timedelta


class Stopwatch:
    def __init__(self):
        self._records: dict[timedelta] = {}
        self.reset()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback) -> bool:
        return False

    def __str__(self) -> str:
        return str(self.duration())

    def reset(self):
        self._start = time_ns()

        return self

    def get_record(self, name: int | str) -> timedelta:
        return self._records.get(name)

    def get_records(self) -> dict[timedelta]:
        return deepcopy(self._records)

    def duration(self) -> timedelta:
        return timedelta(microseconds=(time_ns() - self._start) / 1000)

    def record(self, name: str = None):
        if name is None:
            name = len(self._records)

        self._records[name] = self.duration()

        return self
