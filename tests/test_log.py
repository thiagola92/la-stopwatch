from time import sleep
from logging import getLogger, basicConfig
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestLog(TestCase):
    def setUp(self) -> None:
        basicConfig(level=0)

        return super().setUp()

    def test_log(self):
        print("\nTest timedelta")

        stopwatch = Stopwatch(logger=getLogger())

        sleep(1)
        stopwatch.log("First sleep took %(duration)s")

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s")

    def test_log_ns(self):
        print("\nTest nanoseconds")

        stopwatch = StopwatchNS(logger=getLogger())

        sleep(1)
        stopwatch.log("First sleep took %(duration)s")

        sleep(1)
        stopwatch.log("Total sleep took %(duration)s")


if __name__ == "__main__":
    main()
