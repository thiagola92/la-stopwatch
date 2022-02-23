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

with open("filename", "r") as f:
    raw = f.readlines()

print(stopwatch) # 0:00:04.103807
```

Record each *lap time* for future analysis.  
```python
from la_stopwatch import Stopwatch

stopwatch = Stopwatch()

with open("matheus_grades.txt", "r") as f:
    raw = f.readlines()
stopwatch.record()

with open("leonardo_grades.txt", "r") as f:
    raw = f.readlines()
stopwatch.record()

with open("thiago_grades.txt", "r") as f:
    raw = f.readlines()
stopwatch.record("thiago")

# Dictionary with all records
print(stopwatch.get_records())

# First record in the dictionary
print(stopwatch,get_record(0))

# Record with name "thiago"
print(stopwatch,get_record("thiago"))
```

