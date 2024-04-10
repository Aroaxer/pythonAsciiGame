import utils
import math

class Trait():
    name = ""
    tiedEquipment = None
    freeAction = False

    # Should be: "Active" / "Turn" / "Action" / "Before Damage" / "After Damage" / "Attack"
    trigger = ""
    # Should be: "Standard" / "Directional" / "Point" / "Point No Enemy" / "Multi {number}" / "Self" / "Centered" / "Copy Target" / "Damage Source" / "Custom"
    targeting = None
    multi = None
    
    areaType = None
    length = 1
    width = 1
    range = 1

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
    
    def __init__(self, name, trigger, effectKey, targeting = "N/A", maxCharges = -1, recharge = "Turn", rechargePercent = 1, aiPrio = 0, range = 1, length = 1, width = 1, freeAction = False) -> None:
        self.name = name
        self.freeAction = freeAction

        self.trigger = trigger
        if effectKey[:5] == "Repel":
            self.multi = int(effectKey[5:])
            effectKey = "Repel"
        if effectKey[:12] == "Damage Repel":
            self.multi = int(effectKey[12:])
            effectKey = "Damage Repel"
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
        if self.targeting in {"Point", "Point No Enemy", "Centered"} and self.length == 1:
            self.length = width

        self.maxCharges = maxCharges
        self.charges = self.maxCharges
        self.rechargePeriod = recharge
        self.rechargePercent = rechargePercent
        
        # Things that should start with zero charges
        if self.name in {"Bloodwave", "Bloodwhirl", "Divine Slash", "Radiant Pulse", "Divine Intervention", "Superstorm", "Living Deity", "Kingkiller", "Crystal Rain"}:
            self.charges = 0

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

                        y1 = user.y - math.floor(self.width / 2)
                        y2 = y1 + self.width + 1
                    case "Right":
                        x1= user.x + 1
                        x2 = user.x + self.length

                        y1 = user.y - math.floor(self.width / 2)
                        y2 = y1 + self.width + 1
                self.triggerOnRegion((x1, y1), (x2, y2), user, game, equipment, user.testEnem())
            elif self.targeting == "Point":
                x1 = target[0] - math.floor(self.width / 2)
                y1 = target[1] - math.floor(self.length / 2)

                self.triggerOnRegion((x1, y1), (x1 + self.width - 1, y1 + self.length - 1), user, game, equipment, user.testEnem())
            elif self.targeting == "Point No Enemy":
                self.triggerEffectOn(target, user, game, equipment)
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
            
            if self.freeAction:
                user.actionsLeft += 1

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
                    if target == "Cancelled":
                        return "Cancelled"
                    return validsReturn[target]
                
                case "Directional":
                    target = utils.promptChoice("Which direction would you like to attack?", ("Up", "Down", "Left", "Right"))
                    if target == "Cancelled":
                        return "Cancelled"
                    return ("Up", "Down", "Left", "Right")[target]
                
                case "Point" | "Point No Enemy":
                    targetX, targetY = utils.promptCoords("What point would you like to target?", game, (self.range, user.x, user.y), (self.targeting == "Point No Enemy"))
                    if target == "Cancelled":
                        return "Cancelled"
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
                    
                    if target == "Cancelled":
                        return "Cancelled"

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
        # Disable Kingkiller / Twilight if not used
        if equipment.name == "Regal Flail":
            equipment.traits[2].charges = 0
        elif equipment.name == "Dawnbreaker":
            equipment.traits[3].charges = 0

        match self.effectKey:
            # Attacks
            case "1x Damage":
                target.takeDamage(equipment.damage, user, game)
            case "1.5x Damage":
                target.takeDamage(equipment.damage * 1.5, user, game)
            case "0.5x Damage":
                target.takeDamage(equipment.damage * 0.5, user, game)
            case "Ritual Attack":
                target.takeDamage(equipment.damage, user, game)
                if target.hp <= 0:
                    user.actionsLeft += 1
                    user.hp += 0.2
                    self.charges += 1
            case "Decapitate":
                # Should only be used by Vorpal Sword or Excalibur
                target.takeDamage(equipment.damage * 1.25, user, game)
                if target.hp <= 0:
                    equipment.traits[1].charges += 1
                    equipment.traits[2].charges += 1
            case "Royal Strike":
                target.takeDamage(equipment.damage, user, game)
                user.tempDamageModifier *= 0.8
            case "Kingkiller":
                user.move(game.encounter, game, target=(target.x, target.y), ignoreSpd = True)
                target.takeDamage(equipment.damage * 2, user, game)
                # Become briefly invulnerable on kill
                if target.hp <= 0:
                    user.tempDamageModifier = 0
            case "Twilight":
                user.move(game.encounter, game, target=(target.x, target.y), ignoreSpd = True)
                target.takeDamage(equipment.damage * 3, user, game)
                # Become briefly invulnerable on kill
                if target.hp <= 0:
                    user.tempDamageModifier = 0
            case "Crystal Rain":
                self.charges = 0
                target.takeDamage(equipment.damage, user, game)

                # Reset area
                self.width = 1
                self.length = 1
            case "Draining Rays":
                target.takeDamage(equipment.damage * 0.5, user, game)
                if target.hp <= 0:
                    user.hp += 0.1
            case "Power Word Kill":
                if target.hp <= target.maxHp / 2:
                    target.hp = 0

            # Passive Damage
            case "Spikes":
                target.takeDamage(equipment.damage, user, game, False)

            # Defensive (Active)
            case "Block":
                target.tempDamageModifier *= 0.5
            case "Fortify":
                target.tempDamageModifier *= 0.25
            case "Parry":
                target.tempDamageModifier *= 0.75
            case "Invuln":
                target.tempDamageModifier = 0

            # Defensive (Passive)
            case "Regenerate":
                target.hp += 0.2
            case "Minor Block":
                target.tempDamageModifier *= 0.8
            case "Holy Radiance":
                target.takeDamage(equipment.damage / 4, user, game, False)
                user.hp += 0.05
            
            # Utility (Active)
            case "Hasten":
                target.actionsLeft += 2
            case "Pull" | "Damage Pull":
                if self.effectKey == "Damage Pull":
                    target.takeDamage(equipment.damage, user, game)
                target.move(game.encounter, game, target=(user.x, user.y), ignoreSpd = True)
            case "Teleport" | "Charge":
                user.x, user.y = target[0], target[1]
                if self.effectKey == "Charge":
                    # Temporarily runs '1x Damage' on a region around self
                    self.effectKey = "1x Damage"
                    
                    x1 = target[0] - math.floor(self.width / 2)
                    y1 = target[1] - math.floor(self.length / 2)

                    self.triggerOnRegion((x1, y1), (x1 + self.width - 1, y1 + self.length - 1), user, game, equipment, user.testEnem())

                    # Resets effect key so it can be reused
                    self.effectKey = "Charge"
            case "Condense":
                # Should only be used by Crystal Arbalest
                equipment.traits[3].charges += 1
                equipment.traits[3].width += 2
                equipment.traits[3].length += 2

            # Utility (Passive)
            case "Momentum":
                if target.hp <= 0:
                    user.actionsLeft += 0.25

            # Misc
            case "Repel" | "Damage Repel":
                if self.effectKey == "Damage Repel":
                    target.takeDamage(equipment.damage, user, game)
                if target.speed > 0:
                    if target.x < user.x:
                        target.move(game.encounter, game, cx=-self.multi, ignoreSpd = True)
                    elif target.x > user.x:
                        target.move(game.encounter, game, cx=self.multi, ignoreSpd = True)
                    if target.y < user.y:
                        target.move(game.encounter, game, cy=-self.multi, ignoreSpd = True)
                    elif target.y > user.y:
                        target.move(game.encounter, game, cy=self.multi, ignoreSpd = True)

                # Enable Kingkiller / Twilight
                if self.name == "Total Authority":
                    equipment.traits[2].charges += 1
                elif self.name == "High Noon":
                    equipment.traits[3].charges += 1

                if self.name == "Walking Fortress":
                    user.tempDamageModifier = 0
            case "Charge Deity":
                if target.hp <= 0:
                    equipment.traits[2].charges += 0.1
            case "Living Deity":
                user.hp += 1
                user.actionsLeft += 5
            
            case "Embodiment":
                if target.hp <= 0:
                    equipment.traits[3].charges += 0.2
            
            case "Palace Toggle":
                equipment.specialTags["Palace"] = not equipment.specialTags["Palace"]

                if equipment.specialTags["Palace"]:
                    equipment.defense = 90
                    user.mainhand.damage *= 1.25
                    equipment.extraSpeed = -2
                    equipment.extraActions = 1
                else:
                    equipment.defense = 75
                    user.mainhand.damage *= (4/5)
                    equipment.extraSpeed = 0
                    equipment.extraActions = 0

            # Charge Superstorm
            case "Mjolnir":
                equipment.traits[3].charges += 0.25

            # Exc Alt should never be directly used
            case "Excalibur":
                self.effectKey = "Exc Alt"

                x1 = target.x - math.floor(self.width / 2)
                y1 = target.y - math.floor(self.length / 2)

                self.triggerOnRegion((x1, y1), (x1 + self.width - 1, y1 + self.length - 1), user, game, equipment, user.testEnem())

                self.effectKey = "Excalibur"
            case "Exc Alt":
                target.takeDamage(equipment.damage * 0.5, user, game, False)
                if target.hp <= 0:
                    equipment.traits[3].charges += 0.1
            case "Divine Intervention":
                user.hp += user.maxHp / 4
                user.actionsLeft += 3
                user.tempDamageModifier = 0

            # Asmodeus
            case "Summon Lesser":
                for x in range(user.x - 1, user.x + 2):
                    for y in range(user.y - 1, user.y + 2):
                        if 0 < x < game.encounter.width + 1 and 0 < y < game.encounter.height + 1:
                            for object in game.allObjects:
                                if x == object.x and y == object.y:
                                    break
                            else:
                                if x != game.player.x and y != game.player.y:
                                    game.spawn("Lesser Devil", 25, x, y)
            case "Summon Greater":
                for x, y in ((user.x - 1, user.y), (user.x + 1, user.y)):
                    if 0 < x < game.encounter.width + 1 and 0 < y < game.encounter.height + 1:
                        for object in game.allObjects:
                            if x == object.x and y == object.y:
                                break
                        else:
                            if x != game.player.x and y != game.player.y:
                                game.spawn("Greater Devil", 70, x, y)




            case _:
                pass


    