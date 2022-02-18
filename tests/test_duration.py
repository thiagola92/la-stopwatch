from time import sleep
from datetime import timedelta
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestDuration(TestCase):
    def test_duration(self):
        print("\nTest timedelta")

        with Stopwatch() as stopwatch:
            sleep(1)
            print(stopwatch.duration())
            assert stopwatch.duration() > timedelta(seconds=1)

            sleep(2)
            print(stopwatch.duration())
            assert stopwatch.duration() > timedelta(seconds=3)

            sleep(3)
            print(stopwatch.duration())
            assert stopwatch.duration() > timedelta(seconds=6)

    def test_duration_ns(self):
        print("\nTest nanoseconds")

        with StopwatchNS() as stopwatch:
            sleep(1)
            print(stopwatch.duration())
            assert stopwatch.duration() > 1_000_000_000

            sleep(2)
            print(stopwatch.duration())
            assert stopwatch.duration() > 3_000_000_000

            sleep(3)
            print(stopwatch.duration())
            assert stopwatch.duration() > 6_000_000_000


if __name__ == "__main__":
    main()
