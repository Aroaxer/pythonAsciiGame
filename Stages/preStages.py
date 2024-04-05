from Stages.stage import Stage
import premades as pre


# Stages
# Each row holds stages that can be at that position
stages = [
    [Stage("Sunlit Field", 1, pre.preEnemies["Sunlit Field"], pre.lootPools["Tier 1"], 5, 5, length=4, enemCount=(2,3))],
    [Stage("Shaded Forest", 2, pre.preEnemies["Shaded Forest"], pre.lootPools["Tier 1"], 3, 5, 5, 7, length=4, enemCount=(2,4)),
        Stage("Dark Cave", 2, pre.preEnemies["Dark Cave"], pre.lootPools["Tier 1"], 3, 5, 5, 7, length=4, enemCount=(3,4), lootAmount=5)],
    [Stage("Forest Tower", 3, pre.preEnemies["Forest Tower"], pre.lootPools["Tier 1"], 7, 7, 7, 7, length=6, prevStages=["Shaded Forest"], enemCount=(3,5)),
        Stage("Crystal Cavern", 3, pre.preEnemies["Crystal Cavern"], pre.lootPools["Tier 1"], 5, 5, 7, 9, length=6, prevStages=["Dark Cave"], enemCount=(4,5), lootAmount=5)],
    [Stage("Fey Grove", 4, pre.preEnemies["Fey Grove"], pre.lootPools["Tier 2"], 5, 5, 7, 7, length=8, prevStages=["Forest Tower"], enemCount=(5,5)),
        Stage("Scorched Desert", 4, pre.preEnemies["Scorched Desert"], pre.lootPools["Tier 2"], 7, 7, 11, 11, length=8, enemCount=(6,8), lootAmount=5),
        Stage("Icy Tundra", 4, pre.preEnemies["Icy Tundra"], pre.lootPools["Tier 2"], 5, 5, 9, 9, length=8, enemCount=(5,7))]
]

