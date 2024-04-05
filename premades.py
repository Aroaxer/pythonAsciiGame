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
        # Vorpal Sword
    "Decapitate" : Action("Decapitate", "Decapitate"),
    "Bloodwave" : Action("Bloodwave", "1x Damage", "Directional", maxCharges=5, recharge="Never", width=3, length=5),
    "Bloodwhirl" : Action("Bloodwhirl", "1x Damage", "Centered", maxCharges=5, recharge="Never", width=5),
        # Gaian Maul
    "Stone Swing" : Action("Stone Swing", "Damage Repel 1", "Directional", width=3),
    "Terran Crush" : Action("Terran Crush", "Damage Repel 2", "Directional", maxCharges=2, width=3, length=3),
    "Earthwake" : Action("Earthwake", "Damage Repel 3", "Centered", maxCharges=2, recharge="Encounter", range=5, width=5),
        # Dragonlance
    "Dragon's Arm" : Action("Dragon's Arm", "1x Damage", range=2),
    "Dragon's Tail" : Action("Dragon's Tail", "Damage Repel 1", "Centered", width=3),
    "Dragon's Breath" : Action("Dragon's Breath", "Damage Repel 1", "Directional", maxCharges=1, width=3, length=5),
    "Dragon's Wings" : Action("Dragon's Wings", "Charge", "Point No Enemy", maxCharges=3, range=7, width=3),
        # Regal Flail
    "Royal Strike" : Action("Royal Strike", "Royal Strike"),
    "Total Authority" : Action("Total Authority", "Repel 50", "Centered", maxCharges=2, recharge="Encounter", width=75),
    "Kingkiller" : Action("Kingkiller", "Kingkiller", maxCharges=1, recharge="Never", range=75, freeAction=True),
    
    # Physical Ranged
    "Basic Shot" : Action("Basic Shot", "1x Damage", range=3),
    "Pierce" : Action("Pierce", "1x Damage", "Directional", maxCharges=1, length=5),
    "Shatter" : Action("Shatter", "1.5x Damage", maxCharges=1, range=3),
    "Shatterwave" : Action("Shatterwave", "1.5x Damage", "Directional", maxCharges=2, rechargePercent=0.5, width=1, length=5),
    "Throw" : Action("Throw", "1x Damage", range=2),
    "Toss" : Action("Toss", "1x Damage", maxCharges=1, range=2, freeAction=True),
    "Twin Shot" : Action("Twin Shot", "0.5x Damage", "Multi 2", range=3),
        # Trinity Bow
    "Flame Arrows" : Action("Flame Arrows", "0.5x Damage", "Multi 3", range=4),
    "Frost Arrow" : Action("Frost Arrow", "1x Damage", "Directional", width=3, length=5),
    "Shock Arrow" : Action("Shoch Arrow", "1.5x Damage", range=6),
        # Crystal Arbalest
    "Shard Blast" : Action("Shard Blast", "1x Damage", "Directional", width=3, length=3),
    "Shardlance" : Action("Shardlance", "1x Damage", "Directional", length=7),
    "Condense" : Action("Condense", "Condense", "Self"),
    "Crystal Rain" : Action("Crystal Rain", "Crystal Rain", "Point", maxCharges=1, recharge="Never", range=5),
        # Thunderbolt
    "Thunderstrike" : Action("Thunderstrike", "Damage Repel 1", range=3),
    "Shockwave" : Action("Shockwave", "Damage Repel 1", "Centered", width=3, length=3),
    "Living Deity" : Action("Living Deity", "Living Deity", "Self", maxCharges=1, recharge="Never"),

    # Magical
    "Firebolt" : Action("Firebolt", "1x Damage", maxCharges=1, range=3),
    "Fireball" : Action("Fireball", "1x Damage", "Point", maxCharges=1, rechargePercent=0.5, range=3, width=3),
    "Enhanced Firebolt" : Action("Enhanced Firebolt", "1x Damage", range=5),
    "Flamethrower" : Action("Flamethrower", "1x Damage", "Directional", maxCharges=2, rechargePercent=0.5, length=4),
    "Arcane Rays" : Action("Arcane Rays", "0.5x Damage", "Multi 2", maxCharges=5, rechargePercent=0.2, range=3),
    "Magic Missiles" : Action("Magic Missiles", "0.5x Damage", "Multi 4", maxCharges=1, rechargePercent=0.5, range=4),
    "Call Lightning" : Action("Call Lightning", "1x Damage", "Point", maxCharges=2, rechargePercent=0.25, range=5, width=3),
        # Volcanic Staff
    "Flamestone" : Action("Flamestone", "1x Damage", range=4),
    "Meteor" : Action("Meteor", "1x Damage", "Point", maxCharges=1, range=5, width=3),
    "Firestorm" : Action("Firestorm", "Damage Repel 2", "Centered", maxCharges=3, recharge="Encounter", width=5),
    "Eruption" : Action("Eruption", "1.5x Damage", "Centered", maxCharges=1, recharge="Encounter", rechargePercent=0.25, width=9),
        # Lich's Cane
    "Draining Rays" : Action("Draining Rays", "Draining Rays", "Multi 3", range=5),
    "Arcane Lance" : Action("Arcane Lance", "Damage Repel 4", maxCharges=1, range=4),
    "Power Word Kill" : Action("Power Word Kill", "Power Word Kill", maxCharges=2, range=10),

    # Utility
    "Hasten" : Action("Hasten", "Hasten", "Self", maxCharges=2, recharge="Encounter"),
    "Shove" : Action("Shove", "Repel 3"),
    "Pull" : Action("Pull", "Pull", maxCharges=1, range=4, freeAction=True),
    "Damage Pull" : Action("Pull", "Damage Pull", maxCharges=1, range=4, freeAction=True),
    "Double Hook" : Action("Double Hook", "Damage Pull", "Multi 2", maxCharges=1, range=5, freeAction=True),
    "Teleport" : Action("Teleport", "Teleport", "Point No Enemy", range=10),
    "Charge" : Action("Charge", "Charge", "Point No Enemy", maxCharges=1, range=5, width=3),

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
    "Fireball" : Action("Fireball", "1.5x Damage", aiPrio=2, range = 3, maxCharges=1, rechargePercent=0.5),
    "Call" : Action("Call", "Pull", range=10, maxCharges=1, rechargePercent=0.5, aiPrio=1),
    "Beam" : Action("Beam", "1x Damage", range=3, aiPrio=2)
}

# Traits
traits = {
    "Spikes" : Trait("Spikes", "After Damage", "Spikes"),
    "Repel" : Trait("Repel", "After Damage", "Repel 1"),
    "Regenerate" : Trait("Regenerate", "Turn", "Regenerate"),
    "Chain Reduction" : Trait("Chain Reduction", "Before Damage", "Minor Block"),
    "Charge Deity" : Trait("Charge Deity", "Attack", "Charge Deity", "Copy Target")
}

# Equips
# This must be defined in this order
# Tier 3 weapons generally have something special
tier3Weps = {
    # Physical Melee
    "Vorpal Sword" : Equip("Vorpal Sword", 20, 0, [acs["Decapitate"], acs["Bloodwave"], acs["Bloodwhirl"]], speedBoost=1),
    "Gaian Maul" : Equip("Gaian Maul", 20, 10, [acs["Stone Swing"], acs["Terran Crush"], acs["Earthwake"]]),
    "Dragonlance" : Equip("Dragonlance", 20, 0, [acs["Dragon's Arm"], acs["Dragon's Tail"], acs["Dragon's Breath"], acs["Dragon's Wings"]], actionBoost=1),
    "Regal Flail" : Equip("Regal Flail", 18, 40, [acs["Royal Strike"], acs["Total Authority"], acs["Kingkiller"]]),

    # Physical Ranged
    "Trinity Bow" : Equip("Trinity Bow", 16, 0, [acs["Flame Arrows"], acs["Frost Arrow"], acs["Shock Arrow"]]),
    "Crystal Arbalest" : Equip("Crystal Arbalest", 16, 0, [acs["Shard Blast"], acs["Shardlance"], acs["Condense"], acs["Crystal Rain"]]),
    "Thunderbolt" : Equip("Thunderbolt", 15, 25, [acs["Thunderstrike"], acs["Shockwave"], acs["Living Deity"], traits["Charge Deity"]], speedBoost=1),

    # Magical Ranged
    "Volcanic Staff" : Equip("Volcanic Staff", 16, 0, [acs["Flamestone"], acs["Meteor"], acs["Firestorm"], acs["Eruption"]]),
    "Lich's Cane" : Equip("Lich's Cane", 16, 0, [acs["Draining Rays"], acs["Arcane Lance"], acs["Power Word Kill"]])
}
tier2Weps = {
    # Physical Melee
    "Wind Blade" : Equip("Wind Blade", 10, 0, [acs["Basic Attack"], acs["Slash"], acs["Whirl"]], upgr=tier3Weps["Vorpal Sword"]),
    "Flamehammer" : Equip("Flamehammer", 10, 0, [acs["Basic Attack"], acs["Slam"], acs["Fireball"]], upgr=tier3Weps["Gaian Maul"]),
    "Runed Halberd" : Equip("Runed Halberd", 10, 0, [acs["Basic Attack"], acs["Impale"], acs["Slash"], acs["Firebolt"]], upgr=tier3Weps["Dragonlance"]),
    "Defender Flail" : Equip("Defender Flail", 9, 20, [acs["Basic Attack"], acs["Charge"], acs["Parry"]], upgr=tier3Weps["Regal Flail"]),

    # Physical Ranged
    "Twinshot Bow" : Equip("Twinshot Bow", 8, 0, [acs["Twin Shot"], acs["Pierce"], acs["Shove"]], upgr=tier3Weps["Trinity Bow"]),
    "Handheld Ballista" : Equip("Handheld Ballista", 8, 0, [acs["Basic Shot"], acs["Shatterwave"]], upgr=tier3Weps["Crystal Arbalest"]),
    "Storm Spear" : Equip("Storm Spear", 7, 15, [acs["Throw"], acs["Impale"], acs["Call Lightning"]], upgr=tier3Weps["Thunderbolt"]),

    # Magical Ranged
    "Inferno Cane" : Equip("Inferno Cane", 8, 0, [acs["Enhanced Firebolt"], acs["Fireball"], acs["Flamethrower"]], upgr=tier3Weps["Volcanic Staff"]),
    "Archmage Rod" : Equip("Archmage Rod", 8, 0, [acs["Arcane Rays"], acs["Magic Missiles"], acs["Arcane Shield"]], upgr=tier3Weps["Lich's Cane"])
}
weps = {
    # Physical Melee
    "Sword" : Equip("Sword", 5, 0, [acs["Basic Attack"], acs["Slash"]], upgr=tier2Weps["Wind Blade"]),
    "Hammer" : Equip("Hammer", 5, 0, [acs["Basic Attack"], acs["Slam"]], upgr=tier2Weps["Flamehammer"]),
    "Spear" : Equip("Spear", 5, 0, [acs["Basic Attack"], acs["Impale"]], upgr=tier2Weps["Runed Halberd"]),
    "Mace" : Equip("Mace", 4, 10, [acs["Basic Attack"], acs["Charge"]], upgr=tier2Weps["Defender Flail"]),

    # Physical Ranged
    "Bow" : Equip("Bow", 4, 0, [acs["Basic Shot"], acs["Pierce"]], upgr=tier2Weps["Twinshot Bow"]),
    "Crossbow" : Equip("Crossbow", 4, 0, [acs["Basic Shot"], acs["Shatter"]], upgr=tier2Weps["Handheld Ballista"]),
    "Javelin" : Equip("Javelin", 4, 5, [acs["Throw"], acs["Impale"]], upgr=tier2Weps["Storm Spear"]),

    # Magical Ranged
    "Fire Staff" : Equip("Fire Staff", 4, 0, [acs["Firebolt"], acs["Fireball"]], upgr=tier2Weps["Inferno Cane"]),
    "Arcane Staff" : Equip("Arcane Staff", 4, 0, [acs["Arcane Rays"], acs["Magic Missiles"]], upgr=tier2Weps["Archmage Rod"])
}

enemWeps = {
    "Weak Melee" : Equip("Weak Melee", 2, 0, [enemAcs["Melee"]]),
    "Weak Ranged" : Equip("Weak Ranged", 1, 0, [enemAcs["Ranged"]]),
    "Weak Magic" : Equip("Weak Magic", 2, 0, [enemAcs["Magic"], enemAcs["Fireball"]]),

    "Medium Melee" : Equip("Medium Melee", 3, 0, [enemAcs["Melee"]]),
    "Medium Ranged" : Equip("Medium Ranged", 2, 0, [enemAcs["Ranged"]]),
    "Medium Magic" : Equip("Medium Magic", 2, 0, [enemAcs["Magic"], enemAcs["Fireball"]]),

    # Special
    "Crystal Heart" : Equip("Crystal Heart", 2, 20, [enemAcs["Call"], enemAcs["Beam"]])
}

# Other Helds
tier2Offs = {
    # Offensive
    "Ritual Blade" : Equip("Ritual Blade", 8, 0, [acs["Ritual Stab"], acs["Pull"]]),
    "Chain Hooks" : Equip("Chain Hooks", 3, 0, [acs["Double Hook"]]),
    "Shrouded Dagger" : Equip("Shrouded Dagger", 5, 0, [acs["Toss"], acs["Parry"]]),

    # Defensive
    "Crystal Shield" : Equip("Crystal Shield", 2, 30, [acs["Block"], traits["Spikes"]]),
    "Castle Shield" : Equip("Castle Shield", 0, 50, [acs["Block"], acs["Repel"]])

    # Utility

}
offs = {
    # Offensive
    "Ritual Dagger" : Equip("Ritual Dagger", 4, 0, [acs["Ritual Stab"]], upgr=tier2Offs["Ritual Blade"]),
    "Rope Hook" : Equip("Rope Hook", 1, 0, [acs["Damage Pull"]], upgr=tier2Offs["Chain Hooks"]),
    "Kunai" : Equip("Kunai", 2, 0, [acs["Toss"]], upgr=tier2Offs["Shrouded Dagger"]),

    # Defensive
    "Kite Shield" : Equip("Kite Shield", 0, 20, [acs["Block"]], speedBoost=1, upgr=tier2Offs["Crystal Shield"]),
    "Tower Shield" : Equip("Tower Shield", 0, 30, [acs["Block"]], upgr=tier2Offs["Castle Shield"])

    # Utility
    
}

# Armor
tier2Armors = {
    # Defensive
    "Battlerager Mail" : Equip("Battlerager Mail", 5, 25, [traits["Spikes"], acs["Charge"]]),
    "Druidic Plate" : Equip("Druidic Plate", 0, 40, [traits["Regenerate"], acs["Block"]]),
    "Titanic Plate" : Equip("Titanic Plate", 0, 60, [traits["Chain Reduction"]], speedBoost=-1),

    # Utility
    "Leathers of the Wind" : Equip("Leathers of the Wind", 0, 10, [acs["Hasten"]], speedBoost=3, actionBoost=2)
}
armors = {
    # Defensive
    "Spiked Mail" : Equip("Spiked Mail", 2, 15, [traits["Spikes"]], upgr=tier2Armors["Battlerager Mail"]),
    "Overgrown Plate" : Equip("Overgrown Plate", 0, 25, [traits["Regenerate"]], upgr=tier2Armors["Druidic Plate"]),
    "Heavy Plate" : Equip("Heavy Plate", 0, 40, [traits["Chain Reduction"]], speedBoost=-1, upgr=tier2Armors["Titanic Plate"]),

    # Utility
    "Swift Leather" : Equip("Swift Leather", 0, 0, [], speedBoost=1, actionBoost=1, upgr=tier2Armors["Leathers of the Wind"])
}

enemArmrs = {
    "Weak No Special" : Equip("Weak No Special", 0, 10),
    "Weak Reflect" : Equip("Weak Reflect", 0.5, 10, [traits["Spikes"]]),

    "Medium No Special" : Equip("Medium No Special", 0, 20)
}

# Accesories
tier2Accs = {
    # Defensive
    "Barrier Necklace" : Equip("Barrier Necklace", 0, 10, [acs["Arcane Shield"], traits["Chain Reduction"]]),

    # Utility
    "Lightspeed Amulet" : Equip("Lightspeed Amulet", 0, 0, [acs["Hasten"]], speedBoost=2, actionBoost=1),
    "Repelling Gloves" : Equip("Repelling Gloves", 0, 5, [acs["Shove"], traits["Repel"]], speedBoost=2)

}
accs = {
    # Defensive
    "Brooch of Shielding" : Equip("Brooch of Shielding", 0, 5, [acs["Arcane Shield"]], upgr=tier2Accs["Barrier Necklace"]),

    # Utility
    "Hastening Amulet" : Equip("Hastening Amulet", 0, 0, actionBoost=1, upgr=tier2Accs["Lightspeed Amulet"]),
    "Shoving Gauntlets" : Equip("Shoving Gauntlets", 0, 0, [acs["Shove"]], speedBoost=1, upgr=tier2Accs["Repelling Gloves"])

    # Offensive

}

# Set slots
for item in utils.merge(weps.values(), tier2Weps.values(), tier3Weps.values(), enemWeps.values()):
    item.slot = "Mainhand"
for item in utils.merge(armors.values(), tier2Armors.values(), enemArmrs.values()):
    item.slot = "Armor"
for item in utils.merge(offs.values(), tier2Offs.values()):
    item.slot = "Offhand"
for item in utils.merge(accs.values(), tier2Accs.values(), enemAcs.values()):
    item.slot = "Accessory"

# Loot Pools
lootPools = {
    "Tier 1" : utils.merge(weps.values(), armors.values(), offs.values(), accs.values()),
    "Tier 2" : utils.merge(tier2Weps.values(), tier2Armors.values(), tier2Offs.values(), tier2Accs.values())
}



# Enemies
# Name, Health
preEnemies = {
    "Sunlit Field" : [("Wild Boar", 7), ("Spitting Cobra", 4), ("Forest Golem", 35)],
    "Shaded Forest" : [("Goblin", 10), ("Hobgoblin", 12), ("Bugbear", 14), ("Hobgoblin Devastator", 60)],
        "Dark Cave" : [("Bat", 6), ("Goblin", 10), ("Giant Spider", 12), ("Stone Giant", 70)],
    "Forest Tower" : [("Turret", 15), ("Stone Golem", 20), ("Golem Mage", 18), ("Iron Golem", 100)],
        "Crystal Cavern" : [("Gem Crawler", 18), ("Crystal Golem", 20), ("Jeweled Spire", 25), ("Crystal Heart", 100)],
    "Fey Grove" : [("Sprite", 25), ("Quickling", 25), ("Dryad", 35), ("Treant", 50), ("Archfey", 125)],
        "Scorched Desert" : [("Giant Scorpion", 40), ("Sand Elemental", 30), ("Giant Snake", 50), ("Vulture", 25), ("Sandworm", 150)],
        "Icy Tundra" : [("Ice Elemental", 30), ("Yeti", 50), ("Snow Golem", 25), ("Frost Giant", 150)]
}
