import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestContextManager(IsolatedAsyncioTestCase):
    def A(duration):
        assert duration > timedelta(seconds=1)

    def B(duration):
        assert duration > 1_000_000_000

    async def C(duration):
        assert duration > timedelta(seconds=1)

    async def D(duration):
        assert duration > 1_000_000_000

    def E(arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    async def F(arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    # Test using stopwatch inside with

    def test_context_manager(self):
        with Stopwatch() as stopwatch:
            time.sleep(1)
            assert stopwatch.duration() > timedelta(seconds=1)

    def test_context_manager_ns(self):
        with StopwatchNS() as stopwatch:
            time.sleep(1)
            assert stopwatch.duration() > 1_000_000_000

    async def test_context_manager_2(self):
        with Stopwatch() as stopwatch:
            await asyncio.sleep(1)
            assert stopwatch.duration() > timedelta(seconds=1)

    async def test_context_manager_ns_2(self):
        with StopwatchNS() as stopwatch:
            await asyncio.sleep(1)
            assert stopwatch.duration() > 1_000_000_000

    # Test if callback is called after 1 second

    def test_context_manager_cb(self):
        with Stopwatch(TestContextManager.A):
            time.sleep(1)

    def test_context_manager_cb_ns(self):
        with StopwatchNS(TestContextManager.B):
            time.sleep(1)

    async def test_context_manager_cb_2(self):
        with Stopwatch(TestContextManager.A):
            await asyncio.sleep(1)

    async def test_context_manager_cb_ns_2(self):
        with StopwatchNS(TestContextManager.B):
            await asyncio.sleep(1)

    async def test_context_manager_cb_3(self):
        async with Stopwatch(TestContextManager.C):
            await asyncio.sleep(1)

    async def test_context_manager_cb_ns_3(self):
        async with StopwatchNS(TestContextManager.D):
            await asyncio.sleep(1)

    # Test passing arguments

    def test_arguments(self):
        with Stopwatch(TestContextManager.E, 1, 2, 3, kwarg=4):
            pass

    def test_arguments_ns(self):
        with StopwatchNS(TestContextManager.E, 1, 2, 3, kwarg=4):
            pass

    async def test_arguments_2(self):
        async with Stopwatch(TestContextManager.F, 1, 2, 3, kwarg=4):
            pass

    async def test_arguments_ns_2(self):
        async with StopwatchNS(TestContextManager.F, 1, 2, 3, kwarg=4):
            pass


if __name__ == "__main__":
    main()
