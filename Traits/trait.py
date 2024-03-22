import utils
import math


class Trait():
    name = ""

    # Should be: "Active" / "Turn" / "Action" / "Before Damage" / "After Damage" / "Attack"
    trigger = ""
    # Should be: "Standard" / "Directional" / "Point" / "Multi {number}" / "Self" / "Centered" / "Global" / "Copy Target" /"Damage Source" / "Custom"
    targeting = None
    multi = None
    
    areaType = None
    length = 1
    width = 1
    range = 1

    # Stores tied equipment, initialized by the equipment
    tiedEquipment = None


    # Determines effect when triggered
    effectKey = ""
    
    # -1 charges is infinite
    charges = 0
    maxCharges = 0
    # Should be: "Turn" / "Action" / "Encounter" / "Never"
    rechargePeriod = ""
    # Percent from 0 to 1
    rechargePercent = 0

    # For enemy AI
    aiPrio = 0
    
    def __init__(self, name, trigger, effectKey, targeting = "N/A", maxCharges = -1, recharge = "Turn", rechargePercent = 1, aiPrio = 0, range = 1, length = 1, width = 1) -> None:
        self.name = name

        self.trigger = trigger
        if effectKey[:5] == "Repel":
            self.multi = int(effectKey[5:])
            effectKey = "Repel"
        self.effectKey = effectKey
        if targeting == "N/A":
            if trigger == "After Damage" or trigger == "Before Damage":
                targeting = "Damage Source"
            elif trigger == "Attack":
                targeting = "Copy Target"
            elif trigger == "Turn":
                targeting = "Self"
        if targeting[:5] == "Multi":
            self.multi = int(targeting[5:])
            targeting = "Multi"
        

        self.targeting = targeting

        self.range = range
        self.length = length
        self.width = width
        if self.targeting == "Point" and self.length == 1:
            self.length = width

        self.maxCharges = maxCharges
        self.charges = self.maxCharges
        self.rechargePeriod = recharge
        self.rechargePercent = rechargePercent

        self.aiPrio = aiPrio

    def recharge(self, trigger):
        # Recharge on recharge period
        if self.rechargePeriod == trigger:
            self.charges += self.maxCharges * self.rechargePercent
        if self.charges > self.maxCharges:
            self.charges = self.maxCharges
        
        match trigger:
            case "Encounter":
                self.recharge("Turn")
            case "Turn":
                self.recharge("Action")
    
    # 'target' is only used by some targeting types
    def activate(self, game, trigger, equipment = None, user = None, target = None):
        if self.trigger == trigger and (self.charges >= 1 or self.maxCharges < 0):

            # Causes no charges to be lost
            didntTrigger = False
            match self.effectKey:


                case _:
                    pass
            
            target = self.getTarget(game, user, target)

            if target == "Cancelled":
                didntTrigger = True
            elif self.targeting == "Directional":
                # I don't think there's a way to make this shorter
                x1 = None
                x2 = None
                y1 = None
                y2 = None
                match target:
                    case "Up":
                        x1 = user.x - math.floor(self.width / 2)
                        x2 = x1 + self.width - 1

                        y1 = user.y - self.length
                        y2 = user.y - 1
                    case "Down":
                        x1 = user.x - math.floor(self.width / 2)
                        x2 = x1 + self.width - 1

                        y1 = user.y + 1
                        y2 = user.y + self.length
                    case "Left":
                        x1 = user.x - self.length
                        x2 = user.x - 1

                        y1 = user.y + math.floor(self.width / 2)
                        y2 = y1 - self.width + 1
                    case "Right":
                        x1= user.x + 1
                        x2 = user.x + self.length

                        y1 = user.y + math.floor(self.width / 2)
                        y2 = y1 - self.width + 1
                self.triggerOnRegion((x1, y1), (x2, y2), user, game, equipment, user.testEnem())
            elif self.targeting == "Point":
                x1 = target[0] - math.floor(self.width / 2)
                y1 = target[1] - math.floor(self.length / 2)

                self.triggerOnRegion((x1, y1), (x1 + self.width - 1, y1 + self.length - 1), user, game, equipment, user.testEnem())
            elif self.targeting == "Centered":
                x1 = user.x - math.floor(self.width / 2)
                y1 = user.y - math.floor(self.length / 2)

                self.triggerOnRegion((x1, y1), (x1 + self.width - 1, y1 + self.length - 1), user, game, equipment, user.testEnem())
            elif self.targeting == "Multi":
                for entity in target:
                    self.triggerEffectOn(entity, user, game, equipment)
            else:
                self.triggerEffectOn(target, user, game, equipment)

            # Remove charge if effect triggered and not infinite charges
            if self.charges > 0 and not didntTrigger:
                self.charges -= 1
            
            return not didntTrigger

    # 'target' is required only by some targeting types
    def getTarget(self, game, user, target = None):
        plr = game.player
        if user == plr:
            match self.targeting:
                case "Standard":
                    validEnems = []
                    validsReturn = []
                    for enem in game.enemies:
                        if enem.isWithinDistance(self.range, (plr.x, plr.y)):
                            validEnems.append(f"{enem.name}: {math.ceil(enem.hp)}/{enem.maxHp} ({enem.x}, {enem.y})")
                            validsReturn.append(enem)
                    if len(validEnems) == 0:
                        return "Cancelled"
                    target = utils.promptChoice("Which enemy would you like to target?", validEnems)
                    return validsReturn[target]
                
                case "Directional":
                    target = utils.promptChoice("Which direction would you like to attack?", ("Up", "Down", "Left", "Right"))
                    return ("Up", "Down", "Left", "Right")[target]
                
                case "Point":
                    targetX, targetY = utils.promptCoords("What point would you like to target?")
                    return targetX, targetY
                
                case "Multi":
                    validEnems = []
                    validsReturn = []
                    for enem in game.enemies:
                        if enem.isWithinDistance(self.range, (plr.x, plr.y)):
                            validEnems.append(f"{enem.name}: {math.ceil(enem.hp)}/{enem.maxHp} ({enem.x}, {enem.y})")
                            validsReturn.append(enem)
                    if len(validEnems) == 0:
                        return "Cancelled"
                    
                    targets = utils.promptMultipleIds("Which enemies would you like to target?", validEnems, self.multi)

                    finalTargets = []
                    for entry in targets:
                        finalTargets.append(validsReturn[int(entry) - 1])
                    return finalTargets
                    
                case "Self":
                    return user
                
                case "Damage Source" | "Copy Target":
                    return target
                
                case _:
                    return None
                    
        else:
            if self.targeting == "Self":
                return user
            return plr

    def triggerOnRegion(self, topLeft, botRight, user, game, equip, wasEnem = False):
        if not wasEnem:
            for enem in game.enemies:
                if enem.isInRegion(topLeft, botRight):
                    self.triggerEffectOn(enem, user, game, equip)
        else:
            if game.player.isInRegion(topLeft, botRight):
                self.triggerEffectOn(game.player, user, game, equip)

    def triggerEffectOn(self, target, user, game, equipment):
        match self.effectKey:
            # Attacks
            case "1x Damage":
                target.takeDamage(equipment.damage, user, game)
            case "1.5x Damage":
                target.takeDamage(equipment.damage * 1.5, user, game)
            case "0.5x Damage":
                target.takeDamage(equipment.damage * 0.5, user, game)

            # Passive Damage
            case "Spikes":
                target.takeDamage(equipment.damage, user, game, False)

            # Defensive (Active)
            case "Block":
                target.tempDamageModifier *= 0.5

            # Defensive (Passive)
            case "Regenerate":
                target.hp += target.maxHp / 10
                if target.hp > target.maxHp:
                    target.hp = target.maxHp
            
            # Utility (Active)
            case "Hasten":
                target.actionsLeft += 2

            # Utility (Passive)

            # Misc
            case "Repel":
                if target.x < user.x:
                    target.move(cx=-self.multi, ignoreSpd = True)
                elif target.x > user.x:
                    target.move(cx=self.multi, ignoreSpd = True)
                if target.y < user.y:
                    target.move(cy=-self.multi, ignoreSpd = True)
                elif target.y > user.y:
                    target.move(cy=self.multi, ignoreSpd = True)

            case _:
                pass


    