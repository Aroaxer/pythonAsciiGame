import copy

from Traits.trait import Trait
from Traits.action import Action
from Traits.action import enemAction
from Items.Gear.weapon import Weapon
from Items.Gear.armor import Armor
from Items.Gear.accessory import Accessory
from Items.Gear.heldItem import HeldItem

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
    "Ritual Stab" : Action("Ritual Stab", "Ritual Attack", maxCharges=2, recharge="Encounter"),
    "Whirl" : Action("Whirl", "1x Damage", targeting="Centered", maxCharges=5, rechargePercent=0.2, width=5),
    
    # Physical Ranged
    "Basic Shot" : Action("Basic Shot", "1x Damage", range=3),
    "Pierce" : Action("Pierce", "1x Damage", targeting="Directional", maxCharges=1, length=5),
    "Shatter" : Action("Shatter", "1.5x Damage", maxCharges=1, range=3),

    # Magical
    "Fire Bolt" : Action("Fire Bolt", "1x Damage", maxCharges=1, range=3),
    "Fireball" : Action("Fireball", "1x Damage", targeting="Point", maxCharges=1, rechargePercent=0.5, range=3, width=3),
    "Arcane Rays" : Action("Arcane Rays", "1x Damage", targeting="Multi 2", maxCharges=5, rechargePercent=0.2, range=3),
    "Magic Missiles" : Action("Magic Missiles", "1x Damage", targeting="Multi 4", maxCharges=1, rechargePercent=0.5, range=4),

    # Utility
    "Hasten" : Action("Hasten", "Hasten", targeting="Self", maxCharges=2, recharge="Encounter"),
    "Shove" : Action("Shove", "Repel 3"),

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
    "Repel" : Trait("Repel", "After Damage", "Repel 1"),
    "Regenerate" : Trait("Regenerate", "Turn", "Regenerate"),
    "Extra Action" : Trait("Extra Action", "Turn", "Action 1")
}

# Weapons
weps = {
    # Physical Melee
    "Sword" : Weapon("Sword", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slash"])]),
    "Hammer" : Weapon("Hammer", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slam"])]),
    "Spear" : Weapon("Spear", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Impale"])]),
    "Ritual Dagger" : Weapon("Ritual Dagger", 6, "Melee", traits=[c(acs["Ritual Stab"])], specialTags=["Light"]),

    # Physical Ranged
    "Bow" : Weapon("Bow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Pierce"])]),
    "Crossbow" : Weapon("Crossbow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Shatter"])]),

    # Magical Ranged
    "Fire Staff" : Weapon("Fire Staff", 4, "Magic", traits = [c(acs["Fire Bolt"]), c(acs["Fireball"])]),
    "Arcane Staff" : Weapon("Arcane Staff", 2, "Magic", traits = [c(acs["Arcane Rays"]), c(acs["Magic Missiles"])])
}
upgradedWeps = {
    # Physical Melee
    "Wind Blade" : Weapon("Wind Blade", 8, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slash"]), c(acs["Whirl"])]),
    "Flamehammer" : Weapon("Flamehammer", 8, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slam"]), c(acs["Fireball"])])

    # Physical Ranged

    # Magical Ranged
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
    "Shield" : HeldItem("Shield", 0, traits=[c(acs["Block"])])

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
    "Hastening Amulet" : Accessory("Hastening Amulet", speedBoost=1, actionBoost=1),
    "Shoving Gauntlets" : Accessory("Shoving Gauntlets", speedBoost=1, traits=[c(acs["Shove"])])

    # Offensive

}

# Loot Pools
lootPools = {
    "Standard" : utils.merge(weps.values(), armors.values(), offs.values(), helms.values(), accs.values()),
    "Upgraded" : utils.merge(upgradedWeps.values())
}



# Enemies
preEnemies = {
    "Sunlit Field" : [("Wild Boar", 7), ("Spitting Cobra", 4), ("Forest Golem", 15)],
    "Shaded Forest" : [("Goblin", 5), ("Hobgoblin", 8), ("Bugbear", 10), ("Hobgoblin Devastator", 20)],
    "Forest Tower" : [("Turret", 3), ("Stone Golem", 10), ("Golem Mage", 8), ("Iron Golem", 25)]
}
