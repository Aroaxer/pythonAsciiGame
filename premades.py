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
        # Excalibur
    "Holy Blade" : Action("Holy Blade", "Decapitate"),
    "Divine Slash" : Action("Divine Slash", "1x Damage", "Directional", maxCharges=10, recharge="Never", width=5, length=7),
    "Radiant Pulse" : Action("Radiant Pulse", "1x Damage", "Centered", maxCharges=10, recharge="Never", width=7),
    "Divine Intervention" : Action("Divine Intervention", "Divine Intervention", "Self", maxCharges=1, recharge="Never", width=11, length=11),
        # Gaian Maul
    "Stone Swing" : Action("Stone Swing", "Damage Repel 1", "Directional", width=3),
    "Terran Crush" : Action("Terran Crush", "Damage Repel 2", "Directional", maxCharges=2, width=3, length=3),
    "Earthwake" : Action("Earthwake", "Damage Repel 3", "Point", maxCharges=2, recharge="Encounter", range=5, width=5),
        # Mjolnir
    "Storm Swing" : Action("Storm Swing", "Damage Repel 1", "Directional", width=5, length=2),
    "Lightning Slam" : Action("Lightning Slam", "Damage Repel 2", "Directional", maxCharges=3, width=5, length=5),
    "Thunderwave" : Action("Thunderwave", "Damage Repel 3", "Point", maxCharges=3, recharge="Encounter", range=7, width=7),
    "Superstorm" : Action("Superstorm", "Damage Repel 20", "Centered", maxCharges=1, recharge="Never", width=25),
        # Dragonlance
    "Dragon's Arm" : Action("Dragon's Arm", "1x Damage", range=2),
    "Dragon's Tail" : Action("Dragon's Tail", "Damage Repel 1", "Centered", width=3),
    "Dragon's Breath" : Action("Dragon's Breath", "Damage Repel 1", "Directional", maxCharges=1, width=3, length=5),
    "Dragon's Wings" : Action("Dragon's Wings", "Charge", "Point No Enemy", maxCharges=3, range=7, width=3),
        # Aetheryte
    "Aetherial Lance" : Action("Aetherial Lance", "1.5x Damage", range=3),
    "Cloud Whirl" : Action("Cloud Whirl", "Damage Repel 2", "Centered", width=5),
    "Spatial Thrust" : Action("Spatial Thrust", "Damage Repel 1", "Directional", maxCharges=2, width=3, length=7),
    "Sky Call" : Action("Sky Call", "Damage Pull", "Centered", maxCharges=2, width=7),
    "Void Phase" : Action("Void Phase", "Charge", "Point No Enemy", maxCharges=4, range=9, width=5),
        # Regal Flail
    "Royal Strike" : Action("Royal Strike", "Royal Strike"),
    "Total Authority" : Action("Total Authority", "Repel 50", "Centered", maxCharges=2, recharge="Encounter", width=75),
    "Kingkiller" : Action("Kingkiller", "Kingkiller", maxCharges=1, recharge="Never", range=75, freeAction=True),
        # Dawnbreaker
    "Dawn Strike" : Action("Dawn Strike", "Damage Repel 1", "Directional", width=3),
    "Radiant Rush" : Action("Radiant Rush", "Charge", "Point No Enemy", range=3, width=3),
    "High Noon" : Action("High Noon", "Repel 75", "Centered", maxCharges=2, recharge="Encounter", width=125),
    "Twilight" : Action("Twilight", "Twilight", maxCharges=1, recharge="Never", range=125, freeAction=True),
    
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
    "Shock Arrow" : Action("Shock Arrow", "1.5x Damage", range=6),
        # Tsunami
    "Tidesplinter" : Action("Tidesplinter", "0.5x Damage", "Multi 4", range=5),
    "Tidal Wave" : Action("Tidal Wave", "1x Damage", "Directional", width=5,length=9),
    "Whirlpool" : Action("Whirlpool", "Damage Repel 3", "Centered", width=5),
    "Surf" : Action("Surf", "Charge", "Point No Enemy", range=5, width=3),
        # Crystal Arbalest
    "Shard Blast" : Action("Shard Blast", "1x Damage", "Directional", width=3, length=3),
    "Shardlance" : Action("Shardlance", "1x Damage", "Directional", length=7),
    "Condense" : Action("Condense", "Condense", "Self"),
    "Crystal Rain" : Action("Crystal Rain", "Crystal Rain", "Point", maxCharges=1, recharge="Never", range=5),
        # Skypiercer
    "Cloudburst" : Action("Cloudburst", "1x Damage", "Directional", width=3, length=5),
    "Starspear" : Action("Starspear", "1.5x Damage", "Directional", length=15),
    "Accumulate" : Action("Accumulate", "Condense", "Self"),
    "Skyfall" : Action("Skyfall", "Crystal Rain", "Point", maxCharges=1, recharge="Never", range=10),
        # Thunderbolt
    "Thunderstrike" : Action("Thunderstrike", "Damage Repel 1", range=3),
    "Shockwave" : Action("Shockwave", "Damage Repel 1", "Centered", width=3),
    "Living Deity" : Action("Living Deity", "Living Deity", "Self", maxCharges=1, recharge="Never"),
        # Surpremacy
    "Power" : Action("Power", "1.5x Damage", range=4),
    "Command" : Action("Command", "Damage Repel 2", "Centered", width=5),
    "Destroy" : Action("Destroy", "Damage Repel 1", "Directional", width=3, length=5),
    "Embodiment" : Action("Embodiment", "Living Deity", "Self", maxCharges=1, recharge="Never"),

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
        # Infernum
    "Hellfire" : Action("Hellfire", "1.5x Damage", range=5),
    "Call Flames" : Action("Call Flames", "1x Damage", "Point", maxCharges=3, range=7, width=5),
    "Flamewave" : Action("Flamewave", "Damage Repel 2", "Centered", maxCharges=3, width=5),
    "Inferno" : Action("Inferno", "1.5x Damage", "Centered", maxCharges=1, recharge="Encounter", rechargePercent=0.5, width=13),
        # Lich's Cane
    "Draining Rays" : Action("Draining Rays", "Draining Rays", "Multi 3", range=5),
    "Arcane Lance" : Action("Arcane Lance", "Damage Repel 4", maxCharges=1, range=4),
    "Power Word Kill" : Action("Power Word Kill", "Power Word Kill", maxCharges=1, range=10),
        # Arcanaloth
    "Life Drain" : Action("Life Drain", "Draining Rays", "Multi 4", range=7),
    "Conjured Blade" : Action("Conjured Blade", "Damage Repel 2", "Directional", maxCharges=2, width=5, length=2),
    "Conjured Spear" : Action("Conjured Spear", "Damage Repel 5", maxCharges=2, range=5),
    "Obliterate" : Action("Obliterate", "Power Word Kill", "Point", maxCharges=1, range=15, width=3),

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
    "Arcane Shield" : Action("Arcane Shield", "Invuln", "Self", maxCharges=2, recharge="Encounter", rechargePercent=0.5),
        # T3 Items
    "Fortify" : Action("Fortify", "Fortify", "Self"),
    "Palace Toggle" : Action("Palace Toggle", "Palace Toggle", "Self", maxCharges=1, rechargePercent=0.25),
    "Walking Fortress" : Action("Walking Fortress", "Repel 1", "Centered", maxCharges=3, recharge="Encounter", width=5)
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
    "Charge Deity" : Trait("Charge Deity", "Attack", "Charge Deity"),
    "Momentum" : Trait("Momentum", "Attack", "Momentum"),
    "Holy Radiance" : Trait("Holy Radiance", "Turn", "Holy Radiance", "Centered", width=7),
    "Excalibur" : Trait("Excalibur", "Attack", "Excalibur", width=3),
    "Mjolnir" : Trait("Mjolnir", "After Damage", "Mjolnir", "Self"),
    "Coating" : Trait("Coating", "Attack", "Spikes"),
    "Knockback" : Trait("Knockback", "Attack", "Repel 1"),
    "Embodiment" : Trait("Embodiment", "Attack", "Embodiment")
}

# Equips
# This must be defined in this order

# Other Helds
tier3Offs = {
    # Offensive
    "Oceanic Coating" : Equip("Oceanic Coating", 10, 0, [traits["Coating"], traits["Knockback"], traits["Knockback"]]),

    # Defensive
    "Fiery Shield" : Equip("Fiery Shield", 5, 50, [acs["Fortify"], traits["Spikes"]]),
    "Palace Shield" : Equip("Palace Shield", 0, 75, [acs["Fortify"], acs["Repel"], acs["Palace Toggle"], traits["Chain Reduction"]], specialTags={"Palace" : False})
}
tier2Offs = {
    # Offensive
    "Ritual Blade" : Equip("Ritual Blade", 8, 0, [acs["Ritual Stab"], acs["Pull"]]),
    "Chain Hooks" : Equip("Chain Hooks", 3, 0, [acs["Double Hook"]]),
    "Shrouded Dagger" : Equip("Shrouded Dagger", 5, 0, [acs["Toss"], acs["Parry"]]),
    "Forceful Coating" : Equip("Forceful Coating", 5, 0, [traits["Coating"], traits["Knockback"]], upgr=tier3Offs["Oceanic Coating"]),

    # Defensive
    "Crystal Shield" : Equip("Crystal Shield", 2, 30, [acs["Block"], traits["Spikes"]]),
    "Castle Shield" : Equip("Castle Shield", 0, 50, [acs["Block"], acs["Repel"]], upgr=tier3Offs["Palace Shield"])
}
offs = {
    # Offensive
    "Ritual Dagger" : Equip("Ritual Dagger", 4, 0, [acs["Ritual Stab"]], upgr=tier2Offs["Ritual Blade"]),
    "Rope Hook" : Equip("Rope Hook", 1, 0, [acs["Damage Pull"]], upgr=tier2Offs["Chain Hooks"]),
    "Kunai" : Equip("Kunai", 2, 0, [acs["Toss"]], upgr=tier2Offs["Shrouded Dagger"]),
    "Weapon Coating" : Equip("Weapon Coating", 2, 0, [traits["Coating"]], upgr=tier2Offs["Forceful Coating"]),

    # Defensive
    "Kite Shield" : Equip("Kite Shield", 0, 20, [acs["Block"]], speedBoost=1, upgr=tier2Offs["Crystal Shield"]),
    "Tower Shield" : Equip("Tower Shield", 0, 30, [acs["Block"]], upgr=tier2Offs["Castle Shield"])
}

# Armor
tier3Armors = {
    # Defensive
    "Stormwrath Mail" : Equip("Stormwrath Mail", 10, 40, [traits["Spikes"], traits["Repel"], acs["Charge"]]),

    # Utility
    "Aetherial Robes" : Equip("Aetherial Robes", 0, 20, [acs["Hasten"], traits["Momentum"]], speedBoost=3, actionBoost=2),
    "Enchanter's Robes" : Equip("Enchanter's Robes", 10, 20, [acs["Hasten"], traits["Coating"]], speedBoost=2, actionBoost=1)
}
tier2Armors = {
    # Defensive
    "Battlerager Mail" : Equip("Battlerager Mail", 5, 25, [traits["Spikes"], acs["Charge"]], upgr=tier3Armors["Stormwrath Mail"]),
    "Druidic Plate" : Equip("Druidic Plate", 0, 40, [traits["Regenerate"], acs["Block"]]),
    "Titanic Plate" : Equip("Titanic Plate", 0, 60, [traits["Chain Reduction"]], speedBoost=-1),

    # Utility
    "Leathers of the Wind" : Equip("Leathers of the Wind", 0, 10, [acs["Hasten"]], speedBoost=2, actionBoost=2, upgr=tier3Armors["Aetherial Robes"]),
    "Infusing Robes" : Equip("Infusing Robes", 5, 10, [traits["Coating"]], speedBoost=1)
}
armors = {
    # Defensive
    "Spiked Mail" : Equip("Spiked Mail", 2, 15, [traits["Spikes"]], upgr=tier2Armors["Battlerager Mail"]),
    "Overgrown Plate" : Equip("Overgrown Plate", 0, 25, [traits["Regenerate"]], upgr=tier2Armors["Druidic Plate"]),
    "Heavy Plate" : Equip("Heavy Plate", 0, 40, [traits["Chain Reduction"]], speedBoost=-1, upgr=tier2Armors["Titanic Plate"]),

    # Utility
    "Swift Leather" : Equip("Swift Leather", 0, 0, [], speedBoost=1, actionBoost=1, upgr=tier2Armors["Leathers of the Wind"]),
    "Channeling Robes" : Equip("Channeling Robes", 2, 0, [traits["Coating"]], upgr=tier2Armors["Infusing Robes"])
}

enemArmrs = {
    "Weak No Special" : Equip("Weak No Special", 0, 10),
    "Weak Reflect" : Equip("Weak Reflect", 0.5, 10, [traits["Spikes"]]),

    "Medium No Special" : Equip("Medium No Special", 0, 20)
}

# Accesories
tier3Accs = {
    # Defensive
    "Fortress Necklace" : Equip("Fortress Necklace", 0, 50, [acs["Walking Fortress"], traits["Chain Reduction"]]),
    "Radiant Crown" : Equip("Radiant Crown", 8, 30, [traits["Holy Radiance"]], speedBoost=1),

    # Utility
    "Aerial Gauntlets" : Equip("Aerial Gauntlets", 0, 10, [acs["Shove"], acs["Teleport"], traits["Repel"], traits["Repel"]], speedBoost=3, actionBoost=1)
}
tier2Accs = {
    # Defensive
    "Barrier Necklace" : Equip("Barrier Necklace", 0, 30, [acs["Arcane Shield"], traits["Chain Reduction"]], upgr=tier3Accs["Fortress Necklace"]),
    "Holy Circlet" : Equip("Holy Circlet", 0, 20, [traits["Regenerate"]], upgr=tier3Accs["Radiant Crown"]),

    # Utility
    "Lightspeed Amulet" : Equip("Lightspeed Amulet", 0, 0, [acs["Hasten"]], speedBoost=2, actionBoost=1),
    "Repelling Gloves" : Equip("Repelling Gloves", 0, 5, [acs["Shove"], traits["Repel"]], speedBoost=2)
}
accs = {
    # Defensive
    "Brooch of Shielding" : Equip("Brooch of Shielding", 0, 15, [acs["Arcane Shield"]], upgr=tier2Accs["Barrier Necklace"]),
    "Healing Wreath" : Equip("Healing Wreath", 0, 10, [traits["Regenerate"]], upgr=tier2Accs["Holy Circlet"]),

    # Utility
    "Hastening Amulet" : Equip("Hastening Amulet", 0, 0, actionBoost=1, upgr=tier2Accs["Lightspeed Amulet"]),
    "Shoving Gauntlets" : Equip("Shoving Gauntlets", 0, 0, [acs["Shove"]], speedBoost=1, upgr=tier2Accs["Repelling Gloves"])
}

# Tier 3/4 weapons generally have a special gimmick
# Tier 4 weapons require an extra tier 3 item
tier4Weps = {
    # Physical Melee
    "Excalibur" : Equip("Excalibur", 25, 30, [acs["Holy Blade"], acs["Divine Slash"], acs["Radiant Pulse"], acs["Divine Intervention"], traits["Holy Radiance"], traits["Excalibur"]], speedBoost=1),
    "Mjolnir" : Equip("Mjolnir", 40, 40, [acs["Storm Swing"], acs["Lightning Slam"], acs["Shockwave"], acs["Superstorm"], traits["Repel"], traits["Mjolnir"]]),
    "Aetheryte" : Equip("Aetheryte", 40, 30, [acs["Aetherial Lance"], acs["Cloud Whirl"], acs["Spatial Thrust"], acs["Sky Call"], acs["Void Phase"]], actionBoost=1),
    "Dawnbreaker" : Equip("Dawnbreaker", 36, 60, [acs["Dawn Strike"], acs["Radiant Rush"], acs["High Noon"], acs["Twilight"], traits["Holy Radiance"], traits["Chain Reduction"]]),

    # Physical Ranged
    "Tsunami" :  Equip("Tsunami", 32, 10, [acs["Tidesplinter"], acs["Tidal Wave"], acs["Whirlpool"], acs["Surf"]], speedBoost=1),
    "Skypiercer" : Equip("Skypiercer", 32, 10, [acs["Cloudburst"], acs["Starspear"], acs["Accumulate"], acs["Skyfall"]]),
    "Surpremacy" : Equip("Surpremacy", 30, 40, [acs["Power"], acs["Command"], acs["Destroy"], acs["Embodiment"], traits["Embodiment"]], speedBoost=2),

    # Magical Ranged
    "Infernum" : Equip("Infernum", 32, 0, [acs["Hellfire"], acs["Call Flames"], acs["Flamewave"], acs["Inferno"]], actionBoost=1),
    "Arcanaloth" : Equip("Arcanaloth", 32, 0, [acs["Life Drain"], acs["Conjured Blade"], acs["Conjured Spear"], acs["Obliterate"]])
}
tier3Weps = {
    # Physical Melee
    "Vorpal Sword" : Equip("Vorpal Sword", 20, 10, [acs["Decapitate"], acs["Bloodwave"], acs["Bloodwhirl"]], speedBoost=1, upgr=(tier4Weps["Excalibur"], tier3Accs["Radiant Crown"])),
    "Gaian Maul" : Equip("Gaian Maul", 20, 20, [acs["Stone Swing"], acs["Terran Crush"], acs["Earthwake"]], upgr=(tier4Weps["Mjolnir"], tier3Armors["Stormwrath Mail"])),
    "Dragonlance" : Equip("Dragonlance", 20, 10, [acs["Dragon's Arm"], acs["Dragon's Tail"], acs["Dragon's Breath"], acs["Dragon's Wings"]], actionBoost=1, upgr=(tier4Weps["Aetheryte"], tier3Armors["Aetherial Robes"])),
    "Regal Flail" : Equip("Regal Flail", 18, 40, [acs["Royal Strike"], acs["Total Authority"], acs["Kingkiller"]], upgr=(tier4Weps["Dawnbreaker"], tier3Offs["Palace Shield"])),

    # Physical Ranged
    "Trinity Bow" : Equip("Trinity Bow", 16, 0, [acs["Flame Arrows"], acs["Frost Arrow"], acs["Shock Arrow"]], upgr=(tier4Weps["Tsunami"], tier3Offs["Oceanic Coating"])),
    "Crystal Arbalest" : Equip("Crystal Arbalest", 16, 0, [acs["Shard Blast"], acs["Shardlance"], acs["Condense"], acs["Crystal Rain"]], upgr=(tier4Weps["Skypiercer"], tier3Accs["Aerial Gauntlets"])),
    "Thunderbolt" : Equip("Thunderbolt", 15, 25, [acs["Thunderstrike"], acs["Shockwave"], acs["Living Deity"], traits["Charge Deity"]], speedBoost=1, upgr=(tier4Weps["Surpremacy"], tier3Accs["Fortress Necklace"])),

    # Magical Ranged
    "Volcanic Staff" : Equip("Volcanic Staff", 16, 0, [acs["Flamestone"], acs["Meteor"], acs["Firestorm"], acs["Eruption"]], upgr=(tier4Weps["Infernum"], tier3Offs["Fiery Shield"])),
    "Lich's Cane" : Equip("Lich's Cane", 16, 0, [acs["Draining Rays"], acs["Arcane Lance"], acs["Power Word Kill"]], upgr=(tier4Weps["Arcanaloth"], tier3Armors["Enchanter's Robes"]))
}
tier2Weps = {
    # Physical Melee
    "Wind Blade" : Equip("Wind Blade", 10, 10, [acs["Basic Attack"], acs["Slash"], acs["Whirl"]], upgr=tier3Weps["Vorpal Sword"]),
    "Flamehammer" : Equip("Flamehammer", 10, 10, [acs["Basic Attack"], acs["Slam"], acs["Fireball"]], upgr=tier3Weps["Gaian Maul"]),
    "Runed Halberd" : Equip("Runed Halberd", 10, 10, [acs["Basic Attack"], acs["Impale"], acs["Slash"], acs["Firebolt"]], upgr=tier3Weps["Dragonlance"]),
    "Defender Flail" : Equip("Defender Flail", 9, 30, [acs["Basic Attack"], acs["Charge"], acs["Parry"]], upgr=tier3Weps["Regal Flail"]),

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
    "Sword" : Equip("Sword", 5, 10, [acs["Basic Attack"], acs["Slash"]], upgr=tier2Weps["Wind Blade"]),
    "Hammer" : Equip("Hammer", 5, 10, [acs["Basic Attack"], acs["Slam"]], upgr=tier2Weps["Flamehammer"]),
    "Spear" : Equip("Spear", 5, 10, [acs["Basic Attack"], acs["Impale"]], upgr=tier2Weps["Runed Halberd"]),
    "Mace" : Equip("Mace", 4, 20, [acs["Basic Attack"], acs["Charge"]], upgr=tier2Weps["Defender Flail"]),

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

allItems = (
    utils.merge(weps.values(), armors.values(), offs.values(), accs.values()),
    utils.merge(tier2Weps.values(), tier2Armors.values(), tier2Offs.values(), tier2Accs.values()),
    utils.merge(tier3Weps.values(), tier3Armors.values(), tier3Offs.values(), tier3Accs.values()),
    tier4Weps.values()
)

# Set slots
for item in utils.merge(weps.values(), tier2Weps.values(), tier3Weps.values(), tier4Weps.values(), enemWeps.values()):
    item.slot = "Mainhand"
for item in utils.merge(armors.values(), tier2Armors.values(), tier3Armors.values(), enemArmrs.values()):
    item.slot = "Armor"
for item in utils.merge(offs.values(), tier2Offs.values(), tier3Offs.values()):
    item.slot = "Offhand"
for item in utils.merge(accs.values(), tier2Accs.values(), tier3Accs.values(), enemAcs.values()):
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
    "Fey Grove" : [("Sprite", 20), ("Quickling", 20), ("Dryad", 30), ("Treant", 40), ("Archfey", 125)],
        "Scorched Desert" : [("Giant Scorpion", 30), ("Sand Elemental", 20), ("Giant Snake", 40), ("Vulture", 25), ("Sandworm", 150)],
        "Icy Tundra" : [("Ice Elemental", 20), ("Yeti", 40), ("Snow Golem", 20), ("Frost Giant", 150)],
    "Royal Palace" : [("Guard", 40), ("Archer", 25), ("Dark Knight", 50), ("Warlock", 30), ("Royal Champion", 200)],
        "The Antitower" : [("Tome Spirit", 40), ("Rune Golem", 60), ("Magician", 40), ("Enchanted Golem", 250)],
    "Astral Plane" : [("Astral Spirit", 40), ("Githyanki", 60), ("Wanderer", 50), ("Vlaakith", 250)],
        "The Abyss" : [("Winged Demon", 40), ("Hulking Demon", 70), ("Nimble Demon", 50), ("Yeenoghu", 300)],
    "Mount Celestia" : [("Angel", 50), ("Seraph", 40), ("Archangel", 70), ("Deity", 300)],
        "The Nine Hells" : [("Bone Devil", 50), ("Ice Devil", 60), ("Chain Devil", 60), ("Pit Fiend", 80), ("Asmodeus", 500)],
    "Special" : {
        "Lesser Devil" : ("Lesser Devil", 25),
        "Greater Devil" : ("Greater Devil", 70)
    }
}
