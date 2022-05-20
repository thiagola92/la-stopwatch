import asyncio

from la_stopwatch import Stopwatch


def on_finish(duration):
    print(duration)


@Stopwatch(on_finish)
async def main():
    await asyncio.sleep(1)


# 0:00:01.002338
asyncio.run(main())
