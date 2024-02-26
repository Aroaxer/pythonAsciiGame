from Entities.Characters.character import Character
from Items.Gear.weapon import Weapon
from Items.Gear.armor import Armor
from Items.Consumables.consumable import Consumable

import utils

class Player(Character):

    def __init__(self, hp, x, y, speed, actions = 1) -> None:
        super().__init__("Player", hp, x, y, speed, actions)

    def takeAction(self, game):
        self.rechargeTraits("Action")

        self.speedLeft = self.speed
        self.actionsLeft -= 1

        if len(game.enemies) == 0:
            self.actionsLeft = 0

        game.emptyTerminal()
        game.displayInfo()

        print(f"\nActions Remaining: {self.actionsLeft + 1}")
        print(self.getSkillDisplay())

        action = input()

        try:
            self.readAsMove(action, game)
        except Exception:
            try:
                trait = self.getFullActionList()[int(action) - 1]
                if not trait.activate(game, "Active", trait.tiedEquipment, user = self):
                    self.actionsLeft += 1
            except ValueError:
                if not action == "pass":
                    self.actionsLeft += 1

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
        elif type(item) == Armor:
            slots.append("Armor")
                
        if len(slots) == 1:
            self.putOn(item, slots[0])
        elif len(slots > 1):
            chosenSlot = slots[utils.promptChoice("What slot would you like to equip this in?", slots)]
            self.putOn(item, chosenSlot)

    def getSkillDisplay(self):
        actions = self.getFullActionList()

        display = ""
        for index, action in enumerate(actions):
            display += f"{index + 1}: {action.effectKey}" + ((f", {action.charges} Charge" + ("s" if action.charges > 1 else "") + "\n") if action.maxCharges >= 0 else "\n")

        return display
