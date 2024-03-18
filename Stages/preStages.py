from Stages.stage import Stage
import premades as pre


# Stages
# Each row holds stages that can be at that position
stages = [
    [Stage("Sunlit Field", 1, pre.preEnemies["Sunlit Field"], pre.lootPools["Standard"], 5, 5, length=6)],
    [Stage("Shaded Forest", 2, pre.preEnemies["Shaded Forest"], pre.lootPools["Standard"], 3, 5, 5, 7, length=6)],
    [Stage("Forest Tower", 3, pre.preEnemies["Forest Tower"], pre.lootPools["Standard"], 7, 7, 7, 7, length=6, prevStages = ["Shaded Forest"])]
]

