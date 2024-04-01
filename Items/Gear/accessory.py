from Items.Gear.equippable import Equippable

class Accessory(Equippable):

    def __init__(self, name, damage = 0, speedBoost = 0, actionBoost = 0, upgrade = 0, traits = []) -> None:

        super().__init__(name, upgrade, traits, damage = damage, speedBoost = speedBoost, actionBoost = actionBoost)

    

