
class Player:
    marker = "@"


    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.inventory = []  # <-- här sparas alla pickups

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy, grid):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        if (dx > 1 and dx < g.width -2) or (dy > 1 and dy < g.height -2):
            self.pos_x += dx
            self.pos_y += dy

        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):

        return True
        #TODO: returnera True om det inte står något i vägen


