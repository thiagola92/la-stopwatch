from typing import Awaitable, Callable

from la_stopwatch.stopwatch import StopwatchNS


class AsyncStopwatchNS(StopwatchNS):
    def __init__(
        self,
        callback: Callable[[int], None | Awaitable] = ...,
        is_async: bool = False,
        *args,
        **kwargs
    ):
        super().__init__(callback, *args, **kwargs)

        self._is_async = is_async

    async def __aenter__(self):
        return self.reset()

    async def __aexit__(self, type, value, traceback) -> bool:
        if isinstance(self._callback, Callable) and self._is_async:
            await self._callback(self.duration(), *self._args, **self._kwargs)
        elif isinstance(self._callback, Callable):
            self._callback(self.duration(), *self._args, **self._kwargs)

        return False

    def __call__(self, func: Callable) -> Callable:
        async def wrapper(*args, **kwargs):
            with self:
                return await func(*args, **kwargs)

        async def awrapper(*args, **kwargs):
            async with self:
                return await func(*args, **kwargs)

        if self._is_async:
            return awrapper
        return wrapper
