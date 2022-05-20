from asyncio import sleep
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import AsyncStopwatch, AsyncStopwatchNS


class TestAsyncDecorator(IsolatedAsyncioTestCase):
    # Testing if callback is called after 1 second.

    def a(duration):
        assert duration > timedelta(seconds=1)

    @AsyncStopwatch(a)
    async def test_decorator(self):
        await sleep(1)

    def b(duration):
        assert duration > 1_000_000_000

    @AsyncStopwatchNS(b)
    async def test_decorator_ns(self):
        await sleep(1)

    # Testing if async callback is called after 1 second.

    async def c(duration):
        assert duration > timedelta(seconds=1)

    @AsyncStopwatch(c, is_async=True)
    async def test_decorator_async(self):
        await sleep(1)

    async def d(duration):
        assert duration > 1_000_000_000

    @AsyncStopwatchNS(d, is_async=True)
    async def test_decorator_ns_async(self):
        await sleep(1)

    # Test if even when the function is wrapped
    # still returns the expected result.

    @AsyncStopwatch(print)
    async def e(self):
        await sleep(1)
        return True

    async def test_decorator_return(self):
        assert await self.e()

    @AsyncStopwatchNS(print)
    async def f(self):
        await sleep(1)
        return True

    async def test_decorator_ns_return(self):
        assert await self.f()


if __name__ == "__main__":
    main()
