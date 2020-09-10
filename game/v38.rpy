

init:
    $ gigabolt = 0
    $ phantom_t = 0
    $ aura_shield = 0
    $ rebound = 0
    $ armor_warrior = 0
    $ transmutehp = 0
    $ steves = 0


    $ visitkatroom38 = 0
    $ visitlibraryv38 = 0
    $ visitmidaroom38 = 0
    $ checkallv38 = 0
    $ sexv038 = 0
    $ evilweapon = 0
    $ midapregcount = 0
    $ fannaypregcount = 0
    $ sitnextto = "none"
    $ resistsoulstone = 0



label v038:
    scene portalroom
    with dissolve

    enainia "Hey, hello? What are you waiting for?"

    scene v38214
    with dissolve
    MC "Hum?? What happened?"
    enainia "Hmmm... We arrived at the college..."
    MC "How long did you wait for me?"
    enainia "You mean... right now? Only a few seconds... "
    "A few seconds? Was all that in your imagination?"
    "No... You can feel that thing inside of you..."
    scene v38215
    with dissolve
    enainia "No time to lose, let's go!"
    MC "Hmm.. Right..."
    "You leave the portal room and reach the college hall"
    scene v38216
    with dissolve
    "The Archmage is there waiting for you"
    ayna "I'm glad you're both here"
    ayna "We'll be having a meeting to plan our next steps"
    ayna "Princess, would you care to follow me?"
    enainia "Of course, Archmage"
    scene v38217
    with dissolve
    ayna "[MC], Can you go and check on Katriona?"
    MC "Sure, where is she?"
    ayna "She's resting in her room, you remember where it is right?"
    MC "Yes, of course I do"
    ayna "Good, tell her the meeting is starting soon"
    MC "Very well"
    jump collegebluev38

label collegebluev38:
    scene hall
    with dissolve

    call screen collegebluev4


label collegeportalroomv38:
    scene portalroom
    with dissolve
    MC "I don't think I need anything from here..."
    jump collegebluev38

label collegelibraryv38:
    scene library
    with dissolve
    if visitlibraryv38 == 0:
        MC "I should really check Katriona first"
        MC "And it looks like Yisnna isn't here"
        jump collegebluev38
    if visitlibraryv38 == 2:
        scene v18055
        with dissolve
        "As always Yisnna is in the middle of the books"
        scene v18056
        with dissolve
        yisnna "Oh you're back... I thought you said you were going to rest"
        yisnna "I'm a little busy right now, can you come back later?"
        MC "Sure..."
        jump collegebluev38

    if visitlibraryv38 == 1:
        scene v38199
        with dissolve
        "You see Yisnna taking a book out of the shelves"
        MC "Hello Yisnna"
        scene v38200
        with dissolve
        yisnna "[MC]? where have you been? How are you?"
        MC "I'm good, how are you? Reading much?"
        yisnna "Indeed, just received a new book"
        MC "New book?"
        scene v38193
        with dissolve
        yisnna "Yes, it's called Love of Magic, it's a story about a student of magic"
        yisnna "And his way to magical discoveries"

        menu:
            "{color=#1BBB20}Can I see it?":
                yisnna "Sure... Here you go"
                scene v38194
                with dissolve
                MC "Love of Magic..."
                "Welcome to the world of Magic, where demi-Gods drink in your local pub"
                "The great grand-daughter of King Arthur is your study-buddy."
                "Fight your way through the Paths of Elsewhere, romance gorgeous women"
                "Discover your destiny.​"
                MC "Seems interesting..."
                scene v38195
                with dissolve
                MC "Politics and games..."
                scene v38196
                with dissolve
                MC "Interesting... Should I keep reading?"
                call screen lom38
            "Hmm... I prefer spell books":

                jump bothtalksv38l

label talkbackv38:
    scene v38196
    with dissolve
    yisnna "Can I get my book back, please?"
    scene v38197
    with dissolve
    MC "Oh, sorry..."
    yisnna "No problem, you're always welcome to come here and read"
    scene v38198
    with dissolve
    yisnna "I have some spell books too"
    jump bothtalksv38lib

label bothtalksv38l:
    scene v38198
    with dissolve
    yisnna "I have those too you know"
    jump bothtalksv38lib

label bothtalksv38lib:
    MC "Can I see them?"
    yisnna "Sure, let me just put this back on it's place"
    scene v38199
    with dissolve
    "You see her putting the book back, she's really careful with books"
    scene v38200
    with dissolve
    yisnna "So let's see what we got shall we?"
    "You start to feel something weird inside you...Burning..."
    MC "What is this? It's like I can feel her emotions"
    scene v38202
    with dissolve
    yisnna "What... Is.. this... I...Feel..."
    "The feeling is stronger... You feel like you can control her emotions"
    yisnna "I... Kiss me..."
    scene v38201
    with dissolve
    "Is this for real? What's going on? Is this about that weird stone?"
    MC "Should I kiss her? Should I try to fight this thing?"
    scene v38200
    with dissolve
    yisnna "I... Sorry... I got distracted... Where were we?"
    MC "..."
    yisnna "Right... The spell books..."
    scene v38203
    with dissolve
    yisnna "Follow me please"
    MC "Sure..."
    "What just happened? I must be careful with this thing"
    scene v38204
    with dissolve
    yisnna "So, level 10 spells, what do you say?"
    MC "Hell yeah! "
    scene v38205
    with dissolve
    yisnna "Heheheh... I knew you would like it"
    yisnna "But can you handle them?"
    MC "I can try"
    scene v38204
    with dissolve
    yisnna "Go ahead"
    MC "Let's see"
    "Once again you start to feel the thing inside you burning"
    "You are presented with some high level spell books"


label booksfor10:
    menu:
        "Read Gigabolt {image=001battle}" if gigabolt == 0:
            $ v38 += 1
            $ gigabolt = 1
            "Gigabolt?"
            "Deals massive electrical damage and paralyzes the target"
            "You learn the level 10 spell Gigabolt"

            if Destpoints >= 10:
                "Since you have 10 or more Battlemagic skill points you can use it"
            elif Destpoints >= 5:
                "You will only able to use it with 10 or above Battlemagic skil"
            else:
                "I wish my battlemagic skill was higher"
            jump booksfor10

        "Read Phantom Terrain {image=001illusion}" if phantom_t == 0:
            $ v38 += 1
            $ phantom_t = 1
            "Phantom Terrain?"
            "Makes them see an illusion of a dangerous area between you"
            "An enemy would feel real pain trying to attack."
            "You learn level 10 spell Phantom Terrain"

            if Iluspoints >= 10:
                "Since you have 10 or more Illusion skill points you can use it"
            elif Iluspoints >= 5:
                "You will only able to use it with 10 or above Illusion skill"
            else:
                "I wish my Illusion skill was higher"
            jump booksfor10

        "Read Aura Shield {image=001heal}" if aura_shield == 0:
            $ v38 += 1
            $ aura_shield = 1
            "Aura Shield?"
            "It's like a Greater Ward."
            "Only it turns your target's damage into Health instead"
            "You learn the level 10 spell Aura Shield"

            if Healpoints >= 10:
                "Since you have 10 or more Healing skill points you can use it"
            elif Healpoints >= 5:
                "You will only able to use it with 10 or above Healing skil"
            else:
                "I wish my Healing skill was higher"
            jump booksfor10

        "Read Rebound {image=001myst}" if rebound == 0:
            $ v38 += 1
            $ rebound = 1
            "Rebound?"
            "Seems to be a powerful barrier"
            "It causes the enemy to feel their own attack instead of you"
            "You learn the level 10 spell Rebound"

            if Mystpoints >= 10:
                "Since you have 10 or more Mysticism skill points you can use it"
            elif Mystpoints >= 5:
                "You will only able to use it with 10 or above Mysticism skil"
            else:
                "I wish my Mysticism skill was higher"
            jump booksfor10

        "Read Armored Warrior {image=001summon}" if armor_warrior == 0:
            $ v38 += 1
            $ armor_warrior = 1
            "Armored Warrior?"
            "A shielded creature that defends you and counterattacks"
            "You learn the level 10 spell Armored Warrior"

            if Summpoints >= 10:
                "Since you have 10 or more Summoning skill points you can use it"
            elif Summpoints >= 5:
                "You will only able to use it with 10 or above Summoning skil"
            else:
                "I wish my Summoning skill was higher"
            jump booksfor10

        "Read Transmute Health {image=001alteration}" if transmutehp == 0:
            $ v38 += 1
            $ transmutehp = 1
            "Transmute Health?"
            "Wow, it lets me sacrifice my life energy for magic energy"
            "I'll have to be careful or I could end up killing myself"
            "You learn the level 10 spell Transmute Health"

            if Altepoints >= 10:
                "Since you have 10 or more Alteration skill points you can use it"
            elif Altepoints >= 5:
                "You will only able to use it with 10 or above Alteration skil"
            else:
                "I wish my Alteration skill was higher"
            jump booksfor10

        "Read Summon Wraith {image=001necro}" if steves == 0:
            $ v38 += 1
            $ steves = 1
            "Summon Wraith?"
            "Lets me summon a Wraith that deals damage and steals magical energy"
            "I think I'd name him Steve"
            "You learn the level 10 spell Summon Wraith"

            if Necropoints >= 10:
                "Since you have 10 or more Necromancy skill points you can use it"
            elif Necropoints >= 5:
                "You will only able to use it with 10 or above Necromancy skil"
            else:
                "I wish my Necromancy skill was higher"
            jump booksfor10

        "Finish reading" if v38 == 7:
            MC "I guess that's all..."
            jump afterspell10


label afterspell10:
    $ v38 = 1

    scene v38205
    with dissolve
    yisnna "So... Too much for your head?"
    MC "That was intense... But I got them..."
    yisnna "With one read? Ahahaha sure you did..."
    "But you did..."
    MC "I think I need a rest now..."
    yisnna "Good idea, go and rest now"
    "Or maybe you can explore a bit more before you do..."
    $ visitmidaroom38 = 1
    $ visitlibraryv38 = 2
    jump collegebluev38

label throneroomcollegev38:
    scene throne
    with dissolve
    MC "Nobody is here..."
    jump collegebluev38

label liliroomcollegev38:
    MC "The door is locked"
    jump collegebluev38

label classroomcollegev38:
    scene classroommiss
    with dissolve
    MC "Nobody is here..."
    jump collegebluev38

label bathroomcollegev38:
    scene bathhousemiss
    with dissolve
    MC "Oh I remember the first time I entered this place..."
    MC "Sadly there is nobody here"
    jump collegebluev38

label aynaroomv2v38:
    MC "The door is locked"
    jump collegebluev38

label v2exitroom01v38:
    MC "That's where I am..."
    jump collegebluev38

label courtyardv38:
    MC "I don't have time for this right now"
    jump collegebluev38

label mcroomv38:
    scene mcroomad
    with dissolve
    if checkallv38 == 0:
        if my_path_is == "evil":
            MC "This is my old room... Before I landed on Bredita's place"
            MC "I haven't been here for some weeks now..."
        if my_path_is == "neutral":
            MC "...My old room... Before I started to travel with Isabella"
            MC "Feels like I left for so long... how long was it really, some weeks?"
            if devilbloodbottle == 1:
                MC "I should come here later and try the bottle Rolf gave me"
        else:
            MC "This is my room"
        "I have nothing to do here now..."

        jump collegebluev38
    else:



        jump collegebluev38

label katroomv38:
    if visitkatroom38 == 1:
        MC "It's locked..."
        jump collegebluev38
    else:
        scene v38001
        with dissolve
        "You enter Katrionas room"
        MC "There she is... Sleeping"
        "With a soft and gentle voice you start to call her"
        MC "Hey... Kat... are you gonna nap all day?"
        scene v38002
        with dissolve
        katriona "Hmmmm Wha... "
        MC "Hey, time to wake up sleepy head"
        katriona "Hmmmm [MC] ? "
        scene v38002a
        with dissolve

        MC "Feels like we've been in this situation before"
        MC "So this is the point where I ask..."
        MC "Do you remember what happened, do you know what your name is?"
        MC "Then I'm supposed to look all flirty and tease you"
        MC "While you have no idea what's going on"
        katriona "Ugh.. Just give me a minute, I still have a bit of a headache"
        katriona "I'll make fun of you in a second."
        scene v38003
        with dissolve
        MC "You know Kat...I've been practicing this spell called Healing Touch"
        MC "Let me try it on you..."
        scene v38004
        with dissolve
        katriona "Ha Ha, Fuck you! Like you'd be so lucky.."
        MC "Whatever... I was just trying to help you..."
        katriona "Yeah right... Help yourself to a feel you mean"
        scene v38005
        with dissolve
        katriona "Why don't you actually help by getting me my robe"
        MC "Your robe?"
        katriona "Yes dummy, right over there"
        scene v38006
        with dissolve
        MC "..."
        menu:
            "I think you look better like this{color=#FF0000} (+1 Katriona's Corruption)":
                $ katrionacorr +=1
                scene v38004
                with dissolve
                katriona "..."
                katriona "Fuck.... You..."
                katriona "Fine... I get it myself"
                scene v38007
                with dissolve
                MC "See... I knew I was right..."
                "Katriona corruption increased"
            "Sure, let me get it{color=#1BBB20} (+1 Katriona's Love)":


                $ katrionalove +=1
                scene v38008
                with dissolve
                MC "There you go"
                katriona "Thank you..."
                "Katriona love increased"

        scene v38009
        with dissolve
        katriona "I wonder what our next move is"
        MC "I don't know what is going on..."
        if my_path_is == "evil":
            "But Liliana must have been caught by them..."
            "You wonder if you'll be able to find her"
        if my_path_is == "neutral":
            "But Isabella and Katla must have been caught by them..."
            "You wonder if you'll be able to find them"
        else:
            "But Queen Zordruza must have been caught by them..."
            "You wonder if you'll be able to find her"
        scene v38010
        with dissolve
        katriona "I'm ready. Let's go?"
        MC "Dressed already? No fair..."
        scene v38011
        with dissolve
        katriona "Ahaha, you think you're funny..."
        MC "You should take it as a compliment..."
        katriona "What? Having a pervert checking me out?"
        MC "Checking you out? Ok yeah, I was.."
        MC "But a pervert?! Ok yeah, can't deny that either"
        scene v38103
        with dissolve
        katriona "Lucky for you, you're a cute one..."
        katriona "Or we might have some trouble here"
        MC "Yeah right..."
        katriona "Or did you think the Archmage never told me about the bath?"
        MC "Wait, what?!"
        katriona "Come along, little boy"
        scene v38012
        with dissolve
        katriona "Hope you stared enough to help you.."
        katriona "Ahem 'entertain yourself' tonight..."
        MC "Ahaha... Very funny..."
        katriona "Let's go..."
        $ visitlibraryv38 = 1
        jump afterkattalkv38

label afterkattalkv38:
    "You both move to the throne room"
    scene v38207
    with dissolve
    ayna "Glad to see you're ok"
    katriona "It takes more than a Slayer and demon army to take me down"
    MC "Ahahah sure..."
    scene v38206
    with dissolve
    ayna "[MC], we need to have a discussion, feel free to walk around the college"
    ayna "You should rest after all the recent events, your room is untouched"
    scene v38208
    with dissolve
    katriona "You heard the lady... Go rest, my delicate little flower"
    MC "Why you..."
    katriona "Ahahah bye!"
    scene throne
    with dissolve
    "They leave"
    MC "Time for some more exploring I guess"
    $ visitkatroom38 = 1


    jump collegebluev38

label midaroomv38:
    if visitmidaroom38 == 0:
        "The door to Midas room is locked..."
        jump collegebluev38
    if visitmidaroom38 == 1:
        $ visitmidaroom38 = 0
        $ checkallv38 = 1
        "Oh.. the door is open..."
        if my_path_is == "evil":
            jump evilpartroomv38
        else:
            jump otherpartroomv38


label otherpartroomv38:
    scene v38013
    with dissolve
    "You can see inside the room without being noticed"
    "You see Mida and Fannay talking"
    fannay "Don't tell me you don't miss him..."
    amida "I..."
    fannay "But we can still have fun, you know?"
    scene v38014
    with dissolve
    amida "Wait...What are you doing?"
    fannay "Don't you want to have some fun?"
    if midacorr >= midalove:
        jump tisbetterthan2
    else:
        jump soloingisgood2

label tisbetterthan2:
    scene v38015
    with dissolve
    amida "I...Do..."
    "You wonder what the hell is going on"
    fannay "You're so pretty..."
    scene v38016
    with dissolve
    amida "Fannay we shouldn't..."
    fannay "Why not? Don't you want to?"
    amida "I'm not sure..."
    scene v38017
    with dissolve
    "Fannay pushes Mida to the bed"
    "Placing herself on top of her"
    fannay "Look at these... So big... So soft"
    amida "Come here..."
    scene v38018
    with dissolve
    amida "Mwuah...."
    fannay "{i}Kiss"
    MC "They are really going at it..."
    MC "Oh... they are getting naked..."
    scene v38019
    with dissolve
    "You keep watching the girls going at it"
    "They are kissing each other passionately"
    amida "Hmmmm"
    fannay "It feels good right?"
    amida "Hmm Hmm"
    fannay "This will feel better..."
    scene v38020
    with dissolve
    fannay "{i} Lick... Slurp.."
    amida "Ahhh... Yes..."
    fannay "You taste great..."
    fannay "Let's try something else..."
    scene v38021
    with dissolve
    "Once again the girls switch positions..."
    fannay "Ah.... Yes... Hmmm"
    amida "Hmmmm"
    MC "Shit... This is so hot... What should I do?"
    menu:
        "Join them":
            "You slowly move towards them"
            scene v38022
            with dissolve
            "Fannay spots you, but you signal her to keep quiet"
            "While Mida is just trying to have fun..."
            scene v38023
            with dissolve
            "Fannay understands what you are planning and smiles"
            "This is a hot scene to witness..."
            scene v38024
            with dissolve
            "She is clearly waiting for your move"
            "You signal her to keep going... And she does..."
            scene v38025
            with dissolve
            amida "Ah! Yes.... More..."
            "Shit... You're getting really hard..."
            fannay "You like this don't you?"
            amida "Ah..."
            "Time to do something..."
            scene v38026
            with dissolve
            "You start to feel Fannays ass cheeks"
            "She has a good, firm ass..."
            "Time to go a little further"
            scene v38027
            with dissolve
            "You are not sure what the burning you're feeling inside is"
            "Is it because of the scene or the same thing as earlier?"
            "You keep your left hand on Fannay's butt"
            "And start to rub Mida's leg with your right one"
            scene v38028
            with dissolve
            "Until Mida notices it"
            amida "What the...? [MC] ?"
            scene v38029
            with dissolve
            amida "What is going on!!?? [MC]"
            if my_path_is == "good":
                amida "You went to Darkaria and disappeared..."
                amida "I thought you..."
            else:
                amida "You're alive? But they said..."


            MC "Calm down... I'm fine, you are too... Let's enjoy it"
            if midalove or midacorr >=4:
                $ sexv038 = 3
                scene v38032
                with dissolve
                amida "{i} Kiss"
                amida "You are right... Let's enjoy it..."
                "Was it this easy? Something is not right"
                "It's like I can feel them..."
                fannay "Hmmm, the love birds are back... I like it"
                scene v38034
                with dissolve
                MC "Oh... I missed these my dear..."
                MC "I think they should get a special treatment..."
                MC "Don't you agree Fannay?"
                fannay "Of course..."
                scene v38035
                with dissolve
                fannay "{i}Slurp... Lick..."
                amida "Ah...Mhmmm"

                scene v38036
                with dissolve
                "You are forced to lie down by the two girls"
                "Mida gets on top of you"
                fannay "Look at this dick! Damn... You're lucky Mida"
                fannay "I would use it every single day if I could!"
                amida "Maybe you will in the future"
                scene v38037
                with dissolve
                fannay "{i} Kiss"
                "You feel Fannays soft lips touching your penis"
                fannay "It's... Like... It's pulling me to it..."
                fannay "I have to taste it now..."
                scene v38038
                with dissolve
                "Her mouth starts to wrap around your dick"
                fannay "Hmmmm tasty... Big... Hmmmff"
                fannay "Let me get it nice and wet for you Mida"
                scene v38039
                with dissolve
                fannay "There... Take it girl..."
                "You feel Fannays hand directing your dick inside Mida"
                amida "AHH!! Hmmmm"
                MC "Oh... Yes..."
                amida "Hmmm I missed that..."
                scene v38040
                with dissolve
                fannay "This is a sexy view..."
                "Mida starts to move slowly..."
                amida "Hmmm yes... Slowly..."
                fannay "Let me taste you two combined"
                "Those words make Mida jump on your face"
                scene v38041
                with dissolve
                amida "Yes... Lick my pussy...Hmmm"
                "You do as she says"
                amida "Yes... I'm cumming!!"
                "You feel Midas body trembling as she cums"
                fannay "Oh my... Hmmm...Ready or not..."
                scene v38042
                with dissolve
                fannay "{i} Grublgl"
                MC "Ah!! Shit..."
                "You feel the tip of your dick touching Fannays throat"
                fannay "Mhhhmmmff"
                amida "Yes... Don't stop now..."
                "You have your tongue buried deep inside Mida's pussy"
                "And your penis buried deep inside Fannays throat..."
                "That feeling of burning inside you is getting stronger"
                scene v38041
                with dissolve
                fannay "Enough... I need to feel this big dick, not just taste it"
                "With those words, Fannay sits on your lap"
                scene v38043
                with dissolve
                "Sliding your cock all the way inside her pussy"
                fannay "AHH!!! YES!! YES!!"
                "Before Fannay could say anything else, Mida kissed her"
                amida "{i} Kiss"
                fannay "Mhmmm"
                scene v38044
                with dissolve
                fannay "You are both amazing..."
                fannay "Ah... Yes..."
                "This is too much for you... You feel your orgasm approaching"
                "Fannay feels your body shaking and jumps off of your dick"
                scene v38045
                with dissolve
                "Both girls position their faces close to your dick"
                "They know what's about to happen..."
                amida "Yeah baby, give it to us"
                fannay "Yes... Come on..."
                MC "I can't... Hold anymore..."
                show shot
                with hpunch
                scene v38046
                with dissolve
                show shot
                with vpunch
                hide shot
                MC "Ahh!!! FUCK!!"
                show shot
                with hpunch
                scene v38047
                with dissolve
                fannay "Hmm... So much..."
                amida "Did you save all that for us?"
                MC "What can I say... This was beyond amazing..."
                fannay "You look so sexy Mida..."
                scene v38048
                with dissolve
                fannay "{i}Slurp, lick"
                amida "Hmmm..."
                MC "Damn that's hot..."
                "You watch the girls kiss and lick each other"
                scene v38049
                with dissolve
                "What a fantastic view that you have in front of you..."
                MC "I hope this is not a dream..."
                fannay "Hehehe... It could be..."
                amida "Having two girls licking the cum off of your dick"
                amida "Sure seems like one..."
                "The burning feeling inside you is starting to vanish"
                scene v38050
                with dissolve
                "You see Fannay getting off of the bed"
                fannay "This... Was... Unexpected..."
                amida "I... Yes... It was strange... Like...I don't know..."
                MC "But it was good right?"
                amida "Yes... It was..."
                fannay "I loved it... We should do this again"
                scene v38051
                with dissolve
                fannay "Bye bye love birds... Call me if you ever need me"
                amida "..."
                "You think for yourself that you definitely will"
                $ renpy.end_replay()
                jump aftersexv38NG
            else:
                $ sexv038 = 5
                scene v38030
                with dissolve
                amida "How can you say that??!!"
                amida "Leave... Please... I.."
                MC "But I..."
                amida "Leave!!"
                scene v38031
                with dissolve
                MC "Very well"
                "Shit that didn't go well... You probably need a rest..."
                jump lustlairv38
        "Keep watching":

            $ sexv038 = 2
            fannay "Let me try something pretty girl..."
            scene v38056
            with dissolve
            amida "Hmmm... Oh..."
            "You see both girls using their mouths to satisfy each other"
            fannay "You taste so good girl"
            amida "Ah... Yes..."
            scene v38057
            with dissolve
            amida "Hmmm... Oh..."
            fannay "You like this?"
            amida "Yes... It's good..."
            fannay "You dirty girl... Let me show you more"
            scene v38058
            with dissolve
            MC "Damn... They're really going at it"
            amida "Yes!! Yes!! Don't Stop!"
            amida "I'm.... About... To..."
            fannay "Yeah... You like this don't you?"
            fannay "You dirty girl!"
            amida "Ahhhh!!!"
            "You see Mida cumming in front of your eyes"
            "And both girls collapse on the bed"
            scene v38059
            with dissolve
            fannay "Was that great or what?"
            amida "Ah... Yes...Great..."
            MC "I guess I should leave now..."
            $ renpy.end_replay()
            jump lustlairv38
        "Leave":

            $ sexv038 = 6
            MC "I... Should go"
            $ renpy.end_replay()
            jump lustlairv38

label soloingisgood2:
    scene v38061
    with dissolve
    amida "Get out!! Stop this..."
    fannay "Hey... Come on..."
    amida "I said leave!"
    scene v38062
    with dissolve
    fannay "Geez... Fine..."
    fannay "Just wanted to make you enjoy your day..."
    fannay "Whatever..."
    "Fannay leaves the room"
    scene v38063
    with dissolve
    "Mida is crying on her bed"
    menu:
        "{color=#1BBB20}Talk to her":
            MC "Hello Mida..."
            scene v38064
            with dissolve
            amida "[MC]!!??"
            amida "Is it really you??"
            MC "I think so..."
            scene v38065
            with dissolve
            amida "Oh my god!! It's you!!"
            "She jumps out of the bed!"
            MC "Wow..."
            scene v38066
            with dissolve
            "She kisses you"
            amida "I missed you so much!!!"
            MC "I'm here now"
            scene v38067
            with dissolve
            "Her expression changes"
            amida "Where have you been??! I was..."
            MC "Please calm down... I'm here now"
            scene v38068
            with dissolve
            amida "I still can't believe it... Is it really you..."
            amida "This isn't a dream or an illusion?"
            "You start to feel something inside you..."
            MC "I'll show you it's neither..."
            "You throw her on top of the bed"
            scene v38069
            with dissolve
            "She awaits for your next move..."
            "You take off her dress"
            scene v38070
            with dissolve
            MC "I'll make it up to you now..."
            "You remove her panties"
            MC "Now open your legs"
            scene v38071
            with dissolve
            amida "Yes..."
            MC "Beautiful..."
            "The feeling inside you starts to burn your insides"
            "You somehow feel Mida's emotions"
            "You feel that somehow it's related with that weird stone"
            scene v38072
            with dissolve
            "You get down on her pussy and start licking her"
            amida "Hmmm.. Yes... Oh.."
            "She tastes sweet and salty"
            "You start to move your tongue more franticly"
            scene v38073
            with dissolve
            "And using your fingers to aid you"
            amida "Hmmm... Ah... Wait..."
            scene v38074
            with dissolve
            MC "What's wrong?"
            amida "I'm completely soaked... It's your turn now..."
            MC "You don't have to ask me twice"
            scene v38075
            with dissolve
            "Mida gets closer to you"
            "Almost hypnotized by the sight of your penis"
            "Before you could say anything"
            scene v38076
            with dissolve
            "Mida puts her mouth around your cock"
            MC "Hmmm... That's great..."
            amida "Hmmm Hmmm"
            "She's really going at it"
            scene v38077
            with dissolve
            amida "Hmmm {i} Yhu Lke ith?"
            MC "Hmm? Yeah... I like it..."
            amida "{i} Slurp, slurp"
            scene v38078
            with dissolve
            "Oh... She's going deeper now..."
            "You feel her throat touching the tip of your dick"
            MC "Oh... That's something new..."
            scene v38079
            with dissolve
            MC "But it's time for the main event..."
            amida "Really? And what would that be?"
            MC "Ahaha"
            scene v38080
            with dissolve
            MC "Do you really want to know?"
            amida "Hmmm... No? {i} giggle"
            amida "Does it have something to do with this?"
            scene v38081
            with dissolve
            MC "Oh... You tease..."
            amida "So was there something you wanted to show me?"
            scene v38082
            with dissolve
            MC "You bet..."
            "You start aiming your dick to her entrance"
            scene v38083
            with dissolve
            "It's going inside"
            amida "Ah....Hmmm..."
            "It's tight... But she's all wet... Allowing you to go deeper"
            scene v38084
            with dissolve
            amida "Ah... So big... Hmmm yes..."
            MC "You're so tight... Hmm.."
            amida "That's so good..."
            scene v38085
            with dissolve
            MC "You're so hot Mida... This feels amazing..."
            amida "You too my love... I love you"
            scene v38086
            with dissolve
            MC "You're so pretty... I missed you"
            amida "I missed you too..."
            amida "Now...Fuck me hard!"
            "Did she really say that? We don't want to disappoint her right?"
            scene v38087
            with dissolve
            "You start thrusting with all your might"
            amida "Ah!! Yes... More!! More!!"
            scene v38088
            with dissolve
            MC "You like it like this?"
            amida "Yes!!! Yes!! I'm..."
            scene v38089
            with dissolve
            amida "About to...Ahhhhh!!"
            "You feel her body shaking uncontrollably"
            scene v38092
            with dissolve
            amida "Ahh.... I'm cumming!!"
            amida "Oh my god... Oh my god..."
            MC "Call me [MC] ... Eheheh"
            "As you are preparing to finish yourself"
            scene v38090
            with dissolve
            amida "Do...You...Hmm... Want to try anal?"
            MC "What? Anal?"
            amida "We never did... So..."
            scene v38091
            with dissolve
            amida "I want to make you feel good..."
            MC "I... "
            amida "Please be gentle..."
            MC "I will, don't worry"
            scene v38093
            with dissolve
            "You take your dick out of her pussy"
            scene v38094
            with dissolve
            "And you start to point it to the other hole"
            "You feel a lot of resistance entering"
            MC "Just relax my love..."
            "Your words seemed to have an effect"
            scene v38095
            with dissolve
            amida "Hmmff... It's getting in..."
            MC "Damn that's tight..."
            "You start to move in and out"
            scene v38096
            with dissolve
            "You feel the burning inside you getting stronger"
            amida "Uhmmm I... it's feeling... Better?"
            MC "It feels great honey"
            amida "Yes... You can try and move faster now"
            "You can't resist the power of those words"
            scene v38097
            with dissolve
            "And you pick up the pace"
            amida "AHHH!!"
            MC "Are you ok?"
            amida "Yes... Keep going! Give me more"
            scene v38098
            with dissolve
            "You give it to her even harder, faster..."
            amida "Oh my God!!! I'm... Cumming!!"
            MC "Shit I can't hold it either..."
            MC "I'm about to..."
            menu:
                "Cum inside her ass":
                    scene v38099
                    with dissolve
                    show shot
                    with hpunch
                    hide shot
                    MC "AHHH!!!"
                    show shot
                    with vpunch
                    hide shot
                    amida "Ahhhh!! Yes... You're filling me..."
                "Pull out":
                    scene v380100
                    with dissolve
                    show shot
                    with hpunch
                    hide shot
                    MC "AHHH!!!"
                    show shot
                    with vpunch
                    hide shot
                    amida "Ahhhh!! Yes... You're covering me..."
            "You both collapse on the bed"
            $ renpy.end_replay()
            jump aftersexv38NG
        "Leave her be":


            MC "I don't have time for this shit"
            MC "What I need is a good rest..."
            $ renpy.end_replay()
            jump lustlairv38



label aftersexv38NG:


    scene v38052
    with dissolve
    amida "What was this? I felt like I couldn't stop"
    amida "Even if I tried..."
    MC "But you didn't try right?"
    amida "No... I mean... I don't know..."
    scene v38053
    with dissolve
    amida "Tell me... where have you been? What happened"
    MC "It's a long story..."
    scene v38054
    with dissolve
    amida "I'm listening..."
    MC "Well it all started when..."
    jump lustlairv38

label evilpartroomv38:
    scene v38104
    with dissolve
    "You notice that Fannay is inside"
    MC "What is she doing here?"
    menu:
        "{color=#1BBB20}Keep watching":
            scene v38105
            with dissolve
            "It looks like she's looking for something"
            MC "I wonder what could that be..."
            scene v38106
            with dissolve
            fannay "Where is it? It remember putting it here"
            fannay "Is that..."
            scene v38107
            with dissolve
            fannay "Ha ha, here you are..."
            fannay "I hope this was worth the trouble"
            MC "I wonder what that is..."
            menu:
                "Leave":
                    MC "I don't care... I'm out"
                    $ sexv038 = 6
                    jump lustlairv38
                "Show your presence":

                    MC "So... What is that?"
                    scene v38108
                    with dissolve
                    fannay "AH!.... Shit... You scared me..."
                    MC "Can you tell me what are you doing here?"
                    MC "And what is that book?"
                    scene v38109
                    with dissolve
                    fannay "I could ask you the same..."
                    fannay "You've been gone for weeks..."
                    fannay "And now you show up here in front of me?"
                    scene v38110
                    with dissolve
                    MC "Come on... You don't need to hide anything from me..."
                    MC "And I can clearly see that you shouldn't have that book"
                    "You start to feel something inside you... It burns..."
                    "It's messing with your emotions... And somehow with hers"
                    MC "I..."
                    scene v38111
                    with dissolve
                    MC "Come on... Let me see the book"
                    fannay "Ok"
                    scene v38112
                    with dissolve
                    MC "That was easy..."
                    fannay "I... Don't..."
                    MC "Ritual of the Bound Weapon? Looks interesting..."
                    MC "I'll have to read it"
                    scene v38113
                    with dissolve
                    fannay "Wouldn't you prefer to fuck me?"
                    MC "What?!"
                    fannay "I'm feeling... This is..."
                    scene v38114
                    with dissolve
                    fannay "{i} Kiss"
                    menu:
                        "Reject her":
                            MC "Stop this!"
                            scene v38115
                            with dissolve
                            fannay "But... I..."
                            MC "I'm out of here, I'm taking the book"
                            $ sexv038 = 6
                            $ renpy.end_replay()
                            jump lustlairv38
                        "{color=#1BBB20}Hell yeah":
                            $ evilweapon = 1
                            "You kiss her back"
                            scene v38116
                            with dissolve
                            fannay "Hmmm... I've missed a man's touch"
                            MC "You said you needed to be fucked right?"
                            fannay "Yes..."
                            MC "Then take off those clothes!"
                            scene v38117
                            with dissolve
                            "She imediately takes off her clothes"
                            fannay "Do you like my body?"
                            MC "Yes... But what can you do with it?"
                            scene v38118
                            with dissolve
                            fannay "Anything you want..."
                            MC "Good girl..."
                            scene v38119
                            with dissolve
                            fannay "Should I lie on the bed?"
                            MC "Is that even a question? Of course"
                            scene v38120
                            with dissolve
                            fannay "So eager... I like it..."
                            MC "You little tease..."
                            scene v38121
                            with dissolve
                            fannay "So... What do you want to do with me?"
                            MC "Spread your legs and you'll see"
                            scene v38122
                            with dissolve
                            fannay "I like where this is going..."
                            MC "You haven't seen anything yet"
                            scene v38123
                            with dissolve
                            "With her hand on her pussy she says..."
                            fannay "There's something you want from here?"
                            MC "..."
                            scene v38124
                            with dissolve
                            "You start by inserting your finger inside her"
                            fannay "Hmmm.... That feels nice..."
                            "You can't resist your urges to taste her pussy"
                            scene v38125
                            with dissolve
                            "So you do..."
                            fannay "Ah... Yes...Uhmmm"
                            MC "{i} Slurp, lick"
                            fannay "Yes! Keep going at it..."
                            scene v38126
                            with dissolve
                            "Her pussy has a pleasant sweet and salty taste"
                            fannay "Ah... Please don't stop..."
                            "But you do stop..."
                            MC "It's your turn to please me"
                            scene v38127
                            with dissolve
                            "You move, grab her head and push it towards your dick"
                            fannay "Oh... I will..."
                            scene v38128
                            with dissolve
                            "She puts her lips around your penis"
                            MC "That's it... Good girl"
                            MC "Time to go deeper"
                            "You push her head further"
                            scene v38129
                            with dissolve
                            fannay "Uhmm... Hmmm... {i} Slurp..."
                            MC "I said deeper!"
                            "You push her even more"
                            scene v38130
                            with dissolve
                            fannay "Mmmmmmh... "
                            MC "Yes... That's it..."
                            "She starts to move her head on her own..."
                            "You feel that somehow you're controlling her..."
                            scene v38131
                            with dissolve
                            MC "You like this don't you, you little slut?"
                            fannay "Yesh... I duhmmm..."
                            "You grab her head and force it all the way in"
                            scene v38132
                            with dissolve
                            fannay "{i} Cough cough"
                            MC "Ah... Yes... That's great"
                            fannay "Uhmmm {i} cough cough"
                            "You remove her head from your dick and push her on the bed"
                            scene v38133
                            with dissolve
                            fannay "Oh..."
                            MC "Now the real fun starts..."
                            "She has a mixed expression of surprise and desire"
                            "You don't waste another second..."
                            scene v38134
                            with dissolve
                            "You start to put it inside of her"
                            fannay "Ah... Damn... It's so big..."
                            MC "Shit you're really tight..."
                            "You begin to pound her almost immediately"
                            scene v38135
                            with dissolve
                            fannay "Ah... Yes!! That's it! YES!!"
                            "You now realize that you are fucking Fannay on your girlfriend's bed"
                            "But you can't control yourself... Something inside you just..."
                            "..Needs the pleasure...and it's so hot"
                            scene v38136
                            with dissolve
                            "You keep giving it to her with all your might"
                            fannay "Ah!! YES YES!!! I'm going to cum..."
                            MC "Take it all slut!! Cum!!"
                            fannay "AHHH!!!! FUCK!!! YEEESSS!"
                            MC "Get on all fours slut!"
                            scene v38137
                            with dissolve
                            "She obeys your command..."
                            "You're fucking her with all your strength"
                            "You begin to feel your orgasm coming"
                            fannay "AHHH... I can't take it anymore..."
                            menu:
                                "Cum inside her":
                                    $ fannaypregcount +=1
                                    scene v38138
                                    with dissolve
                                    MC "I'm gonna fill you up!!"
                                    show shot
                                    with hpunch
                                    hide shot
                                    MC "Fuck yeah..."
                                    show shot
                                    with hpunch
                                    hide shot
                                    fannay "Ahhhh.... Yes..."
                                    scene v38139
                                    with dissolve
                                    MC "Next time I want to try this hole..."
                                    jump afterfannaysexv38
                                "Pull out":

                                    scene v38138
                                    with dissolve
                                    MC "I'm about to cum..."
                                    scene v38140
                                    with dissolve
                                    fannay "Yes... Cum on me..."
                                    scene v38141
                                    with dissolve
                                    show shot
                                    with hpunch
                                    hide shot
                                    MC "Ahhh! Fuck yeah..."
                                    scene v38142
                                    with dissolve
                                    show shot
                                    with hpunch
                                    hide shot
                                    fannay "Ahhhh.... Yes..."
                                    MC "That was intense..."
                                    jump afterfannaysexv38
                                "Cum on her belly":

                                    scene v38138
                                    with dissolve
                                    MC "I'm about to cum..."
                                    scene v38140
                                    with dissolve
                                    fannay "Yes... Cum on me..."
                                    scene v38143
                                    with dissolve
                                    show shot
                                    with hpunch
                                    hide shot
                                    MC "Ahhh! Fuck yeah..."
                                    scene v38144
                                    with dissolve
                                    show shot
                                    with hpunch
                                    hide shot
                                    fannay "Ahhhh.... Yes..."
                                    MC "That was intense..."
                                    jump afterfannaysexv38
                                "Cum on her face":

                                    scene v38138
                                    with dissolve
                                    MC "I'm about to cum..."
                                    scene v38140
                                    with dissolve
                                    fannay "Yes... Cum on me..."
                                    scene v38143
                                    with dissolve
                                    show shot
                                    with hpunch
                                    hide shot
                                    MC "Ahhh! Fuck yeah..."
                                    scene v38145
                                    with dissolve
                                    show shot
                                    with hpunch
                                    hide shot
                                    fannay "Ahhhh.... Yes..."
                                    MC "That was intense..."
                                    jump afterfannaysexv38
        "Leave":


            MC "I don't care... I'm out"
            $ sexv038 = 6
            $ renpy.end_replay()
            jump lustlairv38

label afterfannaysexv38:
    $ renpy.end_replay()
    scene v38146
    with dissolve
    fannay "That was..."
    MC "Awesome..."
    "She cleans herself"
    scene v38147
    with dissolve
    fannay "I don't know what you did... But...Yes... That was awesome"
    "You don't know what you did either but it felt great..."
    fannay "I need to go now..."
    scene v38148
    with dissolve
    fannay "I... Um... Bye..."
    MC "..."
    MC "I'll be waiting for next time Fannay"
    jump lustlairv38

label lustlairv38:
    scene meanwhile
    with dissolve
    scene v38149
    with dissolve
    lust "Now my children... You'll help me..."
    lust "Won't you?"
    isabella "Yes... Mistress..."
    lust "You will love me?"
    lili "Yes my mistress..."
    scene v38150
    with dissolve
    lust "Good girls... You'll be quite useful to my plans"
    lust "My precious things..."
    scene v38151
    with dissolve
    lust "Isabella my dear... Rise... "
    isabella "Yes mistress"
    scene v38152
    with dissolve
    isabella "What can I do to please?"
    lust "Oh my dear... There is so much you can do..."
    lust "But the first thing..."
    scene v38153
    with dissolve
    lust "Your little group... The big bad Demon Hunters"
    lust "I want to know everything..."
    isabella "Yes mistress..."
    scene v38154
    with dissolve
    lust "And you my lovely queen Zordruza..."
    lust "You'll be one of my greatest assets..."
    lust "Won't you?"
    zordruza "Everything for you my mistress"
    scene v38155
    with dissolve
    lust "So pretty... And so much sorrow..."
    lust "Don't worry I'll take good care of you"
    jump afterlustlairv38

label afterlustlairv38:
    scene mcroomad
    with dissolve
    "You are back on your room..."
    MC "I really need a rest after all this..."
    if my_path_is == "evil":
        if evilweapon == 1:
            $ weapon = 1
            MC "I could also read that book Fannay was hiding"
            show bookv38aa
            with dissolve
            MC "Ritual of the Bound Weapon..."
            "After reading the book you feel that you gained something..."
            "A spectral weapon that will allow you to fight hand to hand"
            "You can now use melee during combat"
            hide bookv38aa
            jump postevilv38
        else:

            MC "I'm tired I should lie down..."
            "You feel something under your pillow..."
            MC "What is this?"
            show bookv38aa
            with dissolve
            MC "Ritual of the Bound Weapon? Who put this here?"
            "After reading the book you feel that you gained something..."
            "A spectral weapon that will allow you to fight hand to hand"
            "You can now use melee during combat"
            hide bookv38aa
            jump postevilv38

    if my_path_is == "neutral":
        if devilbloodbottle == 1:
            MC "What about that bottle Rolf gave me?"
            MC "Now it's the perfect time to try it"
            scene v38218
            with dissolve
            MC "I wonder what will happen... Demon blood..."
            MC "Fuck it! Let's do it"
            scene v38219
            with dissolve
            MC "Bottoms up!"
            MC "Shit.... This is terrible..."
            MC "What is..."
            show shot
            with hpunch
            MC "Hmmmm..."
            hide shot
            scene v38220
            with dissolve
            MC "Cough Cough...What..."
            MC "Cough Cough.... This is..."
            scene v38221
            with dissolve
            MC "It's..."
            "You start to feel your senses leave you"
            show blink1
            with dissolve
            show blink2
            with dissolve
            show blink3
            with dissolve
            scene black
            with dissolve
            MC "Shit..."
            "Toc toc toc..."
            MC "What is this?"
            "Toc toc toc..."
            "You force your eyes open"
            scene v38222
            show blink3
            with dissolve
            MC "What is that?"
            hide blink3
            show blink2
            MC "Where am I... Is this an illusion? An hallucination?"
            hide blink2
            show blink1
            MC "You... Who are you?"
            scene v38223
            show blink1
            with dissolve
            demon "Pfff... Another one... Fuck you!!"
            hide blink1
            MC "What do you mean? What is this place?"
            demon "Fucking mortals... You're all the same..."
            demon "YOU ARE ALL THE SAME!!! YOU ARE ALL... Wait..."
            scene v38224
            with dissolve
            demon "You... You're not the same... AHAHAHA"
            demon "You are not the same!! AHAHAHA"
            MC "Can you explain me what's going on? Who are you?"
            demon "Ahahaha..... Ahahaha"
            demon "You're not a regular mortal..."
            demon "You might be able to defeat me... And release me..."
            demon "Ahahaha... Ahahaha"
            "You start to feel a lot of energy coming from the creature"
            demon "Get ready!!"
            $ companion = 0
            $ enemy = "v38demon"
            jump combat
        else:
            jump postevilv38
    else:
        jump postevilv38


label v38afterdemon:
    scene v38225
    with dissolve
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    demon "AHAHAHA... I knew it... You did it..."
    demon "Ahahaha I'm finally free!!! Ahahah"
    "You see the demon rising..."
    scene v38224
    with dissolve
    "It looks like his power is growing again..."
    MC "Oh shit..."
    demon "Let me savor your power..."
    $ powercount = Destpoints + Iluspoints + Healpoints + Mystpoints + Summpoints + Altepoints + Necropoints + 5

    $ Destpoints = 0
    $ Iluspoints = 0
    $ Healpoints = 0
    $ Mystpoints = 0
    $ Summpoints = 0
    $ Altepoints = 0
    $ Necropoints = 0
    "All your skills went down to 0"
    demon "Hmmm.... Yes... You're not a regular one..."
    MC "Why do I feel so weak? What have you done?"
    demon "I've reset you skills..."
    MC "What??!"
    demon "I'll give them back don't worry, and since you helped me..."
    demon "I'll even add 5 extra points... See? Demons can be generous too"

    scene black
    nvl clear
    n "You will now redistribute all your skills"
    n "With a bonus of 5 extra points"


label checkskills_n38:
    if powercount >= 1:
        jump keepchoosingv38n
    else:
        jump nextfasev38neutral


label keepchoosingv38n:
    "You have [powercount] skill points to assign"
    menu:
        "Raise Battlemagic {image=001battle}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))

            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Destpoints = skillcheck + Destpoints
                "Your Battlemagic skill improved"
                $ powercount = powercount - skillcheck
        "Raise Summoning {image=001summon}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))

            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Summpoints = skillcheck + Summpoints
                "Your Summoning skill improved"
                $ powercount = powercount - skillcheck
        "Raise Alteration {image=001alteration}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Altepoints = skillcheck + Altepoints
                "Your Alteration skill improved"
                $ powercount = powercount - skillcheck
        "Raise Illusion {image=001illusion}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Iluspoints = skillcheck + Iluspoints
                "Your Illusion skill improved"
                $ powercount = powercount - skillcheck
        "Raise Mysticism {image=001myst}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Mystpoints = skillcheck + Mystpoints
                "Your Mysticism skill improved"
                $ powercount = powercount - skillcheck
        "Raise Healing{image=001heal}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Healpoints = skillcheck + Healpoints
                "Your Healing skill improved"
                $ powercount = powercount - skillcheck
        "Raise Necromancy{image=001necro}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv38n
            else:
                $ Necropoints = skillcheck + Necropoints
                "Your Necromancy skill improved"
                $ powercount = powercount - skillcheck

    jump checkskills_n38

label nextfasev38neutral:
    scene v38225
    with dissolve
    "There you go... You're so big and strong... Ahahahaha"
    scene black
    with dissolve
    scene mcroomad
    with dissolve
    MC "Shit!! Was that a nightmare?! What the hell?"
    "But it's clear it wasn't... You feel stronger"
    MC "Now I really need a rest..."
    "You start to feel your eyes shut"
    scene black
    with dissolve
    "You fell asleep"
    jump katwakeupv38

label postevilv38:
    "Lying on the bed you start to feel your eyes closing"
    scene black
    with dissolve
    "You fell asleep"
    jump katwakeupv38

label katwakeupv38:
    scene black
    with dissolve
    scene mcroomad
    with dissolve
    MC "Yawn... How long did I sleep?"
    MC "I should try to find the Archmage"
    "You leave the room and start looking for her"
    scene v38156
    with dissolve
    "As you travel towards the throne"
    "You notice some unknown people"
    MC "I wonder who they are..."
    katriona "Hey there, my little flower boy"
    scene v38157
    with dissolve
    MC "Would you just stop with that already?"
    katriona "Hmmmm let me think.... No"
    MC "You're infuriating sometimes."
    katriona "Thank you"
    MC "Never mind"
    MC " Anyway, who are those people?"
    katriona "Nagatashi royalty or something like that..."
    MC "Nagatashi huh? The girl is looking at us..."
    katriona "Well then, let's introduce you to them..."
    scene v38158
    with dissolve
    "You and Katriona approach them"
    ayna "Oh [MC] ! You are right on time"
    scene v38160
    with dissolve
    ayna "Meet Lord Heihachi and his daughter..."
    ayna "Princess Ryo, from Sarojini family"
    scene v38159
    with dissolve
    "Look at those eyes..."
    MC "My pleasure... I'm [MC]"
    scene v38160
    with dissolve
    ayna "[MC], can you please show the princess around the College?"
    MC "I guess... But what about..."
    ayna "Please?"
    MC "Very well, Archmage..."
    scene v38161
    with dissolve
    "You and princess Ryo left the others"
    "She's pretty but you feel like she's not easy to deal with"
    scene v38162
    with dissolve
    MC "So... Princess... You like it here?"
    ryo "Anata wa dai bakadesu"
    MC "Say what?"
    ryo "Anata wa dai bakadesu!"
    MC "..."
    ryo "Typical... You all think we should speak your language..."
    ryo "But you have no clue about ours..."
    MC "Oh boy... I see where this is going..."
    "You take her to the courtyard"
    scene v38163
    with dissolve
    MC "Well, this is our courtyard..."
    ryo "I can see that, you know?"
    ryo "I'm from a different country, not blind"
    ryo "Or maybe you saw my eyes and thought my vision was weird?"
    MC "I apologize if you misunderstood me"
    scene v38164
    with dissolve
    ryo "Do I scare you?"
    MC "Scare me? What do you mean?"
    ryo "Every single person on my kingdom fears me"
    ryo "So I can't trust anyone... Or ask for honesty"
    scene v38165
    with dissolve
    ryo "So do I scare you?"
    MC "Ahahah... I don't even know you..."
    MC "But no.. You don't scare me..."
    scene v38166
    with dissolve
    ryo "Good... Then... Let's fight!!"
    MC "What? Fight? Why would I want to fight?"
    scene v38167
    with dissolve
    ryo "Just as I imagined... You're just like the others"
    MC "I just don't have a reason to fight you..."
    ryo "Because I'm asking you to?"
    MC "You know that I'm a Mage right?"
    scene v38168
    with dissolve
    ryo "Show it to me... Show me what a Mage is capable of"
    MC "Do you really want to?"
    scene v38170
    with dissolve
    ryo "You think that you're the only Mage in the world?"
    MC "No... But I know we are pretty rare... Are you a Mage as well?"
    scene v38171
    with dissolve
    "Without a word she's starts doing some weird acrobatics to kick you"
    "You barely manage to dodge"
    scene v38172
    with dissolve
    ryo "Good reflexes, you're faster than I expected"
    MC "What the hell? Why did you do that?"
    scene v38173
    with dissolve
    "And she tries to attack you again!"
    "This time it was so close you felt the air on your face"
    "Somehow you feel that she's not hitting you on purpose"
    scene v38174
    with dissolve
    ryo "Is that all a Mage can do? Dodge? Ahaha"
    ryo "Or is this that spell you call Stone Skin, where you don't make a move at all?"
    MC "Ahaha you think you're funny... Let me show you..."
    show shot
    with hpunch
    show shot
    with vpunch
    hide shot
    scene v38169
    with dissolve
    MC "You see? This is magic.. I didn't even have to move..."
    "She looks surprised, and intrigued..."
    scene v38166
    with dissolve
    ryo "Finally... Someone that takes me serious..."
    MC "Hmmm...I.."
    fannay "Who do we have here?"
    scene v38175
    with dissolve
    fannay "Mister important and some new cute girl"
    MC "Hi Fannay..."
    scene v38176
    with dissolve
    fannay "Pleasure to meet you cutie, I'm Fannay"
    ryo "Stay away..."
    "That was kind of weird..."
    scene v38177
    with dissolve
    fannay "The Archmage asked me to feed you, that's why I'm here"
    MC "Feed us?"
    fannay "You know... take you to the kitchen for a meal?"
    scene v38178
    with dissolve
    fannay "Come on let's go... Both of you"
    "Ryo looks at Fannay with very piercing eyes"
    scene v38179
    with dissolve
    ryo "Come with me, or I might kill that bitch..."
    "After that she said some more words you have no idea the meaning of"
    scene v38181
    with dissolve
    MC "I'm... right behind you..."
    scene v38180
    with dissolve
    ryo "Shouldn't you be the one showing me this place?"
    ryo "Why am I going on front?"
    MC "Just being polite, ladies first and such"
    "She's not easy at all..."
    scene v38182
    with dissolve
    "You both reach the kitchen where Fannay is waiting"
    fannay "Who died? Why the long faces?"
    fannay "Come on, let's eat something... And drink..."
    scene v38183
    with dissolve
    ryo "Can I kill her? Is she important?"
    MC "Ahahah... I'd rather you didn't"
    menu:
        "Sit next to Fannay":
            $ sitnextto = "fannay"
            scene v38184
            with dissolve
            fannay "Hey Nagatashi princess girl... Alright, suit yourself"
            fannay "There is plenty of food here for us"
            scene v38185
            with dissolve
            fannay "Care for a drink [MC]?"
            MC "Sure..."
            scene v38186
            with dissolve
            MC "Go ahead..."
        "Sit next to Ryo":


            $ sitnextto = "ryo"
            scene v38187
            with dissolve
            fannay "You're already prefering that girl over me?"
            fannay "Meh... typical..."
            scene v38188
            with dissolve
            fannay "At least this bottle of wine doesn't disappoint me..."
            fannay "A toast?"
            MC "Sure..."
            scene v38189
            with dissolve
            "Ryo look intrigued by you two"
            fannay "Cheers!"
            scene v38190
            with dissolve
            MC "Cheers!"

    scene v38191
    with dissolve
    "After some time eating, drinking and talking"
    "You all leave the table, the mood has lightned"
    fannay "Princess, come with me I'll show you your room"
    MC "Princess, take care. Please don't kill her."
    ryo "We'll see"
    scene v38192
    with dissolve
    fannay "[MC] you should meet the Archmage"
    "Once again... you move to the throne room"
    scene v38206
    with dissolve
    "The Archmage and Mistress Katriona are awaiting you"
    MC "Hello again... So is the meeting over?"
    ayna "Over? Ha, no it hasn't even started..."
    ayna "Do you think we would have a meeting without you?"
    katriona "Yeah... You have been closer to the enemy than anyone"
    scene v38207
    with dissolve
    ayna "But we are still waiting for some more people to arrive"
    katriona "We need to know on who we may count..."
    scene v38206
    with dissolve
    ayna "Katriona and I were talking"
    ayna "And we've been wondering what happened with the Orcs"
    ayna "I imagine that the Slayers defeated them"
    scene v38207
    with dissolve
    katriona "So that's what we are going to go find out"
    MC "We?"
    katriona "You and me"
    ayna "Very well"
    scene v38206
    with dissolve
    ayna "Good luck you two, hope to see you soon"
    scene v38208
    with dissolve
    katriona "Shall we go little flower boy?"
    MC "Sigh.. so we're going to the Orc Lands?"
    katriona "Yes..."
    MC "With the big, smelly, brutish orcs?"
    katriona "Oh come on, you'll fit right in"
    MC "You just don't stop, do you?"
    katriona "All these years of me giving you shit, you'd think you'd learn"
    MC "I don't know why I put up with you"
    katriona "Because I've been like a sister to you?"
    MC "Yeah, sure, that must be it..."
    scene v38209
    with dissolve
    katriona "Come along my little orc boy"
    MC "Better than flower boy, at least"
    katriona "To the portal room!"
    scene v2210
    with dissolve
    katriona "Hop in..."
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    scene v38210
    with dissolve
    katriona "What the hell happened here?!"
    MC "A battle?"
    katriona "Yeah.. But who won? Where are the bodies?"
    MC "I have a bad feeling about this..."
    "That burning feeling inside you returns"
    MC "Oh... not this again..."
    scene v38211
    with dissolve
    katriona "I've never seen something like this..."
    katriona "No bodies... No blood... This can't be..."
    "The thing inside you is emanating anger...Fury..."
    scene v38212
    with dissolve
    katriona "There was clearly a battle here..."
    katriona "Between Orcs and the damned Slayers"
    katriona "And..."
    scene v38213
    with dissolve
    katriona "Theres someone here..."
    MC "What?!"
    katriona "We know you're there!! Come out..."
    scene v38226
    with dissolve
    "You see a green figure emerge from the rocks"
    katriona "It's an Orc... A young female"
    MC "Looks like she's ready to fight..."
    scene v38227
    with dissolve
    katriona "Hey, please calm down... We don't want to hurt you"
    katriona "Do you understand us?"
    katriona "It looks like she..."
    scene v38228
    with dissolve
    katriona "Is about to faint..."
    "The young orc falls to the ground"
    scene v38229
    with dissolve
    katriona "Poor thing... I wonder what she witnessed..."
    show shotr
    with vpunch
    hide shotr
    MC "Grah... What the...."
    show shotr
    with vpunch
    hide shotr
    MC "Again?... What is this feeling?"
    scene v38230
    with dissolve
    katriona "Holy shit...."
    MC "My head....What's wrong?"
    katriona "Look..."
    scene v38231
    with dissolve
    MC "What is that thing?"
    katriona "looks like some sort of demon..."
    MC "Demon?"
    demon "Food? Need food... Hehehe"
    katriona "Get ready... This is going to be ugly"
    MC "Not any uglier than him..."
    show shotr
    with hpunch
    hide shotr
    "Once again the thing inside you feels like it wants to come out"
    scene v38232
    with dissolve
    demon "FOOD!!"
    katriona "Watch out!!"
    show shotr
    with hpunch
    hide shotr
    scene v38233
    with dissolve
    show shotr
    with hpunch
    hide shotr
    katriona "How did you do that?"
    MC "My head... Hmmm..."
    "Did you just push the demon away?"
    scene v38235
    with dissolve
    demon "FOOD!! I'm hungry!!"
    katriona "Get ready... Here he comes again..."
    show shotr
    with dissolve
    MC "I'm...Ready..."
    $ companion = 1
    $ companion_name = "Katriona"
    $ enemy = "v38fatdemon"
    jump combat

label v38afterfatdemon:
    $ companion = 0
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    stop music
    play sound "sounds/beat.mp3"
    scene v38233
    with dissolve
    "You see the demon on the ground..."
    show shotr
    with hpunch
    hide shotr
    "It like you are pulling his very essence towards you..."
    show shotr
    with hpunch
    hide shotr
    "But you can't control it..."
    show shotr
    with hpunch
    MC "I... "
    show shotr
    with hpunch
    menu:
        "Resist the stone":
            "You need all your will to resist it..."
            $ resistsoulstone = 0
        "Pull the demon essence to you":

            "You feel like something is being transfered from the creature to you"
            $ resistsoulstone = 1

    scene v38234
    show shotr
    katriona "Are you ok? [MC]? [MC]?!! Hey!!"
    "Her voice starts to fade..."
    show blink1
    with dissolve
    show blink2
    with dissolve
    show blink3
    with dissolve
    scene black
    with dissolve
    "And you lose your senses..."
    stop sound
    jump v39
