import asyncio
import time
from unittest import TestCase

from la_stopwatch import Stopwatch


class TestREADME(TestCase):
    def test_readme(self):
        stopwatch = Stopwatch()

        time.sleep(1)
        print(stopwatch.duration())  # 0:00:01.001374

        ###############################################

        stopwatch = Stopwatch()

        time.sleep(1)
        stopwatch.record()

        time.sleep(1)
        stopwatch.record()

        print(stopwatch.get_record(0))  # 0:00:01.001317
        print(stopwatch.get_record(1))  # 0:00:02.002678

        ###############################################

        stopwatch = Stopwatch()

        time.sleep(1)
        stopwatch.record("leo")

        time.sleep(1)
        stopwatch.record("thiago")

        time.sleep(1)
        stopwatch.record("matheus")

        print(stopwatch.get_record("leo"))  # 0:00:01.001374
        print(stopwatch.get_record("thiago"))  # 0:00:02.002231
        print(stopwatch.get_record("matheus"))  # 0:00:03.003551

        ###############################################

        stopwatch = Stopwatch()

        time.sleep(1)
        stopwatch.record()

        time.sleep(1)
        stopwatch.record("hello")

        time.sleep(1)
        stopwatch.record()

        # {
        #   0: datetime.timedelta(seconds=1, microseconds=392),
        #   'hello': datetime.timedelta(seconds=2, microseconds=1447),
        #   1: datetime.timedelta(seconds=3, microseconds=2614)
        # }
        print(stopwatch.get_records())

        ###############################################

        stopwatch = Stopwatch()

        time.sleep(1)
        stopwatch.record().reset()

        time.sleep(1)
        stopwatch.record()

        print(stopwatch.get_record(0))  # 0:00:01.001267
        print(stopwatch.get_record(1))  # 0:00:01.000460

        ###############################################

        # 0:00:01.001578
        with Stopwatch(print):
            time.sleep(1)

        ###############################################

        # 0:00:00.000082
        with Stopwatch(print) as stopwatch:
            time.sleep(1)
            stopwatch.reset()

        ###############################################

        def on_finish(msg, duration):
            print(msg, duration)

        # Success 0:00:01.001218
        with Stopwatch(on_finish, "Success"):
            time.sleep(1)

        ###############################################

        class Test:
            def on_finish(self, msg, duration, grade):
                print(msg, duration, grade)

            def start(self):
                with Stopwatch(self.on_finish, "Success", grade="A+"):
                    time.sleep(1)

        # Success 0:00:01.001470 A+
        Test().start()

        ###############################################

        @Stopwatch(print)
        def main():
            time.sleep(1)

        # 0:00:01.001281
        main()

        ###############################################

        def on_finish(msg, duration, grade):
            print(msg, duration, grade)

        @Stopwatch(on_finish, "Success", grade="A+")
        def main():
            time.sleep(1)

        # Success 0:00:01.001084 A+
        main()

        ###############################################

        def on_finish(student, msg, duration, grade):
            print(student, msg, duration, grade)

        @Stopwatch(on_finish, "Success", grade="A+")
        def main(student):
            time.sleep(1)

        # thiagola92 Success 0:00:01.000698 A+
        main("thiagola92")

        ###############################################

        class Test:
            def on_finish(self, student, msg, duration, grade):
                print(student, msg, duration, grade)

            @Stopwatch(on_finish, "Success", grade="A+")
            def start(self, student):
                time.sleep(1)

        # thiagola92 Success 0:00:01.000500 A+
        Test().start("thiagola92")

        ###############################################

        async def on_finish_1(duration):
            print(duration)

        def on_finish_2(duration):
            print(duration)

        async def main():
            async with Stopwatch(on_finish_1):
                await asyncio.sleep(1)

            async with Stopwatch(on_finish_2):
                await asyncio.sleep(1)

        # 0:00:01.001196
        # 0:00:01.001875
        asyncio.run(main())

        ###############################################

        async def on_finish(duration):
            print(duration)

        @Stopwatch(on_finish)
        async def main():
            await asyncio.sleep(1)

        # 0:00:01.002338
        asyncio.run(main())

        ###############################################

        def on_finish(duration):
            print(duration)

        @Stopwatch(on_finish)
        async def main():
            await asyncio.sleep(1)

        # 0:00:01.002063
        asyncio.run(main())
