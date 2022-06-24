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

time.sleep(1)
print(stopwatch.duration())  # 0:00:01.001374
```

Retrive the current time with `duration()`.  

## record
You can record each *lap time* for future analysis using `record()`.  

```python
stopwatch = Stopwatch()

time.sleep(1)
stopwatch.record()

time.sleep(1)
stopwatch.record()

print(stopwatch.get_record(0))  # 0:00:01.001317
print(stopwatch.get_record(1))  # 0:00:02.002678
```
Use `get_record(n)` to get the nº record.   

## named record
Is possible to give a name for each record.  

```python
stopwatch = Stopwatch()

time.sleep(1)
stopwatch.record("first")

time.sleep(1)
stopwatch.record("second")

time.sleep(1)
stopwatch.record("third")

print(stopwatch.get_record("first"))  # 0:00:01.001374
print(stopwatch.get_record("second"))  # 0:00:02.002231
print(stopwatch.get_record("third"))  # 0:00:03.003551
```

## all records
All records (nameless or not) are available with `get_records()`.  

```python
stopwatch = Stopwatch()

time.sleep(1)
stopwatch.record()

time.sleep(1)
stopwatch.record("second")

time.sleep(1)
stopwatch.record()

# {
#   0: datetime.timedelta(seconds=1, microseconds=392),
#   'second': datetime.timedelta(seconds=2, microseconds=1447),
#   1: datetime.timedelta(seconds=3, microseconds=2614)
# }
print(stopwatch.get_records())
```

## chain calls
Some methods return the `Stopwatch` so you can chain method calls. For example, you can record how much time take to do each action if you reset every time after recording.  

```python
stopwatch = Stopwatch()

time.sleep(1)
stopwatch.record().reset()

time.sleep(1)
stopwatch.record()

print(stopwatch.get_record(0))  # 0:00:01.001267
print(stopwatch.get_record(1))  # 0:00:01.000460
```

## context manager
`Stopwatch` accepts a callback as argument which will be called on exit of context managers receving the duration.  

```python
# 0:00:01.001578
with Stopwatch(print):
    time.sleep(1)
```

The advantage of context manager is that you can interact with `Stopwatch` during the scope.  

```python
# 0:00:00.000082
with Stopwatch(print) as stopwatch:
    time.sleep(1)
    stopwatch.reset()
```

The callback receive any extra arguments during `Stopwatch` initialization and the duration. Duration will be passed inside `kwargs` with the name duration **or** as last argument (in case `kwargs` is empty).  

```python
def on_finish(msg, duration):
    print(msg, duration)

# Success 0:00:01.001218
with Stopwatch(on_finish, "Success"):
    time.sleep(1)
```

It's okay to use inside a class with `self` keyword.  

```python
class Test():
    def on_finish(self, msg, grade, duration):
        print(msg, grade, duration)
    
    def start(self):
        with Stopwatch(self.on_finish, "Success", grade="A+"):
            time.sleep(1)

# Success A+ 0:00:01.001470
Test().start()
```

## decorator 
`Stopwatch` accepts a callback as argument which will be called on exiting decoratored functions.  

```python
@Stopwatch(print)
def main():
    time.sleep(1)


# 0:00:01.001281
main()
```

The callback needs to be identical to the decorated function but with the last argument being duration. Duration will be passed inside `kwargs` with the name duration **or** as last argument (in case `kwargs` is empty).  

```python
def on_finish(student, msg, duration, grade):
    print(student, msg, duration, grade)


@Stopwatch(on_finish)
def main(student, msg="Success", grade="A+"):
    time.sleep(1)


# Bob Success 0:00:01.000698 A+
main("Bob")
```

It's okay to use inside a class with `self` keyword.  

```python
class Test():
    def on_finish(self, student, msg, duration, grade):
        print(student, msg, duration, grade)
    
    @Stopwatch(on_finish)
    def start(self, student, msg="Success", grade="A+"):
        time.sleep(1)

# thiagola92 Success 0:00:01.000500 A+
Test().start("thiagola92")
```

## async
While `Stopwatch` alone doesn't have reason to use asynchronous code, it can fit your asynchronous code easly. You may need this when:  
- Decorating an `async` function
- The Callback is an `async` function

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

It will check whenever you callback is asynchronous or not before calling, so you can change the callback as you feel like without breaking your code.  

## async - decorator
Same as context managers, it will check whenever your callback is asynchronous or not before calling.  

```python
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
