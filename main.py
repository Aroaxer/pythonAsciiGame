import math
import random
import copy

from Entities.object import Object
from Entities.Characters.character import Character
from Entities.Characters.enemy import Enemy
from Entities.Characters.player import Player
from Stages.Encounters.encounter import Encounter
from Stages.stage import Stage

import premades as pre
import Stages.preStages as preS
import utils

class Game():
    # Properties
    player = None
    allObjects = []
    encounter = None
    stage = preS.stages[0][0]

    completedEncounters = 0
    complEncsPerStage = 0

    oldEnemInfo = {}

    ended = False

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
        self.getLoot(10)

    def beginLoop(self):
        self.startNewEncounter()
        shouldEnd = False
        while not shouldEnd:
            shouldEnd = self.loopCycle()

    def startPlayer(self):
        plr = Player(10, 0, 0, 2, 2)
        plr.putOn(pre.weps["Sword"], "Mainhand")

        return plr

    # Run game
    def loopCycle(self):

        self.player.takeTurn(self)

        actionRecord = []

        for enemy in self.enemies:
            actionRecord.append(enemy.takeTurn(self))

        if actionRecord == []:
            actionRecord = ["Encounter Complete!"]

        self.printEndRound(actionRecord)

        if len(self.enemies) == 0:
            self.completedEncounters += 1
            self.complEncsPerStage += 1
            if self.stage.length <= self.complEncsPerStage:
                self.advanceStage()
            self.startNewEncounter()

    def printEndRound(self, actionRecord):
        self.emptyTerminal()
        print(self.assembleMap())
        for item in actionRecord:
            print(item)
        input("Press enter to continue\n")

    def kill(self, entity):
        for i, object in enumerate(self.allObjects):
            if object.uid == entity.uid:
                del self.allObjects[i]
                del entity
                break

    def emptyTerminal(self):
        cyc = 0
        while cyc < 20:
            print("\n\n\n")
            cyc += 1

    def assembleMap(self, format = "str"): # Format is either "str" or "arr"
        map = [["-" for _ in range(self.encounter.width)] for _ in range(self.encounter.height)]

        map[round(self.player.y - 1)][round(self.player.x - 1)] = "@"

        for enem in self.enemies:
            map[round(enem.y - 1)][round(enem.x - 1)] = enem.mapIcon

        if format == "str":
            reduced = []
            for row in map:
                reduced.append(" ".join(row))
            return "\n".join(reduced)
        return map
    
    def displayInfo(self):
        print(f"Stage: {self.stage.name}")

        print(self.assembleMap("str"))

        print(self.player.getInfo(self))

        print("")

        for enem in self.enemies:
            try:
                print(enem.getInfo(self, oldHp = self.oldEnemInfo[enem]))
            except KeyError:
                print(enem.getInfo(self))
            self.oldEnemInfo[enem] = enem.hp
            

    def startNewEncounter(self):
        self.oldEnemInfo = {}
        if self.complEncsPerStage == self.stage.length / 2 or self.complEncsPerStage == 0:
            self.getLoot(3)

        self.player.rechargeTraits("Encounter")

        enc = self.stage.genEncounter(self.complEncsPerStage)
        self.encounter = enc[0]
        self.enemies = enc[1]
        self.player.y = enc[0].height
        self.player.x = math.ceil(enc[0].width / 2)

    def advanceStage(self):
        self.complEncsPerStage = 0
        nextStage = None
        while True:
            nextStage = preS.stages[self.stage.stageOrder][random.randint(0, len(preS.stages[self.stage.stageOrder]) - 1)]
            if len(nextStage.prevStages) == 0 or self.stage.name in nextStage.prevStages:
                self.stage = nextStage
                break

    def getLoot(self, amount):
        loot = utils.getXRandom(self.stage.lootPool, amount)

        names = []
        for item in loot:
            names.append(item.name)

        names.append("Upgrade an Item")

        choice = utils.promptChoice("You found some loot!", names)

        if choice == amount:
            self.player.getUpgrade()
        elif choice != "Cancelled":
            self.player.collect(loot[choice])
        

game = Game()