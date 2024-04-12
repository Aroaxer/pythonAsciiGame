from Stages.stage import Stage
import premades as pre


# Stages
# Each row holds stages that can be at that position
stages = [
    [Stage("Sunlit Field", 1, pre.preEnemies["Sunlit Field"], pre.lootPools["Tier 1"], 5, 5, length=4, enemCount=(2,3))],
    [Stage("Shaded Forest", 2, pre.preEnemies["Shaded Forest"], pre.lootPools["Tier 1"], 3, 5, 5, 7, length=4, enemCount=(2,4)),
        Stage("Dark Cave", 2, pre.preEnemies["Dark Cave"], pre.lootPools["Tier 1"], 3, 5, 5, 7, length=4, enemCount=(3,4))],
    [Stage("Forest Tower", 3, pre.preEnemies["Forest Tower"], pre.lootPools["Tier 1"], 7, 7, 7, 7, length=6, prevStages=["Shaded Forest"], enemCount=(3,5)),
        Stage("Crystal Cavern", 3, pre.preEnemies["Crystal Cavern"], pre.lootPools["Tier 1"], 5, 5, 7, 9, length=6, prevStages=["Dark Cave"], enemCount=(4,5))],
    [Stage("Fey Grove", 4, pre.preEnemies["Fey Grove"], pre.lootPools["Tier 1"], 5, 5, 7, 7, length=8, prevStages=["Forest Tower"], enemCount=(5,5)),
        Stage("Scorched Desert", 4, pre.preEnemies["Scorched Desert"], pre.lootPools["Tier 1"], 7, 7, 11, 11, length=8, enemCount=(6,8)),
        Stage("Icy Tundra", 4, pre.preEnemies["Icy Tundra"], pre.lootPools["Tier 1"], 5, 5, 9, 9, length=8, enemCount=(5,7))],
    [Stage("Royal Palace", 5, pre.preEnemies["Royal Palace"], pre.lootPools["Tier 2"], 5, 7, 7, 9, length=10, enemCount=(6,8)),
        Stage("The Antitower [Hard]", 5, pre.preEnemies["The Antitower"], pre.lootPools["Tier 1"], 3, 7, 5, 9, length=8, enemCount=(5, 7), lootAmount=5)],
    [Stage("Astral Plane [Hard]", 6, pre.preEnemies["Astral Plane"], pre.lootPools["Tier 1"], 7, 7, 11, 11, length=10, prevStages=["The Antitower [Hard]"], enemCount=(7, 9), lootAmount=5),
        Stage("The Abyss [Very Hard]", 6, pre.preEnemies["The Abyss"], pre.lootPools["Tier 1"], 9, 9, 13, 13, length=12, prevStages=["The Antitower [Hard]"], enemCount=(8, 10), lootAmount=7)],
    [Stage("Mount Celestia [Hard]", 7, pre.preEnemies["Mount Celestia"], pre.lootPools["Tier 2"], 7, 7, 11, 11, length=10, prevStages=["Astral Plane [Hard]"], enemCount=(7, 9), lootAmount=5),
        Stage("The Nine Hells [Very Hard]", 7, pre.preEnemies["The Nine Hells"], pre.lootPools["Tier 2"], 11, 11, 15, 15, length=12, prevStages=["The Abyss [Very Hard]"], enemCount=(9, 12), lootAmount=7)]
]

