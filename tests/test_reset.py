from time import sleep
from datetime import timedelta
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestReset(TestCase):
    def test_reset(self):
        stopwatch = Stopwatch()

        sleep(1)
        stopwatch.reset()
        assert stopwatch.duration() < timedelta(seconds=1)

    def test_reset_ns(self):
        stopwatch = StopwatchNS()

        sleep(1)
        stopwatch.reset()
        assert stopwatch.duration() < 1_000_000_000


if __name__ == "__main__":
    main()
