# la-stopwatch
Measure the amount of time that elapses between *lap times*.  

# install
`pip install la-stopwatch`  

# usage
There is two versions of stopwatch:  
  - `StopwatchNS`
  - `Stopwatch`

While both measure using nanoseconds, the second option convert nanoseconds to `timedelta` before returning any time measurement. All examples will be using `Stopwatch` but both have the same methods.  

Time start when `Stopwatch` is created.  
```python
from la_stopwatch import Stopwatch


stopwatch = Stopwatch()

with open("filename", "r") as f:
    raw = f.readlines()

print(stopwatch.duration()) # 0:00:00.000292
print(stopwatch) # same as above
```

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

with open("filename3", "r") as f:
    raw = f.readlines()
stopwatch.record("last record")

# Dictionary with all records
print(stopwatch.get_records())

# First record in the dictionary
print(stopwatch.get_record(0))

# Record with name "last record"
print(stopwatch.get_record("last record"))
```

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

print(stopwatch.get_record(0))
print(stopwatch.get_record(1))
```

Use `log()` method to log the duration.  
```python
from logging import basicConfig
from la_stopwatch import Stopwatch


# To show log level DEBUG
basicConfig(level=0)

stopwatch = Stopwatch()

with open("filename", "r") as f:
    raw = f.readlines()

stopwatch.log("Duration: %(duration)s")
```

There is support for context manager.  
```python
from la_stopwatch import Stopwatch


with Stopwatch("Duration: %(duration)s"):
    with open("filename", "r") as f:
        raw = f.readlines()
```

And support for decorator.  
```python
from la_stopwatch import Stopwatch


@Stopwatch("Duration: %(duration)s")
def open_file():
    with open("filename", "r") as f:
        raw = f.readlines()
```
