from Items.item import Item

class Equippable(Item):
    user = None
    upgrade = 0

    damage = 0

    traits = []
    specialTags = []

    def __init__(self, name, upgrade = 0, traits = [], specialTags = [], damage = 0) -> None:
        self.upgrade = upgrade
        self.traits = traits
        for trait in self.traits:
            trait.tiedEquipment = self
        self.specialTags = specialTags
        self.damage = damage
        super().__init__(name)