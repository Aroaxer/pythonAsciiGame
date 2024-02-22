import math

from Entities.Characters.character import Character

import aStar

class Enemy(Character):
    preferredDist = 0
    mapIcon = ""
    
    def __init__(self, name, hp, x, y, speed = 1, actions = 1, preferredDist = 1, mapIcon = "E") -> None:
        self.preferredDist = preferredDist
        self.mapIcon = mapIcon
        super().__init__(name, hp, x, y, speed, actions)

    def takeAction(self, game):
        self.speedLeft = self.speed
        self.actionsLeft -= 1

        action = self.determineBestAction(game)

        match action[0]:
            case "Active":
                pass
            case "Move":
                while self.speedLeft > 0 and len(action[1]) > 1:
                    del action[1][-1]
                    self.move(game.encounter, game, target = action[1][-1])

    # Returns: ("Active", Action) / ("Move", route) / ("Wait")
    def determineBestAction(self, game):
        actions = self.getFullActionList()

        currentBestAction = "Move"

        for action in enumerate(actions):
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
    
    def isInRegion(self, topLeft, botRight):
        return (self.x >= topLeft[0] and self.y >= topLeft[1]) and (self.x <= botRight[0] and self.y <= botRight[1])
    
    def isWithinDistance(self, distance, point):
        return max(abs(self.x - point[0]), abs(self.y - point[1])) <= distance



   

        

