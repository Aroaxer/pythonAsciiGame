import copy

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

enemAcs = {
    "Gore" : Action("Gore", aiPrio=1),
    "Spit" : Action("Spit", aiPrio=1, range = 2)
}

# Traits

# Weapons
weps = {
    "Sword" : Weapon("Sword", 5, "Melee", traits = [c(acs["Basic Attack"])])
}

enemWeps = {
    "Boar Tusk" : Weapon("Boar Tusk", 2, "Melee", traits = [c(enemAcs["Gore"])]),
    "Spit" : Weapon("Spit", 1, "Ranged", traits = [c(enemAcs["Spit"])])
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
