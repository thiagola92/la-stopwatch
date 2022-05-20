import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(IsolatedAsyncioTestCase):
    def A(duration):
        assert duration > timedelta(seconds=1)

    def B(duration):
        assert duration > 1_000_000_000

    async def C(duration):
        assert duration > timedelta(seconds=1)

    async def D(duration):
        assert duration > 1_000_000_000

    @Stopwatch(lambda _: None)
    def E(self):
        return True

    @StopwatchNS(lambda _: None)
    def F(self):
        return True

    @Stopwatch(lambda _: None)
    async def G(self):
        return True

    @StopwatchNS(lambda _: None)
    async def H(self):
        return True

    # Testing if callback is called after 1 second.

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

    # Test if wrapped functions still return their value

    def test_decorator_return(self):
        assert self.E()

    def test_decorator_ns_return(self):
        assert self.F()

    async def test_decorator_return(self):
        assert self.E()

    async def test_decorator_ns_return(self):
        assert self.F()

    async def test_decorator_return(self):
        assert await self.G()

    async def test_decorator_ns_return(self):
        assert await self.H()


if __name__ == "__main__":
    main()
