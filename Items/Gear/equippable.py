import copy
import math

from Items.item import Item

class Equippable(Item):
    user = None
    upgraded = False
    extraActions = 0
    extraSpeed = 0

    damage = 0
    defense = 0

    traits = []
    specialTags = {}

    slot = ""

    upgradedForm = None

    def __init__(self, name, damage = 0, defense = 0, newTraits = [], specialTags = {}, upgr = None, actionBoost = 0, speedBoost = 0) -> None:
        self.extraActions = actionBoost
        self.extraSpeed = speedBoost
        self.traits = [copy.deepcopy(trait) for trait in newTraits]
        for trait in self.traits:
            trait.tiedEquipment = self
        self.specialTags = specialTags
        self.damage = damage
        self.defense = defense
        self.upgradedForm = upgr
        super().__init__(name)

    def upgrade(self):
        if self.upgraded and self.upgradedForm != None:
            match self.slot:
                case "Mainhand":
                    self.user.putOn(copy.deepcopy(self.upgradedForm))
                case "Offhand":
                    self.user.putOn(copy.deepcopy(self.upgradedForm))
                case "Armor":
                    self.user.putOn(copy.deepcopy(self.upgradedForm))
                case "Helmet":
                    self.user.putOn(copy.deepcopy(self.upgradedForm))
                case "Accessory":
                    self.user.putOn(copy.deepcopy(self.upgradedForm))
        else:
            if self.extraSpeed > 0:
                self.extraSpeed += max(1, math.floor(self.extraSpeed / 2))
            if self.damage > 0:
                self.damage += max(1, math.ceil(self.damage / 3))
            if self.defense > 0:
                self.defense += max(5, math.ceil(self.defense / 5))

            self.upgraded = True
            self.name += "+"

    def allActions(self):
        for trait in self.traits:
            if trait.trigger == "Active":
                yield trait