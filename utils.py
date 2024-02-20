
# Returns an index for the entry chosen, starting with 0
def promptChoice(startMessage, options):
    print(f"{startMessage}\n")
    for index, option in enumerate(options):
        print(f"{index + 1}: {option}")
    print("\nEnter an index to make a selection")
    while True:
        try:
            choice = int(input())
            if not choice in range(1, len(options) + 1):
                print("Invalid Index")
                continue
            return choice - 1
        except Exception:
            print("Bad Input")