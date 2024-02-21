from Items.Gear.equippable import Equippable

class Weapon(Equippable):
    attacks = []

    category = ""

    def __init__(self, attacks, category, upgrade = 0, traits = []) -> None:
        self.attacks = attacks
        self.category = category
        super().__init__(upgrade, traits)

    

