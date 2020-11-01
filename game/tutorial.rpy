label combat_tutorial:

    "You are about to enter a fight, know that this is a different kind of battle"
    "You can die, but you won't run out of magic... Yet..."
    "Anyway do you want to see the {color=#f00}TUTORIAL{/color} for this battle?"
    menu:
        "[abgreen]Yes, show me how it works":
            jump tutorial01
        "No, I can handle it myself":
            jump combat


label tutorial01:
    hide screen points_allhh
    scene tut01
    with dissolve
    "So this will be what combats look like"
    "The orbs represent your HP and MP and the bar your enemy's HP"
    "Then you have many choices of what to do between the orbs"
    scene tut02
    with dissolve
    "Here Battlemagic is selected"
    "When opened you will have new options"
    "You have the level 1 spells on the first menu"
    "You also have 'Level 5 spells' available because our Battlemagic skill is at least 5"
    scene tut04
    with dissolve
    "On the level 5 spells, a new list will show up"
    "You start only knowing one level 5 spell for each school, fireball here"
    "During the game you will learn some more spells for each level"
    "As soon as you get to level 10, a new list of spells will unlock, and so on"
    scene tut05
    with dissolve
    "We are using Fireball here to damage our opponent"
    "Then it's your opponent turn to attack"
    scene tut06
    with dissolve
    "As you can see both your HP and MP lowered, but also your opponent's HP"
    scene tut07
    with dissolve
    "To wrap it up, the sword means it's an attack spell"
    "While the shield means that it's a defensive one"
    "There are also healing spells that will show a green cross"
    "As you can see here, there are also combined spells, that are used as attack and defense"
    scene tut03
    with dissolve
    "Ohh... One last thing, spells that have an hourglass, like Icy wind here"
    "Stay active for multiple turns, in this case the (3x) means it will stay for 3 turns"






    if enemy == "g1":
        "That's all, get ready to fight that minotaur"

        show screen points_allhh
        jump combat

    elif enemy == "e1":
        "That's all, get ready to fight that skeleton mage"

        show screen points_allhh
        jump combat

    elif enemy == "n1":
        "That's all, get ready to fight that Hooded mage"

        show screen points_allhh
        jump combat

    hide screen MC_bars
    hide screen hpbar
    scene black
    with dissolve

label endtut:

    nvl clear






    nvl clear
    n "Since you won you can choose a skill to upgrade"
    nvl clear





    menu:
        "Raise Battlemagic[abgreen] [abdestpoint]":
            $ Destpoints += 1
            "Your Battlemagic skill improved"
        "Raise Summoning[abgreen] [absummpoint]":

            $ Summpoints += 1
            "Your Summoning skill improved"
        "Raise Alteration[abgreen] [abaltepoint]":

            $ Altepoints += 1
            "Your Alteration skill improved"
        "Raise Illusion[abgreen] [abiluspoint]":

            $ Iluspoints += 1
            "Your Illusion skill improved"
        "Raise Mysticism[abgreen] [abmystpoint]":

            $ Mystpoints += 1
            "Your Mysticism skill improved"
        "Raise Healing[abgreen] [abhealpoint]":

            $ Healpoints += 1
            "Your Healing skill improved"
        "Raise Necromancy[abgreen] [abnecropoint]":

            $ Necropoints += 1
            "Your Necromancy skill improved"



label postcombatskills:
    if enemy == "g1":
        jump Goodsidesv25
    elif enemy == "e1":
        jump Evilsidesv25
    elif enemy == "n1":
        jump Neutralsidesv25
    elif enemy == "evilstatue":
        jump killedstatuev3g

label Goodsidesv25:
    scene v25179
    with dissolve
    ayna "Not bad but I'm sure you can do a lot better"
    scene v25180
    with dissolve
    ayna "Don't you agree?"
    jump v026

label Evilsidesv25:
    scene v25012
    with dissolve
    Bredita "It was ok, you have a lot to learn"
    scene v25013
    with dissolve
    Bredita "It's a good start"
    jump v026

label Neutralsidesv25:
    scene v25231
    with dissolve
    Nonen "Shit!!! I'm out of here"
    jump v026
