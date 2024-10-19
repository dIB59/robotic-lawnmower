from grid import process_map_csv, plot_grid_map, get_start_pos, get_obstacles
from lawnmower import Lawnmower


def main():
    grid = process_map_csv("simple.csv")
    plot_grid_map(grid)
    start_pos_x, start_pos_y = get_start_pos(grid)
    print(start_pos_x)

    lm = Lawnmower(start_pos_x, start_pos_y, 0.1, 0.1, 5, 4, get_obstacles(grid))
    time = 0
    visited_positions = []
    while True:
        lm.move()
        x, y = lm.get_pos()
        x_int, y_int = round(x), round(y)
        visited_positions.append((x, y))
        time += 1
        if time > 600:
            break
    print(get_obstacles(grid))

    lm.draw_path(visited_positions)
    print("POSITIONS: ", visited_positions)


main()
