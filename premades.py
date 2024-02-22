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
    [("Wild Boar", 7)]
]

# Stages
sunlitField = Stage("Sunlit Field", preEnemies[0], 5, 5, 7, 7)

