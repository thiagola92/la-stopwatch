import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(IsolatedAsyncioTestCase):
    """Test if wrapped functions still return their value"""

    @Stopwatch(lambda *args: None)
    def A(self):
        return True

    @StopwatchNS(lambda *args: None)
    def B(self):
        return True

    @Stopwatch(lambda *args: None)
    async def C(self):
        return True

    @StopwatchNS(lambda *args: None)
    async def D(self):
        return True

    def test_decorator_return(self):
        assert self.A()

    def test_decorator_ns_return(self):
        assert self.B()

    async def test_decorator_return(self):
        assert self.A()

    async def test_decorator_ns_return(self):
        assert self.B()

    async def test_decorator_return(self):
        assert await self.C()

    async def test_decorator_ns_return(self):
        assert await self.D()


if __name__ == "__main__":
    main()
