from Entities.Characters.character import Character
import premades as pre

import aStar
import settings

class Enemy(Character):
    preferredDist = 0
    difficultyValue = 0
    mapIcon = ""
    
    def __init__(self, name, hp, x, y, speed = 1, actions = 1, preferredDist = 1, mapIcon = "E", difficultyValue = 1) -> None:
        self.preferredDist = preferredDist
        self.mapIcon = mapIcon
        self.difficultyValue = difficultyValue

        match name:
            # Stage 1
                # Sunlit Field
            case "Wild Boar":
                self.mapIcon = "B"

                self.putOn(pre.enemWeps["Weak Melee"])
            case "Spitting Cobra":
                self.mapIcon = "C"
                self.preferredDist = 2

                self.putOn(pre.enemWeps["Weak Ranged"])

                # Boss
            case "Treant":
                self.mapIcon = "#"
                
                self.putOn(pre.enemWeps["Treant"])
                self.putOn(pre.enemArmrs["Weak No Special"])


            # Stage 2
                # Shaded Forest
            case "Goblin":
                self.mapIcon = "G"

                self.putOn(pre.enemWeps["Weak Melee"])
            case "Hobgoblin":
                self.mapIcon = "H"
                self.preferredDist = 2

                self.putOn(pre.enemWeps["Weak Ranged"])
            case "Bugbear":
                self.mapIcon = "B"
                self.difficultyValue = 2
                
                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
                
                # Boss
            case "Hobgoblin Lord":
                self.mapIcon = "#"

                actions = 2

                self.putOn(pre.enemWeps["Hobgob Lord"])


                # Dark Cave
                # Note: Also references 'Goblin' from Shaded Forest
            case "Bat":
                self.mapIcon = "B"

                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"])
            case "Giant Spider":
                self.mapIcon = "S"

                actions = 2

                self.putOn(pre.enemWeps["Weak Melee"])

                # Boss
            case "Spider Queen":
                self.mapIcon = "#"

                actions = 3

                self.putOn(pre.enemWeps["Spider Queen"])
            case "Egg":
                self.mapIcon = "E"
                speed = 0
                self.putOn(pre.enemWeps["Egg"])
            

            # Stage 3
                # Forest Tower
            case "Turret":
                self.mapIcon = "T"
                
                speed = 0

                self.putOn(pre.enemWeps["Weak Ranged"])
            case "Stone Golem":
                self.mapIcon = "S"
                self.difficultyValue = 2

                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Golem Mage":
                self.mapIcon = "M"
                self.preferredDist = 3
                self.difficultyValue = 2

                actions = 2

                self.putOn(pre.enemWeps["Weak Magic"])

                # Boss
            case "Iron Golem":
                self.mapIcon = "#"

                speed = 2
                actions = 3

                self.putOn(pre.enemWeps["Iron Golem"])
                self.putOn(pre.enemArmrs["Weak No Special"])


                # Crystal Cavern
            case "Gem Crawler":
                self.mapIcon = "C"

                speed = 3

                self.putOn(pre.enemWeps["Weak Melee"])
            case "Crystal Golem":
                self.mapIcon = "G"

                speed = 2
                actions = 2

                self.putOn(pre.enemWeps["Weak Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Jeweled Spire":
                self.mapIcon = "S"

                speed = 0
                
                self.putOn(pre.enemWeps["Weak Ranged"])
                self.putOn(pre.enemArmrs["Weak No Special"])

                # Boss
            case "Crystal Heart":
                self.mapIcon = "#"

                speed = 0
                actions = 2

                self.putOn(pre.enemWeps["Crystal Heart"])


            # Stage 4
                # Fey Grove
            case "Sprite":
                self.mapIcon = "S"

                actions = 2

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Quickling":
                self.mapIcon = "Q"

                speed = 3

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Dryad":
                self.mapIcon = "D"

                self.putOn(pre.enemWeps["Medium Magic"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Treant":
                self.mapIcon = "T"

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])

                # Boss
            case "Archfey":
                self.mapIcon = "#"

                self.putOn(pre.enemWeps["Medium Magic"])
                self.putOn(pre.enemArmrs["Medium No Special"])


                # Scorched Desert
            case "Giant Scorpion":
                self.mapIcon = "S"

                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Sand Elemental":
                self.mapIcon = "E"

                speed = 2

                self.putOn(pre.enemWeps["Medium Ranged"])
            case "Giant Snake":
                self.mapIcon = "G"

                actions = 2
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Vulture":
                self.mapIcon = "V"

                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])

                # Boss
            case "Sandworm":
                self.mapIcon = "#"

                actions = 2
                speed = 3

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])


                # Icy Tundra
            case "Ice Elemental":
                self.mapIcon = "E"

                speed = 2

                self.putOn(pre.enemWeps["Medium Magic"])
            case "Yeti":
                self.mapIcon = "Y"

                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Snow Golem":
                self.mapIcon = "S"

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Weak No Special"])

                # Boss
            case "Frost Giant":
                self.mapIcon = "#"

                actions = 3

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])

            # Stage 5
                # Royal Palace
            case "Guard":
                self.mapIcon = "G"

                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Archer":
                self.mapIcon = "A"

                preferredDist = 2
                actions = 2

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Dark Knight":
                self.mapIcon = "K"

                speed = 3
                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Warlock":
                self.mapIcon = "W"

                preferredDist = 3
                speed = 2

                self.putOn(pre.enemWeps["Medium Magic"])
                self.putOn(pre.enemArmrs["Weak No Special"])

                # Boss
            case "Royal Champion":
                self.mapIcon = "#"

                speed = 3
                actions = 3

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])

                # The Antitower
            case "Tome Spirit":
                self.mapIcon = "S"

                preferredDist = 3
                speed = 2
                
                self.putOn(pre.enemWeps["Medium Magic"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Rune Golem":
                self.mapIcon = "G"

                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Magician":
                self.mapIcon = "M"

                preferredDist = 3
                speed = 3

                self.putOn(pre.enemWeps["Medium Magic"])
                self.putOn(pre.enemArmrs["Medium No Special"])

                # Boss
            case "Enchanted Golem":
                self.mapIcon = "#"

                speed = 5
                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])

            # Stage 6
                # Astral Plane
            case "Astral Spirit":
                self.mapIcon = "S"

                speed = 3

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Githyanki":
                self.mapIcon = "G"

                actions = 2
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Wanderer":
                self.mapIcon = "W"

                actions = 3
                preferredDist = 2
                
                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Medium No Special"])

                # Boss
            case "Vlaakith":
                self.mapIcon = "#"

                actions = 4

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            
                # The Abyss
            case "Winged Demon":
                self.mapIcon = "W"

                preferredDist = 2
                actions = 2
                speed = 2

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Hulking Demon":
                self.mapIcon = "H"

                actions = 3
                
                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Nimble Demon":
                self.mapIcon = "N"

                actions = 2
                speed = 3

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])

                # Boss
            case "Yeenoghu":
                self.mapIcon = "#"

                actions = 6

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            
            # Stage 7
                # Mount Celestia
            case "Angel":
                self.mapIcon = "a"

                actions = 2
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Seraph":
                self.mapIcon = "S"

                actions = 3
                preferredDist = 2

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Archangel":
                self.mapIcon = "A"

                actions = 3
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            
                # Boss
            case "Deity":
                self.mapIcon = "#"

                actions = 4
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            
                # The Nine Hells
            case "Bone Devil":
                self.mapIcon = "B"

                actions = 2
                speed = 2
                preferredDist = 2

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Ice Devil":
                self.mapIcon = "I"

                actions = 3
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Chain Devil":
                self.mapIcon = "C"

                # Intentionally prefers distance 1
                actions = 2
                speed = 3

                self.putOn(pre.enemWeps["Medium Ranged"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Pit Fiend":
                self.mapIcon = "F"
                
                actions = 3
                speed = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            
                # Asmodeus
            case "Asmodeus":
                self.mapIcon = "Ω"

                actions = 3
                speed = 2
                
                self.putOn(pre.enemWeps["Asmodeus"])
                self.putOn(pre.enemArmrs["Medium No Special"])
            case "Lesser Devil":
                self.mapIcon = "L"

                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"])
                self.putOn(pre.enemArmrs["Weak No Special"])
            case "Greater Devil":
                self.mapIcon = "G"

                speed = 2
                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"])
                self.putOn(pre.enemArmrs["Medium No Special"])
                

            case _:
                pass


        super().__init__(name, hp * settings.enemyHpMod, x, y, speed, actions)

    def takeAction(self, game):
        self.speedLeft = self.speed
        self.actionsLeft -= 1

        action = self.determineBestAction(game)

        match action[0]:
            case "Active":
                oldPlHp = game.player.hp
                action[1].activate(game, "Active", action[1].tiedEquipment, self)
                return f"used {action[1].name}" + (f" for {round(oldPlHp - game.player.hp, 2)} damage" if oldPlHp != game.player.hp else (" for no damage" if game.player.tempDamageModifier == 0 else ""))
            case "Move":
                while self.speedLeft > 0 and len(action[1]) > 1:
                    del action[1][-1]
                    self.move(game.encounter, game, target = action[1][-1])
                return "moved"
            case "Wait":
                return "waited"

    # Returns: ("Active", Action) / ("Move", route) / ("Wait")
    def determineBestAction(self, game):
        actions = self.getFullActionList()

        currentBestAction = "Move"

        for action in actions:
            if self.checkCanUse(action, game) and (currentBestAction == "Move" or action.aiPrio > currentBestAction.aiPrio):
                currentBestAction = action

        if self.speed <= 0 and currentBestAction == "Move":
            return ("Wait",)

        if currentBestAction == "Move":
            distToPlr = max(abs(self.x - game.player.x), abs(self.y - game.player.y))
            if distToPlr > self.preferredDist:
                move = aStar.getRoute((self.x, self.y), (game.player.x, game.player.y), self, game)
            elif distToPlr < self.preferredDist:
                targX = 1 if self.x < game.player.x else (game.player.x if self.x == game.player.x else game.encounter.width)
                targY = 1 if self.y < game.player.y else (game.player.y if self.y == game.player.y else game.encounter.height)
                move = aStar.getRoute((self.x, self.y), (targX, targY), self, game, True)
            else:
                return ("Wait",)

            if move == "No Path":
                return ("Wait",)
            
            return ("Move", move)
        else:
            return ("Active", currentBestAction)

    # Check if an action can be used against the player
    def checkCanUse(self, action, game):
        plr = game.player
        dist = max(abs(plr.x - self.x), abs(plr.y - self.y))

        return action.range >= dist and (action.charges >= 1 or action.charges < 0)
    
    def isWithinDistance(self, distance, point):
        return max(abs(self.x - point[0]), abs(self.y - point[1])) <= distance
    
    def testEnem(self):
        return True



   

        

