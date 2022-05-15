from datetime import timedelta
from time import sleep
from unittest import TestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDuration(TestCase):
    def test_duration(self):
        stopwatch = Stopwatch()

        sleep(1)
        assert stopwatch.duration() > timedelta(seconds=1)

        sleep(1)
        assert stopwatch.duration() > timedelta(seconds=2)

        sleep(1)
        assert stopwatch.duration() > timedelta(seconds=3)

    def test_duration_ns(self):
        stopwatch = StopwatchNS()

        sleep(1)
        assert stopwatch.duration() > 1_000_000_000

        sleep(1)
        assert stopwatch.duration() > 2_000_000_000

        sleep(1)
        assert stopwatch.duration() > 3_000_000_000


if __name__ == "__main__":
    main()
