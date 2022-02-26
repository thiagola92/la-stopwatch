from time import sleep
from datetime import timedelta
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestContextManager(TestCase):
    def test_context_manager(self):
        with Stopwatch() as stopwatch:
            sleep(1)
            assert stopwatch.duration() > timedelta(seconds=1)

    def test_context_manager_ns(self):
        with StopwatchNS() as stopwatch:
            sleep(1)
            assert stopwatch.duration() > 1_000_000_000


if __name__ == "__main__":
    main()
