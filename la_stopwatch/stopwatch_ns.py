from time import time_ns
from copy import deepcopy
from typing import Callable
from logging import Logger


class StopwatchNS:
    def __init__(self, logger: Logger = ..., msg: str = ..., *args, **kwargs):
        self._records: dict[int] = {}

        self._logger = logger
        self._msg = msg
        self._args = args
        self._kwargs = kwargs

        self.reset()

    def __enter__(self):
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

    def get_record(self, name: int | str) -> int:
        return self._records.get(name)

    def get_records(self) -> dict[int]:
        return deepcopy(self._records)

    def duration(self) -> int:
        return time_ns() - self._start

    def record(self, name: str = ...):
        if not isinstance(name, str):
            name = len(self._records)

        self._records[name] = self.duration()

        return self

    def log(self, msg: str, name: str = ..., *args, **kwargs):
        if not isinstance(name, str):
            name = len(self._records)

        self._records[name] = self.duration()

        self._log(msg, self._records[name], *args, **kwargs)

        return self

    def _log(self, msg: str, duration: int, *args, **kwargs) -> None:
        msg = msg % {"duration": duration}
        args = args or self._args
        kwargs = kwargs or self._kwargs

        if isinstance(self._logger, Logger):
            self._logger.debug(msg, *args, **kwargs)
        else:
            print(msg, *args, **kwargs)
