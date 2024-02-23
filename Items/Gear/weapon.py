from Items.Gear.equippable import Equippable

class Weapon(Equippable):
    damage = 0

    category = ""

    def __init__(self, name, damage, category, upgrade = 0, traits = []) -> None:
        self.damage = damage
        self.category = category

        

        super().__init__(name, upgrade, traits)

    

