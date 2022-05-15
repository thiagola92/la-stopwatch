from datetime import timedelta
from time import sleep
from unittest import TestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestContextManager(TestCase):
    def test_context_manager(self):
        with Stopwatch(print) as stopwatch:
            sleep(1)
            assert stopwatch.duration() > timedelta(seconds=1)

    def test_context_manager_ns(self):
        with StopwatchNS(print) as stopwatch:
            sleep(1)
            assert stopwatch.duration() > 1_000_000_000


if __name__ == "__main__":
    main()
