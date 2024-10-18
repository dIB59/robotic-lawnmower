import matplotlib.pyplot as plt


class Lawnmower:
    def __init__(self, x=0.0, y=0.0, v_x=0.0, v_y=0.0, grid_len_x=0, grid_len_y=0):
        self.x = x
        self.y = y

        self.v_x = v_x
        self.v_y = v_y

        self.max_x = grid_len_x
        self.max_y = grid_len_y

        # if cos(v_x)*cos(v_x) + cos(v_x)*cos(v_x) > 3:
        #     raise AssertionError

    def move(self, dt: int = 1):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

        if self.x > self.max_x:
            self.v_x *= -1

        if self.y > self.max_y:
            self.v_y *= -1

        if self.x < 0:
            self.v_x *= -1

        if self.y < 0:
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
