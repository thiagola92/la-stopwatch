from time import sleep
from logging import getLogger, basicConfig
from datetime import timedelta
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestLog(TestCase):
    def test_log(self):
        stopwatch = Stopwatch()

        sleep(1)
        stopwatch.log("First sleep took %(duration)s", record=True)

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s", record=True)

        assert stopwatch.get_record(0) > timedelta(seconds=1)
        assert stopwatch.get_record(1) > timedelta(seconds=2)

    def test_log_ns(self):
        stopwatch = StopwatchNS()

        sleep(1)
        stopwatch.log("First sleep took %(duration)s", record=True)

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s", record=True)

        assert stopwatch.get_record(0) > 1_000_000_000
        assert stopwatch.get_record(1) > 2_000_000_000
    
    def test_logger(self):
        basicConfig(level=0)

        stopwatch = Stopwatch(logger=getLogger())

        sleep(1)
        stopwatch.log("First sleep took %(duration)s", record=True)

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s", record=True)

        assert stopwatch.get_record(0) > timedelta(seconds=1)
    
    def test_logger_ns(self):
        basicConfig(level=0)

        stopwatch = StopwatchNS(logger=getLogger())

        sleep(1)
        stopwatch.log("First sleep took %(duration)s", record=True)

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s", record=True)

        assert stopwatch.get_record(0) > 1_000_000_000
    
    def test_log_name(self):
        stopwatch = Stopwatch()

        sleep(1)
        stopwatch.log("First sleep took %(duration)s", "first", record=True)

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s", "total", record=True)

        assert stopwatch.get_record("first") > timedelta(seconds=1)
        assert stopwatch.get_record("total") > timedelta(seconds=2)
    
    def test_log_name_ns(self):
        stopwatch = StopwatchNS()

        sleep(1)
        stopwatch.log("First sleep took %(duration)s", "first", record=True)

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s", "total", record=True)

        assert stopwatch.get_record("first") > 1_000_000_000
        assert stopwatch.get_record("total") > 2_000_000_000



if __name__ == "__main__":
    main()
