from Entities.Characters.character import Character
from Items.Gear.weapon import Weapon
from Items.Consumables.consumable import Consumable

import utils

class Player(Character):

    def __init__(self, hp, x, y, speed, actions = 1) -> None:
        super().__init__("Player", hp, x, y, speed, actions)

    def takeAction(self, game):
        self.speedLeft = self.speed
        self.actionsLeft -= 1

        game.emptyTerminal()
        game.displayInfo()

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

    def collect(self, item):
        if type(item) == Consumable:
            pass
        else:
            self.equip(item)

    def equip(self, item):
        slots = []
        if type(item) == Weapon:
            slots.append("Mainhand")
            if "Light" in item.specialTags:
                slots.append("Offhand")
        #elif type(item) == Armor:
                
        if len(slots) == 1:
            self.putOn(item, slots[0])
        elif len(slots > 1):
            chosenSlot = slots[utils.promptChoice("What slot would you like to equip this in?", slots)]
            self.putOn(item, chosenSlot)

    def putOn(self, item, slot):
        match slot:
                case "Mainhand":
                    self.mainhand = item
                case "Offhand":
                    self.offhand = item
                case "Armor":
                    self.armor = item
                case "Helmet":
                    self.armor = item
                case "Accesory":
                    self.accesory = item
