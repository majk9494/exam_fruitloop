import random


# Bas- klass för föremål att plocka upp
class Item:
    def __init__(self, name, value=20, symbol="?"):
        self.name = name      # Namnet (apple, key osv)
        self.value = value    # Poängvärde
        self.symbol = symbol  # Tecknet som visas på kartan

    def __str__(self):
        return self.symbol


# Fälla ger -10 Poäng i avdrag
class Trap:
    def __str__(self):
        return "T"  # Visas som T på kartan



# Kista/Chest
class Chest:
    def __str__(self):
        return "C"


# ORIGINAL-FRUKTER (måste plockas innan exit funkar)
original_fruits = [
    Item("carrot"),
    Item("apple"),
    Item("strawberry"),
    Item("cherry"),
]

# Spade
shovel = Item("shovel", 0, "S")

# Nyckel
key = Item("key", 0, "K")

# Exit
exit_item = Item("exit", 0, "E")


# Slumpar ut alla saker på kartan

def randomize(grid):

    # Lägger ut originalfrukterna
    for fruit in original_fruits:
        place_random(grid, fruit)

    # Lägger ut 2 fällorna
    for _ in range(2):
        place_random(grid, Trap())

    # Lägger ut spaden
    place_random(grid, shovel)

    # Lägg ut 2 nycklar och 2 kistor
    for _ in range(2):
        place_random(grid, Item("key", 0, "K"))
        place_random(grid, Chest())

    # Lägg ut exit
    place_random(grid, exit_item)


# Placera objekt slumpmässigt

def place_random(grid, obj):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, obj)
            break


# Skapar ny frukt (bördig jord
def spawn_random_fruit(grid):
    place_random(grid, random.choice(original_fruits))