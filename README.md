# Timeblock

A very simple library to easily be able to measure time from blocks.

Install it by running:

```bash
pip install git+https://github.com/geoalgo/timeblock.git
```

You can also add the line "git+https://github.com/geoalgo/timeblock.git" to a requirements.txt.

Use it by doing:
```python
from timeblock import Timeblock
import time

with Timeblock("Sleeping for 0.5 seconds"):
    time.sleep(0.5)

with Timeblock(verbose=False) as t:
    time.sleep(0.5)

print(f"Time taken by block: {t.duration} seconds")
```

Which will print something like:

```
Sleeping for 0.5 seconds took 0.5127689838409424 seconds
Time taken by block: 0.5010147094726562 seconds
```

In particular, `Timeblock` takes an optional `name` and an optional boolean `verbose`. If `verbose` is true, then 
the time will be printed when exiting the context.



