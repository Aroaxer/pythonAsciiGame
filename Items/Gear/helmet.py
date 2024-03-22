from Items.Gear.equippable import Equippable

class Helmet(Equippable):

    def __init__(self, name, damage = 0, upgrade = 0, traits = []) -> None:

        super().__init__(name, upgrade, traits, damage = damage)

    

