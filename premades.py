from Stages.stage import Stage
from Traits.trait import Trait
from Traits.action import Action
from Items.Gear.weapon import Weapon

# Actions
acs = {
    "Basic Attack" : Action("Basic Attack"),
    "Slam" : Action("Slam", maxCharges=1, aiPrio=1)
}

# Traits

# Weapons
weps = {
    "Sword" : Weapon(acs["Basic Attack"], "Melee",)
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
    ["Wild Boar"]
]

# Stages
sunlitField = Stage("Sunlit Field", preEnemies[0], 5, 5, 7, 7)

