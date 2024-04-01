from Items.Gear.equippable import Equippable

class HeldItem(Equippable):

    def __init__(self, name, damage, upgrade = 0, traits = [], specialTags = [], speedBoost = 0, actionBoost = 0) -> None:

        super().__init__(name, upgrade, traits, specialTags, damage, speedBoost = speedBoost, actionBoost = actionBoost)

    

