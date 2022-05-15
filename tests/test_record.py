from datetime import timedelta
from time import sleep
from unittest import TestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestRecord(TestCase):
    def test_record(self):
        stopwatch = Stopwatch()

        sleep(1)
        stopwatch.record()

        sleep(1)
        stopwatch.record()

        sleep(1)
        stopwatch.record()

        assert stopwatch.get_record(0) > timedelta(seconds=1)
        assert stopwatch.get_record(1) > timedelta(seconds=2)
        assert stopwatch.get_record(2) > timedelta(seconds=3)

    def test_record_ns(self):
        stopwatch = StopwatchNS()

        sleep(1)
        stopwatch.record()

        sleep(1)
        stopwatch.record()

        sleep(1)
        stopwatch.record()

        assert stopwatch.get_record(0) > 1_000_000_000
        assert stopwatch.get_record(1) > 2_000_000_000
        assert stopwatch.get_record(2) > 3_000_000_000

    def test_record_name(self):
        stopwatch = Stopwatch()

        sleep(1)
        stopwatch.record("first")

        sleep(1)
        stopwatch.record("second")

        assert stopwatch.get_record("first") > timedelta(seconds=1)
        assert stopwatch.get_record("second") > timedelta(seconds=2)

    def test_record_name_ns(self):
        stopwatch = StopwatchNS()

        sleep(1)
        stopwatch.record("first")

        sleep(1)
        stopwatch.record("second")

        assert stopwatch.get_record("first") > 1_000_000_000
        assert stopwatch.get_record("second") > 2_000_000_000


if __name__ == "__main__":
    main()
