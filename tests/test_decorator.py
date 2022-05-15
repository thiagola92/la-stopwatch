from time import sleep
from unittest import TestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(TestCase):
    @Stopwatch(print)
    def test_decorator(self):
        pass

    @StopwatchNS(print)
    def test_decorator_ns(self):
        pass


if __name__ == "__main__":
    main()
