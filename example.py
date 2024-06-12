from timeblock import Timeblock
import time

with Timeblock("Sleeping for 0.5 seconds"):
    time.sleep(0.5)

with Timeblock(verbose=False) as t:
    time.sleep(0.5)

print(f"Time taken by block: {t.duration} seconds")
