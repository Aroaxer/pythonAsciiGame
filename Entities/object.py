import string
import random

class Object():
    x = 0
    y = 0

    invincible = False
    collides = True

    uid = ""

    def __init__(self, x, y, invincible = False, collides = True, uid = "") -> None:
        self.x = x
        self.y = y

        self.invincible = invincible
        self.collides = collides

        # Assign a fifty character uid to all entities, so that the correct one dies when something has zero hp
        if uid == "":
            for _ in range(50):
                uid += random.choice(string.ascii_lowercase)
        self.uid = uid