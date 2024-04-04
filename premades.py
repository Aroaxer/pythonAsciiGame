from Traits.trait import Trait
from Traits.action import Action
from Items.Gear.equippable import Equippable as Equip

import utils

# Actions
acs = {
    # Physical Melee
    "Basic Attack" : Action("Basic Attack", "1x Damage"),
    "Slam" : Action("Slam", "1.5x Damage", maxCharges=1),
    "Slash" : Action("Slash", "1x Damage", "Directional", maxCharges=1, width=3),
    "Impale" : Action("Impale", "1x Damage", "Directional", maxCharges=1, length=3),
    "Ritual Stab" : Action("Ritual Stab", "Ritual Attack", maxCharges=2, recharge="Encounter"),
    "Whirl" : Action("Whirl", "1x Damage", "Centered", maxCharges=5, rechargePercent=0.2, width=3),
    "Bloodwave" : Action("Bloodwave", "1.5x Damage", "Directional", maxCharges=5, recharge="Never", width=3, length=5),
    
    # Physical Ranged
    "Basic Shot" : Action("Basic Shot", "1x Damage", range=3),
    "Pierce" : Action("Pierce", "1x Damage", "Directional", maxCharges=1, length=5),
    "Shatter" : Action("Shatter", "1.5x Damage", maxCharges=1, range=3),
    "Shatterwave" : Action("Shatterwave", "1.5x Damage", "Directional", maxCharges=2, rechargePercent=0.5, width=1, length=5),
    "Throw" : Action("Throw", "1x Damage", range=2),
    "Toss" : Action("Toss", "1x Damage", maxCharges=1, range=2, freeAction=True),
    "Twin Shot" : Action("Twin Shot", "0.5x Damage", "Multi 2", range=3),

    # Magical
    "Firebolt" : Action("Firebolt", "1x Damage", maxCharges=1, range=3),
    "Fireball" : Action("Fireball", "1x Damage", "Point", maxCharges=1, rechargePercent=0.5, range=3, width=3),
    "Enhanced Firebolt" : Action("Enhanced Firebolt", "1x Damage", range=5),
    "Flamethrower" : Action("Flamethrower", "1x Damage", "Directional", maxCharges=2, rechargePercent=0.5, length=4),
    "Arcane Rays" : Action("Arcane Rays", "1x Damage", "Multi 2", maxCharges=5, rechargePercent=0.2, range=3),
    "Magic Missiles" : Action("Magic Missiles", "1x Damage", "Multi 4", maxCharges=1, rechargePercent=0.5, range=4),
    "Call Lightning" : Action("Call Lightning", "1x Damage", "Point", maxCharges=2, rechargePercent=0.25, range=5, width=3),

    # Utility
    "Hasten" : Action("Hasten", "Hasten", "Self", maxCharges=2, recharge="Encounter"),
    "Shove" : Action("Shove", "Repel 3"),
    "Pull" : Action("Pull", "Pull", maxCharges=1, range=4, freeAction=True),
    "Double Hook" : Action("Double Hook", "Pull", "Multi 2", maxCharges=1, range=5, freeAction=True),
    "Teleport" : Action("Teleport", "Teleport", "Point No Enemy", range=10),
    "Charge" : Action("Charge", "Charge", "Point No Enemy", range=5),

    # Defensive
    "Block" : Action("Block", "Block", "Self"),
    "Parry" : Action("Parry", "Parry", "Self", maxCharges=3, recharge="Encounter", freeAction=True),
    "Repel" : Action("Repel", "Repel 1", "Centered", maxCharges=1, rechargePercent=0.5, width=5, freeAction=True),
    "Arcane Shield" : Action("Arcane Shield", "Invuln", "Self", maxCharges=2, recharge="Encounter", rechargePercent=0.5)
}

enemAcs = {
    "Melee" : Action("Melee", "1x Damage", aiPrio=1),
    "Ranged" : Action("Ranged", "1x Damage", aiPrio=1, range = 2),
    "Magic" : Action("Magic", "1x Damage", aiPrio=1, range = 3, maxCharges=1),
    "Fireball" : Action("Fireball", "1.5x Damage", aiPrio=2, range = 3, maxCharges=1, rechargePercent=0.5)
}

# Traits
traits = {
    "Spikes" : Trait("Spikes", "After Damage", "Spikes"),
    "Repel" : Trait("Repel", "After Damage", "Repel 1"),
    "Regenerate" : Trait("Regenerate", "Turn", "Regenerate"),
    "Chain Reduction" : Trait("Chain Reduction", "Before Damage", "Minor Block")
}

# Equips
# This must be defined in this order
tier3Weps = {
    # Physical Melee
    "Vorpal Sword" : Equip("Vorpal Sword", 20, 0, [acs["Basic Attack"], acs["Whirl"]])

    # Physical Ranged

    # Magical Ranged

}
tier2Weps = {
    # Physical Melee
    "Wind Blade" : Equip("Wind Blade", 10, 0, [acs["Basic Attack"], acs["Slash"], acs["Whirl"]]),
    "Flamehammer" : Equip("Flamehammer", 10, 0, [acs["Basic Attack"], acs["Slam"], acs["Fireball"]]),
    "Runed Halberd" : Equip("Runed Halberd", 10, 0, [acs["Basic Attack"], acs["Impale"], acs["Slash"], acs["Firebolt"]]),
    "Defender Flail" : Equip("Defender Flail", 9, 20, [acs["Basic Attack"], acs["Charge"], acs["Parry"]]),

    # Physical Ranged
    "Twinshot Bow" : Equip("Twinshot Bow", 8, 0, [acs["Twin Shot"], acs["Pierce"], acs["Shove"]]),
    "Handheld Ballista" : Equip("Handheld Ballista", 8, 0, [acs["Basic Shot"], acs["Shatterwave"]]),
    "Storm Spear" : Equip("Storm Spear", 7, 15, [acs["Throw"], acs["Impale"], acs["Call Lightning"]]),

    # Magical Ranged
    "Inferno Cane" : Equip("Inferno Cane", 8, 0, [acs["Enhanced Firebolt"], acs["Fireball"], acs["Flamethrower"]]),
    "Archmage Rod" : Equip("Archmage Rod", 4, 0, [acs["Arcane Rays"], acs["Magic Missiles"], acs["Arcane Shield"]])
}
weps = {
    # Physical Melee
    "Sword" : Equip("Sword", 5, 0, [acs["Basic Attack"], acs["Slash"]], upgradedForm = tier2Weps["Wind Blade"]),
    "Hammer" : Equip("Hammer", 5, 0, [acs["Basic Attack"], acs["Slam"]], upgradedForm = tier2Weps["Flamehammer"]),
    "Spear" : Equip("Spear", 5, 0, [acs["Basic Attack"], acs["Impale"]], upgradedForm = tier2Weps["Runed Halberd"]),
    "Mace" : Equip("Mace", 4, 10, [acs["Basic Attack"], acs["Charge"]], upgradedForm = tier2Weps["Defender Flail"]),

    # Physical Ranged
    "Bow" : Equip("Bow", 4, 0, [acs["Basic Shot"], acs["Pierce"]], upgradedForm = tier2Weps["Twinshot Bow"]),
    "Crossbow" : Equip("Crossbow", 4, 0, [acs["Basic Shot"], acs["Shatter"]], upgradedForm = tier2Weps["Handheld Ballista"]),
    "Javelin" : Equip("Javelin", 4, 5, [acs["Throw"], acs["Impale"]], upgradedForm = tier2Weps["Storm Spear"]),

    # Magical Ranged
    "Fire Staff" : Equip("Fire Staff", 4, 0, [acs["Firebolt"], acs["Fireball"]], upgradedForm = tier2Weps["Inferno Cane"]),
    "Arcane Staff" : Equip("Arcane Staff", 2, 0, [acs["Arcane Rays"], acs["Magic Missiles"]], upgradedForm = tier2Weps["Archmage Rod"])
}

enemWeps = {
    "Weak Melee" : Equip("Weak Melee", 2, 0, [enemAcs["Melee"]]),
    "Weak Ranged" : Equip("Weak Ranged", 1, 0, [enemAcs["Ranged"]]),
    "Weak Magic" : Equip("Weak Magic", 2, 0, [enemAcs["Magic"], enemAcs["Fireball"]]),

    "Medium Melee" : Equip("Medium Melee", 3, 0, [enemAcs["Melee"]]),
    "Medium Ranged" : Equip("Medium Ranged", 2, 0, [enemAcs["Ranged"]]),
    "Medium Magic" : Equip("Medium Magic", 2, 0, [enemAcs["Magic"], enemAcs["Fireball"]])
}

# Other Helds
tier2Offs = {
    # Offensive
    "Ritual Blade" : Equip("Ritual Blade", 8, 0, [acs["Ritual Stab"], acs["Pull"]]),
    "Chain Hooks" : Equip("Chain Hooks", 3, 0, [acs["Double Hook"]]),
    "Shrouded Dagger" : Equip("Shrouded Dagger", 5, 0, [acs["Toss"], acs["Parry"]]),

    # Defensive
    "Crystal Shield" : Equip("Crystal Shield", 2, 20, [acs["Block"], traits["Spikes"]]),
    "Castle Shield" : Equip("Castle Shield", 0, 30, [acs["Block"], acs["Repel"]])

    # Utility

}
offs = {
    # Offensive
    "Ritual Dagger" : Equip("Ritual Dagger", 4, 0, [acs["Ritual Stab"]], upgradedForm = tier2Offs["Ritual Blade"]),
    "Rope Hook" : Equip("Rope Hook", 1, 0, [acs["Pull"]], upgradedForm = tier2Offs["Chain Hooks"]),
    "Kunai" : Equip("Kunai", 2, 0, [acs["Toss"]], upgradedForm = tier2Offs["Shrouded Dagger"]),

    # Defensive
    "Kite Shield" : Equip("Kite Shield", 0, 10, [acs["Block"]], speedBoost=1, upgradedForm = tier2Offs["Crystal Shield"]),
    "Tower Shield" : Equip("Tower Shield", 0, 15, [acs["Block"]], upgradedForm = tier2Offs["Castle Shield"])

    # Utility
    
}

# Armor
tier2Armors = {
    # Defensive
    "Battlerager Mail" : Equip("Battlerager Mail", 5, 25, [traits["Spikes"], acs["Charge"]]),
    "Druidic Plate" : Equip("Druidic Plate", 0, 40, [traits["Regenerate"], acs["Block"]]),
    "Titanic Plate" : Equip("Titanic Plate", 0, 60, [traits["Chain Reduction"]], speedBoost=-1),

    # Utility
    "Leathers of the Wind" : Equip("Leathers of the Wind", 0, 10, [acs["Hasten"]], speedBoost=5, actionBoost=2)
}
armors = {
    # Defensive
    "Spiked Mail" : Equip("Spiked Mail", 2, 15, [traits["Spikes"]], upgradedForm = tier2Armors["Battlerager Mail"]),
    "Overgrown Plate" : Equip("Overgrown Plate", 0, 25, [traits["Regenerate"]], upgradedForm = tier2Armors["Druidic Plate"]),
    "Heavy Plate" : Equip("Heavy Plate", 0, 40, [traits["Chain Reduction"]], speedBoost=-1, upgradedForm = tier2Armors["Titanic Plate"]),

    # Utility
    "Swift Leather" : Equip("Swift Leather", 0, 0, [], speedBoost=2, actionBoost=1, upgradedForm = tier2Armors["Leathers of the Wind"])
}

enemArmrs = {
    "Weak No Special" : Equip("Weak No Special", 0, 10),
    "Weak Reflect" : Equip("Weak Reflect", 0, 10, [traits["Spikes"]])
}

# Accesories
tier2Accs = {
    # Defensive
    "Barrier Necklace" : Equip("Barrier Necklace", 0, 10, [acs["Arcane Shield"], traits["Chain Reduction"]]),

    # Utility
    "Lightspeed Amulet" : Equip("Lightspeed Amulet", 0, 0, [acs["Hasten"]], speedBoost=2, actionBoost=2),
    "Repelling Gloves" : Equip("Repelling Gloves", 0, 5, [acs["Shove"], traits["Repel"]], speedBoost=2)

}
accs = {
    # Defensive
    "Brooch of Shielding" : Equip("Brooch of Shielding", 0, 5, [acs["Arcane Shield"]], upgradedForm = tier2Accs["Barrier Necklace"]),

    # Utility
    "Hastening Amulet" : Equip("Hastening Amulet", 0, 0, actionBoost=1, upgradedForm = tier2Accs["Lightspeed Amulet"]),
    "Shoving Gauntlets" : Equip("Shoving Gauntlets", 0, 0, [acs["Shove"]], speedBoost=1, upgradedForm = tier2Accs["Repelling Gloves"])

    # Offensive

}

# Set slots
for item in utils.merge(weps.values(), tier2Weps.values(), enemWeps.values()):
    item.slot = "Mainhand"
for item in utils.merge(armors.values(), tier2Armors.values(), enemArmrs.values()):
    item.slot = "Armor"
for item in utils.merge(offs.values(), tier2Offs.values()):
    item.slot = "Offhand"
for item in utils.merge(accs.values(), tier2Accs.values(), enemAcs.values()):
    item.slot = "Accessory"

# Loot Pools
lootPools = {
    "Standard" : utils.merge(weps.values(), armors.values(), offs.values(), accs.values()),
    "Upgraded" : utils.merge(tier2Weps.values(), tier2Armors.values(), tier2Offs.values(), tier2Accs.values())
}



# Enemies
preEnemies = {
    "Sunlit Field" : [("Wild Boar", 7), ("Spitting Cobra", 4), ("Forest Golem", 20)],
    "Shaded Forest" : [("Goblin", 5), ("Hobgoblin", 8), ("Bugbear", 10), ("Hobgoblin Devastator", 25)],
        "Dark Cave" : [("Bat", 4), ("Goblin", 5), ("Giant Spider", 8), ("Stone Giant", 30)],
    "Forest Tower" : [("Turret", 3), ("Stone Golem", 10), ("Golem Mage", 8), ("Iron Golem", 40)]
}
