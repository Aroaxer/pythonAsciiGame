import copy

from Traits.trait import Trait
from Traits.action import Action
from Items.Gear.weapon import Weapon

# Copy an object without a really long command
def c(obj):
    return copy.deepcopy(obj)

# Actions
acs = {
    # Physical Melee
    "Basic Attack" : Action("Basic Attack"),
    "Slam" : Action("Slam", maxCharges=1),
    "Slash" : Action("Slash", targeting="Directional", maxCharges=1, width=3),
    "Impale" : Action("Impale", targeting="Directional", maxCharges=1, length=3),
    
    # Physical Ranged
    "Basic Shot" : Action("Basic Shot", range=3),
    "Pierce" : Action("Pierce", targeting="Directional", maxCharges=1, length=5)

    # Magical

}

enemAcs = {
    "Gore" : Action("Gore", aiPrio=1),
    "Spit" : Action("Spit", aiPrio=1, range = 2)
}

# Traits

# Weapons
weps = {
    # Physical Melee
    "Sword" : Weapon("Sword", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slash"])]),
    "Hammer" : Weapon("Hammer", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slam"])]),
    "Spear" : Weapon("Spear", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Impale"])]),

    # Physical Ranged
    "Bow" : Weapon("Bow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Pierce"])])
}
upgradedWeps = {

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

# Loot Pools
lootPools = {
    "Standard" : weps.values(),
    "Upgraded" : upgradedWeps.values()
}



# Enemies
preEnemies = [
    [("Wild Boar", 7), ("Spitting Cobra", 4)]
]
