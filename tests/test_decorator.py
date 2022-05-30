import asyncio
import time
from datetime import timedelta
from unittest import IsolatedAsyncioTestCase, main

from la_stopwatch import Stopwatch, StopwatchNS


class TestDecorator(IsolatedAsyncioTestCase):
    def A(self, duration):
        assert duration > timedelta(seconds=1)

    def B(self, duration):
        assert duration > 1_000_000_000

    async def C(self, duration):
        assert duration > timedelta(seconds=1)

    async def D(self, duration):
        assert duration > 1_000_000_000

    @Stopwatch(lambda *args: None)
    def E(self):
        return True

    @StopwatchNS(lambda *args: None)
    def F(self):
        return True

    @Stopwatch(lambda *args: None)
    async def G(self):
        return True

    @StopwatchNS(lambda *args: None)
    async def H(self):
        return True

    def I(self, arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    async def J(self, arg1, arg2, arg3, duration, kwarg):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3
        assert kwarg == 4

    def K(self, arg1, arg2, arg3, duration):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    async def L(self, arg1, arg2, arg3, duration):
        assert arg1 == 1
        assert arg2 == 2
        assert arg3 == 3

    @Stopwatch(lambda _, d: None)
    def M(self):
        return True

    @StopwatchNS(lambda _, d: None)
    def N(self):
        return True

    @Stopwatch(lambda _, d: None)
    async def O(self):
        return True

    @StopwatchNS(lambda _, d: None)
    async def P(self):
        return True

    # Testing if callback is called after 1 second.

    @Stopwatch(A)
    def test_decorator(self):
        time.sleep(1)

    @StopwatchNS(B)
    def test_decorator_ns(self):
        time.sleep(1)

    @Stopwatch(A)
    async def test_decorator_2(self):
        await asyncio.sleep(1)

    @StopwatchNS(B)
    async def test_decorator_ns_2(self):
        await asyncio.sleep(1)

    @Stopwatch(C)
    async def test_decorator_3(self):
        await asyncio.sleep(1)

    @StopwatchNS(D)
    async def test_decorator_ns_3(self):
        await asyncio.sleep(1)

    # Test if wrapped functions still return their value

    def test_decorator_return(self):
        assert self.E()

    def test_decorator_ns_return(self):
        assert self.F()

    async def test_decorator_return(self):
        assert self.E()

    async def test_decorator_ns_return(self):
        assert self.F()

    async def test_decorator_return(self):
        assert await self.G()

    async def test_decorator_ns_return(self):
        assert await self.H()

    # Test passing arguments

    @Stopwatch(I, 1, 2, 3, kwarg=4)
    def test_arguments(self):
        pass

    @StopwatchNS(I, 1, 2, 3, kwarg=4)
    def test_arguments_ns(self):
        pass

    @Stopwatch(J, 1, 2, 3, kwarg=4)
    async def test_arguments_2(self):
        pass

    @StopwatchNS(J, 1, 2, 3, kwarg=4)
    async def test_arguments_ns_2(self):
        pass

    @Stopwatch(K, arg1=1, arg2=2, arg3=3)
    def test_arguments_3(self):
        pass

    @StopwatchNS(K, arg1=1, arg2=2, arg3=3)
    def test_arguments_ns_3(self):
        pass

    @Stopwatch(L, arg1=1, arg2=2, arg3=3)
    async def test_arguments_4(self):
        pass

    @StopwatchNS(L, arg1=1, arg2=2, arg3=3)
    async def test_arguments_ns_4(self):
        pass

    # Test calling two times

    def test_calling_two_times(self):
        assert self.M()

    def test_calling_two_times_ns(self):
        assert self.N()

    async def test_calling_two_times_2(self):
        assert await self.O()

    async def test_calling_two_times_ns_2(self):
        assert await self.P()


if __name__ == "__main__":
    main()
