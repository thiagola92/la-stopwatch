# la-stopwatch
Measure the amount of time that elapses between *lap times*.  

# install
`pip install la-stopwatch`  

# usage synchronous
There is two versions of synchronous stopwatch:  
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

## context manager
Pass a callback function to `Stopwatch` and it'll be called when exit the context manager passing the duration.  

```python
from time import sleep

from la_stopwatch import Stopwatch

# 0:00:01.001578
with Stopwatch(print):
    sleep(1)
```

Any extra argument or keyword argument will be passed to the callback after the duration.  

```python
from time import sleep

from la_stopwatch import Stopwatch


def on_finish(duration, msg):
    print(duration, msg)


# 0:00:01.001766 - Success!
with Stopwatch(on_finish, "- Success!"):
    sleep(1)
```

## decorator 
Same as context manager but now as decorator 😂.  

```python
from time import sleep

from la_stopwatch import Stopwatch


@Stopwatch(print)
def main():
    sleep(1)


# 0:00:01.001745
main()
```

# usage asynchronous
There is two versions of asynchronous stopwatch:  
  - `AsyncStopwatchNS`
  - `AsyncStopwatch`

There is two occasions that you need them:  
  - Your callback is asynchronous
  - Decorated function is asynchronous

## context manager
```python
import asyncio

from la_stopwatch import AsyncStopwatch


async def on_finish(duration):
    print(duration)


async def main():
    async with AsyncStopwatch(on_finish, is_async=True):
        await asyncio.sleep(1)


# 0:00:01.001583
asyncio.run(main())
```

## decorator
If your decorated function is asynchronous, you need to decorate with the asynchronous classes.

```python
import asyncio

from la_stopwatch import AsyncStopwatch


@AsyncStopwatch(print)
async def main():
    await asyncio.sleep(1)

# 0:00:01.002297
asyncio.run(main())
```

Notice that the callback doesn't need to be asynchronous.  
In case it is, pass `is_async` as `True`.  

```python
import asyncio

from la_stopwatch import AsyncStopwatch


async def on_finish(duration):
    print(duration)


@AsyncStopwatch(on_finish, is_async=True)
async def main():
    await asyncio.sleep(1)


# 0:00:01.001583
asyncio.run(main())
```