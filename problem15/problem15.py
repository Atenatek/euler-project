# Lattice paths
   
# Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


def grid_routes(n):
    # return the number of routes (only right and bottom direction) in a x*x grid)
    size_x = [i for i in range(n + 1)]
    size_y = size_x
    grid = []
    for x in size_x:
        for y in size_y:
            grid.append((x, y))
    patterns = [p for p in grid]
    return patterns

print(grid_routes(3))