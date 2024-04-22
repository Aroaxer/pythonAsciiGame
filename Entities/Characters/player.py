from Entities.Characters.character import Character
from Items.Consumables.consumable import Consumable

import settings

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

        if action[:4].lower() == "info":
            try:
                action = int(action[4:])
                trait = self.getFullActionList()[action - 1]
                input(f"\n{trait.name}\n Targeting:\n  {trait.getTargetDesc()}\n Effect:\n  {trait.getEffectDesc()}\n\nPress enter to continue")
            except (ValueError, IndexError): pass
            self.actionsLeft += 1
        else:

            try:
                if self.actionsLeft >= 0 and action.lower() != "pass":
                    self.readAsMove(action, game)
                elif action.lower() != "pass":
                    input("You're out of actions. Enter 'pass' to end your turn, or use your free actions.\nPress enter to clear this prompt.")
                    self.actionsLeft += 1
                else:
                    self.actionsLeft = 0
                    return "End"
            except Exception:
                try:
                        trait = self.getFullActionList()[int(action) - 1]

                        if self.actionsLeft >= 0 or trait.freeAction:
                            if not trait.activate(game, "Active", trait.tiedEquipment, user = self):
                                self.actionsLeft += 1
                        else:
                            input("You're out of actions. Enter 'pass' to end your turn, or use your free actions.\nPress enter to clear this prompt.")
                            self.actionsLeft += 1
                except (ValueError, IndexError):
                    if not action.lower() == "pass":
                        self.actionsLeft += 1
                    else:
                        self.actionsLeft = 0
                        return "End"

        if len(game.enemies) == 0:
            self.actionsLeft = 0

        return ""

    def readAsMove(self, entered, game):
        enArr = entered.replace(" ", "").split(",")
        didMove = False
        for entry in enArr:
            change = int(entry[1:])
            if entry[0] == settings.moveControls[0]:
                self.move(game.encounter, game, cy = -change)
                didMove = True
            elif entry[0] == settings.moveControls[1]:
                self.move(game.encounter, game, cx = -change)
                didMove = True
            elif entry[0] == settings.moveControls[2]:
                self.move(game.encounter, game, cy = change)
                didMove = True
            elif entry[0] == settings.moveControls[3]:
                self.move(game.encounter, game, cx = change)
                didMove = True
        if not didMove:
            self.actionsLeft += 1


    def collect(self, item):
        if type(item) == Consumable:
            pass
        else:
            self.putOn(item)

    def getSkillDisplay(self):
        display = ""
        totalIndex = 1
        for slot in (self.mainhand, self.offhand, self.armor, self.accessory):
            try:
                display += f"\n{slot.name}" + (f" ({slot.damage} Damage)" if slot.damage else "")
                for _ in slot.allActions():
                    display += ":"
                    for action in slot.allActions():
                        display += f"\n   {totalIndex}: {action.name}"
                        display += ((f", {round(action.charges, 3)} Charge" + ("s" if action.charges != 1 else "")) if action.maxCharges >= 0 else "") if not (action.recharge == "Never") else (f", {action.charges} Ready" if action.charges >= 1 else ", Not Ready")
                        display += (f", {action.range} Range" if action.range else "") if action.range != 1 else (", Melee" if action.targeting != "Centered" else ", Centered")
                        display += f", {action.width}x{action.length} Area" if action.width + action.length > 2 else ""
                        display += " - Free Action" if action.freeAction else ""
                        totalIndex += 1
                    break
            except AttributeError: pass

        return display + "\n"
