import math

from Entities.Characters.character import Character
from Entities.Characters.enemy import Enemy
from Entities.Characters.player import Player

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
    endType = "You Died"

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
        self.emptyTerminal()
        self.getLoot(0, pre.weps, customMsg="What weapon would you like to start with?", separators={1:" Melee", 5:"\n Ranged", 8:"\n Magic"})
        self.emptyTerminal()
        self.getLoot(0, utils.merge(pre.offs.values(), pre.armors.values(), pre.accs.values()), allowUpgrade=False, 
                     customMsg="What extra item would you like to start with?", separators={1:" Offhand", 7:"\n Armor", 12:"\n Accesory"})

    def beginLoop(self):
        self.startNewEncounter()
        while not self.ended:
            self.loopCycle()

    def startPlayer(self):
        plr = Player(10, 0, 0, 2, 2)

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

        print("".join(self.player.getInfo(self)))

        print(f"{self.player.defense} Defense\n{self.player.speed} Speed\n")

        allInfos = []
        for enem in self.enemies:
            try:
                allInfos.append(enem.getInfo(self, oldHp = self.oldEnemInfo[enem]))
            except KeyError:
                allInfos.append(enem.getInfo(self))
            self.oldEnemInfo[enem] = enem.hp

        prevInfos = {}
        for entry in allInfos:
            if entry not in prevInfos.keys():
                prevInfos[entry] = 1
            else:
                prevInfos[entry] += 1
        
        for entry in prevInfos.keys():
            print(entry[0] + (f" (x{prevInfos[entry]})" if prevInfos[entry] > 1 else "") + entry[1])
            

    def startNewEncounter(self):
        self.oldEnemInfo = {}
        if (self.complEncsPerStage == self.stage.length / 2 or self.complEncsPerStage == 0) and self.completedEncounters > 0:
            self.getLoot(self.stage.lootAmount)

        self.player.rechargeTraits("Encounter")

        enc = self.stage.genEncounter(self.complEncsPerStage)
        self.encounter = enc[0]
        self.enemies = enc[1]
        self.player.y = enc[0].height
        self.player.x = math.ceil(enc[0].width / 2)

    def advanceStage(self):
        self.player.hp = self.player.maxHp
        self.complEncsPerStage = 0
        nextStages = [(stage, stage.name) for stage in preS.stages[self.stage.stageOrder] if self.stage.name in stage.prevStages or not len(stage.prevStages)]

        if len(nextStages) > 1:    
            self.stage = nextStages[utils.promptChoice("Which stage would you like to go to next?", [stage[1] for stage in nextStages])][0]
        elif nextStages:
            self.stage = nextStages[0][0]
        else:
            self.endType = "You Won!"
            self.ended = True
            

    def getLoot(self, amount, category = None, allowUpgrade = True, customMsg = None, separators = {}):
        if category:
            try:
                loot = list(category.values())
            except AttributeError:
                loot = category
            amount = len(loot)
        else:
            loot = utils.getXRandom(self.stage.lootPool, amount)

        names = []
        for item in loot:
            names.append(item.name)

        options = []
        for slot in (self.player.mainhand, self.player.offhand, self.player.armor, self.player.accessory):
            try:
                if slot.upgradedForm and type(slot.upgradedForm) != tuple and slot.upgradedForm.name in [item.name for item in self.stage.valUpgrades]:
                    options.append(slot)
                else:
                    for compareSlot in (self.player.mainhand, self.player.offhand, self.player.armor, self.player.accessory):
                        try:
                            if slot.upgradedForm[1].name == compareSlot.name and slot.upgradedForm[0].name in [item.name for item in self.stage.valUpgrades]:
                                options.append(slot)
                                break
                        except (AttributeError, TypeError): pass
            except AttributeError: pass

        if options and allowUpgrade:
            names.append("Upgrade an Item")

        choice = utils.promptChoice((customMsg if customMsg else "You found some loot!"), names, separators)

        if choice == amount:
            upgradeOption = utils.promptChoice("Which item would you like to upgrade?", [item.name for item in options])
            options[upgradeOption].upgrade()
        elif choice != "Cancelled":
            self.player.collect(loot[choice])
        

game = Game()

game.emptyTerminal()
print(f"{game.endType}\n\n")