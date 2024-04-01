from Items.Gear.equippable import Equippable

class Armor(Equippable):
    defense = 0

    def __init__(self, name, defense = 0, upgrade=0, traits=[], specialTags=[], damage=0, speedBoost = 0, actionBoost = 0) -> None:
        self.defense = defense

        super().__init__(name, upgrade, traits, specialTags, damage, speedBoost = speedBoost, actionBoost = actionBoost)