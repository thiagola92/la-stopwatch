import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestContextManager(IsolatedAsyncioTestCase):
    """Test using stopwatch inside with"""

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


if __name__ == "__main__":
    main()
