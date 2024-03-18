import copy

from Traits.trait import Trait
from Traits.action import Action
from Traits.action import enemAction
from Items.Gear.weapon import Weapon
from Items.Gear.armor import Armor
from Items.Gear.accessory import Accessory as Acc
from Items.Gear.equippable import Equippable as Equip

import utils

# Copy an object without a really long command
def c(obj):
    return copy.deepcopy(obj)

# Actions
acs = {
    # Physical Melee
    "Basic Attack" : Action("Basic Attack", "1x Damage"),
    "Slam" : Action("Slam", "1.5x Damage", maxCharges=1),
    "Slash" : Action("Slash", "1x Damage", targeting="Directional", maxCharges=1, width=3),
    "Impale" : Action("Impale", "1x Damage", targeting="Directional", maxCharges=1, length=3),
    
    # Physical Ranged
    "Basic Shot" : Action("Basic Shot", "1x Damage", range=3),
    "Pierce" : Action("Pierce", "1x Damage", targeting="Directional", maxCharges=1, length=5),
    "Shatter" : Action("Shatter", "1.5x Damage", maxCharges=1, range= 3),

    # Magical
    "Fire Bolt" : Action("Fire Bolt", "1x Damage", maxCharges=1, range= 3),
    "Fireball" : Action("Fireball", "1x Damage", targeting="Point", maxCharges=1, rechargePercent=0.5, range=3, width=3),

    # Utility
    "Hasten" : Action("Hasten", "Hasten", targeting="Self", maxCharges=2, recharge="Encounter"),

    # Defensive
    "Block" : Action("Block", "Block", targeting="Self")
}

enemAcs = {
    "Melee" : enemAction("1x Damage", aiPrio=1),
    "Ranged" : enemAction("1x Damage", aiPrio=1, range = 2),
    "Magic" : enemAction("1x Damage", aiPrio=1, range = 3, maxCharges=1),
    "Fireball" : enemAction("1.5x Damage", aiPrio=2, range = 3, maxCharges=1, rechargePercent=0.5)
}

# Traits
traits = {
    "Spikes" : Trait("Spikes", "After Damage", "Spikes"),
    "Repel" : Trait("Repel", "After Damage", "Repel"),
    "Regenerate" : Trait("Regenerate", "Turn", "Regenerate")
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
    "Weak Ranged" : Weapon("Weak Ranged", 1, "Ranged", traits = [c(enemAcs["Ranged"])]),
    "Weak Magic" : Weapon("Weak Magic", 2, "Ranged", traits=[c(enemAcs["Magic"]), c(enemAcs["Fireball"])])
}

# Other Helds
offs = {
    # Offhand weapons have the 'light' special tag
    # Offensive
    
    # Defensive
    

    # Utility
    
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
    # Defensive

    # Utility

}

# Accesories
accs = {
    # Defensive

    # Utility

    # Offensive

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
