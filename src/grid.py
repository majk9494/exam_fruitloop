import random

class Grid:
    width = 36
    height = 12
    empty = "."
    wall = "■"

    def __init__(self):
        self.data = [[self.empty for y in range(self.width)]
                     for z in range(self.height)]

    def get(self, x, y):
        # Hindrar att vi läser utanför kartan
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.wall  # behandla utanför kartan som vägg

        return self.data[y][x]

    def set(self, x, y, value):
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        self.set(x, y, self.empty)

    def __str__(self):
        xs = ""
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(self.data[y][x])
            xs += "\n"
        return xs

    def make_walls(self):
        # Yttre väggar
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # H. Inre sammanhängande väggar (ingen instängd yta)
        for x in range(5, 30):
            self.set(x, 4, self.wall)

        for y in range(6, 10):
            self.set(10, y, self.wall)

    def get_random_x(self):
        return random.randint(0, self.width - 1)

    def get_random_y(self):
        return random.randint(0, self.height - 1)

    def is_empty(self, x, y):
        return self.get(x, y) == self.empty