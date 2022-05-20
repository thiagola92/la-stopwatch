from datetime import timedelta
from time import sleep
from unittest import TestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(TestCase):
    # Testing if callback is called after 1 second.

    def a(duration):
        assert duration > timedelta(seconds=1)

    @Stopwatch(a)
    def test_decorator(self):
        sleep(1)

    def b(duration):
        assert duration > 1_000_000_000

    @StopwatchNS(b)
    def test_decorator_ns(self):
        sleep(1)

    # Test if even when the function is wrapped
    # still returns the expected result.

    @Stopwatch(print)
    def c(self):
        return True

    def test_decorator_return(self):
        assert self.c()

    @StopwatchNS(print)
    def d(self):
        return True

    def test_decorator_ns_return(self):
        assert self.d()


if __name__ == "__main__":
    main()
