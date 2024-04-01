from Items.Gear.equippable import Equippable

class HeldItem(Equippable):

    def __init__(self, name, damage, traits = [], specialTags = [], speedBoost = 0, actionBoost = 0, upgradedForm = None) -> None:

        super().__init__(name, traits, specialTags, damage, speedBoost = speedBoost, actionBoost = actionBoost, upgradedForm = upgradedForm)

    

