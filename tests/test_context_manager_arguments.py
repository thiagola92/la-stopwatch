import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestContextManager(IsolatedAsyncioTestCase):
    """Test passing arguments"""

    def A(arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    async def B(arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    def test_arguments(self):
        with Stopwatch(TestContextManager.A, 1, 2, 3, kwarg=4):
            pass

    def test_arguments_ns(self):
        with StopwatchNS(TestContextManager.A, 1, 2, 3, kwarg=4):
            pass

    async def test_arguments_2(self):
        async with Stopwatch(TestContextManager.B, 1, 2, 3, kwarg=4):
            pass

    async def test_arguments_ns_2(self):
        async with StopwatchNS(TestContextManager.B, 1, 2, 3, kwarg=4):
            pass


if __name__ == "__main__":
    main()
