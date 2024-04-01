from Items.Gear.equippable import Equippable

class Accessory(Equippable):

    def __init__(self, name, damage = 0, speedBoost = 0, actionBoost = 0, traits = [], upgradedForm = None) -> None:

        super().__init__(name, traits, damage = damage, speedBoost = speedBoost, actionBoost = actionBoost, upgradedForm = upgradedForm)

    

