import math

from Entities.Characters.character import Character
import premades as pre

import aStar

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

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
            case "Spitting Cobra":
                self.mapIcon = "C"
                self.preferredDist = 2

                self.putOn(pre.enemWeps["Weak Ranged"], "Mainhand")

                # Boss
            case "Forest Golem":
                self.mapIcon = "#"
                
                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
                self.putOn(pre.enemArmrs["Weak Reflect"], "Armor")


            # Stage 2
                # Shaded Forest
            case "Goblin":
                self.mapIcon = "G"

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
            case "Hobgoblin":
                self.mapIcon = "H"
                self.preferredDist = 2

                self.putOn(pre.enemWeps["Weak Ranged"], "Mainhand")
            case "Bugbear":
                self.mapIcon = "B"
                self.difficultyValue = 2
                
                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
                self.putOn(pre.enemArmrs["Weak No Special"], "Armor")
                
                # Boss
            case "Hobgoblin Devastator":
                self.mapIcon = "#"
                self.preferredDist = 3

                actions = 2

                self.putOn(pre.enemWeps["Weak Magic"], "Mainhand")

                # Dark Cave
                # Note: Also references 'Goblin' from Shaded Forest
            case "Bat":
                self.mapIcon = "B"

                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
            case "Giant Spider":
                self.mapIcon = "S"

                actions = 3

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")

                # Boss
            case "Stone Giant":
                self.mapIcon = "#"

                actions = 4

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
            

            # Stage 3
                # Forest Tower
            case "Turret":
                self.mapIcon = "T"
                
                speed = 0

                self.putOn(pre.enemWeps["Weak Ranged"], "Mainhand")
            case "Stone Golem":
                self.mapIcon = "S"
                self.difficultyValue = 2

                speed = 2

                self.putOn(pre.enemWeps["Weak Melee"], "Mainhand")
                self.putOn(pre.enemArmrs["Weak No Special"], "Armor")
            case "Golem Mage":
                self.mapIcon = "M"
                self.preferredDist = 3
                self.difficultyValue = 2

                actions = 2

                self.putOn(pre.enemWeps["Weak Magic"], "Mainhand")

                # Boss
            case 'Iron Golem':
                self.mapIcon = "#"

                speed = 3
                actions = 2

                self.putOn(pre.enemWeps["Medium Melee"], "Mainhand")
                self.putOn(pre.enemArmrs["Weak No Special"], "Armor")

                
                


            case _:
                pass


        super().__init__(name, hp, x, y, speed, actions)

    def takeAction(self, game):
        self.speedLeft = self.speed
        self.actionsLeft -= 1

        action = self.determineBestAction(game)

        match action[0]:
            case "Active":
                oldPlHp = game.player.hp
                action[1].activate(game, "Active", action[1].tiedEquipment, self)
                return f"used {action[1].name}" + (f" and did {oldPlHp - game.player.hp} damage" if oldPlHp != game.player.hp else "")
            case "Move":
                while self.speedLeft > 0 and len(action[1]) > 1:
                    del action[1][-1]
                    self.move(game.encounter, game, target = action[1][-1])
                return "moved"

    # Returns: ("Active", Action) / ("Move", route) / ("Wait")
    def determineBestAction(self, game):
        actions = self.getFullActionList()

        currentBestAction = "Move"

        for action in actions:
            if self.checkCanUse(action, game) and (currentBestAction == "Move" or action.aiPrio > currentBestAction.aiPrio):
                currentBestAction = action

        if currentBestAction == "Move":
            move = aStar.getRoute((self.x, self.y), (game.player.x, game.player.y), self, game)

            if move == "No Path":
                return ("Wait")

            return ("Move", move)
        else:
            return ("Active", currentBestAction)

    # Check if an action can be used against the player
    def checkCanUse(self, action, game):
        plr = game.player
        dist = max(abs(plr.x - self.x), abs(plr.y - self.y))

        return action.range >= dist
    
    def isWithinDistance(self, distance, point):
        return max(abs(self.x - point[0]), abs(self.y - point[1])) <= distance
    
    def testEnem(self):
        return True



   

        

