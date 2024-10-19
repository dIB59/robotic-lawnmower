import matplotlib.pyplot as plt
from grid import get_obstacles


class Lawnmower:
    def __init__(self, x=0.0, y=0.0, v_x=0.0, v_y=0.0, grid_len_x=0, grid_len_y=0,
                 obstacles: list[tuple[int, int]] = None):
        self.x = x
        self.y = y

        self.v_x = v_x
        self.v_y = v_y

        self.max_x = grid_len_x
        self.max_y = grid_len_y

        self.obstacles = obstacles

        # if cos(v_x)*cos(v_x) + cos(v_x)*cos(v_x) > 3:
        #     raise AssertionError

    def move(self, dt: int = 1):
        new_x = self.x + self.v_x * dt
        new_y = self.y + self.v_y * dt

        if self.is_in_obstacle(new_x, self.y):
            self.v_x *= -1
        else:
            self.x = new_x

        if self.is_in_obstacle(self.x, new_y):
            self.v_y *= -1
        else:
            self.y = new_y

        if self.x > self.max_x or self.x < 0:
            self.v_x *= -1
        if self.y > self.max_y or self.y < 0:
            self.v_y *= -1

    def get_pos(self) -> (float, float):
        return self.x, self.y

    def draw_path(self, coordinates: list) -> None:
        x_vals = [x for x, y in coordinates]
        y_vals = [y for x, y in coordinates]

        plt.figure(figsize=(self.max_x, self.max_y))
        plt.plot(x_vals, y_vals, linestyle='-', color='blue')

        # Set labels and title
        plt.title("Graph of Visited Positions")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)

        # Show the plot
        plt.show()

    def is_in_obstacle(self, new_x, new_y):
        # Check if the new position is in an obstacle
        for ox, oy in self.obstacles:
            if ox <= new_x <= ox + 1 and oy <= new_y <= oy + 1:
                return True
        return False
