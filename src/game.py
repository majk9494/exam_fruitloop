from .grid import Grid
from .player import Player
from . import pickups



player = Player(2, 1)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.random_walls(20)
pickups.randomize(g)

start_x = g.width // 2
start_y = g.height // 2
player = Player(start_x, start_y)
g.set_player(player)

# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

command = "a"

# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, I for inventory, Q/X to quit. ")
    command = command.casefold()[:1]

    directions = {
        "w": (0, -1),
        "s": (0, 1),
        "a": (-1, 0),
        "d": (1, 0)
    }

    # 🔹 INVENTORY
    if command == "i":
        print("Inventory:")
        if not inventory:
            print("  (empty)")
        else:
            for item in inventory:
                print(f"  - {item.name} (+{item.value} points)")
        continue   # hoppa över resten av loopen

    # 🔹 RÖRELSE
    if command in directions:
        dx, dy = directions[command]

        if player.can_move(dx, dy, g):

            maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)

            player.move(dx, dy, g)

            if isinstance(maybe_item, pickups.Item):
                score += maybe_item.value
                inventory.append(maybe_item)
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                g.clear(player.pos_x, player.pos_y)

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")