from Stages.stage import Stage
from Traits.trait import Trait

# Enemies
preEnemies = [
    ["Wild Boar"]
]

# Stages
sunlitField = Stage("Sunlit Field", preEnemies[0], 5, 5, 7, 7)

stall = Trait("Active", "", aiPrio = 100)