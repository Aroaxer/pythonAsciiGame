from Items.Gear.equippable import Equippable

class HeldItem(Equippable):

    def __init__(self, name, damage, upgrade = 0, traits = []) -> None:

        super().__init__(name, upgrade, traits, damage = damage)

    

