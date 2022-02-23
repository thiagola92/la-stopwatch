# la-stopwatch
Measure the amount of time that elapses between *lap times*.  

# install
`pip install la-stopwatch`  

# usage
There is two versions of stopwatch: 
    - `StopwatchNS`
    - `Stopwatch`
While both measure using nanoseconds, the second option convert nanoseconds to `timedelta` before returning any time measurement. All examples will be using `Stopwatch` but both have the same methods, but you should expect only integers when dealing with `StopwatchNS`.  

Time start when `Stopwatch` is created.  
```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()

print(stopwatch) # 0:00:00.000292
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
# {0: datetime.timedelta(microseconds=199), 1: datetime.timedelta(microseconds=260), 'last record': datetime.timedelta(microseconds=304)}
print(stopwatch.get_records())

# First record in the dictionary
# 0:00:00.000199
print(stopwatch.get_record(0))

# Record with name "thiago"
# 0:00:00.000304
print(stopwatch.get_record("last record"))
```

Some methods return the stopwatch so you can chain method calls. For example, you can record how much time take to open each file if you reset every time after recording.  
```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()
stopwatch.record().reset()

with open("filename2", "r") as f:
    raw = f.readlines()
stopwatch.record().reset()

# {0: datetime.timedelta(microseconds=214), 1: datetime.timedelta(microseconds=48)}
print(stopwatch.get_records())
```

The `log()` method will print on screen and record the *lap time*.  
```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("filename1", "r") as f:
    raw = f.readlines()

# Duration: 0:00:00.000160
stopwatch.log("Duration: %(duration)s")
```

If instead of `print()` you want to use a `Logger.debug()`, you can do it passing the logger in the constructor.  
```python
from logging import getLogger, basicConfig
from la_stopwatch import Stopwatch

basicConfig(level=0)

stopwatch = Stopwatch(getLogger())

with open("filename1", "r") as f:
    raw = f.readlines()

# DEBUG:root:Duration: 0:00:00.000160
stopwatch.log("Duration: %(duration)s")
```

There is support for context manager.  
```python
from la_stopwatch import Stopwatch

with Stopwatch() as stopwatch:
    with open("filename1", "r") as f:
        raw = f.readlines()
    
    print(stopwatch) # 0:00:00.000292
```

A message can be pass to the constructor and will only be used when exiting the context manager.  
```python
from logging import getLogger, basicConfig
from la_stopwatch import Stopwatch

# Using print
with Stopwatch(msg="Duration: %(duration)s"):
    with open("filename1", "r") as f:
        raw = f.readlines()

# Using logger
basicConfig(level=0)
with Stopwatch(logger=getLogger(), msg="Duration: %(duration)s"):
    with open("filename1", "r") as f:
        raw = f.readlines()
```