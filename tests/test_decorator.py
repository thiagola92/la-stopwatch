from time import sleep
from logging import getLogger, basicConfig
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(TestCase):
    def setUp(self) -> None:
        basicConfig(level=0)

        return super().setUp()

    @Stopwatch(logger=getLogger(), msg="Total operation took %(duration)s")
    def test_decorator(self):
        print("\nTest timedelta")

    @StopwatchNS(logger=getLogger(), msg="Total operation took %(duration)s")
    def test_decorator_ns(self):
        print("\nTest nanoseconds")


if __name__ == "__main__":
    main()
