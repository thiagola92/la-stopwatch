# la-stopwatch
Measure the amount of time that elapses between *lap times*.  

# install
`pip install la-stopwatch`  

# usage
There is two versions of stopwatch:  
  - `StopwatchNS`
  - `Stopwatch`

While both measure using nanoseconds, the second option convert nanoseconds to `timedelta` before returning any time measurement. All examples will be using `Stopwatch` but both have the same methods.  

## basic
Time start when `Stopwatch` is created.  

```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename", "r") as f:
    raw = f.readlines()

print(stopwatch.duration())  # 0:00:00.000228
```

## record
Record each *lap time* for future analysis.  

```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()
stopwatch.record()

with open("filename2", "r") as f:
    raw = f.readlines()
stopwatch.record()

print(stopwatch.get_record(0))  # 0:00:00.000174
print(stopwatch.get_record(1))  # 0:00:00.000214
```

## named record
Is possible to give a name for each record.  

```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()
stopwatch.record("leo")

with open("filename2", "r") as f:
    raw = f.readlines()
stopwatch.record("thiago")

with open("filename3", "r") as f:
    raw = f.readlines()
stopwatch.record("matheus")

print(stopwatch.get_record("leo"))  # 0:00:00.000167
print(stopwatch.get_record("thiago"))  # 0:00:00.000207
print(stopwatch.get_record("matheus"))  # 0:00:00.000236
```

## all records
All records (nameless or not) are available any time.  

```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()
stopwatch.record()

with open("filename2", "r") as f:
    raw = f.readlines()
stopwatch.record()

with open("filename3", "r") as f:
    raw = f.readlines()
stopwatch.record("last")

# {
#   0: datetime.timedelta(microseconds=203),
#   1: datetime.timedelta(microseconds=251),
#   'last': datetime.timedelta(microseconds=288)
# }
print(stopwatch.get_records())
```

## chain calls
Some methods return the `Stopwatch` so you can chain method calls. For example, you can record how much time take to open each file if you reset every time after recording.  

```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()
stopwatch.record().reset()

with open("filename2", "r") as f:
    raw = f.readlines()
stopwatch.record()

print(stopwatch.get_record(0))  # 0:00:00.000199
print(stopwatch.get_record(1))  # 0:00:00.000041
```

## context manager
Pass a callback function to `Stopwatch` and it'll be called when exit the context manager passing the duration. It's possible to pass more information to callback with `*args` and `**kwargs`.  

```python
from la_stopwatch import Stopwatch

# 0:00:00.000378
with Stopwatch(print):
    with open("filename", "r") as f:
        raw = f.readlines()
```

## decorator 
Same as context manager.  

```python
from la_stopwatch import Stopwatch


@Stopwatch(print)
def read_file():
    with open("filename", "r") as f:
        return f.readlines()


# 0:00:00.000341
read_file()
```
