class Player:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy

    # Kontrollerar om spelaren får röra sig
    def can_move(self, dx, dy, grid, inventory):
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        target = grid.get(new_x, new_y)

        # Om det är en vägg
        if target == grid.wall:

            # Om spelaren har en spade
            if "shovel" in inventory:
                inventory.remove("shovel")      # Spaden förbrukas
                grid.clear(new_x, new_y)       # Ta bort väggen
                print("You broke a wall using the shovel!")
                return True

            return False  # Ingen spade = kan inte gå

        return True