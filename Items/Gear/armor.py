from Items.Gear.equippable import Equippable

class Armor(Equippable):
    defense = 0

    def __init__(self, name, defense = 0, traits=[], specialTags=[], damage=0, speedBoost = 0, actionBoost = 0, upgradedForm = None) -> None:
        self.defense = defense

        super().__init__(name, traits, specialTags, damage, speedBoost = speedBoost, actionBoost = actionBoost, upgradedForm = upgradedForm)

    def upgrade(self):
        self.defense += max(self.defense / 5, 5)

        super().upgrade()