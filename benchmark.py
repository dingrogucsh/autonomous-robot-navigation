import time
import statistics
from pathfinding import bfs
def generate_empty_grid(rows, cols):
    grid = [
        [0 for col in range(cols)]
        for row in range(rows)
    ]
    return grid
grid = generate_empty_grid(10,10)
goal = (len(grid) - 1, len(grid[0]) - 1)
# Warm-up
for i in range(5):
    bfs(grid, (0,0),goal)
times = []
for i in range(10):
    start_time = time.perf_counter()
    result = bfs (grid,(0,0), goal)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    elapsed_ms = elapsed_time * 1000
    times.append(elapsed_ms)

mean_time = sum(times) / len(times)
median_time = statistics.median(times)
print(f"mean:{mean_time:.4f}")
print(f"median:{median_time:.4f}")
print(times)