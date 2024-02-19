import math

from Entities.object import Object

class Character(Object):
    speed = 0
    speedLeft = 0

    actions = 0
    actionsLeft = 0

    mainhand = None
    offhand = None
    armor = None
    helmet = None
    accesory = None

    def __init__(self, x, y, speed, actions = 1) -> None:
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

        while abs(cx) > 0:
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

            cx -= (cx / abs(cx))

        self.speedLeft -= abs(stX - cx)

        while abs(cy) > 0:
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

            cy -= (cy / abs(cy))

        self.speedLeft -= abs(stY - cy)

        self.speedLeft -= abs(stY - self.y) if not ignoreSpd else 0

    def takeTurn(self, game):
        self.actionsLeft = self.actions

        while self.actionsLeft > 0:
            self.takeAction(game)

    def takeAction(self, game):
        self.actionsLeft = 0
        return None # This function is defined by subclasses
    
    # Returns a list of all actions for all equipments
    def getFullActionList(self):
        actionList = []

        # I have no clue if there is a shorter way to do this
        try: actionList.append(action for action in self.mainhand.traits if action.trigger == "Active")
        except Exception: pass
        try: actionList.append(action for action in self.offhand.traits if action.trigger == "Active")
        except Exception: pass
        try: actionList.append(action for action in self.armor.traits if action.trigger == "Active")
        except Exception: pass
        try: actionList.append(action for action in self.helmet.traits if action.trigger == "Active")
        except Exception: pass
        try: actionList.append(action for action in self.accesory.traits if action.trigger == "Active")
        except Exception: pass

        return actionList
