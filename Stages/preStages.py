from Stages.stage import Stage
import premades as pre


# Stages
# Each row holds stages that can be at that position
stages = [
    [Stage("Sunlit Field", 1, pre.preEnemies[0], pre.lootPools[0], 5, 5, length=6)],
    [Stage("Shaded Forest", 2, pre.preEnemies[0], pre.lootPools[1], 3, 5, 5, 7, length=6)],
    [Stage("Forest Tower", 3, pre.preEnemies[0], pre.lootPools[2], 7, 7, 7, 7, length=6, prevStages = ["Shaded Forest"])]
]

