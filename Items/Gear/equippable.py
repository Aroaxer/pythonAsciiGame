from Items.item import Item

class Equippable(Item):
    user = None
    upgrade = 0

    traits = []

    def __init__(self, user, upgrade = 0, traits = []) -> None:
        self.user = user
        self.upgrade = upgrade
        self.traits = traits
        super().__init__()