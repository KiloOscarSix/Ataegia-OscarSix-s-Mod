

label ver036:
    scene v36001
    with dissolve
    cari "Let's see if the others are as resilient as you..."
    scene v36002
    with dissolve
    cari "Who should try first? Hmm..."
    cari "Maybe the big Tanzani boy?"
    scene v36003
    with dissolve
    cari "Let's see what you have inside that little head of yours..."
    scene v36004
    with dissolve
    cari "Hmmm... Your name is... Irgodon... And.."
    cari "Interesting... Isabella you say? Did we capture her too?"
    scene v36005
    with dissolve
    cari "Tell me more... Please..."
    irgodon "Who.... Are you? Isabella? Is that you?"
    cari "Yes... It's me... I need your help"
    scene v36006
    with dissolve
    irgodon "You know I would do anything for you"
    cari "I know... Do you love me?"
    irgodon "Yes... "
    scene v36007
    with dissolve
    cari "How long have you been waiting for this day?"
    cari "To have me? All of me?"
    irgodon "So long... Since you joined us..."
    cari "Joined who?"
    irgodon "The Demon Hunters..."
    cari "Interesting... Do you remember where it was? The place we met?"
    irgodon "Yes, I... I... You..."
    scene v36008
    with dissolve
    cari "Oh come on... You were doing so good..."
    irgodon "Who... Are... You?"
    cari "Well... Let's use another method then..."
    scene v36009
    with dissolve
    irgodon "Ahhhh!! Ahhh!!"
    cari "Don't fight it... I'll find out what I need to know anyway..."
    scene v36010
    with dissolve
    irgodon "Ahrgrrggg..."
    scene v36011
    with dissolve
    irgodon "Ah...."
    "What just happened? It's like he was drained..."
    scene v36012
    with dissolve
    cari "Yes... Show me everything... Hmmm... Great..."
    scene v36013
    with dissolve
    cari "Now it's your turn elf..."
    cari "Let's see what you can tell me..."
    scene v36014
    with dissolve
    cari "Hey... Do you hear me?"
    scene v36015
    with dissolve
    cari "No? What if I tell you your queen is in danger?"
    scene v36016
    with dissolve
    onzanu "My Queen? Where is she?!"
    cari "Don't you see Onzanu? I am your queen..."
    onzanu "You... Yes... You're my queen..."
    scene v36017
    with dissolve
    cari "Yes my dear Onzanu... I'm safe... Thanks to you..."
    onzanu "It's my duty, your grace"
    cari "Yes... But you deserve my gratitude"
    cari "I shall thank you in a special way"
    scene v36018
    with dissolve
    cari "Do you like it? Hmm?"
    onzanu "Yes my queen... But we shouldn't..."
    cari "Nonsense... I'm the queen, I get to decide what to give you"
    scene v36019
    with dissolve
    onzanu "Yes... Thank you my queen..."
    cari "Hmmm so good..."
    cari "Thank you for all the information"
    scene v36020
    with dissolve
    onzanu "What?! Who..."
    cari "Yes... So good, dark elves are so tasty..."
    onzanu "Ahhhh!!"
    "And again... She drained him too"
    scene v36021
    with dissolve
    cari "Oh... Already? I wanted to play a bit more..."
    cari "I need more... Much more..."
    scene v36022
    with dissolve
    cari "I guess it's your turn... Are you ready?"
    scene v36023
    with dissolve
    MC "Oh shit..."
    play sound "sounds/explosionayna.wav"
    scene v36023
    with hpunch
    cari "What the hell?!"
    play sound "sounds/explosionayna.wav"
    scene v36024
    with vpunch
    scene v36024
    with hpunch
    cari "What is happening?!"
    scene v36025
    with dissolve
    cari "Are we under attack? How dare they?"
    scene v36026
    with dissolve
    "You see her turn back to normal and open the gates"
    MC "If I could move this would be a great chance of getting out"
    scene v36027
    with dissolve
    cari "What is the meaning of this? Who are you?"
    play sound "sounds/explosionayna.wav"
    scene v36028
    with hpunch
    scene v36029
    with dissolve
    scene v36030
    with dissolve
    cari "Ahhhhhh!"
    play sound "sounds/explosionayna.wav"
    scene v36031
    with hpunch
    MC "Oh fuck!!"
    scene v36032
    with dissolve
    silvana "How dare you!! I will kill you all!"
    silvana "I'll..... DESTROY YOU ALL!!!"
    scene v36033
    with dissolve
    silvana "DIIIEEE!!!"
    scene v36034
    with dissolve
    MC "Ahhhhhh!!"
    scene black
    with dissolve
    pause 0.5

    scene black
    with dissolve
    MC "What just happened..."
    play sound "sounds/horror.ogg"
    scene v36monster2
    with hpunch
    MC "What was that?!"
    MC "Where am I? Silvana? Anyone?"
    play sound "sounds/horror.ogg"
    scene v36monster3
    with vpunch
    MC "Again?? What is happening here? Who's there?"
    play sound "sounds/horror.ogg"
    scene v36monster
    with vpunch
    MC "OH shit!! What the fuck is that?!"

    $ enemy = "Horror"
    $ companion = 0
    jump combat

label v36afterhorror:
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    scene black
    with dissolve
    amida "Why did this happened? Why?"
    MC "Mida? Is that you?"
    scene v36035
    with dissolve
    "As you open your eyes you can see Mida sitting down"
    MC "Mida? Where am I? I had a terrible dream with some weird creature..."
    scene v36036
    with dissolve
    amida "[MC]??! You're ok! Are you?"
    MC "I think I am but how did I get here?"
    scene v36037
    with dissolve
    amida "What do you mean?"
    amida "You've been on a coma for months..."
    amida "Nobody knew what was wrong with you"
    scene v36038
    with dissolve
    amida "But now you are ok..."
    MC "I was in a coma for months?"
    MC "What happened after I got captured?"
    amida "Captured? By whom?"
    MC "By the Slayers... Or demons I guess..."
    amida "You must still be confused my love"
    scene v36039
    with dissolve
    amida "Hey look who's here!"
    amida "Can you believe he has finally awoken?"

    if wheretoafterslayerbath == "neutral":

        jump v36isabela

    elif wheretoafterslayerbath == "Evil":
        jump v36liliana
    else:

        jump v36fannay


label v36fannay:
    scene v36040
    with dissolve
    fannay "The pretty boy is up? Do you know where you are?"
    MC "The College? I feel like I'm at the College"
    fannay "Yeah, you are"
    MC "But how... The last thing I remember is Mistress Silvana..."
    scene v36041
    with dissolve
    fannay "You know, while you were in a coma, me and Mida here..."
    fannay "Decided that if you ever opened your eyes again"
    scene v36042
    with dissolve
    amida "We would give you a gift..."
    MC "A gift?"
    amida "Well... Two gifts... And by looking at you..."
    fannay "You already know what it is..."
    MC "What do you mean?"
    fannay "Really...."
    scene v36043
    with dissolve
    fannay "Are you going to pretend that you're not happy to see us?"
    MC "What the..."
    scene v36044
    with dissolve
    amida "Hmmm... So hard... Glad to know that you like our gift..."
    MC "Wait a minute... This... Can't be real..."
    scene v36045
    with dissolve
    fannay "Don't tell me you don't want to have some fun with us..."
    MC "I... This.."
    fannay "Give it to him Mida... Let's see if he resists us"
    scene v36046
    with dissolve
    amida "Hmmm... I love this..."
    MC "Ah.... That's..."
    fannay "Good, right? She is amazing..."
    fannay "Give him more honey"
    scene v36047
    with dissolve
    MC "Ahhh...Shit..."
    amida "Hmmm..."
    fannay "That's it girl, get into it"
    scene v36048
    with dissolve
    amida "Hmmmmmm"
    fannay "Yes... Keep going..."
    "This feels amazing, but also very strange..."
    scene v36049
    with dissolve
    fannay "Good girl, now it's my turn"
    amida "I want more..."
    scene v36050
    with dissolve
    fannay "Hmmmm this is good"
    MC "Ahhh..."
    amida "Kiss me love"
    scene v36051
    with dissolve
    amida "Kiss me..."
    MC "Wait I..."
    fannay "Hmmmm yes...."
    scene v36052
    with dissolve
    amida "I missed you so much... you can't imagine how much..."
    MC "This can't be real..."
    scene v36053
    with dissolve
    fannay "What do you mean silly? Not real?"
    amida "Didn't you miss me?"
    MC "This is a dream I'm sure of it...Or a spell? An illusion?"
    scene v36054
    with hpunch
    amida "Ahhhhh!"
    fannay "Ahhhh!"
    MC "Oh fuck!!"
    $ renpy.end_replay()
    jump v36afterdream

label v36liliana:
    scene v36055
    with dissolve
    lili "The pretty boy is up? Do you know where you are?"
    MC "The College? I feel like I'm at the College"
    lili "Yeah, you are"
    MC "But how... The last thing I remember is Mistress Silvana..."
    scene v36056
    with dissolve
    lili "You know, while you were in a coma, me and Mida here..."
    lili "Decided that if you ever opened your eyes again"
    scene v36057
    with dissolve
    amida "We would give you a gift..."
    MC "A gift?"
    amida "Well... Two gifts... And by looking at you..."
    lili "You already know what it is..."
    MC "What do you mean?"
    lili "Really...."
    scene v36058
    with dissolve
    lili "Are you going to pretend that you're not happy to see us?"
    MC "What the..."
    scene v36059
    with dissolve
    amida "Hmmm... So hard... Glad to know that you like our gift..."
    MC "Wait a minute... This... Can't be real..."
    scene v36060
    with dissolve
    lili "Don't tell me you don't want to have some fun with us..."
    MC "I... This.."
    lili "Give it to him Mida... Let's see if he resists us"
    scene v36061
    with dissolve
    amida "Hmmm... I will..."
    MC "Wait.... That's..."
    scene v36062
    with dissolve
    MC "Ahhh...Shit..."
    amida "Look how hard it is"
    lili "Yeah... He likes the gift... Show him more"
    scene v36063
    with dissolve
    amida "Hmmmmmm"
    lili "Yes... Keep going..."
    "This feels amazing, but also very strange..."
    scene v36064
    with dissolve
    lili "Good girl, put it all in"
    amida "Hmmmm..."
    scene v36065
    with dissolve
    lili "It's my turn now..."
    MC "Ahhh..."
    amida "Yes show him"
    scene v36066
    with dissolve
    amida "Kiss me love..."
    MC "Wait I..."
    lili "Hmmmm yes...."
    scene v36067
    with dissolve
    amida "I missed you so much... you can't imagine how much..."
    MC "This can't be real..."
    scene v36068
    with dissolve
    lili "What do you mean silly? Not real?"
    amida "Didn't you miss me?"
    MC "This is a dream I'm sure of it...Or a spell? An illusion?"
    scene v36069
    with hpunch
    amida "Ahhhhh!"
    lili "Ahhhh!"
    MC "Oh fuck!!"
    jump v36afterdream

label v36isabela:
    scene v36070
    with dissolve
    isabella "[MC]? You are finally awake!! Do you know where you are?"
    MC "The College? I feel like I'm at the College"
    isabella "Yeah, you are"
    MC "But how... The last thing I remember is Mistress Silvana..."
    scene v36071
    with dissolve
    isabella "You know, while you were in a coma, me and Mida here..."
    isabella "Decided that if you ever opened your eyes again"
    scene v36072
    with dissolve
    amida "We would give you a gift..."
    MC "A gift?"
    amida "Well... Two gifts... And by looking at you..."
    isabella "You already know what it is..."
    MC "What do you mean?"
    isabella "Really...."
    scene v36073
    with dissolve
    isabella "Are you going to pretend that you're not happy to see us?"
    MC "What the..."
    scene v36074
    with dissolve
    amida "Hmmm... So hard... Glad to know that you like our gift..."
    MC "Wait a minute... This... Can't be real..."
    scene v36077
    with dissolve
    isabella "Don't tell me you don't want to have some fun with us..."
    MC "I... This.."
    isabella "Give it to him Mida... Let's see if he resists us"
    scene v36078
    with dissolve
    amida "Hmmm... I will..."
    MC "Wait.... That's..."
    scene v36079
    with dissolve
    MC "Ahhh...Shit..."
    amida "hmmmm"
    isabella "Do you like it? She's good isn't she?"
    scene v36075
    with dissolve
    amida "Hmmmmmm"
    isabella "Yes... Keep going..."
    "This feels amazing, but also very strange..."
    scene v36080
    with dissolve
    isabella "Good girl, put it all in"
    amida "Hmmmm..."
    scene v36076
    with dissolve
    isabella "Let me taste it..."
    scene v36extra
    with dissolve
    amida "Hmmm"
    isabella "It's good... My turn now..."
    scene v36081
    with dissolve
    MC "Oh shit..."
    amida "Do you like it?"
    MC "Wait I..."
    isabella "Hmmmm yes...."
    scene v36082
    with dissolve
    amida "I missed you so much... you can't imagine how much..."
    MC "This can't be real..."
    scene v36083
    with dissolve
    isabella "What do you mean silly? Not real?"
    amida "Didn't you miss me?"
    MC "This is a dream I'm sure of it...Or a spell? An illusion?"
    scene v36084
    with hpunch
    amida "Ahhhhh!"
    isabella "Ahhhh!"
    MC "Oh fuck!!"
    jump v36afterdream

label v36afterdream:
    scene black
    with dissolve
    cari "That's it my Goddess... I mean, my Queen..."
    scene v36085
    with dissolve
    "You slowly open your eyes..."
    cari "Somehow he resisted my illusions"
    fvoice "Really...? Interesting. Well, guess who just woke up"
    scene v36086
    with dissolve
    cari "You... You're a fascinating specimen..."
    fvoice "He is, isn't he?"
    scene v36087
    with dissolve
    fvoice "Did you had a nice dream? I bet you did"
    fvoice "Why did you choose to wake up? Weren't you enjoying it?"
    cari "Look at your Queen when she asks you a question!"
    scene v36088
    with dissolve
    MC "I..."
    aelia "I'm Aelia, nice to meet you young Mage"
    aelia "Aren't you an impressive character?"
    MC "..."
    scene v36089
    with dissolve
    aelia "You intrigue me... you clearly studied on Allesterra"
    aelia "Yet... I feel like I know you..."
    aelia "I feel like I've known you... For centuries..."
    scene v36090
    with dissolve
    aelia "Carilielle you can leave us now..."
    cari "Of course my queen..."
    scene v36091
    with dissolve
    aelia "Come on... I'll help up get up"
    MC "Why should I trust you?"
    aelia "Do you really think that if I wanted you dead you would still breath?"
    "For some reason her voice is peaceful and calms you"
    aelia "Let's go... I want to show you something"
    "Why? Why do you feel so good with her?"
    MC "Very well... I'll go with you"
    aelia "Good..."
    scene meanwhile
    with dissolve
    scene v36092
    with dissolve
    ayna "... And we need to hold this castle no matter what..."
    Bredita "Because you failed miserably on Darkaria..."
    ayna "You think I don't know that?! Can we focus on the real matters?"
    Bredita "Your little errand boy is about to arrive...And he's brought a friend"
    scene v36093
    with dissolve
    ayna "Impressive as always Bredita..."
    katarro "I found him Archmage, this is Rolf, the leader of the Demon Hunters"
    rolf "Can someone explain me what's this all about?"
    rolf "I'm very busy, some of my people are missing and they need my help"
    scene v36094
    with dissolve
    ayna "This is really important and may have something to do with your people"
    rolf "What do you mean?"
    ayna "Some of our people are also missing..."
    rolf "And...?"
    Bredita "And there are Demons involved..."
    scene v36095
    with dissolve
    rolf "I've been feeling so much Demon activity that I don't know where to turn to..."
    Bredita "Luckily for you we do know... But for now, we need to hold this castle..."
    ayna "Yes, the Slayers are almost here"
    scene v36096
    with dissolve
    rolf "The Slayers?"
    ayna "Yes...Before you say anything, we are sure the Demons are working with them"
    Bredita "Let's discuss our defensive plan with Enainia"
    scene v36097
    with dissolve
    aelia "This is my personal space... Do you like it?"
    MC "I guess..."
    scene v36098
    with dissolve
    aelia "Oh you will like it.. You'll see.."
    MC "Care to explain me why you brought me here? And what you want?"
    aelia "There is so much fire in you..."
    scene v36099
    with dissolve
    aelia "Why do I get this feeling... I'm sure I know you..."
    aelia "I want to try something with you..."
    MC "What do you mean?"
    aelia "I need you to trust me, I'll give you everything you want"
    aelia "If you don't trust me and if you want nothing from me.."
    aelia "I'll let you go, do we have a deal?"
    MC "A deal? But I have nothing to offer you..."
    aelia "You do... Believe me... So do we have a deal?"
    MC "Let me get this straight, you will give me everything I want?"
    aelia "Everything..."
    MC "But can I refuse your offer?"
    aelia "Ahahah yes... But do you want to?"
    scene v36100
    with dissolve
    aelia "Follow me please..."
    "You decide to follow her"
    scene v36101
    with dissolve
    aelia "Like I was saying... You get everything you want"
    MC "What is happening here? Is this another Illusion?"
    aelia "Yes... and no..."
    MC "What do you mean?"
    aelia "Imagine, you can live here forever this is your new world"
    aelia "Nothing else matters, no wars, no pain, no sadness..."
    aelia "Just you, you are all that matters, let your lust free"
    aelia "All the pleasures you dream of... All the women..."
    scene v36102
    with dissolve
    aelia "Me included... Don't you want to feel infinite pleasures?"
    aelia "Forever?"
    MC "I... How can I trust this? How can I trust you?"
    aelia "What did I say earlier? This can all be yours... If you trust me..."
    scene v36103
    with dissolve
    aelia "So are you ready to trust me? Are you ready to have all the pleasure in the world?"
    "Are you ready to trust her? Do you want to have all the pleasures in the world?"
    menu:
        "Yes[abgreen] [abendings]":
            jump end_1_nothing_else_matters
        "No":

            jump v36afterlust



label end_1_nothing_else_matters:
    hide screen MC_bars
    hide screen hpbar
    hide screen points_allhh
    scene v36111
    with dissolve
    aelia "You heard him ladies... Time to show him a good time..."
    amida "I missed you [MC] I need you..."
    ayna "[MC] You can have me anyway you want..."
    isabella "Me too!! I want to have some fun!"
    lili "Maybe he would like to watch us first..."
    aelia "Yes show him what he will get for all eternity..."
    scene v36112
    with dissolve
    show text "{color=#f00}{b}Ending 1: Nothing else matters{/b}{/color}" with dissolve
    $ renpy.pause(3, hard=True)

    scene v36112
    with dissolve
    "After your choice you got all that you wanted"
    scene v36113
    with dissolve
    "All the pleasure... No matter your desires"
    scene v36114
    with dissolve
    "They would happen... It was like paradise"
    scene v36115
    with dissolve
    "Was this the real world? Who cares?"
    "You can have everything you want!"
    scene v36116
    with dissolve
    "All the sex... All the girls..."
    scene v36117
    with dissolve
    "All the fetishes... You just need to imagine them"
    scene v36118
    with dissolve
    "If this is not the real world, it should be"
    scene v36119
    with dissolve
    "And if this is not the real world, then fuck the real world!"
    scene v36132
    with dissolve
    "You are really happy here..."
    scene v36120
    with dissolve
    "Forever..."


    scene 1yann
    with dissolve
    ayna "Congratulations! You reached one of the endings of Ataegina!"
    ayna "If you want to find different endings just make different choices"
    enainia "Wait... Are there other endings?"
    ayna "Well... Not yet but I'm sure Kthulian still has a lot to do"
    enainia "Good!! And congratulations once again"
    enainia "You have seen ending 1: Nothing else matters, hope you come back for more"
    $ renpy.end_replay()
    jump endversion

label v36afterlust:
    scene v36104
    with dissolve
    aelia "You... Refuse... How?"
    aelia "No man or beast could have resisted my charms like that..."
    aelia "Not even a God or a Devil could..."
    scene v36105
    with dissolve
    aelia "Yet... You did..."
    aelia "I don't know how... But you did..."
    scene v36106
    with dissolve
    aelia "Come here... Let me kiss you"
    scene v36107
    with dissolve
    aelia "Muhwaaa... By the way..."
    scene v36108
    with hpunch
    lust "I'm Lust... Pleasure to meet you..."
    MC "What? What is the meaning of this?"
    lust "Ahaha you are even cuter like that..."
    scene v36109
    with dissolve
    lust "I wish I could keep you here...I really do"
    lust "But a deal is a deal..."
    scene v36110
    with dissolve
    lust "And the deal was that I would let you go"
    MC "Wait..."
    scene v36121
    with hpunch
    lust "Bye bye..."
    scene v36122
    with dissolve
    MC "Where the hell am I? And what the hell just happened?"
    MC "Is this still an illusion? How can I know from now on?"
    MC "There is a castle over there... Maybe I can find someone inside"
    scene v36123
    with dissolve
    "You walk for some time and reach the bridge that leads to the entrance of the castle..."
    mvoice "Stop right there!!"
    scene v36124
    with dissolve
    MC "Wait! I mean no harm, I'm kind of lost here"
    scene v36125
    with dissolve
    elf "Who are you? What are you doing here?"
    MC "Can you ask your friend to stop pointing that thing at me?"
    elf "Not until you answer to my questions"
    MC "I told you... I'm lost... I don't know how I got here"
    MC "I suppose I'm on elf lands? Since you are elves and are guarding that castle"
    elf "You can't be that stupid... You don't know you are on Elvaria?"
    elf "And you want me to believe you?"
    MC "Yes... Look, I know Princess Enainia, can you take me to her?"
    elf "Ahahaha... You can't be serious, you fail to explain why you are here"
    elf "And you fail to explain who you are, and you ask to see the Princess?"
    elf "Ahahahaha"
    katarro "He's telling the truth..."
    elf "What..."
    scene v36126
    with dissolve
    katarro "Didn't you understand what I said? Or are you doubting me too?"
    MC "Master Katarro..."
    elf "I'm sorry Master Katarro, I had no idea..."
    scene v36127
    with dissolve
    katarro "Follow me [MC] we have a lot to talk about"
    "Katarro being Katarro, just like you remember him..."
    MC "Very well..."
    scene v36128
    with dissolve
    elf "I'm really sorry sir..."
    elf "And my apologizes to you too young man"
    menu:
        "Fuck you asshole!![abred] [abnoalignment]":
            elf "..."
            MC "You're lucky Katarro showed up or you would be dead now..."
            $ Points -= 1
            "You got -1 point"
        "No problem, you are doing your job[abgreen] [abalignment]":

            elf "Thank you sir"
            MC "No problem"
            $ Points += 1
            "You got 1 point"
        "Ignore him":

            MC "..."
            elf "..."

    scene v36129
    with dissolve
    "You followed Katarro through the castle until you reach some stairs"
    "At the top of the stairs you could see some familiar faces"
    scene v36130
    with dissolve
    ayna "[MC]?! How did you find him Katarro?"
    katarro "Actually he found us..."
    scene v36131
    with dissolve
    ayna "I'm so glad to see you... Tell me what happened to you"

    jump vers037
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
