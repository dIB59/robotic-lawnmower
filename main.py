from grid import process_map_csv, plot_grid_map, get_start_pos, get_obstacles, plot_grid_with_visited_tiles
from lawnmower import Lawnmower


def main():
    # grid = process_map_csv("simple.csv")
    grid = process_map_csv("pattern_50x50.csv")
    plot_grid_map(grid)
    start_pos_x, start_pos_y = get_start_pos(grid)
    print(start_pos_x)

    lm = Lawnmower(start_pos_x, start_pos_y, 0.1, 0.1, len(grid[0]), len(grid), get_obstacles(grid))
    time = 1000
    visited_positions = []
    for _ in range(time):
        lm.move()
        x, y = lm.get_pos()
        visited_positions.append((x, y))
    print(get_obstacles(grid))

    lm.draw_path(visited_positions, time)
    print("POSITIONS: ", visited_positions)

    plot_grid_with_visited_tiles(grid, visited_positions)


main()
