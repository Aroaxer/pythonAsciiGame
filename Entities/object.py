

class Object():
    x = 0
    y = 0

    invincible = False
    collides = True

    def __init__(self, x, y, invincible = False, collides = True) -> None:
        self.x = x
        self.y = y

        self.invincible = invincible
        self.collides = collides