from Entities.Characters.character import Character

class Player(Character):


    def takeAction(self, game):
        self.speedLeft = self.speed
        self.actionsLeft -= 1

        game.emptyTerminal()
        print(game.assembleMap("str"))

        print(f"Actions Remaining: {self.actionsLeft + 1}")

        action = input()

        try:
            self.readAsMove(action, game)
        except Exception:
            pass

    def readAsMove(self, entered, game):
        enArr = entered.replace(" ", "").split(",")
        for entry in enArr:
            change = int(entry[1:])
            match entry[0]:
                case "l":
                    self.move(game.encounter, game, cx = -change)
                case "r":
                    self.move(game.encounter, game, cx = change)
                case "u":
                    self.move(game.encounter, game, cy = -change)
                case "d":
                    self.move(game.encounter, game, cy = change)