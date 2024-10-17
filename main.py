from grid import process_map_csv, plot_grid_map


def main():
    grid = process_map_csv("simple.csv")
    plot_grid_map(grid)


main()
