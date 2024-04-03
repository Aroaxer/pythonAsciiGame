import random
import math

from Stages.Encounters.encounter import Encounter
from Entities.Characters.enemy import Enemy

class Stage():
    name = ""

    minWidth = 0
    maxWidth = minWidth

    minHeight = 0
    maxHeight = minHeight

    enemies = []
    lootPool = []

    length = 0
    enemCount = 0
    # Stores the names of the stages that this stage can follow
    prevStages = []
    stageOrder = 0

    def __init__(self, name, stageOrder, enemies, lootPool, minWidth, minHeight, maxWidth = -1, maxHeight = -1, length = 10, prevStages = [], enemCount = 0) -> None:
        self.name = name
        self.length = length
        self.enemCount = enemCount
        self.prevStages = prevStages
        self.stageOrder = stageOrder

        self.minWidth = minWidth
        self.minHeight = minHeight
        self.maxWidth = maxWidth if maxWidth > 0 else minWidth
        self.maxHeight = maxHeight if maxHeight > 0 else minHeight
        self.enemies = enemies
        self.lootPool = lootPool

    def genEncounter(self, encsSoFar):
        desEnemies = random.randint(self.enemCount[0], self.enemCount[1])

        if encsSoFar < self.length - 1:
            # Get normal encounter
            enc = Encounter(random.randint(self.minWidth, self.maxWidth), random.randint(self.minHeight, self.maxHeight))
            enems = []
            while desEnemies > 0:
                index = random.randint(0, len(self.enemies) - 2) # Excludes the boss, which is at the end of the list
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
        else:
            # Get boss encounter
            enc = Encounter(self.maxWidth, self.maxHeight)
            enems = [Enemy(self.enemies[-1][0], self.enemies[-1][1], math.floor(self.maxWidth / 2), math.floor(self.maxHeight / 2))]
            return [enc, enems]