from Items.Gear.equippable import Equippable

class Weapon(Equippable):
    category = ""

    def __init__(self, name, damage, category, traits = [], specialTags = [], speedBoost = 0, actionBoost = 0, upgradedForm = None) -> None:
        self.category = category

        super().__init__(name, traits, specialTags = specialTags, damage = damage, speedBoost = speedBoost, actionBoost = actionBoost, upgradedForm = upgradedForm)

    

