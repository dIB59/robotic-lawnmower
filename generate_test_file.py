import numpy as np
import pandas as pd


# Function to generate a grid pattern with random placement of '0' and 'S'
def generate_pattern(rows, cols, num_zeros=2, num_s=1):
    grid = np.full((rows, cols), 'L')  # Initialize grid with 'L'

    # Randomly place '0's
    for _ in range(num_zeros):
        x, y = np.random.randint(0, rows), np.random.randint(0, cols)
        grid[x, y] = 'O'

    # Randomly place 'S'
    for _ in range(num_s):
        x, y = np.random.randint(0, rows), np.random.randint(0, cols)
        grid[x, y] = 'S'

    return grid


# Function to generate and write grid pattern to file
def generate_file():
    size = int(input("Enter grid size: "))  # Input grid size
    pattern = generate_pattern(size, size, num_zeros=(size * size)//10)
    df = pd.DataFrame(pattern)
    filename = f"pattern_{size}x{size}.csv"
    df.to_csv(f'{filename}', index=False, header=False)
    print(f"File saved as {filename}")


generate_file()
