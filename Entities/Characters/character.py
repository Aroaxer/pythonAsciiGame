import math
import copy

from Entities.object import Object

import utils

class Character(Object):
    hp = 0
    maxHp = 0

    name = ""
    spd = 0
    def getSpeed(self):
        total = self.spd

        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try: total += slot.extraSpeed
            except AttributeError: pass

        return total
    def setSpeed(self, speed):
        self.spd = speed
    speed = property(fget=getSpeed, fset=setSpeed)
    speedLeft = 0

    acs = 0
    def getActions(self):
        total = self.acs
        
        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try: total += slot.extraActions
            except AttributeError: pass

        return total
    def setActions(self, actions):
        self.acs = actions
    actions = property(fget=getActions, fset=setActions)
    actionsLeft = 0

    actionBonus = 0

    mainhand = None
    offhand = None
    armor = None
    helmet = None
    accessory = None

    tempDamageModifier = 1

    def __init__(self, name, hp, x, y, speed, actions = 1) -> None:
        self.name = name
        self.maxHp = hp
        self.hp = self.maxHp
        self.speed = speed
        self.actions = actions
        super().__init__(x, y)

    # target is an (x, y) tuple
    def move(self, area, game, cx = 0, cy = 0, target = None, ignoreSpd = False):

        stX = self.x
        stY = self.y

        if cx == 0 and cy == 0:
            cx = target[0] - self.x
            cy = target[1] - self.y

        while abs(cx) > 0 and (self.speedLeft > 0 or ignoreSpd):
            # Copies the sign but moves by one
            stX = self.x
            self.x += (cx / abs(cx))
           
            if self.x > area.width:
                self.x = stX
            elif self.x < 1:
                self.x = stX
            else:
                for object in game.allObjects:
                    if self.x == object.x and self.y == object.y and object.collides and object != self:
                        self.x = stX
                if self.x == game.player.x and self.y == game.player.y and game.player != self:
                        self.x = stX

            cx -= (cx / abs(cx))
            self.speedLeft -= 1

        while abs(cy) > 0 and (self.speedLeft > 0 or ignoreSpd):
            # Copies the sign but moves by one
            stY = self.y
            self.y += (cy / abs(cy))
           
            if self.y > area.height:
                self.y = stY
            elif self.y < 1:
                self.y = stY
            else:
                for object in game.allObjects:
                    if self.y == object.y and self.x == object.x and object.collides and object != self:
                        self.y = stY
                if self.x == game.player.x and self.y == game.player.y and game.player != self:
                        self.y = stY

            cy -= (cy / abs(cy))
            self.speedLeft -= 1

    def takeTurn(self, game):
        self.tempDamageModifier = 1

        self.rechargeTraits("Turn")

        self.actionsLeft = self.actions + self.actionBonus
        self.actionBonus = 0

        self.activateAllTraits("Turn", game, None)

        record = ""
        while self.actionsLeft > 0:
            self.speedLeft = self.speed
            record = self.takeAction(game)
            if self.hp > self.maxHp:
                self.hp = self.maxHp

        return f"{self.name} {record}"

    def takeAction(self, *args):
        self.actionsLeft = 0
        return "" # This function is defined by subclasses
    
    def takeDamage(self, damage, source, game, shouldTriggerTraits = True):
        if shouldTriggerTraits: self.activateAllTraits("Before Damage", game, source)

        try:
            damage *= 1 - (self.armor.defense / 100)
        except AttributeError: pass

        damage *= self.tempDamageModifier

        self.hp -= damage
        if self.hp <= 0:
            if not self == game.player:
                game.kill(self)
            else:
                game.ended = True
        
        if shouldTriggerTraits: self.activateAllTraits("After Damage", game, source)

    def putOn(self, item, slot):
        item = copy.deepcopy(item)
        match slot:
                case "Mainhand":
                    try:
                        del self.mainhand
                    except AttributeError: pass
                    self.mainhand = item
                    item.user = (self, "Mainhand")
                case "Offhand":
                    try:
                        del self.offhand
                    except AttributeError: pass
                    self.offhand = item
                    item.user = (self, "Offhand")
                case "Armor":
                    try:
                        del self.armor
                    except AttributeError: pass
                    self.armor = item
                    item.user = (self, "Armor")
                case "Helmet":
                    try:
                        del self.helmet
                    except AttributeError: pass
                    self.helmet = item
                    item.user = (self, "Helmet")
                case "Accessory":
                    try:
                        del self.accessory
                    except AttributeError: pass
                    self.accessory = item
                    item.user = (self, "Accessory")
    
    # Returns a list of all actions for all equipments
    def getFullActionList(self):
        actionList = []

        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try: actionList = utils.merge(actionList, slot.allActions())
            except AttributeError: pass

        return actionList
    
    def getAllTraits(self):
        traits = []

        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try: traits = utils.merge(traits, slot.traits)
            except AttributeError: pass

        return traits

    def getInfo(self, game, detailed = False, oldHp = 0):
        plannedAction = False
        try:
            plannedAction = self.determineBestAction(game)
            if plannedAction[0] != "Move":
                plannedAction = f"Use {plannedAction[1].name}"
            else:
                plannedAction = "Move"
        except AttributeError: pass

        infoStr = f"{self.name}: {math.ceil(self.hp)}/{self.maxHp} Health" + (f" (-{oldHp - self.hp})" if oldHp and oldHp != self.hp else "") + (f"\n   Will {plannedAction}" if plannedAction else "")
        if detailed:
            try: infoStr += f"\nMainhand: {self.mainhand.name}, {self.mainhand.damage} Damage"
            except AttributeError: pass
            try: infoStr += f"\nOffhand: {self.offhand.name}" + (f", {self.offhand.damage} Damage" if self.offhand.damage > 0 else "")
            except AttributeError: pass
            try: infoStr += f"\nArmor: {self.armor.name}" + (f", {self.armor.damage} Damage" if self.armor.damage > 0 else "")
            except AttributeError: pass
            try: infoStr += f"\nHelmet: {self.helmet.name}" + (f", {self.helmet.damage} Damage" if self.helmet.damage > 0 else "")
            except AttributeError: pass
            try: infoStr += f"\nAccesory: {self.accessory.name}" + (f", {self.accessory.damage} Damage" if self.accessory.damage > 0 else "")
            except AttributeError: pass
        return infoStr
    
    def isInRegion(self, topLeft, botRight):
        return (self.x >= topLeft[0] and self.y >= topLeft[1]) and (self.x <= botRight[0] and self.y <= botRight[1])
    
    def testEnem(self):
        return False
        # Redefined to return True in the enemy class
    
    def activateAllTraits(self, trigger, game, target):
        for slot in (self.mainhand, self.offhand, self.armor, self.helmet, self.accessory):
            try:
                for trait in slot.traits:
                    trait.activate(game, trigger, slot, self, target)
            except AttributeError: pass
    
    def rechargeTraits(self, trigger):
        for trait in self.getAllTraits():
            trait.recharge(trigger)
