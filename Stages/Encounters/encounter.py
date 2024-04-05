

class Encounter():
    width = 0
    height = 0

    def __init__(self, width, height) -> None:
        if width % 2 == 0: width += 1
        if height % 2 == 0: height += 1
        self.width = width
        self.height = height