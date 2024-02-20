import utils

class Trait():
    # Should be: "Active" / "Turn" / "Action" / "Damage" / "Attack"
    trigger = ""
    targetsTile = False
    needsTarget = False

    length = 0
    width = 0


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
    
    def __init__(self, trigger, effectKey, needsTarget = False, targetsTile = False, maxCharges = -1, recharge = "Turn", rechargePercent = 1, aiPrio = 0) -> None:
        self.trigger = trigger
        self.effectKey = effectKey
        self.targetsTile = targetsTile
        self.needsTarget = needsTarget

        self.maxCharges = maxCharges
        self.charges = self.maxCharges
        self.rechargePeriod = recharge
        self.rechargePercent = rechargePercent

        self.aiPrio = aiPrio

    def recharge(self, trigger):
        # Recharge on recharge period
        if self.rechargePeriod == trigger:
            self.charges = self.maxCharges
        
        match trigger:
            case "Encounter":
                self.recharge("Action")
            case "Action":
                self.recharge("Turn")
    
    def activate(self, game, trigger, equipment):
        if self.trigger == trigger and (self.charges > 0 or self.maxCharges < 0):

            # Causes no charges to be lost
            didntTrigger = False
            match self.effectKey:


                case _:
                    pass
            
            if self.needsTarget:
                target = self.getTarget(game, self.targetsTile)

            # Remove charge if effect triggered and not infinite charges
            if self.charges > 0 and not didntTrigger:
                self.charges -= 1

    def getTarget(self, game, targetsTile = False):
        if not targetsTile:
            target = utils.promptChoice("Which enemy would you like to target?", (f"{enem.name} ({enem.x}, {enem.y})" for enem in game.enemies))
            print(target)

    def triggerOnRegion(self, topLeft, botRight, game):
        for enem in game.enemies:
            if enem.isInRegion(topLeft, botRight):
                self.triggerEffectOn(enem)

    def manageTargeting(self):
        match self.effectKey:


            case _:
                pass

    def triggerEffectOn(self, target):
        match self.effectKey:


            case _:
                pass


    