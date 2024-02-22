import utils

from Entities.Characters.enemy import Enemy

class Trait():
    # Should be: "Active" / "Turn" / "Action" / "Damage" / "Attack"
    trigger = ""
    # Should be: "Standard" / "Directional" / "Point" / "Multi {number}" / "Custom"
    targeting = None
    
    areaType = None
    length = 0
    width = 0
    range = 0


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
    
    def __init__(self, trigger, effectKey, targeting = "Standard", maxCharges = -1, recharge = "Turn", rechargePercent = 1, aiPrio = 0, range = 1, length = 0, width = 0) -> None:
        self.trigger = trigger
        self.effectKey = effectKey
        self.targeting = targeting

        self.range = range
        self.length = length
        self.width = width

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
    
    def activate(self, game, trigger, equipment = None, user = None):
        print(f"{self.trigger} compared to {trigger}: {self.trigger == trigger}")
        if self.trigger == trigger and (self.charges > 0 or self.maxCharges < 0):
            print("Triggered")

            # Causes no charges to be lost
            didntTrigger = False
            match self.effectKey:


                case _:
                    pass
            
            target = self.getTarget(game, user)

            if type(target) == Enemy:
                self.triggerEffectOn(target)

            # Remove charge if effect triggered and not infinite charges
            if self.charges > 0 and not didntTrigger:
                self.charges -= 1

    def getTarget(self, game, user):
        plr = game.player
        if user == plr:
            match self.targeting:
                case "Standard":
                    print("Standard Targeting")
                    validEnems = []
                    for enem in game.enemies:
                        if enem.isInRegion((plr.x - self.range, plr.y - self.range), (plr.x + self.range, plr.y + self.range)):
                            validEnems.append[enem]
                    target = utils.promptChoice("Which enemy would you like to target?", (f"{enem.name} ({enem.x}, {enem.y})" for enem in validEnems))
                    return game.enemies[target]
                case "Directional":
                    target = utils.promptChoice("Which direction would you like to attack?", ("Up", "Down", "Left", "Right"))
                    return ("Up", "Down", "Left", "Right")[target]
                case "Point":
                    target = utils.promptCoords("What point would you like to target? (x,y)", "(_,_)")


                    
        else:
            return plr

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


    