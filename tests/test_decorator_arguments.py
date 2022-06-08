import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(IsolatedAsyncioTestCase):
    """Test passing arguments"""

    def A(self, arg1, arg2, arg3, kwarg, duration):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    async def B(self, arg1, arg2, arg3, kwarg, duration):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    def C(self, arg1, arg2, arg3, duration):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    async def D(self, arg1, arg2, arg3, duration):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    @Stopwatch(A)
    def test_arguments(self, arg1=1, arg2=2, arg3=3, kwarg=4):
        pass

    @StopwatchNS(A)
    def test_arguments_ns(self, arg1=1, arg2=2, arg3=3, kwarg=4):
        pass

    @Stopwatch(B)
    async def test_arguments_2(self, arg1=1, arg2=2, arg3=3, kwarg=4):
        pass

    @StopwatchNS(B)
    async def test_arguments_ns_2(self, arg1=1, arg2=2, arg3=3, kwarg=4):
        pass


if __name__ == "__main__":
    main()
