from grid import GridMapProcessor
from lawnmower import Lawnmower


def main():
    # Initialize GridMapProcessor with the CSV file
    processor = GridMapProcessor.from_file("tricky25x25.csv")

    # Retrieve the grid
    grid = processor.grid

    # Plot the grid
    processor.plot_grid_map()

    # Get the starting position
    start_pos_x, start_pos_y = processor.get_start_pos()
    print(f"Start Position: ({start_pos_x}, {start_pos_y})")

    # Initialize the Lawnmower with the starting position and grid dimensions
    lm = Lawnmower(start_pos_x, start_pos_y,
                   speed=0.3,
                   theta=45,
                   grid_len_x=len(grid[0]),
                   grid_len_y=len(grid),
                   obstacles=processor.get_obstacles()
                   )

    # Define the time for the simulation
    time = 1000
    visited_positions = []

    # Move the Lawnmower and track visited positions
    for _ in range(time):
        x, y = lm.update_position()
        visited_positions.append((x, y))

    print("Obstacles: ", processor.get_obstacles())

    # Draw the path taken by the Lawnmower
    lm.draw_path(visited_positions, time)

    big_grid = processor.magnify(4)
    big_grid.plot_grid_with_visited_tiles(visited_positions)


if __name__ == '__main__':
    # TODO: run in multiple different threads to get coverage time quickly
    # TODO: refactor plot_grid_with_visited_tiles to get coverage separately
    # TODO: add possibility of comparing results with different starting conditions and different collision handlers
    main()
