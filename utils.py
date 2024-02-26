import random

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
def promptChoice(startMessage, options):
    print(f"{startMessage}\n")
    for index, option in enumerate(options):
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
        
def promptCoords(prompt):
    print(prompt)
    
    while True:
        choice = input().replace(" ", "")

        nextNonInt = "("

        # Make sure there's no extra characters at the start and end
        if not (choice[0] == "(" and choice[-1] == ")"): continue

        if choice == nextNonInt:
            match choice:
                case "(":
                    nextNonInt = ","
                case ",":
                    nextNonInt - ")"
                case ")":
                    return choice
        else:
            # Check if integer
            try: int(choice)
            except ValueError: continue