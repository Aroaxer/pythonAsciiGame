import random

from Stages.Encounters.encounter import Encounter
from Entities.Characters.enemy import Enemy

class Stage():
    name = ""

    minWidth = 0
    maxWidth = minWidth

    minHeight = 0
    maxHeight = minHeight

    enemies = []

    length = 0
    # Stores the indices in the premades list that this stage can follow
    prevStages = []

    def __init__(self, name, enemies, minWidth, minHeight, maxWidth = -1, maxHeight = -1, length = 10, prevStages = []) -> None:
        self.name = name
        self.length = length
        self.prevStages = prevStages

        self.minWidth = minWidth
        self.minHeight = minHeight
        self.maxWidth = maxWidth if maxWidth > 0 else minWidth
        self.maxHeight = maxHeight if maxHeight > 0 else minHeight
        self.enemies = enemies

    def genEncounter(self, desEnemies):
        enc = Encounter(random.randint(self.minWidth, self.maxWidth), random.randint(self.minHeight, self.maxHeight))
        enems = []
        while desEnemies > 0:
            index = random.randint(0, len(self.enemies) - 1)
            validCoords = False
            while not validCoords:
                x, y = (random.randint(1, enc.width), random.randint(1, enc.height - 2))

                # Confirm valid coords
                validCoords = True
                for enem in enems:
                    if x == enem.x or y == enem.y:
                        validCoords = False

            enems.append(Enemy(self.enemies[index][0], self.enemies[index][1], x, y))
            desEnemies -= 1
        return [enc, enems]