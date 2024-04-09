import random
import re

def getXRandom(source, number = 1):
    entries = []
    while number > 0:
        entries.append(source[random.randint(0, len(source) - 1)])
        number -= 1
    return entries

def merge(*args):
    list = []
    for entry in args:
        list.extend(entry)
    return list

# Returns an index for the entry chosen, starting with 0
# Separators should be a dictionary {Position : Text}
def promptChoice(startMessage, options, separators = {}):
    print(f"{startMessage}\n")
    for index, option in enumerate(options):
        if index + 1 in separators.keys():
            print(separators[index + 1])
        print(f"{index + 1}: {option}")
    print("\nEnter an index to make a selection, or 'cancel' to cancel this action.")
    while True:
        try:
            entry = input()
            if entry.lower() == "cancel":
                return "Cancelled"
            choice = int(entry)
            if not choice in range(1, len(options) + 1):
                print("Invalid Index")
                continue
            return choice - 1
        except ValueError:
            print("Bad Input")

def promptRegEx(prompt, regEx):
    if prompt != None: print(prompt)
    found = None
    choice = None

    while True:
        choice = input()
        found = re.search(regEx, choice)
        if found != None and found.group() == choice:
            break
        print("Invalid format")

    return choice

# Source is (range, x, y)
def promptCoords(prompt, game, source, cantBeEnemy):
    print(f"{prompt}\nEnter in format (x,y)")

    coords = None
    while True:

        choice = promptRegEx(None, "\(?[0-9]+, *[0-9]+\)?")
        coords = re.findall("[0-9]+", choice)

        for i, entry in enumerate(coords):
            coords[i] = int(entry)

        if not(coords[0] in range(1, game.encounter.width + 1) and coords[1] in range(1, game.encounter.height + 1)):
            print("Point outside map")
            continue

        if not (coords and max(abs(source[1] - coords[0]), abs(source[2] - coords[1])) <= source[0]):
            print("Point out of range")
            continue

        if cantBeEnemy:
            for enemy in game.enemies:
                if (enemy.x, enemy.y) == (coords[0], coords[1]):
                    coords = None
                    print("This action can't target an enemy directly")
                    break
            else:
                break
        else:
            break
        

    return coords

def promptMultipleIds(prompt, options, count):
    print(f"{prompt}\n")
    for index, option in enumerate(options):
        print(f"{index + 1}: {option}")
    print(f"\nEnter {count} " + ("indices" if count > 1 else "index") + " to make a selection, or 'cancel' to cancel this action.")

    ids = []

    while len(ids) != count:
        choice = promptRegEx(None, "[0-9]+(, *[0-9]+)*")
        ids = merge(ids, re.findall("[0-9]+", choice))

    return ids
