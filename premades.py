import copy

from Traits.trait import Trait
from Traits.action import Action
from Traits.action import enemAction
from Items.Gear.weapon import Weapon
from Items.Gear.armor import Armor
from Items.Gear.helmet import Helmet
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
    "Shatterwave" : Action("Shatterwave", "1.5x Damage", targeting="Directional", maxCharges=2, rechargePercent=0.5, width=3, length=5),
    "Toss" : Action("Toss", "1x Damage", maxCharges=1, range=2, freeAction=True),
    "Twin Shot" : Action("Twin Shot", "0.5x Damage", targeting="Multi 2", range=3),

    # Magical
    "Firebolt" : Action("Firebolt", "1x Damage", maxCharges=1, range=3),
    "Fireball" : Action("Fireball", "1x Damage", targeting="Point", maxCharges=1, rechargePercent=0.5, range=3, width=3),
    "Enhanced Firebolt" : Action("Enhanced Firebolt", "1x Damage", range=5),
    "Flamethrower" : Action("Flamethrower", "1x Damage", targeting="Directional", maxCharges=2, rechargePercent=0.5, length=4),
    "Arcane Rays" : Action("Arcane Rays", "1x Damage", targeting="Multi 2", maxCharges=5, rechargePercent=0.2, range=3),
    "Magic Missiles" : Action("Magic Missiles", "1x Damage", targeting="Multi 4", maxCharges=1, rechargePercent=0.5, range=4),

    # Utility
    "Hasten" : Action("Hasten", "Hasten", targeting="Self", maxCharges=2, recharge="Encounter"),
    "Shove" : Action("Shove", "Repel 3"),
    "Pull" : Action("Pull", "Pull", maxCharges=1, range=4, freeAction=True),
    "Teleport" : Action("Teleport", "Teleport", targeting="Point No Enemy", range=10),

    # Defensive
    "Block" : Action("Block", "Block", targeting="Self"),
    "Arcane Shield" : Action("Arcane Shield", "Invuln", targeting="Self", maxCharges=2, recharge="Encounter", rechargePercent=0.5)
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
    "Chain Reduction" : Trait("Chain Reduction", "Before Damage", "Minor Block")
}

# Weapons
# This must be defined in this order
upgradedWeps = {
    # Physical Melee
    "Wind Blade" : Weapon("Wind Blade", 10, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slash"]), c(acs["Whirl"])]),
    "Flamehammer" : Weapon("Flamehammer", 10, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slam"]), c(acs["Fireball"])]),
    "Runed Halberd" : Weapon("Runed Halberd", 10, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Impale"]), c(acs["Slash"]), c(acs["Firebolt"])]),

    # Physical Ranged
    "Twinshot Bow" : Weapon("Twinshot Bow", 8, "Ranged", traits = [c(acs["Twin Shot"]), c(acs["Pierce"]), c(acs["Shove"])]),
    "Handheld Ballista" : Weapon("Handheld Ballista", 8, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Shatterwave"])]),

    # Magical Ranged
    "Inferno Cane" : Weapon("Inferno Cane", 8, "Magic", traits = [c(acs["Enhanced Firebolt"]), c(acs["Fireball"]), c(acs["Flamethrower"])]),
    "Archmage Rod" : Weapon("Archmage Rod", 8, "Magic", traits = [c(acs["Arcane Rays"]), c(acs["Magic Missiles"]), c(acs["Arcane Shield"])])
}
weps = {
    # Physical Melee
    "Sword" : Weapon("Sword", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slash"])], upgradedForm = upgradedWeps["Wind Blade"]),
    "Hammer" : Weapon("Hammer", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Slam"])], upgradedForm = upgradedWeps["Flamehammer"]),
    "Spear" : Weapon("Spear", 5, "Melee", traits = [c(acs["Basic Attack"]), c(acs["Impale"])], upgradedForm = upgradedWeps["Runed Halberd"]),

    # Physical Ranged
    "Bow" : Weapon("Bow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Pierce"])], upgradedForm = upgradedWeps["Twinshot Bow"]),
    "Crossbow" : Weapon("Crossbow", 4, "Ranged", traits = [c(acs["Basic Shot"]), c(acs["Shatter"])], upgradedForm = upgradedWeps["Handheld Ballista"]),

    # Magical Ranged
    "Fire Staff" : Weapon("Fire Staff", 4, "Magic", traits = [c(acs["Firebolt"]), c(acs["Fireball"])], upgradedForm = upgradedWeps["Inferno Cane"]),
    "Arcane Staff" : Weapon("Arcane Staff", 2, "Magic", traits = [c(acs["Arcane Rays"]), c(acs["Magic Missiles"])], upgradedForm = upgradedWeps["Archmage Rod"])
}

enemWeps = {
    "Weak Melee" : Weapon("Weak Melee", 2, "Melee", traits = [c(enemAcs["Melee"])]),
    "Weak Ranged" : Weapon("Weak Ranged", 1, "Ranged", traits = [c(enemAcs["Ranged"])]),
    "Weak Magic" : Weapon("Weak Magic", 2, "Magic", traits = [c(enemAcs["Magic"]), c(enemAcs["Fireball"])]),

    "Medium Melee" : Weapon("Medium Melee", 3, "Melee", traits = [c(enemAcs["Melee"])]),
    "Medium Ranged" : Weapon("Medium Ranged", 2, "Ranged", traits = [c(enemAcs["Ranged"])]),
    "Medium Magic" : Weapon("Medium Magic", 2, "Magic", traits = [c(enemAcs["Magic"]), c(enemAcs["Fireball"])])
}

# Other Helds
offs = {
    # Offensive
    "Ritual Dagger" : HeldItem("Ritual Dagger", 4, traits=[c(acs["Ritual Stab"])]),
    "Rope Hook" : HeldItem("Rope Hook", 1, traits = [c(acs["Pull"])]),
    "Kunai" : HeldItem("Kunai", 2, traits = [c(acs["Toss"])]),

    # Defensive
    "Shield" : HeldItem("Shield", 0, traits = [c(acs["Block"])])

    # Utility
    
}

# Armor
armors = {
    # Defensive
    "Spiked Mail" : Armor("Spiked Armor", 15, damage=2, traits = [c(traits["Spikes"])]),
    "Overgrown Plate" : Armor("Overgrown Plate", 25, traits = [c(traits["Regenerate"])]),

    # Utility
    "Swift Leather" : Armor("Swift Leather", 0, speedBoost=2, actionBoost=1)
}

enemArmrs = {
    "Weak No Special" : Armor("Weak No Special", 10),
    "Weak Reflect" : Armor("Weak Reflect", 10, damage=1, traits = [c(traits["Spikes"])])
}

# Helmets
helms = {
    # Defensive
    "Reactive Helm" : Helmet("Reactive Helm", traits = [c(traits["Chain Reduction"])]),

    # Utility
    "Phasing Helm" : Helmet("Phasing Helm", traits = [c(acs["Teleport"])])
}

# Accesories
accs = {
    # Defensive
    "Brooch of Shielding" : Accessory("Brooch of Shielding", traits = [c(acs["Arcane Shield"])]),

    # Utility
    "Hastening Amulet" : Accessory("Hastening Amulet", actionBoost=1),
    "Shoving Gauntlets" : Accessory("Shoving Gauntlets", speedBoost=1, traits = [c(acs["Shove"])])

    # Offensive

}

# Loot Pools
lootPools = {
    "Standard" : utils.merge(weps.values(), armors.values(), offs.values(), helms.values(), accs.values()),
    "Upgraded" : utils.merge(upgradedWeps.values())
}



# Enemies
preEnemies = {
    "Sunlit Field" : [("Wild Boar", 7), ("Spitting Cobra", 4), ("Forest Golem", 20)],
    "Shaded Forest" : [("Goblin", 5), ("Hobgoblin", 8), ("Bugbear", 10), ("Hobgoblin Devastator", 25)],
        "Dark Cave" : [("Bat", 4), ("Goblin", 5), ("Giant Spider", 8), ("Stone Giant", 30)],
    "Forest Tower" : [("Turret", 3), ("Stone Golem", 10), ("Golem Mage", 8), ("Iron Golem", 40)]
}
