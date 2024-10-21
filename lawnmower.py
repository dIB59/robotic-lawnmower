import math
import matplotlib.pyplot as plt


class Lawnmower:
    def __init__(self, x=0.0, y=0.0, speed=0.3,
                 grid_len_x=0, grid_len_y=0,
                 # speed: int = 0.3,  #remember this bug, when speed is too high, covered tiles are skipped
                 theta: int = 45,
                 dt: float = 0.5,
                 obstacles: list[tuple[int, int]] = None):

        self.x = x
        self.y = y

        self.theta = math.radians(theta)
        self.v_x = round(speed * math.cos(theta), 1)
        self.v_y = round(speed * math.sin(theta), 1)

        self.max_x = grid_len_x
        self.max_y = grid_len_y

        self.dt = dt

        self.obstacles = obstacles


    def update_position(self) -> (float, float):
        new_x = self.x + self.v_x * self.dt
        new_y = self.y + self.v_y * self.dt

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

        print()
        print(self.v_x, self.v_y)
        print(self.x, self.y)

        return self.x, self.y

    def get_pos(self) -> (float, float):
        return self.x, self.y

    def draw_path(self, coordinates: list, time: int) -> None:
        x_vals = [x for x, y in coordinates]
        y_vals = [y for x, y in coordinates]

        plt.figure(figsize=(self.max_x, self.max_y))
        plt.plot(x_vals, y_vals, linestyle='-', color='blue')

        # Set axis limits to always go to max_x and max_y
        plt.xlim(0, self.max_x)
        plt.ylim(0, self.max_y)

        # Set labels and title
        plt.title(f"Graph of Visited Positions in {time} seconds")
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
