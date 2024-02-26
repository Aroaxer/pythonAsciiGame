from Items.item import Item

class Equippable(Item):
    user = None
    upgrade = 0

    dmg = 0
    def getDmg(self): return self.dmg * (1 + (self.upgrade / 5))
    def setDmg(self, dmg): self.dmg = dmg
    damage = property(fget=getDmg, fset=setDmg)

    traits = []
    specialTags = []

    upgradedForm = None

    def __init__(self, name, upgrade = 0, traits = [], specialTags = [], damage = 0, upgradedForm = None) -> None:
        self.upgrade = upgrade
        self.traits = traits
        for trait in self.traits:
            trait.tiedEquipment = self
        self.specialTags = specialTags
        self.damage = damage
        self.upgradedForm = upgradedForm
        super().__init__(name)

    def upgrade(self):
        self.upgrade += 1
        if self.upgrade > 5:
            self = self.upgradedForm