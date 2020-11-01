init:
    $ weapon = 0
    $ minordrainlife = 0
    $ isabellaksister = 0
    $ isabellabjv3 = 0



label v031neutral:
    if isabellalove <= 4:
        $ sleptisa = 0
    else:
        $ sleptisa = 1

    scene black

    if sleptisa == 1:
        isabella "Hey time to wake up"
        scene v31n001
        with dissolve
        isabella "Good morning..."
        MC "Good morning"
        isabella "Did you have a good night's rest?"
        MC "You can say that"
        isabella "Let me pull those blinds up"
        "Isabella moves towards the windows and opens the blinds"
        scene v31n002
        with dissolve
        isabella "{i}Yawn!{/i}"
        isabella "I really needed that"
        scene v31n003
        with dissolve
        MC "Wow... You look even better in the light"
        isabella "Thank you... {w} We need to get ready to go"
        MC "Sure..."
        "You and Isabella get dressed"
        scene v31n004
        with dissolve
        isabella "I hope you feel energetic, I want to find my mother today"
        MC "I'm sure we will!"
        scene v31n005
        with dissolve
        isabella "Thank you for helping me out on this"
        MC "No need to thank me"
        isabella "Really? I wanted to thank you with a kiss..."
        MC "In that case..."
        scene v31n006
        with dissolve
        "She doesn't let you finish the sentence"
        isabella "Muawh"
        scene v31n005
        with dissolve
        isabella "Now that you've been properly thanked let's go"
    else:
        isabella "Rise and shine [MC]"
        scene v31n007
        with dissolve
        MC "Hmmm... What...?"
        isabella "Time to wake up"
        scene v31n008
        with dissolve
        MC "Oh.. Good morning Isabella...{w} I mean, is it morning?"
        isabella "{i}Giggle{/i}, yes it is, are you ready to go?"
        MC "Yes, I'm ready"
        isabella "Great!"
    scene v26n072
    with dissolve
    alice "Hello you two, had a nice night?"
    isabella "Yes thank you for the hospitality"
    alice "We are the ones who should thank you, you saved our village"
    scene v26n073
    with dissolve
    isabella "Hey [MC] are you ready to go?"
    alice "Are you leaving already?"
    scene v26n072
    with dissolve
    isabella "Yeah, we must find someone and time is of the essence"
    scene v31n009
    with dissolve
    alice "Well that's a shame, we fixed your ship and it's ready to go"
    scene v31n010
    with dissolve
    isabella "That is awesome! Thank you, let's go [MC]"
    alice "There is also a reward in there, I'm sure you'll like it"
    scene v31n011
    with dissolve
    alice "We also included some equipment for you to use [MC]"
    MC "Really? That's great I'm tired of using this old robe"
    alice "I'm sure it will fit you nicely"
    alice "I would love to see you try it on for me sometime..."
    menu:
        "I would love for you to see me dressing, maybe more..[abred] [abnoloveidiot]":
            scene v31n013
            with dissolve
            alice "Hmmm what an interesting idea..."
            isabella "..."
            $ isabellalove -= 1
            "Isabella likes you less"
        "I'm sure you'll see it someday[ablovecolor] [ablove]":

            scene v31n012
            with dissolve
            alice "Oh..."
            isabella "{i}Giggle{/i}..."
            $ isabellalove += 1
            "Isabella likes you more"

    scene v31n010
    with dissolve
    isabella "Shall we go [MC]?"
    MC "Yes let's move on"
    alice "See you, and thank you so much, safe journeys to you"
    scene v31n014
    with dissolve
    "You arrive at the ship"
    isabella "I guess they weren't joking about the reward"
    isabella "There is a big chest on board"
    MC "A great chest I must say..."

    if isabellalove <= 4:
        isabella "Let's see what's inside"
    else:

        scene v31n016
        with dissolve
        isabella "A great che... {i}giggle{/i} {w} you pervert"
        MC "It's the truth, I'm not the one to blame"
        isabella "Have you seen all you wanted?"
        isabella "Can I open it now?"
        MC "Sure, go ahead"


    scene v31n015
    with dissolve
    "Isabella opens the chest"
    isabella "Well there is some gold in here"
    isabella "Here take some"
    $ Gold += 50
    "You received 50 gold"
    MC "Thanks"
    isabella "There's also something else here"
    MC "What is it? The equipment Alice was talking about?"
    isabella "Yes, clothing, armor and a knife"
    scene v31n016
    with dissolve
    isabella "You will look better than with those rags"
    "You start to undress"
    if sleptisa == 0:
        scene v31n017
        with dissolve
        "Isabella acts a bit shy, and looks away while you change"
    else:
        scene v31n018
        with dissolve
        "Isabella looks at you changing"
        MC "Are you going to stare while I dress?"
        isabella "There's nothing there that I haven't seen already..."
    MC "So what do I look like?"
    scene v31n019
    with dissolve
    isabella "Like some important noble knight ahaha"
    isabella "Are you inventing a new class? Mage knight? ahaha"
    MC "I have a knife you petty peasant!!"
    isabella "Oh no, please my lord don't punish me, ahaha"
    MC "I'll let you go this time..."
    $ weapon = 1
    "You can now use {color=#f00}{b}Melee{/b}{/color} in combat"
    scene v31n016
    with dissolve
    isabella "{i}Giggle{/i}, we should get going"
    MC "Right let's go!"
    "You sail for some hours"
    scene v31n020
    with dissolve
    isabella "Look! I believe this is where we should stop"
    MC "Do you smell smoke?"
    scene v31n021
    with dissolve
    isabella "I do, maybe they are still here"
    isabella "There's only one way to find out, let's look around"
    scene v31n022
    with dissolve
    "You leave the ship on the shore and venture into the woods"
    isabella "We should be near civilization there are signs of human activity here"
    isabella "Some men and horse footprints, besides the smell of smoke and lack of animals"
    MC "You have some impressive tracking skills"
    isabella "My mother taught me everything I know"
    scene v31n023
    with dissolve
    isabella "I can't stop thinking about her..."
    MC "Don't worry, we must be very close to finding her"
    isabella "I hope you're right..."
    scene v31n024
    with dissolve
    isabella "I know it's selfish of me to bring you with me"
    isabella "Knowing what you faced when you were a kid..."
    menu:
        "Nonsense, I'm here because I want you to find your mother[ablovecolor] [ablove]":
            scene v31n025
            with dissolve
            "She get's really close to you"
            isabella "You're so kind to me..."
            $ isabellalove += 1
            "Isabella likes you more"
            if isabellalove <= 4:
                scene v31n026
                with dissolve
                "It looks like she was going for a kiss but then..."
                isabella "I... {w} We should move on"
            else:
                scene v31n027
                with dissolve
                "She moves in for a kiss"
                "You feel her soft lips against yours and her gentle breath on your face"
                scene v31n025
                with dissolve
                MC "What was that?"
                isabella "I really wanted to do that {i}giggle{/i}"
                jump v31forrest
        "Yeah, And you don't see me crying about that[abred] [abnoloveidiot]":



            scene v31n023
            with dissolve
            isabella "Oh... Right, I'm sorry"
            $ isabellalove -= 1
            "Isabella likes you less"
            jump v31forrest

label v31forrest:
    scene v31n023
    with dissolve
    isabella "What the.. Did you hear that?"
    MC "What?"
    isabella "Shhh, be quiet.. Hurry hide!"
    scene v31n029
    with dissolve
    "You see Isabella ducking and you do the same"
    isabella "Over there..."
    scene v31n030
    with dissolve
    "You see some Slayers a bit away from where you are"
    cpt "How dare you ignore my orders!!??"
    cpt "That's treason you worthless piece of shit!"
    sol "But... Killing children.. I just can't..."
    cpt "Children??!! They are the enemy! They would kill you!"
    cpt "Lift him up you two!"
    scene v31n031
    with dissolve
    cpt "You know what happens to traitors?"
    cpt "Take this!"
    "You see the captain and the soldier punching and kicking the other soldier"
    scene v31n032
    with dissolve
    sol "Please, no more..."
    cpt "Look at the coward now... Not only a traitor but also a coward.."
    cpt "Guess where I'm going to put my knife right now..."
    isabella "Stop it!!"
    scene v31n033
    with dissolve
    cpt "What the..? What do we have here?"
    scene v31n034
    with dissolve
    cpt "Look at that girl... So hot..."
    cpt "Kill that wimp that's with her, I want her for myself"
    isabella "Pfft you don't know what you're getting into"
    scene v31n035
    with dissolve
    cpt "Ahahah let's get them!"
    $ enemy = "Slayer_soldiers"
    $ companion = 1
    $ companion_name = "Isabella"
    jump combat

label v3killedslayers:
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene black
    n "Since you won, you can choose a skill to upgrade"


    menu:
        "Raise Battlemagic[abgreen] [abdestpoint] {image=001battle}":
            $ Destpoints += 1
            "Your Battlemagic skill improved"
        "Raise Summoning[abgreen] [absummpoint] {image=001summon}":

            $ Summpoints += 1
            "Your Summoning skill improved"
        "Raise Alteration[abgreen] [abaltepoint] {image=001alteration}":

            $ Altepoints += 1
            "Your Alteration skill improved"
        "Raise Illusion[abgreen] [abiluspoint] {image=001illusion}":

            $ Iluspoints += 1
            "Your Illusion skill improved"
        "Raise Mysticism[abgreen] [abmystpoint] {image=001myst}":

            $ Mystpoints += 1
            "Your Mysticism skill improved"
        "Raise Healing[abgreen] [abhealpoint] {image=001heal}":

            $ Healpoints += 1
            "Your Healing skill improved"
        "Raise Necromancy[abgreen] [abnecropoint] {image=001necro}":

            $ Necropoints += 1
            "Your Necromancy skill improved"

    scene v31n036
    with dissolve
    isabella "I warned them..."
    "You look at the soldier that was being beaten"
    "He's speechless from the show"
    scene v31n037
    with dissolve
    isabella "Hey you!"
    sol "That was incredible!"
    isabella "I want to ask some questions"
    sol "Of course... Ask away"
    scene v31n038
    with dissolve
    isabella "First, are there more of you close by?"
    sol "I don't think so, they brought me here to beat me up and kill me"
    MC "Yeah we noticed, what happened?"
    scene v31n039
    with dissolve
    sol "Well, I refused to follow orders... I know I'm a traitor.."
    sol "But I can't just kill childrens like that..."
    MC "I believe that you are alive now because of that"
    scene v31n040
    with dissolve
    MC "Isabella jumped out to save you for that reason I think"
    sol "Yes... Thank you for saving me"
    isabella "I think it's the first time I've seen a Slayer who's not a monster"
    scene v31n041
    with dissolve
    sol "You have to understand... We follow orders from the Emperor"
    sol "Some of us don't like it but what can we do?"
    "That's interesting information, there are probably more like him"
    "With the correct actions you can turn them against the Emperor"
    isabella "More important, where is the town you were attacking?"
    scene v31n042
    with dissolve
    sol "It's right after that hill, but there is probably nobody there anymore"
    isabella "Then we must hurry!"
    MC "Right behind you"
    scene v31n043
    with dissolve
    "You reach the town"
    sol "Why does the captain always keeps the good whores to himself?"
    sol2 "Hey you can't complain much, it's not like you don't get pussy"
    sol "Ahahaah"
    isabella "Look over there, more soldiers"
    MC "But there seems to be nobody else"
    isabella "Then we must ask them, let's..."
    scene v31n044
    with dissolve
    "You see one of the soldiers face get hit by an arrow"
    scene v31n045
    with dissolve
    "Then the other two"
    "And you see a woman jumping in front of them"
    MC "Wow"
    isabella "Mom??!!"
    scene v31n046
    with dissolve
    isabella "Mom!!"
    MC "Hey wait a sec..."
    scene v31n047
    with dissolve
    isabella "Mom, I can't believe it's you!"
    "You see Isabella running towards the woman"
    "You also notice the dead soldiers"
    MC "They never had a chance"
    scene v31n048
    with dissolve
    isabella "I was so worried... I couldn't imagine losing you"
    scene v31n049
    with dissolve
    katla "Calm down dear... I'm fine"
    MC "Ahemm"
    scene v31n050
    with dissolve
    isabella "Mom this is [MC], he helped me so much"
    isabella "[MC] this is my mom Katla"
    MC "Pleasure to meet you Katla"
    "Why is her face so familiar to you?"
    scene v31n051
    with dissolve
    katla "Hello [MC] thank you for helping my little girl, she's all I have left"
    katla "Have we met before? You look so familiar..."
    katla "Your eyes... {w} where have I seen those eyes?"
    MC "I... You..."
    "You start to feel weird and weak"
    scene v31n052
    with dissolve
    MC "I..."
    isabella "Look out!"
    scene black
    with dissolve
    sis "Hey come on!"
    scene v31n113
    with dissolve
    MC "Sister?"
    sis "Are you coming or what?"
    MC "But mom said we shouldn't venture into the ruins"
    scene v31n114
    with dissolve
    sis "Come on, don't be such a baby, don't you want to know what's inside?"
    MC "I do..."
    scene v31n115
    with dissolve
    sis "Oh, don't tell me you're scared"
    menu:
        "I'm not scared of anything, you are!":
            scene v31n116
            with dissolve
            sis "Sounds like you are..."
        "[abgreen]You will protect me won't you?":
            scene v31n117
            with dissolve
            sis "Ahaahah funny"

    scene v31n118
    with dissolve
    sis "Lets explore it"
    MC "Wait..."
    scene v31n119
    with dissolve
    sis "Come on!! There is an entrance here"
    scene v31n120
    with dissolve
    "She's gone"
    MC "Wait for me!"
    scene v31n121
    with dissolve
    MC "Where is she? Isabella where are you?"
    "You see an entrance and you get inside"
    "You find yourself inside a cave with running water"
    scene v31n122
    with dissolve
    MC "What is this? It's so dark here"
    MC "Can't see a thing"
    scene v31n123
    with dissolve
    MC "Isabella? where are you? Sister?"
    scene v31n124
    with dissolve
    sis "Run!!"
    MC "What?"
    sis "Run fool!!!"
    scene v31n125
    with dissolve
    MC "Oh my God!! A giant spider"
    sis "Hurry get out"
    scene v31n126
    with dissolve
    MC "It's getting closer!!"
    sis "Oh no!"
    scene v31n127
    with dissolve
    sis "Ah... I'm stuck, my feet are stuck to here"
    "She falls to the ground"
    scene v31n128
    with dissolve
    sis "Ahhhh!! Help me"
    MC "What can I do?!"
    scene v31n129
    with dissolve
    sis "It's going to get me!"
    MC "Grab my hand!"
    scene v31n130
    with dissolve
    MC "Come on!"
    sis "I love you little brother..."
    "She knows this is the end..."
    scene v31n131
    with dissolve
    "When the spider is about to grab your sister"
    "An arrow pierces through one of its eyes"
    scene v31n132
    with dissolve
    sis "Mom!!"
    "You see your mother firing some more arrows"
    scene v31n133
    with dissolve
    mom "Are you ok? Both of you?"
    sis "Yes...."
    MC "Yes..."
    mom "Let's get out of here..."
    scene v31n134
    with dissolve
    mom "What did I tell you?? No visits to the ruins!!"
    sis "I'm sorry mom, it's all my fault..."
    scene v31n135
    with dissolve
    mom "Let's go home, we will talk about it there"
    sis "Sure mom..."
    scene v31n136
    with dissolve
    mom "Don't think you're safe, you have some blame too young man!"
    MC "But mom..."
    scene black
    with dissolve
    mom "And that's why I killed those soldiers"
    scene v31n053
    with dissolve
    katla "They..."
    "Does this mean that they are your mother and sister?"
    "Some memories start to come back to you"
    scene v31n054
    with dissolve
    isabella "So what do we do now?"
    katla "We need to return home and think of what we should do next"
    katla "We're demon hunters after all"
    isabella "I hate demons, but I also hate slayers..."
    MC "Hey...."
    scene v31n055
    with dissolve
    katla "Look who's awake"
    isabella "How are you [MC]?"
    MC "I'm ok I guess"
    scene v31n056
    with dissolve
    isabella "That's good, we were worried"
    katla "You passed out, out of nowhere"
    katla "Isabella was telling me that you are a Mage"
    MC "You could say that"
    scene v31n057
    with dissolve
    katla "Good to know that her boyfriend is not only cute but also talented"
    isabella "Mom!"
    menu:
        "I don't know about that, all I know is that she is beautiful and skilled[ablovecolor] [ablove]":
            scene v31n058
            with dissolve
            katla "And a gentleman I see"
            $ isabellalove += 1
            "Isabella likes you more"
            katla "She is my most precious treasure in the world"
            katla "I'm glad you helped her"
        "Well, it is what it is":

            scene v31n059
            with dissolve
            katla "Ok, young Mage thank you for helping my daughter"
            katla "I hope I can repay you someday"

    katla "Let's rest for the night, tomorrow morning we need energy"
    scene v31n060
    with dissolve
    "You see them leaving the room"
    isabella "Have a nice night"
    katla "Sweet dreams"
    MC "See you tomorrow"
    scene v31n061
    with dissolve
    "They left..."
    MC "Are they my mother and sister?"
    MC "I think they are... What should I do?"
    MC "Should I tell them? Is it better to leave it like this?"
    MC "Guess I need to sleep"
    isabella "Hey [MC] I'm entering"
    MC "Sure.."
    scene v31n062
    with dissolve
    isabella "I wanted to thank you, without you I wouldn't have found my mother"
    MC "You don't need to thank me you know?"
    scene v31n063
    with dissolve
    isabella "Hey, what's the matter? Is everything alright?"
    MC "I'm not sure..."
    isabella "What do you mean?"
    scene v31n064
    with dissolve
    isabella "Did you hit with your head or something?"

    isabella "Can a kiss help with that?"
    scene v31n065
    with dissolve

    menu:
        "[abgreen]Kiss her":
            scene v31n068
            with dissolve
            isabella "Hmmm"
            scene v31n067
            with dissolve
            isabella "You are still not looking good..."
            isabella "What's wrong?"
            menu:
                "Nothing, I'm fine don't worry":
                    isabella "I think I know what you need"
                    isabella "Wait here"
                    scene v31n070
                    with dissolve
                    isabella "I'll be right back"
                    MC "Ok..."
                    scene v31n071
                    with dissolve
                    isabella "Here! Look what I got"
                    isabella "I'm sure this will help with that bad face"
                    scene v31n072
                    with dissolve
                    MC "Where did you get this?"
                    isabella "I have my secrets {i}giggle{/i}"
                    isabella "Are we drinking it or what?"
                    "You spend some time together drinking the whole bottle"
                    "You start to feel a bit tipsy and Isabella must be too"
                    isabella "You see hahah, you have a better look on your face now"
                    scene v31n073
                    with dissolve
                    isabella "So what's on your mind? Do you need a kiss?"
                    scene v31n074
                    with dissolve
                    "You can't resist her beauty, you kiss her"
                    isabella "Hmmm"
                    scene v31n075
                    with dissolve
                    MC "Look at this pretty face, you are beautiful"
                    MC "I need to kiss you again"
                    isabella "Don't let me stop you..."
                    scene v31n076
                    with dissolve
                    isabella "Hmmm you are so kind.."
                    "You keep kissing for some time"
                    scene v31n077
                    with dissolve
                    MC "I'm..."
                    isabella "Out of words?"
                    scene v31n078
                    with dissolve
                    isabella "Muawh"
                    scene v31n066
                    with dissolve
                    isabella "Oh come on why aren't you telling me what's wrong with you?"
                    menu:
                        "I haven't had enough kisses?":
                            isabella "Oh..."
                            scene v31n065
                            with dissolve
                            MC "Much better"
                            jump v3notknowisa
                        "I think you're my sister":


                            scene v31n069
                            with dissolve
                            isabella "What?! What are you talking about?"
                            isabella "Why are you saying that?"
                            isabella "Is it to push me away?"
                            MC "Quite the opposite... I'm telling you because I care about you"
                            scene v31n067
                            with dissolve
                            isabella "But my brother died... {w} I..."
                            MC "Well, I've been told that my family died and my village was destroyed"
                            MC "But now I'm almost sure that's not completely true..."
                            isabella "You can't be him... Your eyes... {w} it... "
                            scene v31n066
                            with dissolve
                            isabella "Is it really you Gortlir?"
                            MC "I don't remember that name, but I do remember you and mom"
                            MC "I just remembered that time we went to the ruins and you were attacked by a spider"
                            MC "Then mom saved us..."
                            scene v31n069
                            with dissolve
                            isabella "But how? I... "
                            isabella "I... this is too much..."

                            jump v3sheknowsisa
                "[abgreen]Tell her that you think she is you sister":


                    scene v31n069
                    with dissolve
                    isabella "What?! What are you talking about?"
                    isabella "Why are you saying that?"
                    isabella "Is it to push me away?"
                    MC "Quite the opposite... I'm telling you because I care about you"
                    scene v31n067
                    with dissolve
                    isabella "But my brother died... {w} I..."
                    MC "Well, I've been told that my family died and my village was destroyed"
                    MC "But now I'm almost sure that's not completely true..."
                    isabella "You can't be him... Your eyes... {w} it... "
                    scene v31n066
                    with dissolve
                    isabella "Is it really you Gortlir?"
                    MC "I don't remember that name, but I do remember you and mom"
                    MC "I just remembered that time we went to the ruins and you were attacked by a spider"
                    MC "Then mom saved us..."
                    scene v31n069
                    with dissolve
                    isabella "But how? I... "
                    isabella "I... this is too much..."
                    scene v31n070
                    with dissolve
                    isabella "I..."
                    MC "..."
                    scene v31n061
                    with dissolve
                    "She left the room"
                    MC "Was this the right thing to do? What now?"

                    scene v31n071
                    with dissolve
                    isabella "Here! Look what I got"
                    isabella "I'm sure this will help me deal with this new information"
                    scene v31n072
                    with dissolve
                    MC "Where did you get this?"
                    isabella "I have my secrets {i}giggle{/i}"
                    isabella "Are we drinking it or what?"
                    "You spend some time together drinking the whole bottle"
                    "You start to feel a bit tipsy and Isabella must be too"
                    isabella "You see hahah, you have a better look on your face now"
                    scene v31n073
                    with dissolve
                    isabella "So what's on your mind? I know what you said but..."
                    scene v31n074
                    with dissolve
                    "You can't resist her beauty, you kiss her"
                    isabella "Hmmm"
                    scene v31n075
                    with dissolve
                    MC "Look at this pretty face, you are beautiful"
                    MC "I need to kiss you again"
                    isabella "But we..."
                    scene v31n076
                    with dissolve
                    isabella "Hmmm you are so kind.."
                    "You keep kissing for some time"
                    scene v31n077
                    with dissolve
                    MC "I'm..."
                    isabella "Out of words?"
                    scene v31n078
                    with dissolve
                    isabella "Muawh"
                    scene v31n066
                    with dissolve
                    jump v3sheknowsisa
        "Stop her and tell her that you think she is you sister":


            scene v31n069
            with dissolve
            isabella "What?! What are you talking about?"
            isabella "Why are you saying that?"
            isabella "Is it to push me away?"
            MC "Quite the opposite... I'm telling you because I care about you"

            scene v31n067
            with dissolve
            isabella "But my brother died... {w} I..."
            MC "Well, I've been told that my family died and my village was destroyed"
            MC "But now I'm almost sure that's not completely true..."
            isabella "You can't be him... Your eyes... {w} it... "
            scene v31n066
            with dissolve
            isabella "Is it really you Gortlir?"
            MC "I don't remember that name, but I do remember you and mom"
            MC "I just remembered that time we went to the ruins and you were attacked by a spider"
            MC "Then mom saved us..."
            scene v31n069
            with dissolve
            isabella "But how? I... "

            isabella "I... {w} this is too much..."
            scene v31n070
            with dissolve
            isabella "I..."
            MC "..."
            scene v31n061
            with dissolve
            "She left the room"
            MC "Was this the right thing to do? What now?"

            scene v31n071
            with dissolve
            isabella "Here! Look what I got"
            isabella "I'm sure this will help me deal with this new information"
            scene v31n072
            with dissolve
            MC "Where did you get this?"
            isabella "I have my secrets {i}giggle{/i}"
            isabella "Are we drinking it or what?"
            "You spend some time together drinking the whole bottle"
            "You start to feel a bit tipsy and Isabella must be too"
            isabella "You see hahah, you have a better look on your face now"
            scene v31n073
            with dissolve
            isabella "So what's on your mind? I know what you said but..."
            scene v31n074
            with dissolve
            "You can't resist her beauty, you kiss her"
            isabella "Hmmm"
            scene v31n075
            with dissolve
            MC "Look at this pretty face, you are beautiful"
            MC "I need to kiss you again"
            isabella "But we..."
            scene v31n076
            with dissolve
            isabella "Hmmm you are so kind.."
            "You keep kissing for some time"
            scene v31n077
            with dissolve
            MC "I'm..."
            isabella "Out of words?"
            scene v31n078
            with dissolve
            isabella "Muawh"
            scene v31n066
            with dissolve
            jump v3sheknowsisa



label v3sheknowsisa:
    if isabellalove <=5:
        scene v31n070
        with dissolve
        isabella "I need to go..."
        scene v31n061
        with dissolve
        "She left you alone in the room"
        jump v3morningmom
    else:

        scene v31n079
        with dissolve
        isabella "You know what? I don't know if it's the drinking or not"
        isabella "But I don't care..."
        MC "What?"
        isabella "I don't care if you are my brother or not..."
        isabella "I feel attracted to you... I have feelings for you.."
        isabella "And I want to show you something"
        scene v31n080
        with dissolve
        "She undresses in front of you"
        MC "You look amazing..."
        isabella "You said something about my great chest earlier?"
        MC "You bet I did... look at them"
        isabella "Do you want to feel them?"
        scene v31n081
        with dissolve
        "You don't wait a second..."
        MC "They feel amazing..."
        isabella "Glad you like them"
        scene v31n082
        with dissolve
        isabella "You don't need to be so gentle, I won't break so easily"
        MC "Wow... You are perfect"
        scene v31n083
        with dissolve
        isabella "Yes that's it... Your hand is so firm"
        scene v31n084
        with dissolve
        isabella "Hmmm yes keep going..."
        MC "Do you like it?"
        isabella "Yes I do..."
        scene v31n085
        with dissolve
        isabella "I never felt like this before"
        "What does she mean? Is she a virgin?"
        isabella "Lie down"
        scene v31n086
        with dissolve
        "You lie down and have a magnificent view in front of you"
        isabella "Can I touch.. {w} it?"
        MC "Yes you can"
        scene v31n087
        with dissolve
        "She starts to touch your dick gently"
        MC "Hmmm"
        isabella "Does it feel good?"
        MC "Yes..."
        scene v31n088
        with dissolve
        "As your dick gets harder she starts to stroke it"
        MC "Ah..."
        isabella "Are you ok? Did that hurt?"
        MC "I'm fine, you can keep going"
        scene v31n089
        with dissolve
        "She increases the pace a bit, you can tell that she not sure what to do"
        "But look at her, she is gorgeous"
        isabella "I want to try something else"
        scene v31n090
        with dissolve
        "She starts using both hands and her face gets very close to your cock"
        MC "Ah... yes... that's it.."
        scene v31n091
        with dissolve
        isabella "Do you like it?"
        MC "I love it..."
        scene v31n092
        with dissolve
        "She then starts to lick you"
        isabella "Lick lick..hmmm"
        MC "Ah yes..."
        scene v31n093
        with dissolve
        "Then she starts to put your penis inside her mouth"
        $ isabellabjv3 = 1
        isabella "Hmmm... It tastes funny"
        "But that doesn't seem to bother her"
        scene v31n094
        with dissolve
        "And she tries deeper"
        MC "Ah....ah.."
        isabella "Hmmm mfnff"
        MC "Do you want to turn around so I can please you too?"
        scene v31n095
        with dissolve
        isabella "I... "
        MC "What's the matter?"
        isabella "I need to go..."
        scene v31n096
        with dissolve
        MC "What, why?"
        isabella "I'm sorry..."
        scene v31n097
        with dissolve
        "She goes to leave"
        scene v31n061
        with dissolve
        "She leaves you alone in the room"
        $ renpy.end_replay()
        jump v3morningmom


label v3notknowisa:
    if isabellalove <=5:
        scene v31n079
        with dissolve
        isabella "Well... I need to go..."
        isabella "We have a long day tomorrow and We should be at our best"
        scene v31n070
        with dissolve
        isabella "See you tomorrow"
        scene v31n061
        with dissolve
        "She leaves you alone in the room"
        jump v3morningmom
    else:

        scene v31n079
        with dissolve
        isabella "You know what? I don't know if it's the drinking or not"
        isabella "But I want..."
        MC "What?"
        isabella "I want to stay here with you..."
        isabella "I feel attracted to you... I have feelings for you.."
        isabella "And I want to show you something"
        scene v31n080
        with dissolve
        "She undress in front of you"
        MC "You look amazing..."
        isabella "you said something about my great chest earlier?"
        MC "You bet I did... look at them"
        isabella "Do you want to feel them?"
        scene v31n081
        with dissolve
        "You don't wait a second..."
        MC "They feel amazing..."
        isabella "Glad you like them"
        scene v31n082
        with dissolve
        isabella "You don't need to be so gentle I won't break so easily"
        MC "Wow... You are perfect"
        scene v31n083
        with dissolve
        isabella "Yes that's it... Your hand is so firm"
        scene v31n084
        with dissolve
        isabella "Hmmm yes keep going..."
        MC "Do you like it?"
        isabella "Yes I do..."
        scene v31n085
        with dissolve
        isabella "I never felt like this before"
        "What does she mean? Is she a virgin?"
        isabella "Lie down"
        scene v31n086
        with dissolve
        "You lie down and have a magnificent view in front of you"
        isabella "Can I touch.. {w} it?"
        MC "Yes you can"
        scene v31n087
        with dissolve
        "She starts to touch your dick gently"
        MC "Hmmm"
        isabella "Does it feel good?"
        MC "Yes..."
        scene v31n088
        with dissolve
        "As your dick gets harder she starts to stroke it"
        MC "Ah..."
        isabella "Are you ok? Did that hurt?"
        MC "I'm fine you can keep going"
        scene v31n089
        with dissolve
        "She increases the pace a bit, you can tell that she's not sure what to do"
        "But look at her, she is gorgeous"
        isabella "I want to try something else"
        scene v31n090
        with dissolve
        "She starts using both hands and her face gets very close to your cock"
        MC "Ah... yes... that's it.."
        scene v31n091
        with dissolve
        isabella "Do you like it?"
        MC "I love it..."
        scene v31n092
        with dissolve
        "She then starts to lick you"
        isabella "Lick lick..hmmm"
        MC "Ah yes..."
        scene v31n093
        with dissolve
        "Then she starts to put your penis inside her mouth"
        $ isabellabjv3 = 1
        isabella "Hmmm... It tastes funny"
        "But that doesn't seem to bother her"
        scene v31n094
        with dissolve
        "And she tries deeper"
        MC "Ah....ah.."
        isabella "Hmmm mfnff"
        MC "Do you want to turn around so I can please you too?"
        scene v31n095
        with dissolve
        isabella "I... "
        MC "What's the matter?"
        isabella "I need to go..."
        scene v31n096
        with dissolve
        MC "What, why?"
        isabella "I'm sorry..."
        scene v31n097
        with dissolve
        "She's goes to leave"
        scene v31n061
        with dissolve
        "She leaves you alone in the room"
        jump v3morningmom

label v3morningmom:
    scene black
    with dissolve
    MC "I guess it's time to sleep..."
    "It takes you a few minutes but you fall asleep"
    scene v31n061
    with dissolve
    MC "{i}Yawn{/i}.. Is it morning already?"
    "You hear voices outside"
    MC "They are already up and out? Let's check"
    scene v31n098
    with dissolve
    "You leave the house where you slept and find Isabella and her mother"
    katla "Are you ready to go home honey?"
    isabella "Yes, I'm sure everyone will be happy to see you"
    isabella "Time to wake up [MC]"
    MC "No need for that"
    scene v31n099
    with dissolve
    MC "Good morning ladies"
    katla "Hello [MC]"
    isabella "Good morning"
    scene v31n100
    with dissolve
    MC "So are we getting ready to go?"
    isabella "Yes we will return home, then you are finally free ahaha"
    MC "What if I want to stay with you?"
    katla "Oh... Are you proposing to my daugther?"
    MC "That's not what I meant..."
    scene v31n101
    with dissolve
    katla "You... I... Your face is so familiar..."
    katla "Even the way you react..."
    scene v31n102
    with dissolve
    katla "It can't be..."
    katla "You remind me of..."
    mvoice "There you are!"
    scene v31n103
    with dissolve
    isabella "Hum??"
    katla "??"
    scene v31n104
    with dissolve
    irgodon "I thought I would never find you"
    irgodon "I see that Isabella got here first"
    scene v31n105
    with dissolve
    isabella "Irgodon!! Are you really ok?!"
    irgodon "You bet I am!"
    scene v31n106
    with dissolve
    isabella "I'm so happy you're safe"
    irgodon "No demon or slayer could beat me"
    scene v31n107
    with dissolve
    katla "Good to see you Irgodon, did everyone decide to come look for me?"
    irgodon "Well, you're one of us, no one would rest until we found you"
    menu:
        "Good to see you Irgodon":
            scene v31n108
            with dissolve
            irgodon "Oh... You again..."
        "Have you finished? Can we go now?[abred] [abnoloveidiot]":

            scene v31n109
            with dissolve
            irgodon "Oh... You again... Polite I see..."
            $ isabellalove -= 1
            "Isabella likes you less"

    scene v31n110
    with dissolve
    irgodon "We need to leave this place, there is a massive Slayer army coming"
    katla "What you mean massive?"
    irgodon "Over 20,000 men, I think they plan to take over this land all at once"
    isabella "20,000?!"
    isabella "How can someone fight against something like that?"
    katla "No time to lose, let's go"
    scene v31n111
    with dissolve
    isabella "Let's take them to our ship, [MC]"
    isabella "We will travel directly home"
    isabella "Follow me guys"
    scene v31n112
    with dissolve
    irgodon "Hmmff"
    MC "Ok...."
    scene v31n137
    with dissolve
    isabella "There it is, let's go"
    irgodon "Lead the way"
    scene v31n138
    with dissolve
    "You all get to the ship and get ready to sail"
    scene v31n139
    with dissolve
    katla "The weather is nice, if it keeps like this"
    katla "We can reach our destination in a day"
    isabella "Is everything ok [MC]?"
    scene v31n140
    with dissolve
    isabella "About last night... {w} I..."
    irgodon "What is that?"
    scene v31n141
    with dissolve
    katla "I can't really tell..."
    katla "Do we stop to see?"

    jump v31orctalk

label v31orctalk:
    scene meanwhile
    with dissolve
    scene v31n142
    with dissolve
    orc "Chief Vakgu! We have one of the puny humans who are attacking us"
    vakgu "Bring him here!"
    scene v31n143
    with dissolve
    vakgu "Are these the things that are killing us?!"
    vakgu "Look at him! He looks so fragile, doesn't look like a soldier to me"
    scene v31n144
    with dissolve
    vakgu "So human... How is it possible for weaklings like you to fight?"
    cpt "I'm a Captain! And we use our brains, things unknown to your kind"
    vakgu "Brains? how do you battle with brains?"
    vakgu "Come on show me, I'll let you throw the first punch"
    scene v31n145
    with dissolve
    cpt "It's not like that... Not that you would understand..."
    vakgu "Either you throw a punch or I do, you choose"
    scene v31n146
    with dissolve
    cpt "Take that!"
    vakgu "Hmmff"
    scene v31n147
    with dissolve
    vakgu "You call that a punch?? Ahahahah"
    orc "Ahahaahh"
    vakgu "Ahaha such a weakling"
    vakgu "Let me show you something"
    scene v31n148
    with dissolve
    vakgu "Do you feel it? Hmm? Real strength?"
    vakgu "How can we be losing to you..."

    if wheretoafterslayerbath == "neutral":

        jump neutralis1year

    elif wheretoafterslayerbath == "Evil":
        jump evilis1year
    else:

        jump goodis1year



label neutralis1year:
    scene 1y011
    with dissolve
    isabella "We need to see if anyone needs help"
    irgodon "I agree!"
    scene 1y012
    with dissolve
    isabella "Look, what happened here? Is that a man?"
    "You start to have a bad feeling... This looks like a trap..."
    MC "Wait I..."
    scene 1y013
    with dissolve
    isabella "What's the matter [MC]?"
    irgodon "Let's check this out!!"
    "Before you can say anything else they all get closer to the body"
    scene 1y014
    with dissolve
    katla "Is he dead?"
    irgodon "I'm not sure, it's like his life was drained from his body"
    katla "Magic?"
    scene 1y015
    with dissolve
    isabella "[MC] is a Mage, maybe he could see what happened to him?"
    MC "Well... I can try I guess"
    scene 1y016
    with dissolve
    "You look at the man and it just looks like he died"
    "With no real reason behind it"
    irgodon "Hmmpff... Useless mage... You don't know either, right?"
    irgodon "I wonder what Isabella sees.... Ahhh..."
    scene 1y017
    with hpunch
    irgodon "What are you... Doing to my head..."
    MC "I..."
    "You start to feel like someone dropped a mountain on your head..."
    MC "Shit, what is happening to me?"
    scene 1y018
    with vpunch
    fvoice "Look what we found..."
    MC "Who are..."
    scene black
    with dissolve
    jump lichthehellout
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
