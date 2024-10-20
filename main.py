from grid import GridMapProcessor
from lawnmower import Lawnmower


def main():
    # Initialize GridMapProcessor with the CSV file
    processor = GridMapProcessor.from_file("pattern_50x50.csv")

    # Retrieve the grid
    grid = processor.grid

    # Plot the grid
    processor.plot_grid_map()

    # Get the starting position
    start_pos_x, start_pos_y = processor.get_start_pos()
    print(f"Start Position: ({start_pos_x}, {start_pos_y})")

    # Initialize the Lawnmower with the starting position and grid dimensions
    lm = Lawnmower(start_pos_x, start_pos_y, 0.1, 0.1, len(grid[0]), len(grid), processor.get_obstacles())

    # Define the time for the simulation
    time = 1000
    visited_positions = []

    # Move the Lawnmower and track visited positions
    for _ in range(time):
        lm.move()
        x, y = lm.get_pos()
        visited_positions.append((x, y))

    print("Obstacles: ", processor.get_obstacles())

    # Draw the path taken by the Lawnmower
    lm.draw_path(visited_positions, time)
    print("Visited Positions: ", visited_positions)

    # Plot the grid with visited tiles
    processor.plot_grid_with_visited_tiles(visited_positions)


if __name__ == '__main__':
    main()
