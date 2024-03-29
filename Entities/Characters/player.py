from Entities.Characters.character import Character
from Items.Gear.weapon import Weapon
from Items.Gear.armor import Armor
from Items.Gear.helmet import Helmet
from Items.Gear.heldItem import HeldItem
from Items.Gear.accessory import Accessory
from Items.Consumables.consumable import Consumable

import premades as pre

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

        if len(game.enemies) == 0:
            self.actionsLeft = 0

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

        if self.mainhand != None:
            items.append(self.mainhand)
            itemNames.append(self.mainhand.name)
        if self.offhand != None:
            items.append(self.offhand)
            itemNames.append(self.offhand.name)
        if self.armor != None:
            items.append(self.armor)
            itemNames.append(self.armor.name)
        if self.helmet != None:
            items.append(self.helmet)
            itemNames.append(self.helmet.name)
        if self.accessory != None:
            items.append(self.accessory)
            itemNames.append(self.accessory.name)

        choice = items[utils.promptChoice("Which item would you like to upgrade?", itemNames)]
        choice.gainUpgrade()



    def equip(self, item):
        slots = []
        if type(item) == Weapon:
            slots.append("Mainhand")
            if "Light" in item.specialTags:
                slots.append("Offhand")
        elif type(item) == Armor:
            slots.append("Armor")
        elif type(item) == Helmet:
            slots.append("Helmet")
        elif type(item) == HeldItem:
            slots.append("Offhand")
        elif type(item) == Accessory:
            slots.append("Accessory")
                
        if len(slots) == 1:
            self.putOn(item, slots[0])
        elif len(slots) > 1:
            chosenSlot = slots[utils.promptChoice("What slot would you like to equip this in?", slots)]
            self.putOn(item, chosenSlot)

    def getSkillDisplay(self):
        actions = self.getFullActionList()

        display = ""
        for index, action in enumerate(actions):
            display += f"{index + 1}: {action.name}" + ((f", {action.charges} Charge" + ("s" if action.charges != 1 else "")) if action.maxCharges >= 0 else "") + (" - Free Action\n" if action.freeAction else "\n")

        return display
