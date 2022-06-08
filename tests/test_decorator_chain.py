import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecoratorChain(IsolatedAsyncioTestCase):
    """Test calling function decorated two times"""

    @Stopwatch(lambda _, d: None)
    @Stopwatch(lambda _, d: None)
    def A(self):
        return True

    @StopwatchNS(lambda _, d: None)
    @StopwatchNS(lambda _, d: None)
    def B(self):
        return True

    @Stopwatch(lambda _, d: None)
    @Stopwatch(lambda _, d: None)
    async def C(self):
        return True

    @StopwatchNS(lambda _, d: None)
    @StopwatchNS(lambda _, d: None)
    async def D(self):
        return True

    # Test calling function decorated two times

    def test_calling_two_times(self):
        assert self.A()

    def test_calling_two_times_ns(self):
        assert self.B()

    async def test_calling_two_times_2(self):
        assert await self.C()

    async def test_calling_two_times_ns_2(self):
        assert await self.D()


if __name__ == "__main__":
    main()
