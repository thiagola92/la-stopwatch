from time import sleep
from datetime import timedelta
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestReset(TestCase):
    def test_reset(self):
        print("\nTest timedelta")

        with Stopwatch() as stopwatch:
            sleep(1)
            stopwatch.reset()
            assert stopwatch.duration() < timedelta(seconds=1)

            sleep(2)
            stopwatch.reset()
            assert stopwatch.duration() < timedelta(seconds=2)

            sleep(3)
            stopwatch.reset()
            assert stopwatch.duration() < timedelta(seconds=3)

    def test_reset_ns(self):
        print("\nTest nanoseconds")

        with StopwatchNS() as stopwatch:
            sleep(1)
            stopwatch.reset()
            assert stopwatch.duration() < 1_000_000_000

            sleep(2)
            stopwatch.reset()
            assert stopwatch.duration() < 2_000_000_000

            sleep(3)
            stopwatch.reset()
            assert stopwatch.duration() < 3_000_000_000


if __name__ == "__main__":
    main()
