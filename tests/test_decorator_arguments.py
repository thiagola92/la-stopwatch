import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(IsolatedAsyncioTestCase):
    """Test passing arguments"""

    def A(self, arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    async def B(self, arg1, arg2, arg3, duration, kwarg):
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

    @Stopwatch(A, 1, 2, 3, kwarg=4)
    def test_arguments(self):
        pass

    @StopwatchNS(A, 1, 2, 3, kwarg=4)
    def test_arguments_ns(self):
        pass

    @Stopwatch(B, 1, 2, 3, kwarg=4)
    async def test_arguments_2(self):
        pass

    @StopwatchNS(B, 1, 2, 3, kwarg=4)
    async def test_arguments_ns_2(self):
        pass

    @Stopwatch(C, arg1=1, arg2=2, arg3=3)
    def test_arguments_3(self):
        pass

    @StopwatchNS(C, arg1=1, arg2=2, arg3=3)
    def test_arguments_ns_3(self):
        pass

    @Stopwatch(D, arg1=1, arg2=2, arg3=3)
    async def test_arguments_4(self):
        pass

    @StopwatchNS(D, arg1=1, arg2=2, arg3=3)
    async def test_arguments_ns_4(self):
        pass


if __name__ == "__main__":
    main()
