from time import sleep
from logging import getLogger, basicConfig
from unittest import TestCase, main
from la_stopwatch import Stopwatch, StopwatchNS


class TestContextManager(TestCase):
    def setUp(self) -> None:
        basicConfig(level=0)

        return super().setUp()

    def test_context_manager(self):
        print("\nTest timedelta")

        with Stopwatch(logger=getLogger(), msg="Total operation took %(duration)s"):
            sleep(1)

    def test_context_manager_ns(self):
        print("\nTest nanoseconds")

        with StopwatchNS(logger=getLogger(), msg="Total operation took %(duration)s"):
            sleep(1)


if __name__ == "__main__":
    main()
