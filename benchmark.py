import time
import statistics
from pathfinding import bfs

grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0]
]
times = []
for i in range(10):
    start_time = time.perf_counter()
    result = bfs (grid,(0,0), (0,4))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    elapsed_ms = elapsed_time * 1000
    times.append(elapsed_ms)

mean_time = sum(times) / len(times)
median_time = statistics.median(times)
print(f"mean:{mean_time:.4f}")
print(f"median:{median_time:.4f}")
print(times)