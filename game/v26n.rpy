label v026neutral:
    scene black
    with dissolve
    scene v26n001
    with dissolve
    isabella "Yawn..... What are you doing?"
    isabella "Is it morning already?"
    MC "Well not exactly..."
    scene v26n003
    with dissolve
    isabella "What's wrong? You look strange"
    menu:
        "[abgreen]It's nothing I just couldn't sleep":
            scene v26n003
            with dissolve
            isabella "Well, shall we move on then?"
            isabella "Let me get ready...."
            scene v26n002
            with dissolve
            isabella "Will you wait for me outside?"
            MC "Sure thing, take your time"
        "There was some weird mage outside that attacked me":

            scene v26n002
            with dissolve
            isabella "What?!! Let's find him then!!"
            MC "Don't worry I kicked his ass and he ran..."
            isabella "Oh fine... But I wanted to kick some ass too"
            isabella "Let me get ready for our journey then"
            isabella "Wait for me outside, please"
            MC "Sure thing, take your time"

    scene black
    with dissolve
    scene v25096
    with dissolve
    MC "So are you ready to go?"
    isabella "I'm ready, let's go!"
    scene v26n004
    with dissolve
    isabella "The tavern keeper said that there is a fisherman that may rent us his boat"
    MC "He also said that it will take a few hours to get there..."
    scene v26n005
    with dissolve
    isabella "Is that supposed to scare me?"
    MC "What? Are you even scared of anything?"
    scene v26n004
    with dissolve
    isabella "Hehe... Well..."
    isabella "Anyway, we don't have time to waste..."
    isabella "You said it yourself we have a few hours of walking ahead of us"
    scene v26n006
    with dissolve
    MC "Very well, let's move"
    "You both walk for a few hours and find the boat"
    scene v26n007
    with dissolve
    isabella "That has to be what we are looking for"
    isabella "Let's see if we can find the fisherman"
    scene v26n008
    with dissolve
    "Isabella starts to move ahead of you"
    MC "Damn where does she get all this energy? Then again, she actually slept..."
    scene v26n009
    with dissolve
    "All of a sudden Isabella stops moving"
    MC "Why are we...."
    scene v26n011
    with dissolve
    isabella "Shhhh..."
    MC "???"
    isabella "Be quiet, look"
    scene v26n012
    with dissolve
    "She points to something inside the boat"
    scene baseboatani
    show v26npboat idle
    show isa01
    isabella "Do you really want to interrupt them?"
    MC "I...."
    hide isa01
    show isa02
    isabella "We should let them finish... We don't want them to get mad"
    hide isa02
    show isa03
    isabella "Let's wait for them over there"
    MC "Sure..."
    hide isa03
    show isa01
    isabella "Or do you want to watch them?"
    MC "I.. No... Let's wait for them over there"
    isabella "You look cute when you blush...."
    scene v26n013
    with dissolve
    "You and Isabella wait for a while on a rock nearby"
    isabella "Let's go find out if they are done"
    scene v26n014
    with dissolve
    MC "Very well..."
    "You follow her in the boat's direction"
    scene v26n015
    with dissolve
    "You can see the couple from before, already dressed and talking"
    isabella "Looks like they're finished"
    scene v26n016
    with dissolve
    isabella "Hello there!"
    karl "Hmmm? Oh Hello..."
    scene v26n017
    with dissolve
    isabella "I'm Isabella and this is [MC] we are looking for a boat to rent"
    karl "Nice to meet you, I'm Karl and this is Miss Petra"
    karl "Her husband also needs my boat that's why she's here"
    "Yeah right..."
    isabella "We really need that boat today...."
    petra "Oh... Hmmm... My husband will only need it next week"
    petra "So I guess Karl here could rent it until then"
    karl "I could but I need to remove all the stuff that I have inside"
    karl "Come to my place to eat and rest a bit"
    "You and Isabella follow the couple inside a house nearby"
    scene v26n018
    with dissolve
    petra "So are you two traveling some place important?"
    isabella "Not really, we just wanted to do a little lovers getaway together"
    petra "Isn't that cute? That's really romantic..."
    karl "Yes... Feel free to sit there and eat some fruit, I'll get the boat ready to sail"
    scene v26n019
    with dissolve
    "You and Isabella sit at the table"
    isabella "I don't trust them... They are very strange..."
    menu:
        "[abgreen]Indeed the way they act is very odd...":
            isabella "Maybe it's because she is cheating on her husband?"
            MC "I guess it could be that, who knows"
        "It's probably nothing, just surprised we showed up when we did":

            isabella "Yeah... I wouldn't want to be in her husband's shoes..."

    isabella "I'm starving let's eat!"
    scene v26n020
    with dissolve
    isabella "It's funny though, they are fearless..."
    isabella "Having sex outside, risking being caught"
    MC "If they really are who they said, yes... But it could be a lie..."
    scene v26n021
    with dissolve
    isabella "Yes, that's true... But hey I just want the boat"
    MC "That's why you also lied?"
    scene v26n020
    with dissolve
    isabella "What? For saying that we were on a romantic trip?"
    MC "Yes..."
    isabella "That was to see how they would react, I have armor equiped"
    isabella "Why would we have a romantic trip wearing armor?"
    "This girl is smart"
    isabella "Still they asked no questions, so they must be hiding something"
    MC "Like her cheating on her husband..."
    isabella "Exactly..."
    petra "Is everything fine?"
    scene v26n022
    with dissolve
    MC "Hi Petra"
    isabella "Yes! Thank you for the fruit"
    petra "No problem... I mean Karl is very hospitable"
    MC "Is your husband ok with you being away for so long?"
    scene v26n023
    with dissolve
    petra "I..."
    "Isabella is looking at you with a serious face"
    "You need to say something"
    MC "I mean... I would be worried if my cute wife here were away for so long..."
    "Petra smiled and turned away"
    scene v26n024
    with dissolve
    "Isabella changed her expression to surprise"
    petra "Anyway, Karl said that the boat is ready for you two, meet us outside"
    "She left you and Isabella alone"
    scene v26n020
    with dissolve
    isabella "Ehehe you were bold there... Let's meet them outside"
    "You and her move outside"
    scene v26n025
    with dissolve
    karl "Well I got everything ready for you, removed everything that you won't need"
    karl "And got everything mounted to sail at will"
    MC "Thank you very much"
    karl "No problem, it will be 20 gold coins per day, and I need two days in advance, so 40"
    menu:
        "Wait to see what Isabella does":
            scene v26n026
            with dissolve
            isabella "Of course, here you go"
            karl "Thank you my lady"
        "[abgreen]Offer to pay it yourself":

            scene v26n027
            with dissolve
            MC "I got this"
            if Gold <=39:
                MC "Oh... I don't have enough"
                scene v26n026
                with dissolve
                isabella "I got this, here you go"
                karl "Thank you my lady"
            else:
                $ Gold -= 40
                $ isabellalove += 2
                karl "Thank you kind sir"
                "Isabella likes you more"
        "[abgreen]Offer to pay half":

            scene v26n027
            with dissolve
            MC "We split it!"
            if Gold <=19:
                MC "Oh... I don't have enough"
                scene v26n026
                with dissolve
                isabella "I got this, here you go"
                karl "Thank you my lady"
            else:
                $ Gold -= 20
                $ isabellalove += 1
                karl "Thank you kind sir"
                "Isabella likes you more"

    scene v26n025
    with dissolve
    karl "Go on, get on the boat!"
    scene v26n028
    with dissolve
    "You and Isabella get onboard and Karl pushes the boat to the sea"
    isabella "I feel that we will find my mother soon"
    MC "That's great, can't wait to meet her"
    isabella "I'm sure you will like her"
    scene v26n029
    with dissolve
    "You travel for a couple of hours"
    "You notice that Isabella looks a bit concerned"
    menu:
        "[abgreen]Talk with her":
            MC "Hey Isabella!"
            scene v26n031
            with dissolve
            isabella "Hmm? Sorry... I was distracted..."
            MC "Is everything ok?"
            scene v26n030
            with dissolve
            isabella "Honestly... I'm a bit worried about my mother..."
            MC "I'm sure she is fine and we will find her in no time"
            scene v26n031
            with dissolve
            isabella "I know... But... She has suffered so much already..."
            isabella "We lost all our family and friends and I was just a child..."
            isabella "She had to take care of me all by herself..."
            MC "She can't be the only one who suffered, I bet you feel just as hurt"
            isabella "Yes... My little brother and my father are gone..."
            menu:
                "You still have her and she still has you, hold to that[ablovecolor] [ablove]":
                    scene v26n034
                    with dissolve
                    isabella "You're right... I should be happy that I still have her"
                    isabella "Thank you for that thought"
                    $ isabellalove += 1
                    "Isabella likes you more"
                "Well I lost everyone and you don't see me cry[abred] [abnoloveidiot]":

                    scene v26n035
                    with dissolve
                    isabella "..."
                    isabella "I guess you're right..."
                    $ isabellalove -= 1
                    "She doesn't seem pleased, she likes you less now"
        "Don't talk with her":



            scene v26n030
            with dissolve
            Isabella "This should take a while..."

    scene v26n033
    with dissolve
    isabella "Hey [MC] I need to meditate a bit, take care of the boat please"
    MC "Sure, don't worry"
    scene v26n034
    with dissolve
    isabella "Thank you"
    scene v26n037
    with dissolve
    "She sits on the deck"
    scene v26n038
    with dissolve
    "She then closes her eyes and starts to meditate"
    "After some time you start to feel sleepy"
    MC "{i}Yawn{/i}.... Shit... I can feel my eyes trying to close"
    MC "Let me sit here for a moment"
    "You try to keep your eyes open but eventually fall asleep"
    scene black
    with dissolve

    isabella "Hey [MC] wake up!"
    scene v26n039
    with dissolve
    MC "Hmmm? Where are we?"
    isabella "What do you mean? We've arrived"
    MC "Arrived where? Is that a Slayer soldier?"
    scene v26n040
    with dissolve
    isabella "Be quiet... Of course it's a Slayer soldier"
    isabella "And we need to get inside that building, I think my mother is in there"
    MC "Ok... What's the plan then?"
    isabella "Distract him, I'll find a way in"
    scene v26n041
    with dissolve
    MC "Wait I... She's gone..."
    MC "Guess I have to distract that guy"
    scene v26n042
    with dissolve
    "As you get closer to the soldier he stares at you"
    scene v26n043
    with dissolve
    sol "Get lost kid!! You are not allowed inside!"
    menu:
        "Tell him a joke":
            scene v26n042
            with dissolve
            MC "Wait listen to this one!"
            MC "I once brought a jackass and a honeycomb into a brothel..."
            scene v26n045
            with dissolve
            sol "Ahahahah.... Stop it... Ahahaha"
            MC "But I haven't finished yet..."
            "Before you could say anything else"
        "[abgreen]Use Illusion to trick him {image=001illusion}":



            MC "What are you talking about? I'm your Commander!!"
            if Iluspoints >= 5:
                scene v26n044
                with dissolve
                sol "I'm... I'm... Sorry Commander..."
                MC "Get the hell out of my way!!"
                sol "Yes sir"
                scene v26n046
                with dissolve
                "As the soldier prepares to run"
            else:

                scene v26n045
                with dissolve
                sol "Ahahah yeah... And I'm the Emperor ahahaha"
                "Before you could do anything else"

    scene v26n047
    with dissolve
    "Isabella shows up and kills the soldier"
    MC "What the...?"
    stop music

    scene v26n048
    with dissolve
    isabella "That one won't bother us anymore, shall we...?"
    play music "<loop 0.0>vampsong.mp3" fadein 5
    goggos "What do we have here?"
    scene v26n049
    with dissolve
    isabella "What... Who said that? I feel..."
    scene v26n050
    with dissolve
    goggos "My power? Is that what you feel? Let me help you then..."
    scene v26n051
    with dissolve
    goggos "Ahhhhh ahahahah"
    isabella "Run [MC]!!! He's a devil.... We are no match for him!!"
    goggos "Ahahahah"
    scene v26n052
    with dissolve
    goggos "Going somewhere you two?"
    scene v26n053
    with dissolve
    goggos "Take this!!"
    scene v26n053
    with hpunch
    "The Devil throws a punch at Isabella, but she is able to block it"
    scene v26n054
    with dissolve
    "But the impact is so powerful you are thrown far away"
    "You can see Isabella being dominated by the creature..."
    goggos "Let's have some fun shall we?"
    scene v26n055
    with dissolve
    goggos "How lucky am I? Finding one of the best Demon Hunters here..."
    goggos "And such a cute one.... Hmm I'm going to enjoy this so much..."
    scene v26n056
    with dissolve
    goggos "Look at those tits... Hmmm firm..."
    isabella "I... Stop.... cough cough...."
    MC "Stop this right now!!"
    scene v26n057
    with dissolve
    goggos "And you are?... Wait... You..."
    goggos "You are him! Ahahaha how lucky am I... Ahahaha"
    goggos "Time to end this!!"
    scene v26n058
    with dissolve
    goggos "DIE!!!!"
    stop music
    scene black
    with dissolve
    isabella "[MC]! [MC] are you okay?"
    play music "<loop 0.0>ingame.mp3"
    scene v26n059
    with dissolve
    MC "What?!!"
    isabella "Are you okay? I was worried... I was meditating then I heard you scream"
    "You are still in shock and speechless"
    scene v26n060
    with dissolve
    isabella "There... Calm down... Everything is fine"
    scene v26n061
    with dissolve
    isabella "So what happened? Nightmare?"
    MC "Yes... a terrible nightmare"
    MC "There was this devil...."
    scene v26n062
    with dissolve
    isabella "A devil? Don't worry it was just a dream"
    scene v26n061
    with dissolve
    isabella "Everything's ok now..."
    isabella "Well, almost... we have a leak on the boat so we need to stop soon"
    scene v26n036
    with dissolve
    isabella "There is a village over there. We should stop and fix the boat"
    "She sails to the shore"
    scene v26n063
    with dissolve
    isabella "Here we are!"
    "You both leave the boat"
    scene v26n064
    with dissolve
    villager "You should leave this place!"
    isabella "Hey calm down, we just need to fix our boat and we'll be on our way"
    scene v26n065
    with dissolve
    villager "I'm sorry, that's not what I meant... If you stay here you'll be in danger"
    isabella "Why? What's the matter?"
    villager "We are being attacked by vampires"
    MC "Vampires?!"
    scene v26n066
    with dissolve
    villager "Yes... vampires"
    MC "But it's daytime... Vampires don't walk in sunlight..."
    scene v26n065
    with dissolve
    villager "Not right now... But every night we are attacked"
    villager "Every night they attack and take some of us to turn into vampires"
    menu:
        "We can help you[abgreen] [abalignment]":
            scene v26n066
            with dissolve
            villager "Really how??"
            MC "We can handle anything"
            scene v26n065
            with dissolve
            isabella "That's right! We can take care of those things"
            $ Points +=1
            "You gained 1 point"
        "Say nothing":

            isabella "We can help you guys! Me and my friend here are capable fighters"
            scene v26n066
            with dissolve
            isabella "Right [MC]? We can handle this!"
            MC "Sure...."

    scene v26n065
    with dissolve
    villager "That's great!! Follow me then!! You need to meet Alice"
    scene v26n067
    with dissolve
    "You follow the villager"
    scene v26n068
    with dissolve
    alice "Who are these people?"
    villager "They said they will help us fight the vampires"
    alice "Really? How?"
    MC "If we kill the Master all of them go away"
    alice "And how do you plan to do that?"
    MC "Do you know where their nest is?"
    alice "I have an idea..."
    alice "Follow me please"
    scene v26n069
    with dissolve
    isabella "You seem to know your stuff. Learn that at the Mages College?"
    MC "Yes, we have an extensive library. Shall we go?"
    scene v26n070
    with dissolve
    alice "Warn everyone, assume defensive positions, they will arrive in a couple of hours"
    villager "Very well!"
    scene v26n071
    with dissolve
    alice "Outside the village you'll see a mountain, that's where we believe they hide"
    alice "Be careful they are very strong and very fast..."
    scene v26n072
    with dissolve
    isabella "So are we!"
    MC "Yes, we can handle it, don't worry"
    scene v26n073
    with dissolve
    alice "If you say so... So let me explain it to you"
    "You listen to Alice for a few minutes and she tells you everything she knows"
    MC "Ok I think I got it, shall we go Isabella?"
    isabella "Sure! Let's kill some vampires"
    "You leave the village"

    $ v26mountcount = 0
    $ dice = renpy.random.randint(1, 2)

label travelvampmap:
    scene vampland01
    with dissolve

    call screen vamplandv26

label villagev026:
    scene v26n073
    with dissolve
    alice "You are back! Have you found anything?"
    MC "No not yet..."
    scene v26n072
    with dissolve
    isabella "But we will! Let's go [MC]"
    "You leave the village"
    jump travelvampmap

label forest1v026:
    scene v26n112
    with dissolve
    isabella "There must be a way to the mountains here, should we look around?"
    menu:
        "[abgreen]Yes let's look around":
            $ dice = renpy.random.randint(1, 8)
            if dice <= 2:
                scene v26n113
                with dissolve
                "A giant frost spider appeared"
                isabella "Oh shit, look out!"
                $ enemy = "Frost Spider"
                $ companion = 1
                $ companion_name = "Isabella"
                jump combat

            elif dice >= 6:
                scene v26n115
                with dissolve
                isabella "We can't find anything and it's too cold"
                isabella "Let's leave please, I'm freezing"
                jump travelvampmap
            else:

                scene v26n114
                with dissolve
                isabella "Look!! we can pass there! Let's go!"
                "You can now move to the mountain"
                $ v26mountcount = 1
                jump travelvampmap
        "No, let's look some place else":



            jump travelvampmap


label forest0v026:
    "That forest is on the other side of the river..."
    "We can't go there..."
    jump travelvampmap

label riverv026:
    scene v26n112
    with dissolve
    isabella "This is a nice place, look the River is almost frozen solid!"
    isabella "Do you want to look around?"
    menu:
        "[abgreen]Yes, let's see what we can find":
            $ dice = renpy.random.randint(1, 4)
            if dice >= 3:
                scene v26n113
                with dissolve
                "A giant frost spider appeared"
                isabella "Oh shit, look out!"
                $ enemy = "Frost Spider"
                $ companion = 1
                $ companion_name = "Isabella"
                jump combat
            else:

                scene v26n115
                with dissolve
                isabella "We can't find anything and it's too cold"
                isabella "Let's leave please, I'm freezing"
                jump travelvampmap
        "No, let's go some place else":

            jump travelvampmap

label mountainv026:
    if v26mountcount == 0:
        "You need to find a way to the mountains first"
        jump travelvampmap
    scene v26n114
    with dissolve
    isabella "There seems to be an entrance there, should we look inside?"
    menu:
        "[abgreen]Yes! Let's go":
            jump vampiresnestv026
        "No, let's look some place else":

            jump travelvampmap

label killedspiderv026:
    hide screen MC_bars
    hide screen hpbar
    scene v26n115
    with dissolve
    isabella "Damned Spiders... They give me the chills..."
    isabella "Let's get the hell out of here"
    $ companion = 0
    $ companion_name = 0
    jump travelvampmap

label vampiresnestv026:
    scene v26n074
    with dissolve
    isabella "It's so dark in here..."
    MC "Let me fix that"
    scene v26n075
    with dissolve
    "You cast Magelight"
    scene v26n076
    with dissolve
    isabella "Wow! that was cool!"
    scene v26n077
    with dissolve
    isabella "What other tricks do you have up your sleeve?"
    MC "Well I know my way around..."
    isabella "Heheh sure..."
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    vampire "What do we have here??"
    scene v26n078
    with dissolve
    isabella "Who said that?!"
    "In a split second Isabella takes her knife out"
    scene v26n079
    with dissolve
    "And gets ready for battle"
    "There are many of them around you..."
    isabella "You want to fight!?"
    scene v26n080
    with dissolve
    vampire "You are the ones trespassing in our territory..."
    vampire "You are the ones looking for a fight!"
    vampire "We have lived over 100 years, do you think you stand a chance?"
    menu:
        "Fight them!":
            MC "You are going down!!"
            scene v26n081
            with dissolve
            "You and Isabella start to fight the vampires"
            "But then..."
            scene v26n081
            with hpunch
            scene black
            with dissolve
            "You are knocked unconscious"
        "[abgreen]Surrender":


            MC "They are right... We can't beat them..."
            vampire "You're smarter than you look, follow me"
            scene v26n082
            with dissolve
            "You and Isabella are taken by the vampires"
            "But then..."
            scene v26n082
            with hpunch
            scene black
            with dissolve
            "You are knocked unconscious"

    scene v26n083
    with dissolve
    "When you come to your senses you are locked somewhere"
    MC "Ah... My head.... Where am I.... Where is Isabella?!"
    vampire "Oh... you are awake!"
    scene v26n084
    with dissolve
    "The door opens and one of them enters"
    vampire "I'm a bit hungry... What do you say?"
    MC "What? I'm not giving you my blood!"
    vampire "You say that... like you have a choice, ahahaha"
    $ vampcount = 0
    menu:
        "[abgreen]Where is Isabella?":
            vampire "You should worry about yourself now..."
            $ enemy = "Vampire"
            scene v26n085
            with dissolve
            jump combat
        "Come get my blood then!":

            vampire "Oh... So cute..."
            $ enemy = "Vampire"
            scene v26n085
            with dissolve
            jump combat

label vampirejailv026:
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    hide screen MC_bars
    hide screen hpbar
    $ vampcount = 1
    scene v26n086
    with dissolve
    "You see the vampire disintegrate in front of you"
    MC "Fucking bastards... I need to find Isabella!"
    scene v26n087
    with dissolve
    MC "The door is open, let's go"
    scene v26n088
    with dissolve

label jaildoorsv26:
    menu:
        "Try the door on the right":
            "It's locked, and looks like an empty cell"
            jump jaildoorsv26
        "[abgreen]Try the door to the front":
            "You open the door to the front"
            jump jaildoorsv26x

label jaildoorsv26x:
    scene v26n089
    with dissolve
    vampire "What the fuck??!!"
    $ enemy = "Vampire"
    jump combat

label vampireoutjailv026:
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    hide screen MC_bars
    hide screen hpbar
    scene v26n090
    with dissolve
    "The vampire disintegrates in front of you"
    MC "Die bastard!"
    scene v26n088
    with dissolve

label jaildoorsv26xx:
    menu:
        "Try the door on the right":
            "It's locked, and looks like an empty cell"
            jump jaildoorsv26xx
        "[abgreen]Try the door to the front":
            "You open the door to the front"
            jump jaildoorsv26xxx

label jaildoorsv26xxx:

    scene v26n091
    with dissolve
    "You reach a very large room"
    "You see a naked woman casting a spell"
    scene v26n092
    with dissolve
    "And then she notices you"
    mvamp01 "Look what we have here...."
    mvamp01 "How did you get here? Who are you?"
    MC "Where is Isabella? Who are you?"
    mvamp01 "I believe I asked first? Is Isabella that cute blondie?"
    mvamp01 "Are you the boy that came with her? Ahahah"
    MC "Where is she?"
    mvamp01 "You know, girls are very rare around here..."
    mvamp01 "And my men need to have fun sometimes"
    MC "You will pay for that!!"
    scene v26n093
    with dissolve
    mvamp01 "We shall see, child!"
    $ enemy = "MVampire"
    "You can feel her power grow, this is not going to be easy..."
    jump combat

label MVampireendv26:
    hide screen MC_bars
    hide screen hpbar
    scene black
    with dissolve
    nvl clear
    n "Since you won, you can choose a skill to upgrade"
    nvl clear

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
    label galleryScene2:
    scene v26n094
    with dissolve
    mvamp01 "How?!!... Could you? You're really powerful..."
    mvamp01 "Now I see how you managed to reach me..."
    scene v26n095
    with dissolve
    mvamp01 "Please don't kill me... I'll do anything you want..."
    mvamp01 "I'll set your friend free... I'll even show you a nice spell"
    scene v26n095
    with dissolve
    mvamp01 "I'll do anything if you let me go"
    $ mvampiredead = 0
    menu:
        "[abgreen]Anything?":

            mvamp01 "Yes..."
            "She gets close to you and removes your robe"
            scene v26n099
            with dissolve
            "Then she gets on her knees..."
            mvamp01 "Wow... Look what we have here..."
            menu:
                "[abgreen]What are you waiting for?":
                    scene v26n100
                    with dissolve
                    mvamp01 "Hmmm... Such a large dick we have here..."
                    mvamp01 "I bet it's also tasty..."
                    scene v026up
                    show v26nvampup idle
                    mvamp01 "Hmmm"
                    MC "Yeah that's it...."
                    scene v26n102
                    with dissolve
                    mvamp01 "Hmmm..."
                    MC "Time to go deeper!!"
                    scene v026side
                    show v26nvampside idle
                    MC "That's it...."
                    mvamp01 "Mhmmmhm"
                    MC "Deeper!!"
                    scene v26n103
                    with dissolve
                    MC "Ahh!! Yes... I'm about to..."
                    scene v26n103
                    show shot
                    with hpunch
                    scene v26n104
                    with dissolve
                    MC "Ahhhhh!"
                    show shot
                    with hpunch
                    scene v26n105
                    with dissolve
                    MC "Shit..... That was great..."
                    scene v26n096
                    with dissolve
                    "You're still recovering from your orgasm"
                    "And you see the Vampire run away.."
                    menu:
                        "Kill her![abred] [abnoalignment]":
                            MC "Oh no you don't bitch!"
                            $ mvampiredead = 1
                            $ Points -= 1
                            scene v26n097
                            with dissolve
                            "You attack her and see her disintegrate in front of you"
                            "You lost 1 Point"
                            jump isabellav026vamps
                        "Let her go":


                            "You let her go"
                            jump isabellav026vamps
                "What are you doing? Get the hell out!!":

                    scene v26n096
                    with dissolve
                    "You see her run away"
                    menu:
                        "Kill her!":
                            MC "Oh no you don't bitch!"
                            $ mvampiredead = 1
                            scene v26n097
                            with dissolve
                            "You attack her and see her disintegrate in front of you"
                            jump isabellav026vamps
                        "Let her go":

                            "You let her go"
                            jump isabellav026vamps
        "You will die!!":
            scene v26n096
            with dissolve
            "You see her run away"
            menu:
                "Kill her!":
                    MC "Oh no you don't bitch!"
                    $ mvampiredead = 1
                    scene v26n097
                    with dissolve
                    "You attack her and see her disintegrate in front of you"
                    jump isabellav026vamps
                "Let her go":

                    "You let her go"
                    jump isabellav026vamps
        "Teach me that spell and go!":

            mvamp01 "Very well come here"
            scene v26n098
            with dissolve
            mvamp01 "Here on this book you will find a spell called 'Minor Drain Life'"
            mvamp01 "During a fight it will damage your opponent and heal you"
            "You start to look at the book"
            scene v26n096
            with dissolve
            "And you see her run away"
            menu:
                "Kill her![abred] [abnoalignment]":
                    MC "Oh no you don't bitch!"
                    $ Points -= 1
                    $ mvampiredead = 1
                    scene v26n097
                    with dissolve
                    "You attack her and see her desintegrate in front of you"
                    "You lost 1 Point"
                    jump isabellav026vamps
                "Let her go":

                    "You let her go"
                    jump isabellav026vamps

label isabellav026vamps:
    $ renpy.end_replay()
    scene v26n106
    with dissolve
    "After a few moments, you see Isabella entering the room"
    scene v26n107
    with dissolve
    isabella "What the hell happened?!"
    MC "I could ask you the same!"

    if mvampiredead == 1:
        isabella "I was surrounded by dozens of those guys"
        isabella "But out of nowhere they all disintegrated..."
    else:

        isabella "I was surrounded by dozens of those guys"
        isabella "But out of nowhere they all ran away..."

    isabella "Did you take care of the Master?"
    MC "You could say that"
    scene v26n108
    with dissolve
    isabella "Great!! Now we can tell the villagers they are safe!"
    isabella "Should we go?"
    $ minordrainlife = 0
    menu:
        "Sure let's go!":
            scene v26n109
            with dissolve
            "You and Isabella return to the village"

            jump villagepostvamps
        "[abgreen]Let me just check this book first":

            isabella "Ok, no problem"
            "You read the book and you find a spell"
            "You learn {color=#f00}{b}Minor Drain Life{/b}{/color}"
            "It's a level 5 Necromancy spell that steals life from your opponents"
            $ minordrainlife = 1
            isabella "All set?"
            MC "Yes, let's go!"
            scene v26n109
            with dissolve
            "You and Isabella return to the village"

            jump villagepostvamps

label villagepostvamps:
    scene v26n110
    with dissolve
    "It's already night when you arrive and Alice is waiting for you"
    alice "You did it, didn't you?"
    scene v26n111
    with dissolve
    isabella "[MC] here did it! He took care of the Master Vampire"
    alice "Great!! That's awesome! We are safe thanks to you!"
    menu:
        "I couldn't have done it without Isabella[ablovecolor] [ablove]":
            $ isabellalove += 1
            "Isabella likes you more"
        "Do we get a reward?":

            alice "Of course, we will talk about that tomorrow"
        "Nothing challenging to be honest...[abred] [abnoloveidiot]":


            $ isabellalove -= 1
            "Isabella likes you less"


    scene v26n111
    with dissolve
    alice "You need to eat something and rest, follow me!"
    $ wheretoafterslayerbath = "neutral"
    jump slayerbathv26

label v026neutralpart2:
    scene v26n116
    with dissolve
    isabella "Wow! Look at all this food! They sure are grateful"
    MC "Yeah, and all the wine and ale too"
    isabella "Let's make a toast!"
    scene v26n117
    with dissolve
    isabella "To the invincible duo!! Isabella and [MC]!!"
    MC "Cheers!!"
    scene v26n118
    with dissolve
    "After a couple of hours eating and drinking you feel a bit drunk"
    isabella "I'm so full.... And I think I'm a bit tipsy"
    scene v26n119
    with dissolve
    isabella "{i}Yawn!!!{/i}"
    "She is definitely drunk..."
    scene v26n120
    with dissolve
    isabella "You look drunk hic! Are you drunk? Ehehehe"
    MC "Ahaha... Sure... I'm the drunk one here..."
    isabella "Let's go to the bedroom, I need to relax"
    isabella "See if you can find a bottle of something good too"
    MC "Yeah.... We drank all of these..."
    scene v26n121
    with dissolve
    "You move to the bedroom"
    MC "Look what I found!!"
    isabella "Yay!!! Come sit next to me!"
    scene v26n122
    with dissolve
    "You sit next to her, she is clearly drunk"
    isabella "Let's celebrate!!"
    isabella "Will you give me a kiss?"
    scene v26n123
    with dissolve
    MC "What??"
    menu:
        "Kiss her":
            isabella "Mwuah"
        "[abgreen]Refuse":

            MC "Look.. I can't..."
            scene v26n124
            with dissolve
            MC "You are drunk and not thinking clearly"
            isabella "Nonsense"
            scene v26n123
            with dissolve
            "And she kisses you"
            isabella "Mwuah"

    scene v26n125
    with dissolve
    isabella "You taste funny hic"
    isabella "Eheheeh are you blushing?"
    MC "It must be the drinks..."
    scene v26n126
    with dissolve
    isabella "You know... You remind me of my brother a bit..."
    MC "I do?"
    isabella "Yes... You have his eyes..."
    scene v26n127
    with dissolve
    isabella "I... sorry... I didn't mean to..."
    scene v26n128
    with dissolve
    isabella "I really miss him... Sometimes it makes me cry for hours..."
    isabella "When I remember what happened to us..."
    menu:
        "If you'll feel better, you can talk to me[abgreen]":
            scene v26n129
            with dissolve
            isabella "Really? You are too kind"
            isabella "And I'm always talking about my problems when you have your own"
            $ isabellalove += 1
            "Isabella likes you more"
            MC "Don't worry about it, I can't remember what happened to me anyway"
            isabella "Let's drink to the future and forget sad things in the past!!"
            scene v26n130
            with dissolve
            "You go a few more rounds... "
        "Here have a drink and forget about that!":


            scene v26n130
            with dissolve
            isabella "Yes let's keep drinking!"
            "You go a few more rounds... "

    scene v26n125
    with dissolve
    isabella "You know what? I'm feeling drunk hic..."
    isabella "I think I need to lie on the bed"
    scene v26n123
    with dissolve
    isabella "Mwuah"
    "She kisses you"
    scene v26n131
    with dissolve
    "She moves toward the bed, wobbling a bit"
    MC "Am I drunk or are you not walking on a straight line?"
    "She doesn't answer you"
    scene v26n132
    with dissolve
    "Instead she starts to undress"
    MC "Did she forget I was here?"
    scene v26n133
    with dissolve
    isabella "Ahhhh much better hic.."
    MC "Damn... She's naked..."
    "You are trying to understand what is happening while fighting your drunkenness"
    scene v26n134
    with dissolve
    isabella "[MC] you're still there?! hic..."
    MC "I'm sorry I'll leave..."
    if isabellalove <= 4:
        isabella "See you tomorrow hic"

        jump devilsv3all
    isabella "And where will you sleep?"
    isabella "Come and join me hic..."
    MC "Okay..."
    scene v26n135
    with dissolve
    isabella "Are you going to sleep like that? hic"
    MC "What do you mean?"
    isabella "Your clothes dummy! You can't be comfortable like that"
    MC "Yeah... Sure hic..."
    "You don't know if it's the alcohol, but you take of your robe"
    scene v26n136
    with dissolve
    "Isabella looks impressed..."
    isabella "I... Hic..."
    scene v26n135
    with dissolve
    isabella "I mean, you look toned for a Mage..."
    MC "I train my body as well as my Magic"
    scene v26n137
    with dissolve
    isabella "Well, I'm sleepy... Let's sleep..."
    "You lie on the bed right next to her"
    scene v26n138
    with dissolve
    isabella "What do you think about my body? hic"
    MC "It's... Perfect..."
    MC "I mean... You must train a lot..."
    isabella "I do hehehe.... {i}Yawn{/i}... Now... I need to sleep...."
    scene v26n139
    with dissolve
    "She lies on the bed and falls asleep..."
    MC "What just happened?... Should I try to do something to her?"
    menu:
        "Try to feel her breasts[abred] [abnoalignment]":
            "She's asleep I might as well have some fun"
            $ Points -= 1
            "You lost 1 point"
            scene v26n140
            with dissolve
            "You start to move your hand to feel her breast"
            scene v26n141
            with dissolve
            isabella "What's going on? Everything ok?"
            MC "Yes yes... Just wanted to check if you were sleeping"
            scene v26n139
            with dissolve
            isabella "I'm trying to at least"
            "That was close, you better sleep now"
        "Try to sleep[abgreen] [abalignment]":


            MC "I like Isabella too much to do that, I better get to sleep"
            $ Points += 1
            "You gained 1 point"
    $ renpy.end_replay()
    jump devilsv3all
