import time
import statistics

from pathfinding import bfs
from dijkstra import dijkstra
from astar import astar


def generate_empty_grid(rows, cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        grid.append(row)
    return grid


def benchmark_algorithm(algorithm, grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(5):
        algorithm(grid, start, goal)

    times = []

    for i in range(10):
        start_time = time.perf_counter()
        result = algorithm(grid, start, goal)
        end_time = time.perf_counter()

        elapsed_ms = (end_time - start_time) * 1000
        times.append(elapsed_ms)

# Outside the timing loop
    assert result["path"] is not None

    path_length = len(result["path"]) - 1
    total_cost = result.get("total_cost", path_length)

    mean_time = sum(times) / len(times)
    median_time = statistics.median(times)
    return {
    "mean_ms": mean_time,
    "median_ms": median_time,
    "nodes_explored": result.get(
    "nodes_explored",
    result.get("nodes explored")
),
    "path_length": path_length,
    "total_cost": total_cost
}


grid = generate_empty_grid(20, 20)

start = (0, 0)
goal = (0, 19)

algorithms = {
    "BFS": bfs,
    "Dijkstra": dijkstra,
    "A*": astar
}

for name, algorithm in algorithms.items():
    metrics = benchmark_algorithm(algorithm, grid, start, goal)

    print(f"Algorithm: {name}")
    print(f"Mean: {metrics['mean_ms']:.4f} ms")
    print(f"Median: {metrics['median_ms']:.4f} ms")
    print(f"Nodes explored: {metrics['nodes_explored']}")
    print(f"Path length: {metrics['path_length']}")
    print(f"Total cost: {metrics['total_cost']}")
    print()