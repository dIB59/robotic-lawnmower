def get_start_pos(grid: list) -> (int, int):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 1:
                return i, j


class Lawnmower:
    def __init__(self, x=0.0, y=0.0, v_x=0.0, v_y=0.0, grid_len_x=0, grid_len_y=0):
        self.x = x
        self.y = y

        self.v_x = v_x
        self.v_y = v_y

        self.max_x = grid_len_x
        self.max_y = grid_len_y

    def move(self, dt: int = 1):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    def get_pos(self) -> (float, float):
        return self.x, self.y

