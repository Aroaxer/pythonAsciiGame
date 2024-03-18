import copy

from Traits.trait import Trait
from Traits.action import Action
from Items.Gear.weapon import Weapon
from Items.Gear.armor import Armor

import utils

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
    "Pierce" : Action("Pierce", targeting="Directional", maxCharges=1, length=5),
    "Shatter" : Action("Shatter", maxCharges=1, range= 3),

    # Magical
    "Fire Bolt" : Action("Fire Bolt", maxCharges=1, range= 3),
    "Fireball" : Action("Fireball", targeting="Point", maxCharges=1, rechargePercent=0.5, range=3, width=3),

    # Utility
    "Hasten" : Action("Hasten", targeting="Self", maxCharges=2, recharge="Encounter"),

    # Defensive
    "Block" : Action("Block", targeting="Self")
}

enemAcs = {
    "Melee" : Action("Melee", aiPrio=1),
    "Ranged" : Action("Ranged", aiPrio=1, range = 2)
}

# Traits
traits = {
    "Spikes" : Trait("After Damage", "Spikes"),
    "Repel" : Trait("After Damage", "Repel"),
    "Regenerate" : Trait("Turn", "Regenerate")
}

# Weapons
weps = {
    # Physical Melee
    "Sword" : Weapon("Sword", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slash"])]),
    "Hammer" : Weapon("Hammer", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slam"])]),
    "Spear" : Weapon("Spear", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Impale"])]),

    # Physical Ranged
    "Bow" : Weapon("Bow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Pierce"])]),
    "Crossbow" : Weapon("Crossbow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Shatter"])]),

    # Magical Ranged
    "Fire Staff" : Weapon("Fire Staff", 4, "Magic", traits = [c(acs["Fire Bolt"]), c(acs["Fireball"])])
}
upgradedWeps = {

}

enemWeps = {
    "Weak Melee" : Weapon("Weak Melee", 2, "Melee", traits = [c(enemAcs["Melee"])]),
    "Weak Ranged" : Weapon("Weak Ranged", 1, "Ranged", traits = [c(enemAcs["Ranged"])])
}

# Other Helds
offs = {
    
}

# Armor
armors = {
    # Defensive
    "Spiked Mail" : Armor("Spiked Armor", 15, damage=2, traits=[c(traits["Spikes"])]),
    "Overgrown Plate" : Armor("Overgrown Plate", 25, traits=[c(traits["Regenerate"])])

    # Utility
}

enemArmrs = {
    "Weak No Special" : Armor("Weak No Special", 10),
    "Weak Reflect" : Armor("Weak Reflect", 10, damage=1, traits=[c(traits["Spikes"])])
}

# Helmets
helms = {

}

# Accesories
accs = {

}

# Loot Pools
lootPools = {
    "Standard" : utils.merge(weps.values(), armors.values()),
    "Upgraded" : utils.merge(upgradedWeps.values())
}



# Enemies
preEnemies = {
    "Sunlit Field" : [("Wild Boar", 7), ("Spitting Cobra", 4), ("Forest Golem", 15)],
    "Shaded Forest" : [("Goblin", 5), ("Hobgoblin", 8), ("Bugbear", 10), ("Hobgoblin Devastator", 20)],
    "Forest Tower" : [("Turret", 3), ("Stone Golem", 10), ("Golem Mage", 8), ("Iron Golem", 25)]
}
