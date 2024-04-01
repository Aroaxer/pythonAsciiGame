from Items.Gear.equippable import Equippable

class Helmet(Equippable):

    def __init__(self, name, damage = 0, traits = [], speedBoost = 0, actionBoost = 0, upgradedForm = None) -> None:

        super().__init__(name, traits, damage = damage, speedBoost = speedBoost, actionBoost = actionBoost, upgradedForm = upgradedForm)

    

