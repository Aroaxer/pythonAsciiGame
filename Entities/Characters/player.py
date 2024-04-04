from Entities.Characters.character import Character
from Items.Consumables.consumable import Consumable

import premades as pre

import utils

class Player(Character):

    def __init__(self, hp, x, y, speed, actions = 1) -> None:
        super().__init__("Player", hp, x, y, speed, actions)

    def takeAction(self, game):
        self.rechargeTraits("Action")

        if self.hp > self.maxHp:
            self.hp = self.maxHp

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
                try:
                    trait = self.getFullActionList()[int(action) - 1]
                    if not trait.activate(game, "Active", trait.tiedEquipment, user = self):
                        self.actionsLeft += 1
                except IndexError:
                    raise ValueError
            except ValueError:
                if not action == "pass":
                    self.actionsLeft += 1

        if len(game.enemies) == 0:
            self.actionsLeft = 0

        return ""

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

    def getUpgrade(self):
        items = []
        itemNames = []
        for slot in (self.mainhand, self.offhand, self.armor, self.accessory):
            try:
                if (not slot.upgraded) or (slot.upgradedForm):
                    items.append(slot)
                    itemNames.append(slot.name)
            except AttributeError: pass

        choice = items[utils.promptChoice("Which item would you like to upgrade?", itemNames)]
        choice.upgrade()

    def equip(self, item):
        self.putOn(item, item.slot)

    def getSkillDisplay(self):
        display = ""
        totalIndex = 1
        for slot in (self.mainhand, self.offhand, self.armor, self.accessory):
            try:
                display += f"\n{slot.name}" + (f" ({slot.damage} Damage)" if slot.damage else "")
                for _ in slot.allActions():
                    display += ":"
                    for action in slot.allActions():
                        display += f"\n   {totalIndex}: {action.name}" + ((f", {action.charges} Charge" + ("s" if action.charges != 1 else "")) if action.maxCharges >= 0 else "")
                        display += (f", {action.range} Range" if action.range else "") if action.range != 1 else ", Melee"
                        display += f", {action.width}x{action.length} Area" if action.width + action.length > 2 else ""
                        display += " - Free Action" if action.freeAction else ""
                        totalIndex += 1
                    break
            except AttributeError: pass

        return display + "\n"
