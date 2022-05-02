from time import time_ns
from copy import deepcopy
from typing import Callable
from logging import Logger
from logging import getLogger
from datetime import timedelta


class Stopwatch:
    def __init__(self, msg: str = ..., logger: Logger = getLogger("la-stopwatch"), *args, **kwargs):
        self._records: dict[timedelta] = {}

        self._msg = msg
        self._logger = logger
        self._args = args
        self._kwargs = kwargs

        self.reset()

    def __enter__(self):
        self.reset()

        return self

    def __exit__(self, type, value, traceback) -> bool:
        if isinstance(self._msg, str):
            self._log(self._msg, self.duration(), *self._args, **self._kwargs)

        return False

    def __call__(self, func) -> Callable:
        def wrapper(*args, **kwargs):
            with self:
                func(*args, **kwargs)

        return wrapper

    def __str__(self) -> str:
        return str(self.duration())

    def reset(self):
        self._start = time_ns()

        return self

    def get_record(self, name: int | str) -> timedelta | None:
        return self._records.get(name)

    def get_records(self) -> dict[timedelta]:
        return deepcopy(self._records)

    def duration(self) -> timedelta:
        return timedelta(microseconds=(time_ns() - self._start) / 1000)

    def record(self, name: str = ...):
        self._record(name)

        return self

    def log(self, msg: str, name: str = ..., record: bool = False, *args, **kwargs):
        if record:
            self._log(msg, self._record(name), *args, **kwargs)
        else:
            self._log(msg, self.duration(), *args, **kwargs)

        return self

    def _record(self, name: str) -> timedelta:
        if not isinstance(name, str):
            name = len(self._records)

        self._records[name] = self.duration()

        return self._records[name]

    def _log(self, msg: str, duration: timedelta, *args, **kwargs) -> None:
        msg = msg % {"duration": duration}
        args = args or self._args
        kwargs = kwargs or self._kwargs

        self._logger.debug(msg, *args, **kwargs)
