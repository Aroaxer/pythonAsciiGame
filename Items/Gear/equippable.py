import copy
import math

from Items.item import Item

class Equippable(Item):
    # Stores the actual entity followed by the slot
    user = (None, None)
    upgraded = False
    extraActions = 0
    extraSpeed = 0

    damage = 0

    traits = []
    specialTags = []

    upgradedForm = None

    def __init__(self, name, traits = [], specialTags = [], damage = 0, upgradedForm = None, actionBoost = 0, speedBoost = 0) -> None:
        self.extraActions = actionBoost
        self.extraSpeed = speedBoost
        self.traits = traits
        for trait in self.traits:
            trait.tiedEquipment = self
        self.specialTags = specialTags
        self.damage = damage
        self.upgradedForm = upgradedForm
        super().__init__(name)

    def upgrade(self):
        if self.upgraded and self.upgradedForm != None:
            match self.user[1]:
                case "Mainhand":
                    self.user[0].putOn(copy.deepcopy(self.upgradedForm), "Mainhand")
                case "Offhand":
                    self.user[0].putOn(copy.deepcopy(self.upgradedForm), "Offhand")
                case "Armor":
                    self.user[0].putOn(copy.deepcopy(self.upgradedForm), "Armor")
                case "Helmet":
                    self.user[0].putOn(copy.deepcopy(self.upgradedForm), "Helmet")
                case "Accessory":
                    self.user[0].putOn(copy.deepcopy(self.upgradedForm), "Accessory")
        else:
            if self.extraSpeed > 0:
                self.extraSpeed += max(1, math.floor(self.extraSpeed / 2))
            if self.extraActions > 0:
                self.extraActions += max(1, math.floor(self.extraActions / 2))
            if self.damage > 0:
                self.damage += max(2, math.ceil(self.damage / 3))

            self.upgraded = True
            self.name += "+"