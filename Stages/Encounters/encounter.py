

class Encounter():
    width = 0
    height = 0

    # Should be: "Equipment" / "Consumable" / "Gold" / "Upgrade"
    rewardType = ""

    def __init__(self, width, height, reward = "Gold") -> None:
        if width % 2 == 0: width += 1
        if height % 2 == 0: height += 1
        self.width = width
        self.height = height

        self.rewardType = reward
    
    # Grant a reward based on rewardType
    def grantReward(self, game):
        match self.rewardType:

            
            case _:
                pass