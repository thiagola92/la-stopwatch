import asyncio

from la_stopwatch import AsyncStopwatch


async def on_finish(duration):
    print(duration)


async def main():
    async with AsyncStopwatch(on_finish, is_async=True):
        await asyncio.sleep(1)


# 0:00:01.001583
asyncio.run(main())
