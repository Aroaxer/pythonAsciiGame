from Items.Gear.equippable import Equippable

class Weapon(Equippable):
    damage = 0
    attacks = []

    category = ""

    def __init__(self, name, damage, attacks, category, upgrade = 0, traits = []) -> None:
        self.attacks = attacks
        self.damage = damage
        self.category = category
        super().__init__(name, upgrade, traits)

    

