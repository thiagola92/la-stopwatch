from datetime import timedelta
from time import time_ns

from la_stopwatch.async_stopwatch_ns import AsyncStopwatchNS


class AsyncStopwatch(AsyncStopwatchNS):
    def duration(self) -> timedelta:
        return timedelta(microseconds=(time_ns() - self._start) / 1000)
