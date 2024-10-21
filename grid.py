import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class GridMapProcessor:

    def __init__(self, grid=None, file_path=None):
        if grid:
            self.grid = grid
        elif file_path:
            self.grid = self.process_map_csv(file_path)
        else:
            raise ValueError("Either a grid or a file_path must be provided.")

    @classmethod
    def from_grid(cls, grid: list[list[str | int]]):
        """Alternate constructor to initialize the class with a grid."""
        return cls(grid=grid)

    @classmethod
    def from_file(cls, file_path: str):
        """Alternate constructor to initialize the class with a file."""
        return cls(file_path=file_path)

    @staticmethod
    def process_map_csv(file_path: str) -> list[list[int]]:
        """Reads a CSV file and processes it into a grid."""
        grid = []
        with open(file_path) as f:
            line = f.readline().replace("\n", "").replace("L", "0").replace("S", "1").replace("O", "2")
            while line:
                num_lst = [int(num) for num in line.split(",")]
                grid.append(num_lst)
                line = f.readline().replace("\n", "").replace("L", "0").replace("S", "1").replace("O", "2")
        grid.reverse()  # Move origo to lower left corner
        return grid

    def magnify(self, size: int) -> 'GridMapProcessor':
        """Magnifies the grid by the given size."""
        big_grid = []
        for row in self.grid:
            new_row = []
            for num in row:
                new_row.extend([num] * size)  # Repeat each number `size` times
            for _ in range(size):  # Repeat the whole row `size` times
                big_grid.append(new_row)

        return GridMapProcessor.from_grid(big_grid)

    def get_start_pos(self) -> tuple[int, int]:
        for i, row in enumerate(self.grid):
            for j, char in enumerate(row):
                if char == 1:
                    return j, i

    def get_obstacles(self) -> list[tuple[int, int]]:
        obs_list = []
        for i, row in enumerate(self.grid):
            for j, char in enumerate(row):
                if char == 2:
                    obs_list.append((j, i))
        return obs_list

    def plot_grid_map(self):
        plot_map = self.grid
        rows = len(plot_map)
        cols = len(plot_map[0])

        # Set the figure size for better visibility
        plt.figure(figsize=(10, 10))

        # Assign color to value: 0 = green, 1 = yellow, 2 = black
        col_map = ListedColormap(['green', 'yellow', 'black'], 'indexed')

        self.plot_default_map(col_map, cols, plot_map, rows)
        plt.title(f"Colored grid of size {rows}x{cols}", fontsize=14)

        # Show the plot with improved layout
        plt.tight_layout()
        plt.show()

    def plot_grid_with_visited_tiles(self, visited_positions: list[tuple[float, float]], magnification: int = 1):
        plot_map = [row[:] for row in self.grid]
        rows = len(plot_map)
        cols = len(plot_map[0])
        tiles = set()
        for x, y in visited_positions:
            if 0 <= y * magnification < rows and 0 <= x * magnification < cols:
                tiles.add((int(y * magnification), int(x * magnification)))
                plot_map[int(y * magnification)][int(x * magnification)] = 3  # Mark visited tiles with 3

        plt.figure(figsize=(10, 10))

        col_map = ListedColormap(['white', 'yellow', 'black', 'red'], 'indexed')

        self.plot_default_map(col_map, cols, plot_map, rows)
        coverage_percent = (len(tiles) * 100) /(rows * cols)
        plt.title(f"Grid Tiles ({len(tiles)} visited) {coverage_percent:.2f}% covered", fontsize=14)

        # Show the plot with improved layout
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_default_map(col_map, cols, plot_map, rows):
        plt.pcolormesh(plot_map, edgecolors='k', linewidth=0.5, cmap=col_map)
        # Get current axis object and set tick marks
        ax = plt.gca()
        ax.set_yticks(range(0, rows + 1, 2))
        ax.set_xticks(range(0, cols + 1, 2))

        ax.tick_params(axis='both', which='major', labelsize=8)
