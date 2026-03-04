from .grid import Grid
from .player import Player
from . import pickups

g = Grid()
player = Player(g.width // 2, g.height // 2)

g.set_player(player)
g.make_walls()
pickups.randomize(g)

score = 0
inventory = []
moves = 0

# Hur många originalfrukter finns?
remaining_fruits = len(pickups.original_fruits)


def print_status():
    print("--------------------------------")
    print(f"Score: {score}")
    print(f"Inventory: {inventory}")
    print(g)


def handle_move(dx, dy):
    global score, moves, remaining_fruits

    if player.can_move(dx, dy, g, inventory):

        new_x = player.pos_x + dx
        new_y = player.pos_y + dy
        target = g.get(new_x, new_y)

        # Flytta spelaren
        player.move(dx, dy)

        score -= 1   # Lava-golv
        moves += 1


        # Fälla
        if isinstance(target, pickups.Trap):
            score -= 10
            print("You stepped on a trap! -10 points")


        # Kista
        elif isinstance(target, pickups.Chest):
            if "key" in inventory:
                inventory.remove("key")
                score += 100
                print("You opened a chest! +100 points")
                g.clear(new_x, new_y)
            else:
                print("You need a key!")


        # Item
        elif isinstance(target, pickups.Item):

            # EXIT
            if target.name == "exit":
                if remaining_fruits == 0:
                    print("YOU WIN! 🎉")
                    exit()
                else:
                    print("Collect all fruits first!")
                    return

            # Lägg till i inventory
            inventory.append(target.name)
            score += target.value
            print(f"You picked up {target.name}")

            g.clear(new_x, new_y)

            # Om det var en originalfrukt
            if target.name in [f.name for f in pickups.original_fruits]:
                remaining_fruits -= 1


        # Bördig jord (var 25:e drag)
        if moves % 25 == 0:
            pickups.spawn_random_fruit(g)
            print("New fruit has grown!")


# Huvudloop
command = ""

while command != "q":
    print_status()
    command = input("WASD, J+WASD to jump, Q to quit: ").lower()

    # Jump-system
    jump = False
    if command.startswith("j") and len(command) > 1:
        jump = True
        command = command[1]

    steps = 2 if jump else 1

    for _ in range(steps):
        if command == "w":
            handle_move(0, -1)
        elif command == "s":
            handle_move(0, 1)
        elif command == "a":
            handle_move(-1, 0)
        elif command == "d":
            handle_move(1, 0)

print("Game over")