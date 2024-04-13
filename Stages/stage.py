import random
import math

from Stages.Encounters.encounter import Encounter
from Entities.Characters.enemy import Enemy

import premades as pre
import utils

class Stage():
    name = ""

    minWidth = 0
    maxWidth = minWidth

    minHeight = 0
    maxHeight = minHeight

    enemies = []
    lootPool = []
    lootAmount = 0

    length = 0
    enemCount = 0
    # Stores the names of the stages that this stage can follow
    prevStages = []
    stageOrder = 0
    valUpgrades = ()

    def __init__(self, name, stageOrder, enemies, lootPool, minWidth, minHeight, maxWidth = -1, maxHeight = -1, length = 10, prevStages = [], enemCount = 0, lootAmount = 3) -> None:
        self.name = name
        self.length = length
        self.enemCount = enemCount
        self.prevStages = prevStages
        self.stageOrder = stageOrder

        temp = []
        if self.stageOrder > 1:
            temp = utils.merge(temp, pre.allItems[1])
        if self.stageOrder > 2:
            temp = utils.merge(temp, pre.allItems[2])
        if self.stageOrder > 3:
            temp = utils.merge(temp, pre.allItems[3])
        self.valUpgrades = temp

        self.minWidth = minWidth
        self.minHeight = minHeight
        self.maxWidth = maxWidth if maxWidth > 0 else minWidth
        self.maxHeight = maxHeight if maxHeight > 0 else minHeight
        self.enemies = enemies
        self.lootPool = lootPool
        self.lootAmount = lootAmount

    def genEncounter(self, encsSoFar):
        print("Generating Encounter")
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
                        if x == enem.x and y == enem.y:
                            validCoords = False

                enems.append(Enemy(self.enemies[index][0], self.enemies[index][1], x, y))
                desEnemies -= 1
            return [enc, enems]
        else:
            # Get boss encounter
            width, height = self.maxWidth, self.maxHeight
            try:
                width, height = self.enemies[-1][2]
            except IndexError: pass

            tX, tY = math.ceil(width / 2), math.ceil(height / 2)
            try:
                tX, tY = self.enemies[-1][3]
            except IndexError: pass

            enc = Encounter(width, height)
            enems = [Enemy(self.enemies[-1][0], self.enemies[-1][1], tX, tY)]
            return [enc, enems]