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
        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try:
                if (not slot.upgraded) or (slot.upgradedForm):
                    items.append(slot)
                    itemNames.append(slot.name)
            except AttributeError: pass

        choice = items[utils.promptChoice("Which item would you like to upgrade?", itemNames)]
        choice.upgrade()



    def equip(self, item):
        slots = []
        if type(item) == Weapon:
            slots.append("Mainhand")
        elif type(item) == Armor:
            slots.append("Armor")
        elif type(item) == Helmet:
            slots.append("Helmet")
        elif type(item) == HeldItem:
            slots.append("Offhand")
        elif type(item) == Accessory:
            slots.append("Accessory")
            
        # This code may be necessary if I add items that can go in multiple slots
        if len(slots) == 1:
            self.putOn(item, slots[0])
        elif len(slots) > 1:
            chosenSlot = slots[utils.promptChoice("What slot would you like to equip this in?", slots)]
            self.putOn(item, chosenSlot)

    def getSkillDisplay(self):
        display = ""
        totalIndex = 1
        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try:
                if slot.allActions():
                    display += f"{slot.name} " + (f"({slot.damage} Damage)" if slot.damage else "") + ":\n"
                    for action in slot.allActions():
                        display += f"   {totalIndex}: {action.name}" + ((f", {action.charges} Charge" + ("s" if action.charges != 1 else "")) if action.maxCharges >= 0 else "") + (f", {action.range if action.range > 1 else "Melee"} Range" if action.range else "") + (f", {action.width}x{action.length} Area" if action.width + action.length > 2 else "") + (" - Free Action\n" if action.freeAction else "\n")
                        totalIndex += 1
            except AttributeError: pass

        return display
