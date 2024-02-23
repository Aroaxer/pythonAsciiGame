import copy

from Stages.stage import Stage
from Traits.trait import Trait
from Traits.action import Action
from Items.Gear.weapon import Weapon

# Copy an object without a really long command
def c(obj):
    return copy.deepcopy(obj)

# Actions
acs = {
    "Basic Attack" : Action("Basic Attack"),
    "Slam" : Action("Slam", maxCharges=1, aiPrio=1)
}

# Traits

# Weapons
weps = {
    "Sword" : Weapon("Sword", 5, "Melee", traits = [c(acs["Basic Attack"])])
}

# Other Helds
offs = {

}

# Armor
armors = {

}

# Helmets
helms = {

}

# Accesories
accs = {

}



# Enemies
preEnemies = [
    [("Wild Boar", 7), ("Spitting Cobra", 4)]
]

# Stages
# Each row holds stages that can be at that position
stages = [
    [Stage("Sunlit Field", preEnemies[0], 5, 5, length=2)],
    [Stage("Shaded Forest", preEnemies[0], 3, 5, 5, 7, length=2)],
    [Stage("Forest Tower", preEnemies[0], 7, 7, 7, 7, length=2, prevStages = [0])]
]

