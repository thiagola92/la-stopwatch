# la-stopwatch
Measure the amount of time that elapses between *lap times*.   

# install
`pip install la-stopwatch`  

# usage
There is two versions of stopwatch:  
  - `StopwatchNS`
  - `Stopwatch`

While both measure using nanoseconds, the second option convert nanoseconds to `timedelta` before returning any time measurement. All examples will be using `Stopwatch` because `timedelta` it's easy to read, but it doesn't matter each you use because both have the same methods.  

## basic
The first thing you should know is that time start when `Stopwatch` is created.  

```python
from time import sleep

from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

sleep(1)
print(stopwatch.duration())  # 0:00:01.001374
```
Retrive the current time with `duration()`.  

## record
You can record each *lap time* for future analysis using `record()`.  

```python
from time import sleep

from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

sleep(1)
stopwatch.record()

sleep(1)
stopwatch.record()

print(stopwatch.get_record(0))  # 0:00:01.001317
print(stopwatch.get_record(1))  # 0:00:02.002678
```
Use `get_record(n)` to get the nº record.   

## named record
Is possible to give a name for each record.  

```python
from time import sleep

from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

sleep(1)
stopwatch.record("leo")

sleep(1)
stopwatch.record("thiago")

sleep(1)
stopwatch.record("matheus")

print(stopwatch.get_record("leo"))  # 0:00:01.001374
print(stopwatch.get_record("thiago"))  # 0:00:02.002231
print(stopwatch.get_record("matheus"))  # 0:00:03.003551
```

## all records
All records (nameless or not) are available with `get_records()`.  

```python
from time import sleep

from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

sleep(1)
stopwatch.record()

sleep(1)
stopwatch.record("hello")

sleep(1)
stopwatch.record()

# {
#   0: datetime.timedelta(seconds=1, microseconds=392),
#   'hello': datetime.timedelta(seconds=2, microseconds=1447),
#   1: datetime.timedelta(seconds=3, microseconds=2614)
# }
print(stopwatch.get_records())
```

## chain calls
Some methods return the `Stopwatch` so you can chain method calls. For example, you can record how much time take to do each action if you reset every time after recording.  

```python
from time import sleep

from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

sleep(1)
stopwatch.record().reset()

sleep(1)
stopwatch.record()

print(stopwatch.get_record(0))  # 0:00:01.001267
print(stopwatch.get_record(1))  # 0:00:01.000460
```

## decorator 
`Stopwatch` accepts a callback as argument which will be called on exit of decorators and context managers. The callback receive the duration as first argument and extra arguments or keywords arguments will be passed to the callback after the duration.  

```python
from time import sleep

from la_stopwatch import Stopwatch


@Stopwatch(print, "- Success!")
def main():
    sleep(1)


# 0:00:01.001281 - Success!
main()
```

## context manager
Works the same way as decorators.  

```python
from time import sleep

from la_stopwatch import Stopwatch

# 0:00:01.001578
with Stopwatch(print):
    sleep(1)
```

But you can interact with `Stopwatch` inside the context manager.  

```python
from time import sleep

from la_stopwatch import Stopwatch

# 0:00:00.000082
with Stopwatch(print) as stopwatch:
    sleep(1)
    stopwatch.reset()
```

## async
While `Stopwatch` alone doesn't have reason to use asynchronous code, it can fit your asynchronous code easly. You may need this when:  
- Decorating an `async` function
- Callback is an `async` function

## async - context manager
Whenever you are inside an asynchronous function use `async with`.

```python
import asyncio

from la_stopwatch import Stopwatch


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
```

It will check whenever you callback is asynchronous or not before calling, so you can change the callback as you feel like.  

## async - decorator
Same as context managers, it will check whenver your callback is asynchronous or not before calling.  

```python
import asyncio

from la_stopwatch import Stopwatch


async def on_finish(duration):
    print(duration)


@Stopwatch(on_finish)
async def main():
    await asyncio.sleep(1)


# 0:00:01.002338
asyncio.run(main())
```

```python
import asyncio

from la_stopwatch import Stopwatch


def on_finish(duration):
    print(duration)


@Stopwatch(on_finish)
async def main():
    await asyncio.sleep(1)


# 0:00:01.002063
asyncio.run(main())
```