label v021:
    $ shipondock = 0

    scene v021003
    with dissolve
    runar "So?... What are you waiting for?"
    scene v021004
    with dissolve
    runar "Go find my ship!"
    "This fat bastard giving you orders..."
    MC "Very well..."
    "You leave his house into the city"
    scene meanwhile
    with dissolve
    scene meanwhile
    with dissolve
    scene v021076
    with dissolve
    goggos "Do you really think it's necessary to summon him?"
    zegladar "Yes, I don't want to take any risks"
    goggos "But I don't like Adamastor"
    zegladar "Come on! you know I can't summon him alone, I need your power"
    scene v021077
    with dissolve
    goggos "But I..."
    zegladar "You owe me one remember?"
    goggos "Bah... Ok... Let's summon Adamastor then..."
    scene v021078
    with dissolve
    zegladar "Adamastor Zencantus Xamantus!!"
    goggos "Adamastor Zencantus Xamantus!!"
    scene v021079
    with dissolve
    zegladar "Yes!! Come to me!!"
    scene black
    with dissolve
    stop music
    play music "<loop 0.0>ingame.mp3"

    $ visiteddock = 0
    $ visittavern = 0
    $ cityguild = 0
    $ visitedbrothel = 0
    $ visitedgraveyard = 0
    $ visitedshop = 0
    $ gravekey = 0
    $ basementshopv21 = 0
    $ chestbasementshop = 0
    $ holewallshop = 0
    jump allesterracitymap_v21

label allesterracitymap_v21:

    if shipondock == 0:

        call screen allesterracitymapnoship
    else:
        call screen allesterracitymapship

label runarmanorv21:
    scene v2169
    with dissolve
    MC "His doors are closed... There is nothing to do here"
    jump allesterracitymap_v21

label arnoldushousev21:
    scene v2169
    with dissolve
    MC "There seems to be nobody home, I should go"
    jump allesterracitymap_v21


label brothelv21:
    scene v021018
    with dissolve
    "You are at the Brothel"
    if visitedbrothel == 0:
        $ visitedbrothel = 1
        madam "Oh... We have a new one here"
        madam "Hello young man, are you looking for some fun?"
        MC "I'm.... Investigating the ship of Lord Runar's that's gone missing"
        madam "All work and no fun? You know that's not healhty"
        scene v021019
        with dissolve
        madam "Emilia dear, come here please!"
        scene v021018
        with dissolve
        madam "Just wait a second and you will see what I mean"
        madam "Here she is"
        scene v021020
        with dissolve
        emilia "Oh, who is this? Did you come here to have fun?"
        MC "Actually, I'm investigating the missing ship, and looking for clues..."
        scene v021021
        with dissolve
        emilia "Oh, I've heard a lot of things before, but looking for clues?"
        emilia "That's funny heheheh"
        madam "So young boy, do you want to have fun?"
        madam "Emilia can satisfy all your desires for just 25 gold"
        menu:
            "{color=#1BBB20}A little fun wouldn't hurt":
                madam "That's great, you have to pay up front though"
                MC "Ok..."
                if Gold >= 25:
                    $ Gold -= 25
                    MC "Here you go"
                    "You lost 25 gold"
                    madam "Ok Emilia take good care of this young man"
                    emilia "I will!"
                    $ visitedbrothel = 3
                    jump emiliasexpart
                else:

                    MC "I don't have the gold right now..."
                    madam "Well, no gold no fun..."
                    scene v021020
                    with dissolve
                    emilia "Bye, hope to see you again"
                    "You left the brothel"
                    $ visitedbrothel = 2
                    jump allesterracitymap_v21
            "That's not what I'm here for":

                MC "I'm looking for information, nothing more"
                madam "Well... I know nothing about the missing ship, but I had important stuff coming"
                madam "I hope you find it soon, see you around"
                "You left the brothel"
                jump allesterracitymap_v21

    elif visitedbrothel == 1:
        madam "Oh... You are back! have you changed your mind?"
        scene v021019
        with dissolve
        madam "Emilia dear, come here please!"
        scene v021020
        with dissolve
        madam "So young boy, do you want to have fun?"
        madam "Emilia can satisfy all your desires for just 25 gold"
        menu:
            "{color=#1BBB20}A little fun wouldn't hurt":
                madam "That's great, you have to pay up front though"
                MC "Ok..."
                if Gold >= 25:
                    $ Gold -= 25
                    MC "Here you go"
                    "You lost 25 gold"
                    madam "Ok Emilia take good care of this young man"
                    emilia "I will!"
                    $ visitedbrothel = 3
                    jump emiliasexpart
                else:

                    MC "I don't have the gold right now..."
                    madam "Well, no gold no fun..."
                    scene v021020
                    with dissolve
                    emilia "Bye, hope to see you again"
                    "You left the brothel"
                    $ visitedbrothel = 2
                    jump allesterracitymap_v21
            "That's not what I'm here for":

                MC "I'm looking for information nothing more"
                madam "Well... I know nothing abou the missing ship, but I had important stuff coming"
                madam "I hope you find it soon, see you around"
                "You left the brothel"
                jump allesterracitymap_v21

    elif visitedbrothel == 2:
        madam "Oh... You are back! have you got enough gold?"
        scene v021019
        with dissolve
        madam "Emilia dear, come here please!"
        scene v021020
        with dissolve
        madam "So young boy, do you want to have fun?"
        madam "Emilia can satisfy all your desires for just 25 gold"
        menu:
            "{color=#1BBB20}A little fun wouldn't hurt":
                madam "That's great, you have to pay up front though"
                MC "Ok..."
                if Gold >= 25:
                    $ Gold -= 25
                    MC "Here you go"
                    "You lost 25 gold"
                    madam "Ok Emilia take good care of this young man"
                    emilia "I will!"
                    $ visitedbrothel = 3
                    jump emiliasexpart
                else:

                    MC "I don't have the gold right now..."
                    madam "Well, no gold no fun..."
                    scene v021020
                    with dissolve
                    emilia "Bye, hope to see you again"
                    "You left the brothel"
                    $ visitedbrothel = 2
                    jump allesterracitymap_v21
            "That's not what I'm here for":

                MC "I'm looking for information nothing more"
                madam "Well... I know nothing abou the missing ship, but I had important stuff coming"
                madam "I hope you find it soon, see you around"
                "You left the brothel"
                jump allesterracitymap_v21

    elif visitedbrothel == 3:
        madam "Oh... You are back! Did you came back for more?"
        scene v021019
        with dissolve
        madam "Emilia dear, come here please!"
        scene v021020
        with dissolve
        madam "So young boy, do you want to have fun?"
        madam "Emilia can satisfy all your desires for just 25 gold"
        menu:
            "{color=#1BBB20}It was fun, why not?":
                madam "That's great, you have to pay up front though"
                MC "Ok..."
                if Gold >= 25:
                    $ Gold -= 25
                    MC "Here you go"
                    "You lost 25 gold"
                    madam "Ok Emilia take good care of this young man"
                    emilia "I will!"
                    $ visitedbrothel = 3
                    jump emiliasexpart
                else:

                    MC "I don't have the gold right now..."
                    madam "Well, no gold no fun..."
                    scene v021020
                    with dissolve
                    emilia "Bye, hope to see you again"
                    "You left the brothel"
                    $ visitedbrothel = 2
                    jump allesterracitymap_v21
            "That's not what I'm here for":

                MC "I'm looking for information nothing more"
                madam "Well... I know nothing abou the missing ship, but I had important stuff coming"
                madam "I hope you find it soon, see you around"
                "You left the brothel"
                jump allesterracitymap_v21




label emiliasexpart:
    scene v021022
    with dissolve
    emilia "Can you follow me please?"
    MC "Of course I can"
    scene v021023
    with dissolve
    "She walks in front of you teasing you with her ass"
    "You follow her into a private room"
    scene v021024
    with dissolve
    emilia "Do you have something in mind?"
    emilia "Let me show you what you've paid for"
    scene v021025
    with dissolve
    "She removes her top clothing"
    emilia "Do you like me? Cat got your tongue?"
    emilia "Let me start then"
    "She moves in front of you and all of a sudden you are naked with your hard cock out"
    scene v021026
    with dissolve
    MC "How the? You sure are a professional"
    emilia "You haven't seen anything yet!"
    "She puts your cock in her mouth to prove her point"
    scene v021027
    with dissolve
    MC "Hmm so warm... So good..."
    scene v021028
    with dissolve
    MC "Ahhh... Yes..."
    scene v021027
    with dissolve
    scene v021028
    with dissolve
    scene v021027
    with dissolve
    scene v021028
    with dissolve

    scene v021029
    with dissolve
    emilia "You have a big cock!"
    "She's too good... You are almost cumming"

    menu:
        "Cum all over her face":
            scene v021029
            with dissolve
            MC "OH!! I can't hold it anymore"
            scene v021030
            with dissolve
            MC "Ahhhh!!"
            emilia "Wow"
            scene v021031
            with dissolve
            emilia "So much... Hmmm"
            MC "Phew... that was..."
            scene v021032
            with dissolve
            emilia "Great, you can come back any time"
            MC "Thanks... I need to go"
            "You dressed and left the Brothel"
            $ renpy.end_replay()
            jump allesterracitymap_v21
        "{color=#1BBB20}Hold on!!":

            scene v021029
            with dissolve
            MC "I need to hold on"
            emilia "Want to try something else?"
            MC "Yes!"
            "She positioned herself on the bed"
            scene v021033
            with dissolve
            MC "You look great Emilia"
            emilia "Are you going to do something about it or just talk?"
            MC "You little..."
            "You grab her from behind and put you cock inside her"
            scene v021034
            with dissolve
            MC "Take that!!"
            emilia "Oh... Rough... I like it!"
            "You start to move"
            scene v021035
            with dissolve
            emilia "Ahww... Yes..."
            scene v021034
            with dissolve
            MC "Hmmm that's it!"
            scene v021034
            with dissolve
            scene v021035
            with dissolve
            scene v021034
            with dissolve
            scene v021035
            with dissolve
            emilia "Let me ride you!"
            "Before you can say anything you are lying on the bed with her on top"
            scene v021036
            with dissolve
            emilia "I have to admit that you are better than I expected"
            MC "And I'm glad to hear that..."
            scene v021037
            with dissolve
            emilia "I'll start moving now"
            scene v021036
            with dissolve
            scene v021037
            with dissolve
            scene v021036
            with dissolve
            scene v021037
            with dissolve
            MC "Shit I'm cumming!!"
            emilia "Do you want to cum in my face?"
            menu:
                "Yes!!":
                    scene v021029
                    with dissolve
                    MC "OH!! I can't hold it anymore"
                    scene v021030
                    with dissolve
                    MC "Ahhhh!!"
                    emilia "Wow"
                    scene v021031
                    with dissolve
                    emilia "So much... Hmmm"
                    MC "Phew... that was..."
                    scene v021032
                    with dissolve
                    emilia "Great, you can come back any time"
                    MC "Thanks... I need to go now"
                    "You dressed and left the Brothel"
                    $ renpy.end_replay()
                    jump allesterracitymap_v21
                "I want to cum inside you!":

                    scene v021037
                    with dissolve
                    MC "OH!! I can't hold it anymore"
                    scene v021036
                    with dissolve
                    MC "Ahhhh!!"
                    emilia "Ahhh....Wow"

                    emilia "So much cum... Hmmm"
                    MC "Phew... that was..."
                    scene v021038
                    with dissolve
                    emilia "Great right? You can come back any time"
                    MC "Thanks... I need to go now"
                    "You dressed and left the Brothel"
                    $ renpy.end_replay()
                    jump allesterracitymap_v21


label tavernv21:
    if visittavern == 0:
        scene v021039
        with dissolve
        "You arrive at the tavern and you see the Tavern Keeper and a girl"
        MC "Is that the girl from before? Let's get closer"
        scene v021040
        with dissolve
        MC "Hello"
        isabella "Hi... Hey I remember you... You're that Mage right?"
        MC "Yes I am, [MC] the Mage... And your are that Demon Hunter"
        isabella "Ahahah exactly!! Isabella the Demon Hunter ahahah"
        scene v021041
        with dissolve
        keeper "A Mage and a Demon Hunter in my tavern"
        keeper "Here these are on me, drink up"
        isabella "Hey thanks!"
        MC "Thanks good sir!"
        scene v021042
        with dissolve
        isabella "I propose a toast!! Cheers!!"
        MC "Cheers!!"
        isabella "Hey [MC], let's sit at a table and talk a bit"
        MC "Sure..."
        scene v021043
        with dissolve
        "In a barely audible voice, you hear the Tavern Keeper say"
        keeper "Hey that's not fair"
        MC "What? What are you talking about?"
        keeper "I was about to make my move on this beauty"
        keeper "Then you showed up and ruined everything"
        menu:
            "Threaten him aggressively{color=#FF0000} (-1 Alignment)":

                MC "You know that I'm a Mage right?"
                keeper "Yes... And?"
                MC "And I can throw a fireball in your face or summon something to kill you?"
                keeper "I.... I'm sorry..."
                $ Points -= 1
                "You gained alignment towards evil"
                "You move to the table"
                $ visittavern = 1
            "Persuade him in a smart way":


                MC "You know that she's a Demon Hunter right?"
                keeper "Yes... And?"
                MC "They are virgins who are protected by a very powerful enchantment"
                MC "If any man tries to put his dick in her, it'll get burned to cinders"
                keeper "I...."
                MC "But hey... If you want to try your luck..."
                keeper "Shit no... I'm fine...."
                "What an idiot..."
                "You move to the table"
                $ visittavern = 2
            "Tell him he can keep her":

                MC "Don't worry, I'm not interested in her I'm just investigating the missing ship"
                keeper "Oh... Okay..."
                "You move to the table"
                $ visittavern = 3

        scene v021044
        with dissolve
        isabella "So [MC] what have you been doing? Mages stuff?"
        MC "In fact I'm investigating the missing ship"
        isabella "Yeah... I heard of it... But I know nothing of it"
        MC "That's ok, and what are you doing around here?"
        isabella "Well, I've been sensing a lot of demon activity around here"
        isabella "I haven't slept all night because I could feel some fearsome demon magic"
        MC "Really? I've faced an Imp before and it was a tough creature"
        scene v021045
        with dissolve
        isabella "Yes, Imps are very clever and persuasive but what I felt is something else"
        isabella "It's something greater than I've ever felt, I can't explain it"
        "You talked for a couple of hours"
        isabella "It was a pleasure talking with you, but I'm going to head to my room"
        isabella "Thanks for talking to me, I may have relaxed enough to sleep now"
        MC "My pleasure, I should go too"
        jump allesterracitymap_v21
    else:
        scene v2102
        with dissolve
        "You are at the Tavern"
        scene v2103
        with dissolve
        if visittavern == 1:
            keeper "Hey, please I don't want no trouble ok?"
            keeper "I made a mistake I'm sorry..."
            MC "Yeah yeah... Weakling... I'm out of here"
            jump allesterracitymap_v21
        elif visittavern == 2:
            keeper "Hey, thanks for the tip. If I tried to hit on that girl"
            keeper "I would be charcoal by now..."
            MC "No problem, just glad to help"
            "You left the tavern"
            jump allesterracitymap_v21
        else:
            keeper "Hey that girl is sleeping here on the room"
            keeper "I'll try my moves on her tomorrow, heheeh'"
            MC "Yeah good luck with that"
            "You left the tavern"
            jump allesterracitymap_v21


label docksallesterrav21:
    scene v021046
    with dissolve
    if visiteddock == 0:
        $ visiteddock = 1
        "You look around and try to find clues of the missing ship"
        $ Gold += 5
        "You found 5 Gold"
        MC "No clues, but gold is always good"
        jump allesterracitymap_v21
    else:
        MC "Still no sign of the ship... Let's go back"
        jump allesterracitymap_v21

label shopv21:
    if visitedshop == 0:
        scene v021007
        with dissolve
        shop "Hello! Welcome to my shop, you are new here right?"
        shop "Can I help you with something?"
        $ visitedshop = 1
        menu:
            "{color=#1BBB20}I'm investigating the missing ship":
                shop "Really? I was expecting some merchandise from that ship"
                shop "If it doesn't show up, I'll lose some gold"
                scene v021008
                with dissolve
                shop "And if that wasn't enough, Some weird stuff is happening in my basement"
                menu:
                    "That's to bad, I got to go":
                        shop "Ok bye..."
                        jump allesterracitymap_v21
                    "{color=#1BBB20}Weird stuff? Like what?":
                        shop "Some strange noises and missing things, I don't believe in ghosts but..."
                        MC "Ghosts? I'm sure that there is another explanation..."
                        shop "I know but... I don't really know what to think..."
                        menu:
                            "I'm sure you'll find out the problem eventually":
                                shop "Yeah... I hope so..."
                                MC "Bye, see you around"
                                jump allesterracitymap_v21
                            "Do you want me to take a look?{color=#1BBB20} (+1 Alignment)":
                                scene v021009
                                with dissolve
                                shop "Really? You would do that?"
                                MC "Yeah, let me check it out"
                                $ Points += 1
                                "You gain alignment towards good"
                                shop "Great!! Just follow the stairs down"
                                jump v21basementshop
            "I was just passing by, see you around":

                shop "Ok... Bye.."
                jump allesterracitymap_v21

    elif visitedshop == 1:
        scene v021007
        with dissolve
        shop "You are back, can I help you with anything?"
        menu:
            "{color=#1BBB20}I'm still investigating the missing ship":
                shop "Really?"
                scene v021008
                with dissolve
                shop "And I'm still having problems on my basement..."
                menu:
                    "That's to bad, I got to go":
                        shop "Ok bye..."
                        jump allesterracitymap_v21
                    "{color=#1BBB20}Weird stuff? Like what?":
                        shop "Some strange noises and missing things, I don't believe in ghosts but..."
                        MC "Ghosts? I'm sure that there is another explanation..."
                        shop "I know but... I don't really know what to think..."
                        menu:
                            "I'm sure you'll find out the problem eventually":
                                shop "Yeah... I hope so..."
                                MC "Bye, see you around"
                                jump allesterracitymap_v21
                            "Do you want me to take a look?{color=#1BBB20} (+1 Alignment)":
                                scene v021009
                                with dissolve
                                shop "Really? You would do that?"
                                MC "Yeah, let me check it out"
                                $ Points += 1
                                "You gained alignment towards good"
                                shop "Great!! Just follow the stairs down"
                                jump v21basementshop

    elif visitedshop == 2:
        scene v021007
        with dissolve
        shop "Are you alright you look a bit pale? What happened down there?"
        MC "Yeah... You have a hole in the wall that should be closed"
        MC "So there are probably... Hmm... Rats entering your basement"
        shop "Thank you, I will ask someone to close it."
        shop "Here, take this as a thank you"
        $ Gold += 10
        $ visitedshop = 3
        "You received 10 Gold"
        MC "Thank you I should go now"
        "You left the shop"
        jump allesterracitymap_v21
    else:

        scene v021007
        with dissolve
        shop "Hello welcome back, still looking for that ship?"
        MC "Yeah..."
        shop "Good luck then"
        "You left the shop"
        jump allesterracitymap_v21





label v21basementshop:
    scene v021056
    with dissolve
    "You're at the basement"
    MC "Well, let's look around and see what I can find"
    scene v021057
    with dissolve

    call screen allesterracityshopbasement

label jarsshopv21:
    MC "It's just some kind of spices in jars"
    jump v21basementshop

label chestshopv21:
    if chestbasementshop == 0:
        MC "There is a book and gold inside, what should I do?"

        menu:
            AB "Random points"
            "Just read the book":
                $ dice = renpy.random.randint(1, 7)
                $ chestbasementshop = 1
                if dice == 1:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Magic and Fire?"
                    "Your Battlemagic increased"
                    $ Destpoints += 1
                    jump v21basementshop

                elif dice == 2:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of the Illusionist?"
                    "Your Illusion increased"
                    $ Iluspoints += 1
                    jump v21basementshop

                elif dice == 3:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of the Cure?"
                    "Your Healing increased"
                    $ Healpoints += 1
                    jump v21basementshop

                elif dice == 4:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Dispel?"
                    "Your Mysticism increased"
                    $ Mystpoints += 1
                    jump v21basementshop

                elif dice == 5:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Creatures of the void?"
                    "Your Summoning increased"
                    $ Summpoints += 1
                    jump v21basementshop

                elif dice == 6:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Transmutation?"
                    "Your Alteration increased"
                    $ Altepoints += 1
                    jump v21basementshop
                else:

                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Ressurrection?"
                    "Your Necromancy increased"
                    $ Necropoints += 1
                    jump v21basementshop
            "Steal the gold and read the book{color=#FF0000} (-1 Alignment/+15 Gold)":




                $ chestbasementshop = 2
                $ Gold += 15
                $ Points -= 1
                "You got 15 Gold and alignment towards evil"
                $ dice = renpy.random.randint(1, 7)

                if dice == 1:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Magic and Fire?"
                    "Your Battlemagic increased"
                    $ Destpoints += 1
                    jump v21basementshop

                elif dice == 2:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of the Illusionist?"
                    "Your Illusion increased"
                    $ Iluspoints += 1
                    jump v21basementshop

                elif dice == 3:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of the Cure?"
                    "Your Healing increased"
                    $ Healpoints += 1
                    jump v21basementshop

                elif dice == 4:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Dispel?"
                    "Your Mysticism increased"
                    $ Mystpoints += 1
                    jump v21basementshop

                elif dice == 5:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Creatures of the void?"
                    "Your Summoning increased"
                    $ Summpoints += 1
                    jump v21basementshop

                elif dice == 6:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Transmutation?"
                    "Your Alteration increased"
                    $ Altepoints += 1
                    jump v21basementshop
                else:

                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Ressurrection?"
                    "Your Necromancy increased"
                    $ Necropoints += 1
                    jump v21basementshop
            "Do nothing":

                MC "I'm here to find the problem, nothing else"
                jump v21basementshop
    else:
        MC "There is nothing else inside"
        jump v21basementshop

label bottlesshopv21:
    MC "A lot of wine bottles, no time to drink though..."
    jump v21basementshop

label bookshopv21:
    MC "It's a book with some merchant records, nothing relevant...."
    jump v21basementshop

label holewallshopv21:
    if holewallshop == 0:
        MC "This looks empty, all the drawers are... Wait..."
        MC "What's behind it..."
        scene v021058
        with dissolve
        MC "Now that's a big hole in the wall"
        MC "Should I take a peak inside?"
        menu:
            "{color=#1BBB20}Yes":
                $ holewallshop = 1
                MC "Let's try to find out what's inside"
                "You start to hear something, and then you see..."
                scene v021059
                with dissolve
                MC "What the hell is that?!"
                scene v021060
                with dissolve
                "In a split second, that thing shocked you"
                scene black
                if Points >= 0:
                    daug "Daddy? Are you alright?"
                    scene v021068
                    show blink3

                    show blink2

                    hide blink3
                    with dissolve
                    show blink1

                    hide blink1
                    with dissolve
                    MC "What? Where the?...."
                    daug "Did you see my spell?"
                    MC "What? What spell?"
                    scene v021069
                    with dissolve
                    daug "You didn't see it?? Why??!! You told me to show you!!"
                    MC "Mida? Is that you? What is happening?"
                    scene v021070
                    with dissolve
                    daug "Have you been drinking daddy? You know that Mom is in classes"
                    daug "Can I show you my summoning skills or what?"
                    MC "Ok... I guess..."
                    daug "You are acting strange... Oh well... Let me show you what I know"
                    scene v021071
                    with dissolve
                    daug "Lagartius Gigantus"
                    scene v021072
                    with dissolve
                    daug "There you go!"
                    MC "Holy shit!! She's amazing!! Can she control it?"
                    scene v021073
                    with dissolve
                    daug "What do you think daddy? Am I good or what?"
                    MC "That's amazing!! You are quite skilled, I wish I could do something like that"
                    daug "Ahahahah, yeah sure... The great Archmage isn't able to do such a simple spell..."
                    daug "But thanks for the motivation"
                    MC "The great what?"
                    jump outofdreamv21
                else:





                    lili "Master? Are you alright?"
                    scene v021061
                    show blink3

                    show blink2

                    hide blink3
                    with dissolve
                    show blink1

                    hide blink1
                    with dissolve
                    MC "What? Where the?...."
                    scene v021062
                    with dissolve
                    lili "Master? What's wrong?"
                    MC "Master? I... Liliana? Where are we?"
                    scene v021063
                    with dissolve
                    lili "Ok Master, we will play that game, we are in your castle"
                    lili "Oh great and powerful [MC] Ruler of Ataegina!"
                    MC "Is this a joke? What is happening?"
                    lili "You called me master, to satisfy you I believe..."
                    "What is happening here?"
                    lili "Do you want me to satisfy your needs master?"
                    menu:
                        "{color=#1BBB20}If you insist...":
                            scene v021066
                            with dissolve
                            lili "You're so hard for me already Master"
                            MC "You know what to do..."
                            scene v021067
                            with dissolve
                            lili "Yes I do... Shall I start?"
                            jump outofdreamv21
                        "No, leave me alone!":

                            scene v021064
                            with dissolve
                            lili "Oh....Ok...."
                            lili "I'll leave Master..."
                            scene v021065
                            with dissolve
                            MC "What the hell is this place? Why did she called me master?"
                            jump outofdreamv21
            "No":


                MC "I'm not putting my head in there..."
                jump v21basementshop
    else:
        MC "Should I take a peak inside?"
        menu:
            "{color=#1BBB20}Yes":
                MC "Let's try to find out what's inside"
                "You start to hear something, and then you see..."
                scene v021059
                with dissolve
                MC "What the hell is that?!"
                scene v021060
                with dissolve
                "In a split second, that thing shocked you"
                scene black
                if Points >= 0:
                    daug "Daddy? Are you alright?"
                    scene v021068
                    show blink3

                    show blink2

                    hide blink3
                    with dissolve
                    show blink1

                    hide blink1
                    with dissolve
                    MC "What? Where the?...."
                    daug "Did you see my spell?"
                    MC "What? What spell?"
                    scene v021069
                    with dissolve
                    daug "You didn't saw it?? Why??!! You told me to show you!!"
                    MC "Mida? Is that you? What is happening?"
                    scene v021070
                    with dissolve
                    daug "Have you been drinking daddy? You know that Mom is in classes"
                    daug "Can I show you my summoning skills or what?"
                    MC "Ok... I guess..."
                    daug "You are acting strange... Oh well... Let me show you what I know"
                    scene v021071
                    with dissolve
                    daug "Lagartius Gigantus"
                    scene v021072
                    with dissolve
                    daug "There you go!"
                    MC "Holy shit!! She's amazing!! Can she control it?"
                    scene v021073
                    with dissolve
                    daug "What do you think daddy? Am I good or what?"
                    MC "That's amazing!! You are quite skilled, I wish I could do something like that"
                    daug "Ahahahah, yeah sure... The great Archmage isn't able to do such a simple spell..."
                    daug "But thanks for the motivation"
                    MC "The great what?"
                    jump outofdreamv21
                else:


                    lili "Master? Are you alright?"
                    scene v021061
                    show blink3

                    show blink2

                    hide blink3
                    with dissolve
                    show blink1

                    hide blink1
                    with dissolve
                    MC "What? Where the?...."
                    scene v021062
                    with dissolve
                    lili "Master? What's wrong?"
                    MC "Master? I... Liliana? Where are we?"
                    scene v021063
                    with dissolve
                    lili "Ok Master we will play that game, we are in your castle"
                    lili "Oh great and powerful [MC] Ruler of Ataegina!"
                    MC "Is this a joke? What is happening?"
                    lili "You called me master, to satisfy you I believe..."
                    "What is happening here?"
                    lili "Do you want me to satisfy your needs master?"
                    menu:
                        "{color=#1BBB20}If you insist...":
                            scene v021066
                            with dissolve
                            lili "You're so hard for me already Master"
                            MC "You know what to do..."
                            scene v021067
                            with dissolve
                            lili "Yes I do... Shall I start?"
                            jump outofdreamv21
                        "No, leave me alone!":

                            scene v021064
                            with dissolve
                            lili "Oh....Ok...."
                            lili "I'll leave Master..."
                            scene v021065
                            with dissolve
                            MC "What the hell is this place? Why did she called me master?"
                            jump outofdreamv21
            "No":
                jump v21basementshop

label outofdreamv21:
    scene v021074
    with dissolve
    $ visitedshop = 2
    MC "I... Now that was a weird dream..."

    MC "But... I feel... stronger"
    $ Destpoints += 1
    $ Iluspoints += 1
    $ Healpoints += 1
    $ Mystpoints += 1
    $ Summpoints += 1
    $ Altepoints += 1
    $ Necropoints += 1
    "All your skills improved"
    MC "Let's check that hole again"
    scene v021058
    with dissolve
    "You look inside the hole"
    scene black
    with dissolve
    MC "It's all dark, that strange thing is gone"
    scene v021057
    with dissolve
    MC "I should go talk with the Shop Keeper"
    jump shopv21


label cityguildv21:
    scene v021005
    with dissolve
    if cityguild == 0:
        $ cityguild = 1
        scene v021005
        with dissolve
        guildm "Who are you? New around here?"
        MC "You can say that..."
        guildm "And what brings you here? Work? Vacation? The brothel?"
        MC "I'm [MC], a Mage from the College"
        MC "I'm looking for the missing ship, so I'm asking around for clues"
        guildm "Yes... The ship is missing, it's quite a strange event..."
        guildm "Maybe I can help you, I know a guy that owns a small boat, I'll ask him"
        MC "Great, thank you!!"
        guildm "Hey! Do you care to help me with something? There have been some reports..."
        guildm "Really weird reports... About the graveyard... Care to check it out?"
        if visitedgraveyard == 0:
            MC "The Graveyard? Sure, I can take a look at it"
            guildm "Great!! See you later then"
            jump allesterracitymap_v21
        else:
            MC "I was there but the gates are locked and I can't get in"
            guildm "Hmmm, I think I have the key somewhere, I'll look for it"
            guildm "Return later please"
            $ gravekey = 1
            "You left the City Guild "
            jump allesterracitymap_v21



    elif gravekey == 1:
        MC "Yes, have you found the key to the graveyard?"
        if visitedshop == 1:
            scene v021006
            with dissolve
            guildm "Yes, here you go"
            "You received the key to the graveyard"
            $ gravekey = 2
            MC "I'll return with news"
            jump allesterracitymap_v21
        else:
            if gravekey == 2:
                guildm "You are back, have you checked the graveyard?"
                menu:
                    "Yes I have" if visitedgraveyard == 3:
                        guildm "And? Found anything?"
                        MC "Yes....I found"
                        menu:
                            "{color=#1BBB20}Tell the truth":
                                MC "There was a Necromancer doing experiments with the corpses"
                                guildm "What??!! That's... Terrible... I need to find a way to deal with it"
                                jump v21laststage
                            "Lie":

                                MC "It was just some kids playing in the graveyard scaring people..."
                                guildm "Kids?! Ahahah... And we were expecting something dangerous, ahaha"
                                jump v21laststage
                    "No I haven't":

                        guildm "Ok, tell me if you find something"
                        jump allesterracitymap_v21
            else:
                guildm "Found anything in the graveyard?"
                MC "I was there but the gates are locked and I can't get in"
                guildm "Hmmm, I think I have the key somewhere..."
                guildm "Ahh... here it is. There, take it"
                guildm "Tell me when you get news"
                $ gravekey = 2
                "You left the City Guild "
                jump allesterracitymap_v21

    elif gravekey == 2:
        guildm "You are back, have you checked the graveyard?"
        menu:
            "Yes I have" if visitedgraveyard == 3:
                guildm "And? Found anything?"
                MC "Yes....I found"
                menu:
                    "{color=#1BBB20}Tell the truth":
                        MC "There was a Necromancer doing experiments with the corpses"
                        guildm "What??!! That's... Terrible... I need to find a way to deal with it"
                        jump v21laststage
                    "Lie":

                        MC "It was just some kids playing in the graveyard scaring people..."
                        guildm "Kids?! Ahahah... And we were expecting something dangerous, ahaha"
                        jump v21laststage
            "No I haven't":

                guildm "Ok, tell me if you find something"
                jump allesterracitymap_v21
    else:



        MC "I was at the graveyard but the gates are locked and I can't get in"
        guildm "Hmmm, I think I have the key somewhere, I'll look for it"
        guildm "Return later please"
        $ gravekey = 1
        "You left the City Guild "
        jump allesterracitymap_v21









label graveyardv21:
    scene v021047
    with dissolve
    "You're at the graveyard"
    if visitedgraveyard == 3:
        scene v021104
        with dissolve
        MC "there is nothing to see here"
        jump allesterracitymap_v21
    else:

        menu:
            "{color=#1BBB20}Try to open the gates":
                if visitedgraveyard == 0:
                    MC "Let's get inside"
                    "You try to open the gates but they're locked"
                    MC "No other way inside, I need to find a way through the Cemetery Gates"
                    MC "Someone in this city might know a way inside"
                    $ visitedgraveyard = 1
                    jump graveyardv21

                elif gravekey == 2:
                    MC "Let's get inside"
                    "You use the key to open the gates"
                    jump v21necrofight
                else:

                    MC "Let's get inside"
                    "You try to open the gates but they're locked"
                    MC "No other way inside, I need to find a way through the Cemetery Gates"
                    MC "Someone in this city might know a way inside"
                    $ visitedgraveyard = 1
                    jump graveyardv21
            "Leave":

                jump allesterracitymap_v21



label v21necrofight:
    scene v021010
    with dissolve
    "You look around the graveyard and you spot some guy dressed in black"
    MC "What the hell is that guy doing?"
    scene v021011
    with dissolve
    "A skeleton is being raised from it's grave"
    MC "Holy shit, he's a necromancer!!"
    scene v021012
    with dissolve
    MC "Is he targeting me? Bring it on!"
    scene v021013
    with dissolve
    "The necromancer turns away"
    MC "Hey wait!!"
    scene v021014
    with dissolve
    "The skeleton starts to charge you!"
    MC "Shit... what should I do?"
    menu:
        "Use Destruction{color=#1BBB20} (+1 Destpoint) {image=001battle}" if Destpoints >= 2:
            scene v021014
            with dissolve
            "You cast a Fireball that hits the skeleton"
            scene v021015dest
            with dissolve
            MC "Take that!!"
            scene v021016
            with dissolve
            "The skeleton stays motionless on the ground"
            MC "That was...Easy..."
            $ Destpoints += 1
            "Your Destruction skill improved"

            jump v21afterskeleton

        "Use Summoning{color=#1BBB20} (+1 Summpoint) {image=001summon}" if Summpoints >= 2:
            scene v021014
            with dissolve
            "You use Unsummon on the skeleton"
            scene v021015summ
            with dissolve
            MC "Take that!!"
            scene v021017
            with dissolve
            "The skeleton stays static and lifeless... Like it should..."
            MC "That was...Easy..."
            $ Summpoints += 1
            "Your Summoning skill improved"

            jump v21afterskeleton

        "Use Alteration{color=#1BBB20} (+1 Altepoint) {image=001alteration}" if Altepoints >= 2:
            scene v021014
            with dissolve
            "You cast Petrification on the skeleton"
            scene v021015alter
            with dissolve
            MC "Take that!!"
            scene v021017
            with dissolve
            "The skeleton is turned to stone, rendering it lifeless"
            MC "That was...Easy..."
            $ Altepoints += 1
            "Your Alteration skill improved"

            jump v21afterskeleton

        "Use Ilusion{color=#1BBB20} (+1 Iluspoint) {image=001illusion}" if Iluspoints >= 2:
            scene v021014
            with dissolve
            "You use fear on the skeleton"
            scene v021015
            with dissolve
            MC "Take that!!"
            scene v021016
            with dissolve
            "The skeleton is scared to death, again. It lays motionless."
            MC "That was...Easy..."
            $ Iluspoints += 1
            "Your Ilusion skill improved"

            jump v21afterskeleton

        "Use Mysticism{color=#1BBB20} (+1 Mystpoint) {image=001myst}" if Mystpoints >= 2:
            scene v021014
            with dissolve
            "You use Telekinesis on the skeleton"
            scene v021015
            with dissolve
            MC "Take that!!"
            "You toss it up in the air"
            scene v021016
            with dissolve
            "The skeleton slams to the ground and no longer moves"
            MC "That was...Easy..."
            $ Mystpoints += 1
            "Your Mysticism skill improved"

            jump v21afterskeleton

        "Use Healing{color=#1BBB20} (+1 Healpoint) {image=001heal}" if Healpoints >= 2:
            scene v021014
            with dissolve
            "You use Cure on the skeleton"
            scene v021015heal
            with dissolve
            MC "Let's hope this works...."
            scene v021017
            with dissolve
            "The skeleton is cured of it's undeath and falls down"
            MC "That was...Easy..."
            $ Healpoints += 1
            "Your Healing skill improved"

            jump v21afterskeleton

        "Use Necromancy{color=#1BBB20} (+1 Necropoint) {image=001necro}" if Necropoints >= 2:
            scene v021014
            with dissolve
            "You use Control Undead on the skeleton"
            scene v021015necro
            with dissolve
            MC "Ahhh... This is hard!!"
            scene v021016
            with dissolve
            "The skeleton falls to the ground lifeless..."
            MC "I... almost gained control of it..."
            $ Necropoints += 1
            "Your Necromancy skill improved"

            jump v21afterskeleton

label v21afterskeleton:
    $ visitedgraveyard = 3
    scene v021104
    with dissolve
    MC "I should talk with the Guild Master now"
    jump allesterracitymap_v21

label v21laststage:
    scene v021005
    with dissolve
    guildm "Well, a deal is a deal, and my friend just arrived"
    scene v021006
    with dissolve
    guildm "Here he comes"
    scene v021048
    with dissolve
    guildm "Hey Shinji, this is the guy I told you about"
    shinji "You're the one who is looking for the missing ship?"
    MC "Yes I am, do you know something about it?"
    shinji "Just that the fisherman are saying that all the fish disapeared"
    shinji "And there is a report that the ship is a couple of miles from the shore"
    MC "But why?"
    shinji "Nobody knows... But I have a boat if you want to go and check it out"
    shinji "My friend here told me you helped him, so..."
    scene v021049
    with dissolve
    guildm "You go with him [MC], good luck finding the boat"
    shinji "Let's go!"
    "You follow Shinji to the docks"
    scene v021050
    with dissolve
    shinji "So my boat is down there, just a few more steps"
    scene v021051
    with dissolve
    shinji "Here it is, so what do you think?"
    MC "Well... That's not exactly what I was expecting"
    shinji "Well, good luck finding the ship"
    MC "You're not coming with me?"
    shinji "Ahahah, I'm not crazy, if the fish are gone, some shit's about to happen"
    scene v021052
    with dissolve
    shinji "Good luck young Mage"
    MC "I guess it's just me then...."
    "You entered the boat and started rowing to the sea"
    scene v021053
    with dissolve
    MC "They said the ship was a few miles from the shore"
    MC "What's that ?"
    "You row a little more until you find the ship"
    scene v021054
    with dissolve
    MC "This must be it, but everything looks ok..."
    scene v021055
    with dissolve
    MC "I need to get up there and find out what's going on"
    "You climb up the ship and find two guys staring at you"
    scene v021081
    with dissolve
    shipcapt "Who the hell are you? And what the hell are you doing on my ship?"
    MC "I'm [MC] and Runar sent me to find this ship"
    shipcapt "What?? That is nonsense!! You lie!!"
    sailor "Should I beat him up captain?"
    scene v021080
    with dissolve
    shipcapt "Wait, It was Lord Runar that told us to stay here"
    shipcapt "So that the merchandise we carry gets more valuable"
    MC "What? Then why...?"
    shipcapt "It doesn't matter, we are going to kill you anyway"
    scene v021082
    with dissolve
    MC "What the hell is that?"
    shipcapt "Ahahah nice try, you think we'll fall for that?"
    scene v021083
    with dissolve
    scene v021084
    with dissolve
    MC "Ohhhh SHIT!!!"
    play sound "sounds/adamastor.wav"
    "All of a sudden a massive creature rises from the sea"
    scene v021085
    with dissolve
    "The whole ship looks like a toy for the creature"
    scene v021087
    with dissolve
    MC "What the fuck is this thing??!!"
    play sound "sounds/adamastor.wav"
    "With a demonic voice you hear the creature"
    adamastor "Puny humans!!! With puny toys!!"
    adamastor "Come here little one"
    scene v021088
    with dissolve
    sailor "Ahhhhhhhhhhh!! Help me!!!"
    scene v021089
    with dissolve
    adamastor "Hmmmm... Tasty, but I need more!!"
    scene v021090
    with dissolve
    adamastor "How about you??"
    MC "OH fuck!! I need to do something"
    MC "I can't move... What is happening?"
    adamastor "I see... You are the one they told me about, I feel magic in you"
    adamastor "Let me show you real power"
    scene v021086
    with dissolve
    adamastor "See?? This is real power!!! And now..."
    scene v021091
    with dissolve
    adamastor "Time to kill you all!!"
    scene v021092
    with dissolve
    MC "I can't move!!! Shit!! Is this his doing?"
    MC "I guess this is the end for me...."
    scene v021093
    with dissolve
    play sound "sounds/explosionayna.wav"
    "BOOOOMM!!" with hpunch
    adamastor "Ahhhhhrg!"
    MC "Who?"
    scene v021094
    with dissolve
    MC "Is that the Archmage?? Amazing!!"
    scene v021095
    with dissolve
    "The massive creature deflects the fireball"
    adamastor "Who dares to attack me???!!"
    adamastor "You... I feel so much magic in you...."
    scene v021096
    with dissolve
    ayna "Stop this, you foul Demon!"
    adamastor "Make me puny wench!!"
    scene v021097
    with dissolve
    "The great Demon tries to grab the Archmage "
    "But she dodges it by levitating from her dragon"
    "With some kind of force field around her"
    adamastor "Prepare to die!!"
    scene v021098
    with dissolve
    play sound "sounds/explosionayna.wav"
    "BOOOOM!!!" with hpunch
    adamastor "Ahhhhhrg!!"
    MC "Who did that?!"

    scene v021099
    with dissolve
    Bredita "Need a hand?"
    ayna "I won't say no... Look at this creature"
    Bredita "I'm sure this was the Devil Siblings doing..."
    ayna "Indeed, I felt that they were summoning something powerful"
    adamastor "Who are you two??!!"
    adamastor "How dare you?? I'm going to kill you both!!"
    Bredita "Let's give him a taste of our power!"
    ayna "Let's do it!"
    scene v021100
    with dissolve
    ayna "AHHHH!!!"
    Bredita "YAHHH!!"
    adamastor "I'll kill you!!"
    scene v021101
    with dissolve
    adamastor "Ahhhhhhhh!"
    scene v021102
    with dissolve
    MC "So much power!!"
    scene v021103
    with dissolve
    MC "OH Shit!!"
    play sound "sounds/explosionayna.wav"
    "BOOOOM!!" with hpunch
    scene black
    with dissolve
    MC "What happened? Am I dead?"
    MC "I can't be... Can I?"
    jump v25
