from Items.item import Item

class Consumable(Item):
    name = ""
    # 'effect' is a Trait
    effect = None

    def __init__(self, name, effect) -> None:
        self.name = name
        self.effect = effect
        super().__init__()