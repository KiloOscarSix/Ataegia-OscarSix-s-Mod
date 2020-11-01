label v026evil:

    if midaowner == 1:
        $ midaown = 1
    elif midaowner == 3:
        $ midaown = 1
    elif midaowner == 5:
        $ midaown = 1

    elif midaowner == 2:
        $ midaown = 2
    elif midaowner == 4:
        $ midaown = 2
    elif midaowner == 6:
        $ midaown = 2

    if midaown == 2:
        scene v25136
        with dissolve
        MC "I'm back in my room, Bredita said she would call me in a moment"
        MC "I wonder what she's doing with Mida..."
        Bredita "I hope you rested enough with these five minutes"
        scene v3e010
        with dissolve
        "You turn around and see Bredita close to your bed"
        MC "Ahah yeah sure..."
        scene v3e011
        with dissolve
        Bredita "So ready to take on a mission? Not that you have a choice..."
        MC "In that case of course I'm ready..."
        Bredita "Good...."
        scene v3e012
        with dissolve
        Bredita "I need someone capable doing this, so Liliana will tag along with you"
        MC "Don't you trust my skills?"
        scene v3e013
        with dissolve
        Bredita "Oh I trust them... That's exactly why she is coming with you"
        Bredita "I can't afford to lose my pretty boy"
        Bredita "Now follow me please..."
        scene black
        with dissolve
    else:

        scene v3e001
        with dissolve
        MC "I'm back in my room, Bredita said she would call me in a moment"
        MC "Let's talk with Mida before she shows up"
        scene v3e002
        with dissolve
        MC "So what are you reading?"
        amida "Just some spells..."
        MC "That's my girl, always trying her best"
        scene v3e003
        with dissolve
        amida "I try, but you seem to get all the attention everytime..."
        menu:
            "You get all my attention dear[ablovecolor] [ablove]":
                $ midalove +=1
                amida "Aww... Such a gentleman..."
                "Mida likes you more"
            "What can I say? I'm the best":
                amida "Ahahah you have such an ego..."

        scene v3e004
        with dissolve
        MC "Can I get a nice kiss?"
        amida "I don't know... What have you done to deserve it?"
        MC "Do I have to deserve kisses now?"
        scene v3e005
        with dissolve
        "Before you can say anything else she kisses you"
        amida "Mhuwaa"
        Bredita "I hope I'm not interrupting anything..."
        scene v3e006
        with dissolve
        amida "...."
        scene v3e007
        with dissolve
        Bredita "Look at this gorgeous girl..."
        Bredita "It's like she was handcrafted to perfection"
        Bredita "I see why you decided to keep her"
        scene v3e008
        with dissolve
        Bredita "But if you want you can still play with me sometime girl..."
        amida "I...."
        Bredita "I'm sure [MC] wouldn't mind if I participated in some of your..."
        scene v3e009
        with dissolve
        Bredita "... Activities... Right [MC]?"
        menu:
            "Of course... I'm sure it would be fun...[abcorruptioncolor] [abmidabreditalovecorruption]":
                $ midacorr +=1
                $ breditalove +=1
                "Mida corruption increased, Bredita likes you more"
            "That's something that she should decide not me[ablovecolor] [abmidalove]":
                $ midalove +=1
                "Mida likes you more"
        scene v3e008
        with dissolve
        Bredita "Anyway, we must leave this for another time..."
        scene v3e009
        with dissolve
        Bredita "[MC] follow me I have an assignment for you"
        MC "Very well..."
        scene black
        with dissolve




    scene v3e014
    with dissolve
    "You follow Bredita until you reach some kind of dungeon"
    MC "Why are we here? Isn't this the place where I woke up?"
    Bredita "Questions, questions..."
    Bredita "Just be quiet for a moment and observe"
    scene v3e015
    with dissolve
    "She points to one of the cells and you see some kind of creature"
    MC "What or who is that?"
    Bredita "That my cute boy, is {color=#f00}Wrath{/color}"
    MC "Wrath? what kind of name is that?"
    scene v3e016
    with dissolve
    Bredita "He is also the supreme lord of Andarth the 4th hell"
    MC "What? 4th hell? How did you trap him?"
    scene v3e015
    with dissolve
    Bredita "Let's just say he is part of a special group..."
    Bredita "And their strength is also their weakness..."
    scene v3e017
    with dissolve
    "You see the devil sitting after hearing Bredita..."
    Bredita "So this one has a lot of wrath, but as you can see..."
    Bredita "He is mine now..."
    scene v3e018
    with dissolve
    "You are a bit shocked by this..."
    "If this is true, Bredita is even more powerful than you imagined"
    MC "And why are you showing me this?"
    Bredita "Because your mission is about him"
    MC "What? How?"
    Bredita "Follow me, I don't want him to hear this"
    scene black
    with dissolve
    "You followed her to a room upstairs"
    scene v3e019
    with dissolve
    "Liliana is there waiting for you two"
    MC "Hello Liliana..."
    lili "Hey there"
    Bredita "Now that we've all been polite, let's talk about important things"
    scene v3e020
    with dissolve
    lili "Of course mistress, what do you need us to do"
    Bredita "I need you to travel to Memia's mountain, one of us is there"
    Bredita "But she stopped sending news, so I need you both to check it out"
    scene v3e019
    with dissolve
    MC "You said earlier that it has to do with that devil..."
    Bredita "You and the questions... I guess it's a good thing to be curious.."
    Bredita "I'm trying to understand how the devils get their power"
    Bredita "And if I can use it somehow."
    Bredita "As you know, we get our power from Allesterium..."
    Bredita "But what about them?"
    scene v3e020
    with dissolve
    lili "I'm ready to go mistress"
    Bredita "Very well, take good care of [MC] here, he's a special boy"
    scene v3e021
    with dissolve
    lili "Very well, let's go"
    Bredita "You behave [MC], Liliana is a cute girl but she is all mine"
    "She winks and doesn't look serious at all"
    scene black
    with dissolve
    scene v3e022
    with dissolve
    "You follow Liliana through a passage that leads to a cliff"
    MC "So what now?"
    scene v3e023
    with dissolve
    lili "Now I summon a massive creature to rape you!"
    MC "What?!"
    lili "Ahahaha you should have seen your face!"
    MC "That's not funny...."
    lili "Then why am I laughing? Ahaha"
    MC "Shouldn't we get going?"
    lili "Ok ok... Special boy is all serious, no time for humor..."
    "She has a unique sense of humor, you have to admit"
    scene v3e024
    with dissolve
    lili "Let's get going then..."
    "You can feel that she is casting something"
    scene v3e025
    with dissolve
    MC "What the hell? Is that a giant housefly?"
    scene v3e026
    with dissolve
    lili "I told you I was summoning something to rape you..."
    MC "And you chose a housefly?"
    lili "Would you prefer to be raped by something else?"
    menu:
        "I'm not a fan of being raped really[ablovecolor] [ablove]":
            lili "Ahahaha you can be funny after all"
            $ lililove += 1
            "Liliana likes you more"
        "I wouldn't mind being raped by you...[abcorruptioncolor] [abcorruption]":
            lili "Ahahah you can be funny after all"
            $ lilicorr += 1
            "Liliana corruption increased"

    scene v3e027
    with dissolve
    "She mounted the creature"
    MC "Are we traveling on that?"
    scene v3e028
    with dissolve
    lili "What? Are you afraid?"
    MC "No... I just wasn't expecting this..."
    lili "I'm sorry I can't summon a dragon, your Highness"
    lili "Maybe you can show us how to summon a great flying creature..."
    MC "Alright, I'm sorry... Let's go"
    scene v3e029
    with dissolve
    "You mount the giant insect and grab Liliana by the waist"
    "You can feel her body pressed against yours"
    lili "Hope you're ready..."
    scene v3e030
    with dissolve
    "In the next moment you are both flying over the forest at great speed"
    lili "I wish I had some other creature capable of flying us around though"
    lili "Flies don't like the cold very much"
    "After what felt like an hour"
    lili "We are close, which is good, this fly can't take the cold anymore"
    scene v3e031
    with dissolve
    "You land at a snow covered place"
    scene v3e032
    with dissolve
    lili "Here we are... Hmmf.. It's cold here..."
    MC "Can't you summon a coat or something?"
    lili "Ahaha funny... Bye fly..."
    scene v3e033
    with dissolve
    lili "Now we need to find what we are looking for"
    MC "And I'm sure you have something up your sleeve?"
    lili "I always have something up my sleeve"
    scene v3e034
    with dissolve
    "Once again you can feel power coming out of her"
    scene v3e035
    with dissolve
    "You know it's summoning magic, but it feels different"
    scene v3e036
    with dissolve
    lili "There we go..."
    MC "Nice... Is that some kind of dog or wolf?"
    scene v3e037
    with dissolve
    lili "It's a special creature I created, I can teach you when you have the power"
    MC "That would be great"
    scene v3e038
    with dissolve
    lili "Now boy, look for people please"
    scene v3e039
    with dissolve
    lili "He found something, let's go!"
    MC "That was fast"
    scene v3e040
    with dissolve
    "You reach a cave inside the mountain"
    lili "Looks like this is the place"
    $ lilitalkv3 = 0
label lilitalkv3evil:
    scene v3e041
    with dissolve

    menu:
        "What are we looking for again?":
            lili "Weren't you paying attention to mistress?"
            lili "We are looking for someone, a girl I guess"
            jump lilitalkv3evil
        "What do you think about Bredita?":

            lili "What do you mean? I think she is great!"
            lili "She may look scary, I mean, I know she is scary"
            lili "I know that what you learn in College always mentions her as evil"
            lili "But she's not heartless, maybe a bit evil but I'm sure she has her reasons"
            lili "She is probably the strongest person you'll ever meet"
            lili "Once I saw her dominate two devils alone..."
            MC "Devils? Like the one she has on the dungeon?"
            lili "Yes... But I believe these two were stronger... Can't really say..."
            $ lilitalkv3 = 1
            MC "That's amazing... She mentioned that Wrath was the lord of the 4th hell"
            MC "Maybe those two were lords of other hells?"
            lili "They could be, I can't really tell, but that makes sense"
            jump lilitalkv3evil
        "Why are you following Bredita?":

            lili "What kind of question is that? Because she is amazing!"
            lili "Why are you following her?"
            jump lilitalkv3evil

        "Let's move on" if lilitalkv3 == 1:
            lili "Let's go"

    lili "He will stay here guarding the entrance while we go inside"
    scene v3e042
    with dissolve
    lili "Look at this crap... Doesn't look like someone would be around here..."
    lili "Hey what the hell is that?!"
    scene v3e043
    with dissolve
    MC "Oh shit... giant spiders.."
    $ enemy = "Giant Spider"
    $ companion = 1
    $ companion_name = "Liliana"
    jump combat
label killedgspiderv03:
    hide screen MC_bars
    hide screen hpbar
    scene v3e044
    with dissolve
    lili "You are stronger than I expected, not bad"
    lili "Let's keep moving"
    scene v3e045
    with hpunch
    lili "Look out!!!"
    scene v3e045
    with vpunch
    scene v3e045
    with hpunch
    MC "Shit!!"
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    scene black
    with hpunch

    scene v3e046
    with hpunch
    MC "Ah... My head... Where the hell am I?"
    lili "[MC]?! Can you hear me?"
    MC "Yes!!"
    lili "You fell through a hole, try to find a way out!"
    lili "I'll try to find a way to get to you"
    MC "Guess I'm alone now... Let's try to find a way out"
    $ companion = 0
label v3cave_evil:
    scene v3evilcave_00

    call screen v3evilcave

label v03evilzombie:
    scene v3e047
    with dissolve
    "As you are looking around you see an undead coming towards you"
    MC "Ah fuck..."
    $ enemy = "Undead"
    jump combat

label killedundeadv3e:
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    hide screen MC_bars
    hide screen hpbar
    scene v3e048
    with dissolve
    MC "Take that you bastard"
    MC "I need to keep looking around..."
    jump v3cave_evil

label v03evilnecrom:
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    scene black
    with dissolve
    "You find some stairs that lead up, you climb them"
    scene v3e049
    with dissolve
    "You reach some kind of ancient ruins and you can see someone"
    MC "Who is that? It can't be who we are looking for"
    MC "Bredita said she was a girl..."
    scene v3e050
    with dissolve
    MC "Is that a naked girl there?"
    Nonen "I've spent almost all my power on you..."
    Nonen "But it was worth it... Now with your sacrifice I'll have great powers"
    Nonen "Now I'll become the... What... How long will you hide over there?"
    "Is he talking to you?"
    scene v3e051
    with dissolve
    scene v3e052
    with dissolve
    "He is..."
    MC "Oh shit..."
    Nonen "I may have spent a lot of power but I can still crush an insect like you"
    MC "Let's find out shall we?"
    scene v3e053
    with dissolve
    $ enemy = "Necromancer"
    jump combat

label Necromancerendv3e:
    hide screen MC_bars
    hide screen hpbar
    scene black
    with dissolve
    nvl clear

    n "Since you won, you can choose a skill to upgrade"

    menu:
        "Raise Battlemagic[abgreen] [abdestpoint] {image=001battle}":
            $ Destpoints += 1
            "Your Battlemagic skill improved"
            jump postcombatskillsv3e
        "Raise Summoning[abgreen] [absummpoint] {image=001summon}":

            $ Summpoints += 1
            "Your Summoning skill improved"
            jump postcombatskillsv3e
        "Raise Alteration[abgreen] [abaltepoint] {image=001alteration}":

            $ Altepoints += 1
            "Your Alteration skill improved"
            jump postcombatskillsv3e
        "Raise Illusion[abgreen] [abiluspoint] {image=001illusion}":

            $ Iluspoints += 1
            "Your Illusion skill improved"
            jump postcombatskillsv3e
        "Raise Mysticism[abgreen] [abmystpoint] {image=001myst}":

            $ Mystpoints += 1
            "Your Mysticism skill improved"
            jump postcombatskillsv3e
        "Raise Healing[abgreen] [abhealpoint] {image=001heal}":

            $ Healpoints += 1
            "Your Healing skill improved"
            jump postcombatskillsv3e
        "Raise Necromancy[abgreen] [abnecropoint] {image=001necro}":

            $ Necropoints += 1
            "Your Necromancy skill improved"
            jump postcombatskillsv3e

label postcombatskillsv3e:
    scene v3e054
    with dissolve
    Nonen "You... are stronger than I anticipated..."
    Nonen "You ruined may have ruined my plans, but I'll make you pay..."
    scene v3e055
    with dissolve
    Nonen "Do you hear ME?! YOU WILL PAY!!"
    "Is he getting ready to fight again? You're spent.."
    scene v3e056
    with dissolve
    Nonen "Bye...."
    scene v3e057
    with dissolve
    MC "Did he just jump?"
    MC "He's gone..."
    scene v3e058
    with dissolve
    MC "This must be the girl we are looking for..."
    MC "What just happened here?"
    scene v3e059
    with dissolve
    MC "She looks familiar somehow... What should I do?"
    MC "Should I try to heal her or take the opportunity to play with her body?"
    menu:
        "Try to heal her[abgreen] [abalignment]":
            scene v3e060
            with dissolve
            MC "Let's try to heal her..."
            MC "I can't, did I spend all my energy with that guy?"
            $ Points += 1
            "You gained 1 point"
            MC "Let's carry her to a more comfortable place"
        "Play with her body[abred] [abnoalignment]":


            scene v3e061
            with dissolve
            MC "Let's take this opportunity to fool around"
            MC "Look at those tits, firm..."
            $ Points -= 1
            "You lost 1 point"
            scene v3e062
            with dissolve
            MC "What about this pussy... hmm feels tight"
            scene v3e063
            with dissolve
            MC "And looks very good... let's try it out"
            scene v3e064
            with dissolve
            MC "So tight... Is she a virgin or what?"
            scene v3e065
            with dissolve
            MC "If she is, I can't wait to change that"
            scene v3e066
            with dissolve
            MC "Oh... I believe I'll have some fun"
            MC "Let's carry her to a more comfortable place"

    scene v3e067
    with dissolve
    "You grab her and start walking to some other place"
    scene v3e068
    with dissolve
    MC "Is this the place where I came from?"
    lili "I leave you alone for a moment and you already have a new girl?"
    scene v3e069
    with dissolve
    MC "Oh... Hi Liliana...I think I found who we were looking for"
    lili "Oh really? Why is she naked?"
    menu:
        "I was about to fuck her but you showed up...[abred] [abnoloveidiot]":
            scene v3e071
            with dissolve
            lili "What?! That's not funny you know?"
            $ lililove -= 1
            "Liliana likes you less"
        "I found her like this, we need to help her":

            scene v3e070
            with dissolve
            lili "Yeah right... You found her like that... Sure..."
            lili "Let's take her to Bredita then"

    scene v3e072
    with dissolve
    $ wheretoafterslayerbath = "Evil"
    lili "Let's go, shall we?"
    jump slayerbathv26

label v026evilpart2:
    scene v3e073
    with dissolve
    lili "And that's how we found her"
    Bredita "I wonder who that Mage you fought was [MC]"
    MC "I don't know... I heard him say that with her sacrifice"
    MC "He would archieve great powers..."
    Bredita "That's odd... Even for a Necromancer... Unless..."
    MC "What?"
    scene v3e074
    with dissolve
    Bredita "Nevermind, I need to take care of Aline now"
    Bredita "It's like her lifeforce was drained... I'll take it from here"
    scene v3e075
    with dissolve
    Bredita "Let's go my dear..."
    "Bredita left"
    scene v3e076
    with dissolve
    lili "We did a great job, don't you think?"
    menu:
        "I found her! I did a great job![abred] [abnoloveidiot]":
            $ lililove -= 1
            "Liliana likes you less"
            lili "Yeah... right..."
        "We make a great team together![ablovecolor] [ablove]":
            $ lililove += 1
            "Liliana likes you more"
            lili "Yes we do..."

    scene v3e077
    with dissolve
    lili "I'll see if Bredita needs some help, see you..."
    MC "Bye"
    scene v3e078
    with dissolve
    wrath "Hey kid... Come here"
    MC "Hmm? What do you want?"
    scene v3e079
    with dissolve
    wrath "Want to make a deal?"
    MC "You are the trapped one, shouldn't I be the one proposing deals?"
    wrath "Stop trying to be funny, do you want to hear my deal?"
    MC "Ok, I guess I'll hear it..."
    wrath "Right, so I need you to help me escape"
    MC "Really? Couldn't have guessed that..."
    wrath "I TOLD YOU TO STOP TRYING TO BE FUNNY!!"
    MC "Hey... Remember that you're asking for my help"
    MC "All this... {i}Wrath{/i}... isn't going to help..."
    scene v3e016
    with dissolve
    wrath "You just can't stop can you...?"
    MC "Are you going to tell me about your deal or what?"
    MC "You want to escape, so what do I get?"
    wrath "Power... Don't you want power?"
    MC "I like power, but what do you mean by power?"
    wrath "The truth is power"
    scene v3e079
    with dissolve
    MC "The truth? What do you mean?"
    wrath "The truth about you, where you came from, who you really are"
    "That's intriguing... What does he know? Is he bluffing?"
    MC "What do you know?"
    wrath "First let me out, then I tell you"
    MC "And I'm supposed to trust some demon's words?"
    wrath "I'M NOT SOME DEMON!! I'M A DEVIL!! I'M WRATH!! LORD OF THE 4TH HELL!"
    MC "Hey! You have some serious anger problems... Tell me about those hells"
    MC "How many exist? Are there other devil lords like you?"
    wrath "I told you, first you release me, then I answer your questions"
    MC "I'll think about that..."
    scene v3e078
    with dissolve
    MC "Now I need to leave, see you demon!"
    wrath "I'M NOT A DEM..."
    scene black
    with dissolve
    "You leave him alone and go looking for Bredita"
    $ liliroomv3e = 0
    $ bredroomv3e = 0
    $ dungeonroomv3e = 0
    $ yourroomv3e = 0
    $ trainingroomv3e = 0
    $ afteralinepart = 0


label travelinsidebredv3e:
    scene bredhouse00
    call screen bredhousev3e



label bredroomv3e:
    if bredroomv3e == 0:
        "The door is locked"
        MC "I don't think I should try to get in her room, that would end badly"
        jump travelinsidebredv3e
    else:
        "The door is locked"
        MC "I don't think I should try to get in her room, that would end badly"
        jump travelinsidebredv3e

label dungeonv3e:
    if afteralinepart == 0:
        scene v3e078
        with dissolve
        MC "I have nothing to do here now..."
        jump travelinsidebredv3e
    else:
        scene v3e078
        with dissolve
        MC "I have nothing to do here now..."
        jump travelinsidebredv3e

label throneroomv3e:
    if afteralinepart == 0:
        "There is nothing to see here"
        jump travelinsidebredv3e
    else:
        scene v25054
        with dissolve
        "You can see Bredita sitting on her throne"
        MC "I don't think she wants to talk right now..."
        jump travelinsidebredv3e


label trainingroomv3e:
    if afteralinepart == 0:
        scene v3e110
        with dissolve
        "You find Bredita with Liliana and the other girl"
        Bredita "There you go my dear, you are ok now"
        scene v3e111
        with dissolve
        aline "I...Mistress? What happened?"
        Bredita "I was expecting you to tell me"
        scene v3e112
        with dissolve
        aline "I... Let me try to gather my thoughts"
        aline "I was studying some demon runes, trying to understand how they work"
        aline "But then... "
        scene v3e113
        with dissolve
        aline "Hey who is that?!"
        Bredita "That's [MC], you can thank him for being alive.."
        Bredita "Let's get you some clothes first"
        scene v3e114
        with dissolve
        lili "Hope you enjoyed the view while it lasted [MC] ahaha"
        scene v3e115
        with dissolve
        Bredita "There you go..."
        aline "Thank you mistress"
        "Now that you can see her face, doesn't she reminds you of Jessica?"
        MC "Hey, I knew I've seen your face... You look like someone I know"
        aline "Really? Who would that be?"
        MC "Do you know someone called Jessica a student at Allesterra College?"
        scene v3e116
        with dissolve
        aline "I don't think so... Am I supposed to know her?"
        MC "Maybe Liliana knows her? Do you Liliana?"
        lili "I don't think so, I don't know that much about students from your generation"
        MC "Oh well... Maybe it's just a coincidence"
        Bredita "You also need some nice clothes, not that ugly thing from the College"
        Bredita "There you go!"
        "You can feel her power around you"
        scene v3e000
        with dissolve
        Bredita "Nice huh?"
        MC "Yeah...Thanks a lot"
        scene v3e116
        with dissolve
        lili "Look at the big Mage now ahaah"
        scene v3e117
        with dissolve
        aline "Thank for saving me [MC] I owe you one"
        Bredita "Are we finished here? Aline let's talk about what happened"
        aline "Yes mistress!"
        scene v3e118
        with dissolve
        "You see Bredita and Aline leave the room"
        scene v3e119
        with dissolve
        lili "Ah... Time to change my clothes and rest... See you"
        $ afteralinepart = 1
        jump travelinsidebredv3e
    if trainingroomv3e == 1:
        MC "It's locked..."
        jump travelinsidebredv3e
    else:
        if midaown == 2:
            scene v3e109
            with dissolve
            "You see Bredita and Mida practicing some spells"
            MC "I should leave, I don't want to piss off Bredita"
            $ trainingroomv3e = 1
            jump travelinsidebredv3e
        else:
            MC "It's locked..."
            $ trainingroomv3e = 1
            jump travelinsidebredv3e


label bathhousev3e:
    if afteralinepart == 0:
        "The door is locked"
        jump travelinsidebredv3e
    if afteralinepart == 1:
        "The door is locked"
        jump travelinsidebredv3e


label liliroomv3e:
    if afteralinepart == 0:
        "The door is locked"
        jump travelinsidebredv3e

    if liliroomv3e == 1:
        "The door is locked"
        jump travelinsidebredv3e

    if afteralinepart == 1:
        "The door is open"
        scene v3e120
        with dissolve
        "You can see Liliana in her room"
        "Should you talk to her?"
        menu:
            "[abgreen]Yes, talk to her":
                MC "Hey there!"
                scene v3e121
                with dissolve
                lili "Oh... Hi [MC], already missing me?"
                MC "Ahaha sure..."
                scene v3e122
                with dissolve
                lili "So what brings you here? Were you trying to spy on me?"
                MC "Well, I told you that I was here. That'd make a pretty bad spy, don't you think?"
                scene v3e123
                with dissolve
                lili "Ahaha funny... But you still haven't told me what you are doing here"
                MC "I wanted to see if everything was fine with you"
                if lililove >= 2:
                    scene v3e124
                    with dissolve
                    "Out of nowhere, Liliana kisses you"
                    lili "Mhuwaa"
                    scene v3e123
                    with dissolve
                    MC "What was that?"
                    lili "Don't you know what a kiss is? Are you a virgin?"
                    MC "That's not what I meant, why did you kiss me?"
                    lili "Because I felt like it, didn't you liked it?"
                    menu:
                        "It was nice...[ablovecolor] [ablove]":
                            scene v3e125
                            with dissolve
                            lili "Ahahah you're cute"
                            scene v3e124
                            with dissolve
                            lili "Mhuwaa"
                            $ lililove += 1
                            "Liliana likes you more now"
                            scene v3e123
                            with dissolve
                            lili "You should leave now though..."
                            scene v3e125
                            with dissolve
                            lili "And don't look back I'm going to change now..."
                            "Funny girl...."
                            "As you leave her room you look one last time"
                            scene v3e127
                            with dissolve
                            "And you notice that she is already naked..."
                            lili "I said don't look back, didn't I?"
                            MC "Right... Sorry..."
                            lili "Bye..."
                            MC "Crazy girl..."
                            $ liliroomv3e = 1
                            jump travelinsidebredv3e
                        "Don't do it ever again!":

                            scene v3e126
                            with dissolve
                            $ lililove = 0
                            $ lilicorr = 0
                            "Liliana love and corruption are now 0"
                            lili "Then what the hell are you doing in my room?!"
                            lili "Get the hell out!"
                            MC "Geez... Sorry..."
                            $ liliroomv3e = 1
                            jump travelinsidebredv3e
                else:
                    lili "Yes it is, I need to rest now see you tomorrow"
                    MC "Ok... Bye"
                    $ liliroomv3e = 1
                    jump travelinsidebredv3e
            "No, leave the room":

                MC "I should leave"
                jump travelinsidebredv3e

label yourroomv3e:
    if afteralinepart == 0:
        scene v25136
        with dissolve
        MC "This is my room.."
        if midaown == 1:
            MC "I wonder were Mida is, she was here before..."
            jump travelinsidebredv3e
        else:
            MC "I should look for Bredita"
            jump travelinsidebredv3e
    if afteralinepart == 1:
        if midaown == 2:
            scene v25136
            with dissolve
            MC "Well I'm back here, maybe I should sleep now"
            jump devilsv3all
        else:
            scene v3e080
            with dissolve
            "Mida is sitting on the bed"
            scene v3e081
            with dissolve
            MC "Hey, you look worried... What the matter?"
            amida "I... I'm scared..."
            scene v3e082
            with dissolve
            amida "That woman is Bredita, isn't she?"
            MC "Yes she is, but don't believe everything you've been told about her"
            amida "I don't like the way she looks at me..."
            menu:
                "I would never let anything happen to you![ablovecolor] [ablove]":
                    scene v3e083
                    with dissolve
                    amida "Oh [MC] my love... Thank you..."

                    $ midalove +=1
                    "Mida likes you more"
                    amida "You know what I want now?"
                    MC "Hmmm... Do I get a hint?"
                    scene v3e084
                    with dissolve
                    amida "How's this for an hint?"
                    MC "Perfect hint! So I take it you want to walk around the castle?"
                    amida "Ahahah funny..."
                    menu:
                        "I'm sorry, but I'm a bit tired for this, I need to sleep":
                            scene v3e085
                            with dissolve
                            amida "Hmmm... Ok... let me blow out the candles and we can go to sleep"
                            scene black
                            with dissolve
                            $ renpy.end_replay()
                            jump devilsv3all
                        "{color=#1BBB20}Can I get a kiss?":
                            scene v3e086
                            with dissolve
                            amida "Mhwaa!"
                            "She kisses you, you can feel all her passion"
                            scene v3e087
                            with dissolve
                            MC "You are so beautiful..."
                            MC "Can you lay down for me?"
                            scene v3e088
                            with dissolve
                            "She lies on the bed exposing her pink pussy"
                            amida "Like this?"
                            MC "Perfect..."
                            scene v3e089
                            with dissolve
                            "You get closer and can see her pussy with better detail"
                            MC "Beautiful..."
                            scene v3e090
                            with dissolve
                            "You started to put a finger inside her"
                            "You could feel her trembling with your touch"
                            MC "Time to please you with my tongue"
                            scene v3e091
                            with dissolve
                            "You start to lick her pussy"
                            "You can taste the bittersweet fluids coming out"
                            scene v3e092
                            with dissolve
                            amida "Ah... Yes.... Keep it up..."
                            "You start to move your tongue faster and deeper"
                            scene v3e093
                            with dissolve
                            amida "Ah!!! Yes!! That's it!"
                            amida "It's my turn to please you"
                            scene v3e096
                            with dissolve
                            "You sit on the edge of the bed with Mida grabbing your cock"
                            scene baseforhjevil

                            show v03ehj idle
                            "She starts to stroke your dick"
                            MC "Hmmmm yes...."
                            scene v3e096
                            with dissolve
                            MC "That feels so good..."
                            scene baseforhjevil

                            show v03ehj2 idle
                            MC "Ahhh...."
                            amida "You like this?"
                            MC "I love it!"
                            scene v3e096
                            with dissolve

                            scene baseforhjevil
                            show v03ehj3 idle
                            MC "Ahhhh.... that's it keep going..."
                            amida "You look so cute like this"
                            scene v3e096
                            with dissolve
                            amida "Lie on the bed now"
                            "You comply"
                            scene v3e095
                            with dissolve
                            "You are now laying on the bed with Mida in front of you"
                            amida "I want to taste it now"
                            scene v3e094
                            with dissolve
                            MC "Ahhhh yes..."
                            "You can feel her tongue moving everywhere"
                            scene v3e095
                            with dissolve
                            amida "Are you enjoying this my love?"
                            MC "Hum hum...."
                            scene v3e097
                            with dissolve
                            "She then rotates her body, aligning her pussy with your dick"
                            MC "I guess you need a little help now"
                            scene v3e098
                            with dissolve
                            "You grab your dick, pointing it to her pussy"
                            scene v3e099
                            with dissolve
                            amida "Ahhh.....Yes..."
                            MC "Hmm.... You feel amazing..."
                            scene v3e100
                            with dissolve
                            "She then starts to move, she is so eager right now"
                            amida "Oh yes, yes..."
                            MC "Oh baby..."
                            amida "Let me change my position again"
                            scene v3e101
                            with dissolve
                            "She is now facing you in cowgirl style"
                            scene v3e102
                            with dissolve
                            "You start to move your hips faster and faster"
                            amida "Ahhh yes! Yes... Go on!"
                            scene v3e103
                            with dissolve
                            "You try even faster and deeper"
                            amida "Ahhhhh! I'm cumming!! Ahhh!"
                            "You can feel her cum but your are not stopping"
                            amida "Ahhh! Yes! Give me more! Fuck me harder!"
                            "You grab her by her waist and throw her on the bed"
                            scene v3e104
                            with dissolve
                            "On all fours"
                            amida "Ahh!! Yes harder! Faster!!"
                            scene basefordsevil
                            show v03eds idle
                            amida "Ahhhh!!!!! I'm cumming again!"
                            amida "Ahhhhhhhhh!"
                            "You can feel her cumming and that brings you to the edge"
                            scene v3e104
                            with dissolve
                            MC "Ahhhh! I'm about to cum!"
                            menu:
                                "Cum inside":

                                    MC "Ahhhhh! Cumming!"
                                    show shot
                                    with hpunch
                                    scene v3e104
                                    with dissolve
                                    amida "Ahhh! I can feel you filling me, it's so warm...."
                                    "You then colapse on the bed"
                                "Pull out":
                                    show shot
                                    with hpunch
                                    scene v3e105
                                    with dissolve
                                    MC "Ahhh! Yeah..."
                                    scene v3e106
                                    with dissolve
                                    "You covered her back with your cum"
                                    "Then you colapse on the bed"

                            scene v3e107
                            with dissolve
                            amida "Are you ok?"
                            MC "Oh believe me, I am....."
                            scene v3e108
                            with dissolve
                            amida "This was so good.... I need to sleep now"
                            MC "Yeah... I could use some sleep too..."
                            scene black
                            with dissolve
                            $ renpy.end_replay()
                            jump devilsv3all
                "Deal with it! I can't be saving you all the time":

                    scene v3e081
                    with dissolve
                    amida "...."
                    $ midalove -=1
                    "Mida likes you less"
                    amida "I think I should go to sleep now..."
                    MC "Yeah... me too..."
                    scene black
                    with dissolve
                    $ renpy.end_replay()
                    jump devilsv3all
