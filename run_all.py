import subprocess
from time import perf_counter

T: float = perf_counter()
for i in range(1, 13):
    t: float = perf_counter()
    print(f"Day {i}")
    subprocess.run([
        "pypy3.10",
        "/".join(__file__.split("/")[:-1]) + f"/Day {i}/main.py"
    ])
    print(f"time used: {perf_counter() - t}s")
    print()
print(f"Total time used: {perf_counter() - T}s")
