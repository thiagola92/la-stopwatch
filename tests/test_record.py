from time import sleep
from datetime import timedelta
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestRecord(TestCase):
    def test_record(self):
        print("\nTest timedelta")

        with Stopwatch() as stopwatch:
            sleep(1)
            stopwatch.record()

            sleep(2)
            stopwatch.record()

            sleep(3)
            stopwatch.record()

            assert stopwatch.get_record(0) > timedelta(seconds=1)
            assert stopwatch.get_record(1) > timedelta(seconds=3)
            assert stopwatch.get_record(2) > timedelta(seconds=6)

            print(stopwatch.get_records())

    def test_record_ns(self):
        print("\nTest nanoseconds")

        with StopwatchNS() as stopwatch:
            sleep(1)
            stopwatch.record()

            sleep(2)
            stopwatch.record()

            sleep(3)
            stopwatch.record()

            assert stopwatch.get_record(0) > 1_000_000_000
            assert stopwatch.get_record(1) > 3_000_000_000
            assert stopwatch.get_record(2) > 6_000_000_000

            print(stopwatch.get_records())


if __name__ == "__main__":
    main()
