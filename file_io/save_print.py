import sys
import time


f = open("myprint.txt", "w+")
for i in range(100):
    print(f"--{i}--", file=f, flush=True)  # flush=True, write in instantly
    print(f"--{i, i}--", file=sys.stdout)
    time.sleep(0.5)
