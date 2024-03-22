from Items.Gear.equippable import Equippable

class Accessory(Equippable):
    extraActions = 0
    extraSpeed = 0

    def __init__(self, name, damage = 0, speedBoost = 0, actionBoost = 0, upgrade = 0, traits = []) -> None:
        self.extraActions = actionBoost
        self.extraSpeed = speedBoost

        super().__init__(name, upgrade, traits, damage = damage)

    

