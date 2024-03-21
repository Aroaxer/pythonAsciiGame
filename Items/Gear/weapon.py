from Items.Gear.equippable import Equippable

class Weapon(Equippable):
    category = ""

    def __init__(self, name, damage, category, upgrade = 0, traits = [], specialTags = []) -> None:
        self.category = category

        super().__init__(name, upgrade, traits, specialTags = specialTags, damage = damage)

    

