from Items.item import Item

class Equippable(Item):
    user = None
    upgrade = 0

    traits = []
    specialTags = []

    def __init__(self, name, upgrade = 0, traits = [], specialTags = []) -> None:
        self.upgrade = upgrade
        self.traits = traits
        for trait in self.traits:
            trait.tiedEquipment = self
        self.specialTags = specialTags
        super().__init__(name)