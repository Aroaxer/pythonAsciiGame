import math

from Entities.object import Object
from Entities.Characters.character import Character
from Entities.Characters.enemy import Enemy
from Entities.Characters.player import Player
from Stages.Encounters.encounter import Encounter
from Stages.stage import Stage

import premades as pre
import utils

class Game():
    # Properties
    player = None
    allObjects = []
    encounter = None
    stage = pre.sunlitField

    def getEnemies(self):
        enems = []
        for object in self.allObjects:
            if type(object) == Enemy:
                enems.append(object)
        return enems
    def setEnemies(self, enems):
        remove = []
        for object in self.allObjects:
            if type(object) != Enemy:
                remove.append(object)
        self.allObjects = remove
        self.allObjects.extend(enems)
    enemies = property(fget = getEnemies, fset = setEnemies)

    def getObjects(self):
        objects = []
        for object in self.allObjects:
            if type(object) != Character:
                objects.append(object)
        return objects
    def setObjects(self, objs):
        remove = []
        for object in self.allObjects:
            if type(object) == Character:
                remove.append(object)
        self.allObjects = remove
        self.allObjects.extend(objs)
    objects = property(fget = getObjects, fset = setObjects)
    
    # Start game
    def __init__(self) -> None:
        self.resetGame()
        self.beginLoop()

    def resetGame(self):
        self.allObjects = []
        self.player = self.startPlayer()

    def beginLoop(self):
        self.startNewEncounter(2)
        shouldEnd = False
        while not shouldEnd:
            shouldEnd = self.loopCycle()

    def startPlayer(self):
        plr = Player(0, 0, 2, 2)
        plr.mainhand = pre.weps["Sword"]
        return plr

    # Run game
    def loopCycle(self):
        if len(self.enemies) == 0:
            self.startNewEncounter(2)

        self.player.takeTurn(self)

        for enemy in self.enemies:
            enemy.takeTurn(self)

    def emptyTerminal(self):
        cyc = 0
        while cyc < 20:
            print("\n\n\n")
            cyc += 1

    def assembleMap(self, format): # Format is either "str" or "arr"
        map = [["-" for i in range(self.encounter.width)] for j in range(self.encounter.height)]

        map[round(self.player.y - 1)][round(self.player.x - 1)] = "@"

        for enem in self.enemies:
            map[round(enem.y - 1)][round(enem.x - 1)] = enem.mapIcon

        if format == "str":
            reduced = []
            for row in map:
                reduced.append(" ".join(row))
            return "\n".join(reduced)
        return map

    def startNewEncounter(self, enems):
        enc = self.stage.genEncounter(enems)
        self.encounter = enc[0]
        self.enemies = enc[1]
        self.player.y = enc[0].height
        self.player.x = math.ceil(enc[0].width / 2)






game = Game()