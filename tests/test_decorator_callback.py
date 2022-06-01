import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(IsolatedAsyncioTestCase):
    """Testing if callback is called after 1 second"""

    def A(self, duration):
        assert duration > timedelta(seconds=1)

    def B(self, duration):
        assert duration > 1_000_000_000

    async def C(self, duration):
        assert duration > timedelta(seconds=1)

    async def D(self, duration):
        assert duration > 1_000_000_000

    @Stopwatch(A)
    def test_decorator(self):
        time.sleep(1)

    @StopwatchNS(B)
    def test_decorator_ns(self):
        time.sleep(1)

    @Stopwatch(A)
    async def test_decorator_2(self):
        await asyncio.sleep(1)

    @StopwatchNS(B)
    async def test_decorator_ns_2(self):
        await asyncio.sleep(1)

    @Stopwatch(C)
    async def test_decorator_3(self):
        await asyncio.sleep(1)

    @StopwatchNS(D)
    async def test_decorator_ns_3(self):
        await asyncio.sleep(1)


if __name__ == "__main__":
    main()
