import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import unittest


def process_map_csv(file_path: str) -> list[list[int]]:
    print(file_path)
    grid = []

    with open(file_path) as f:
        line = f.readline().replace("\n", "").replace("L", "0").replace("S", "1").replace("O", "2")
        while line:
            num_lst = []
            for num in line.split(","):
                num_lst.append(int(num))

            grid.append(num_lst)
            line = f.readline().replace("\n", "").replace("L", "0").replace("S", "1").replace("O", "2")

        print(grid)
    grid.reverse()  # Move origo to lower left corner
    return grid


def get_start_pos(grid: list[list[int]]) -> (int, int):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 1:
                return j, i


def get_obstacles(grid: list[list[int]]) -> list[(int, int)]:
    obs_list = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 2:
                obs_list.append((j, i))

    return obs_list


def plot_grid_map(grid: list):
    plot_map = grid
    rows = len(plot_map)
    cols = len(plot_map[0])

    # Set the figure size for better visibility
    plt.figure(figsize=(10, 10))

    # Assign color to value: 0 = green, 1 = yellow, 2 = black
    col_map = ListedColormap(['green', 'yellow', 'black'], 'indexed')

    plot_default_map(col_map, cols, plot_map, rows)
    plt.title(f"Colored grid of size {rows}x{cols}", fontsize=14)

    # Show the plot with improved layout
    plt.tight_layout()
    plt.show()


def plot_grid_with_visited_tiles(grid: list[list[int]], visited_positions: list[tuple[float, float]]):
    plot_map = [row[:] for row in grid]
    rows = len(plot_map)
    cols = len(plot_map[0])
    tiles = set()
    for x, y in visited_positions:
        if 0 <= int(y) < rows and 0 <= int(x) < cols:
            tiles.add((int(y), int(x)))
            plot_map[int(y)][int(x)] = 3  # Set visited tiles to 3

    plt.figure(figsize=(10, 10))

    col_map = ListedColormap(['white', 'yellow', 'black', 'red'], 'indexed')

    plot_default_map(col_map, cols, plot_map, rows)
    plt.title(f"Grid with Visited Tiles ({len(tiles)} visited)", fontsize=14)

    # Show the plot with improved layout
    plt.tight_layout()
    plt.show()


def plot_default_map(col_map, cols, plot_map, rows):
    plt.pcolormesh(plot_map, edgecolors='k', linewidth=0.5, cmap=col_map)
    # Get current axis object and set tick marks
    ax = plt.gca()
    ax.set_yticks(range(0, rows + 1, 2))
    ax.set_xticks(range(0, cols + 1, 2))

    ax.tick_params(axis='both', which='major', labelsize=8)

#   L,L,O,L,L
#   L,L,O,L,L
#   L,L,L,L,L
#   L,L,L,S,L
#   magnify by 2 becomes
#   note we convert the S into an L
#   L,L,L,L,O,O,L,L,L,L
#   L,L,L,L,O,O,L,L,L,L
#   L,L,L,L,O,O,L,L,L,L
#   L,L,L,L,O,O,L,L,L,L
#   L,L,L,L,L,L,L,L,L,L
#   L,L,L,L,L,L,L,L,L,L
#   L,L,L,L,L,L,L,L,L,L


def magnify(grid: list[list[str]], size: int):
    big_grid = []

    for row in grid:
        new_row = []
        for num in row:
            for i in range(size):
                new_row.append(num)
        for i in range(size):
            big_grid.append(new_row)

    return big_grid