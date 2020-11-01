label v026good:
    scene v25179
    with dissolve
    ayna "That was good but you have so much to learn"
    ayna "I hope you are ready for all the work you'll have to put in"
    MC "I am!"
    scene v25180
    with dissolve
    ayna "We're always looking for potential Elites"
    "Did she just say that you can become an Elite?"

    kitargo "Archmage you here!"
    scene v3g001
    with dissolve
    "You see Kitargo entering the training room"
    ayna "Hello Kitargo, what brings you here?"
    "Why is he dressed in some old rags?"
    kitargo "Kitargo needs to return home yes?"
    kitargo "Kitargo was called by elder Jithak"
    ayna "Is everything alright there?"
    kitargo "Kitargo don't know... Kitargo must go and see"
    ayna "Of course, you are free to return anytime"
    scene v3g002
    with dissolve
    ayna "[MC], I think you should go with Kitargo"
    ayna "Jithak is a different place and it's always good to discover new places"
    MC "Very well"
    scene v3g003
    with dissolve
    kitargo "[MC] coming with Kitargo? That's good!"
    kitargo "[MC] good friend! Will show you my land"
    ayna "So it's settled, follow me to the portal room"
    ayna "[MC], whenever you wish to return just let me know"
    ayna "I'll cast an enchantment on you"
    MC "Very well"
    scene black
    with dissolve
    "You all went to the portal room and the in next moment you and Kitargo teleport"
    scene v3g004
    with dissolve
    kitargo "See? This is Kitargo land! Very good right?"
    MC "Yeah... Sure..."
    kitargo "Yes! Good!"
    MC "So where is everybody?"
    kitargo "Kitargo wonders.."
    scene v3g005
    with dissolve
    kitargo "Kitargo must look for elder"
    scene v3g006
    with dissolve
    "All the tents look empty but you spot one that isn't"
    kitargo "Look! Is Elder!"
    scene v3g007
    with dissolve
    "As you reach the tent you can see another Jithak"
    elderjit "Kitargo bhenvind! Ke thu khompa?"
    "They start talking some language you don't understand"
    scene v3g008
    with dissolve
    elderjit "Thu hemans hestranh phoder"
    MC "Is she talking to me?"
    kitargo "Yes, elder says you have strange power"
    scene v3g009
    with dissolve
    elderjit "Thu... hes ho..."
    scene v3g010
    with dissolve
    elderjit "Hescolhet!!"
    MC "Hmmm... Kitargo a little help here..."
    scene v3g008
    with dissolve
    MC "What was that?"
    kitargo "Elder says you chosen yes? You come with me to mountains"
    "That's not the first time someone has told you something like that"
    scene v3g009
    with dissolve
    elderjit "Hiras deschobr thi"
    scene v3g008
    with dissolve
    MC "Ok... Should we go then?"
    kitargo "Yes, follow Kitargo!"
    scene black
    with dissolve
    "You and Kitargo walk for a while until you reach an entrance"
    scene v3g011
    with dissolve
    kitargo "This sacred place for Jithak"
    MC "Is this the place you wanted me to visit?"
    kitargo "Yes! Elder says you chosen, must visit"
    MC "Very well, lead on"
    scene v3g012
    with dissolve
    "You follow him to the entrance"
    "You wonder what's inside and why would the Elder say that you are the chosen"
    scene v3g013
    with dissolve
    kitargo "Ready to enter?"
    "You feel some power coming from inside"
label v3gentrance:
    scene v3g014
    with dissolve
    menu:
        "What's inside?":
            kitargo "Temple of Gods, my people guard and worship here"
            kitargo "Gods gave temple to Jithak people"
            jump v3gentrance
        "Why was the elder alone?":

            kitargo "Storm coming, Elder stay to tell Kitargo"
            kitargo "Jithak people always moving around"
            jump v3gentrance
        "Who is the chosen?":

            kitargo "[MC] is chosen"
            MC "What does it mean?"
            kitargo "Kitargo don't know, must enter the temple"
            jump v3gentrance
        "Alright, let's get in":

            kitargo "Yes let's get in"
            jump v3gtemple

label v3gtemple:
    scene v3g015
    with dissolve
    "You enter the temple and it's amazing"
    MC "Wow! I wasn't expecting this at all"
    scene v3g016
    with dissolve
    kitargo "Temple is most sacred place of Jithak"
    kitargo "Place of Gods"
    "As you advance to the middle you start to feel strange"
    scene v3g017
    with dissolve
    MC "Are you feeling anything strange?"
    kitargo "..."
    MC "Kitargo?"
    kitargo "..."
    MC "Are you listening to me?"
    kitargo "..."
    Nonen "He will not answer you"
    scene v3g018
    with dissolve
    MC "What the? Who said that?"
    Nonen "You came here to talk to her, didn't you?"
    MC "I don't know what you are talking about..."
    "You feel your body being lifted from the floor"
    MC "Hey! What is happening?"
    scene v3g019
    with dissolve
    Nonen "Don't you know who you are?"
    MC "What is..."
    scene v3g020
    with dissolve
    MC "Hey put me down!"
    scene v3g021
    with dissolve
    MC "What are you doing? These guys... I..."
    scene v3g022
    with dissolve
    "You now feel some amazing power around you"
    "It's incredible, yet familiar"
    MC "I... "
    scene black
    with dissolve
    MC "I've felt this before... I"
    scene v3g032
    with dissolve
    "You open your eyes and see someone familiar"
    MC "You..."
    fvoice "Hello again [MC] come closer please"
    scene v3g033
    with dissolve
    "You feel so good close to her, so warm..."
    fvoice "I'm so glad... I'm proud of you"
    MC "Who are you?"
    scene v3g034
    with dissolve
    fvoice "Now [MC] calm down, you know I would never hurt you right?"
    MC "Yes... You helped me when I was a child... I remember you..."
    MC "Ah... My head... I..."
    "She gets closer"
    scene v3g035
    with dissolve
    "You feel so much peace, you feel so good..."
    fvoice "Now [MC], are you feeling better?"
    MC "Yes... I feel so calm..."
    fvoice "That's good, like I was saying I'm proud of you"
    fvoice "You turned out to be a good person"
    scene v3g036
    with dissolve
    fvoice "You'll have an important role in the wars to come"
    fvoice "I'm glad that you'll be ready to help people"
    scene v3g038
    with dissolve
    fvoice "You will face great dangers, real evil is coming for you"
    fvoice "You must be prepared!"
    scene v3g036
    with dissolve
    fvoice "I'm sure you have many questions"
    fvoice "Ask what you want, I'll answer what I must"
    $ v3goodtalk = 0
label v3gtalkwithher:
    scene v3g036
    with dissolve
    menu:
        "Who are you?":
            fvoice "I can't tell you yet, but you will find out soon enough"
            scene v3g037
            with dissolve
            fvoice "Just know that I'll be always here for you"
            jump v3gtalkwithher
        "Who am I? Why do people say I have some kind of power?":

            fvoice "Because you do have power, don't you feel it?"
            fvoice "Don't you feel it in your dreams? Your learning speed?"
            fvoice "You are more powerful than most people and you are barely an adult"
            scene v3g037
            with dissolve
            MC "What does that mean?"
            fvoice "Most mages that you know have years and years of training and study"
            fvoice "Some of them have over 100 years of practice"
            fvoice "You have barely trained 10 years and you are already a challenge to most of them"
            scene v3g036
            with dissolve
            fvoice "Soon enough you'll surpass them all"
            MC "All of them? What about the Elite?"
            fvoice "Believe me, all of them..."
            MC "But how? I can't even comprehend how the Archmage does some of her spells"
            scene v3g037
            with dissolve
            fvoice "You will"
            $ v3goodtalk = 1
            jump v3gtalkwithher

        "What is this evil that's coming for me?" if v3goodtalk == 1:
            fvoice "You can feel it don't you?"
            MC "I'm not sure of what you mean..."
            fvoice "When I say evil what comes to your mind?"
            MC "Demons? The Slayers?"
            fvoice "Well, that's one point of view, but real evil could be closer than you think"
            MC "What do you mean?"
            fvoice "Imagine someone with infinite power but the desire to destroy everything"
            $ v3goodtalk = 2
            fvoice "That's the real evil"
            MC "Is that even possible?"
            fvoice "Not only is it possible but it already happened once in the past"
            MC "Damn! Is it happening again?"
            fvoice "Maybe..."
            jump v3gtalkwithher
        "Have you been present since my childhood?":


            fvoice "The short answer, yes..."
            MC "And the long answer?"
            scene v3g037
            with dissolve
            fvoice "I've been present since you were born"
            jump v3gtalkwithher

        "I have so many more questions" if v3goodtalk == 2:
            fvoice "I'm sure you have, but it's time to wake now"
            scene v3g038
            with dissolve
            fvoice "You and your friend are in danger"
            fvoice "You'll have to face a challenge, be prepared"
            MC "Wait... Can I at least know your name?"
            scene v3g037
            with dissolve
            fvoice "Ataegina..."
            scene black
            with dissolve
            "Ataegina she said..."
            jump v3goodcombat

label v3goodcombat:
    scene v3g024
    with dissolve
    Nonen "How dare you disturb me with that energy?!"
    Nonen "You will not leave this place alive!"
    MC "What the?"
    $ enemy = "evilstatue"
    jump combat

label killedstatuev3g:

    scene v3g025
    with dissolve
    "You see the strange statue dissolving"
    scene black
    with dissolve
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    scene v3g026
    with dissolve
    kitargo "[MC]!! Hey [MC]!!"
    scene v3g027
    with dissolve
    kitargo "Wake up! Temple is crumbling!"
    scene v3g027
    with hpunch
    scene v3g027
    with vpunch
    MC "What happened?"
    scene v3g027
    with hpunch
    scene v3g027
    with vpunch
    kitargo "[MC] fainted! Kitargo don't know why"
    scene v3g027
    with hpunch
    scene v3g027
    with vpunch
    kitargo "Follow Kitargo fast!"
    scene v3g027
    with hpunch
    scene v3g027
    with vpunch
    MC "Lead the way!"
    scene v3g028
    with dissolve
    "You followed Kitargo to some cave"
    MC "What the hell happened?"
    kitargo "Kitargo don't know... Kitargo saw [MC] faint and all temple trembled"
    kitargo "Kitargo wake [MC] to run to cave"
    MC "Now we need to get out of here, do you know the way out?"
    kitargo "Kitargo don't know exit"
    MC "I guess we will have to look for one then"
    $ companion = 1
    $ companion_name = "Kitargo"


label v3cave_good:
    scene v3evilcave_00

    call screen v3goodcave

label v03goodspider:
    scene v3g029
    with dissolve
    "As you and Kitargo are looking around"
    "A Giant Spider appear"
    MC "Ah fuck..."
    $ enemy = "Gspidergv3"
    jump combat

label killedspiderv3g:
    stop music
    play music "<loop 0.0>vampsong.mp3" fadein 5
    hide screen MC_bars
    hide screen hpbar
    scene v3g039
    with dissolve
    kitargo "Spider dead, we good!"

    jump v3cave_good

label v03goodexit:
    $ companion = 0
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v3g030
    with dissolve
    "You found the exit"
    kitargo "We found exit, we good and strong!"
    MC "Yeah... We are, I guess this is where we take separate paths"
    kitargo "Yes friend! I stay with Jithak, [MC] can visit Kitargo anytime"
    scene v3g031
    with dissolve
    "You shake your hands as a goodbye"
    katarro "Glad to see you are ok"
    scene v3g041
    with dissolve
    MC "What the?"
    "This guy.. always sneaking like this"
    kitargo "Master Katarro, very good magic"
    scene v3g040
    with dissolve
    katarro "The Archmage and I felt some unbelievable power for a brief moment"
    katarro "And it was you [MC], what happened?"
    MC "I wish I knew..."
    katarro "Very well, I'm here to take you back. The Archmage's enchantment was destroyed"
    MC "What do you mean?"
    katarro "She put an enchantment on you before you came here right?"
    MC "Yes, so that when I was ready to go I could tell her"
    katarro "Your burst of powers seems to have destroyed that enchantment"
    katarro "Don't ask me how, I don't have any idea"
    katarro "Let's go, I have other matters to attend to"
    scene v3g041
    with dissolve
    kitargo "Goodbye friend!"
    $ wheretoafterslayerbath = "Good"
    $ gotrobev3good = 0
    jump slayerbathv26


label v026goodpart2:
    scene v2203
    with dissolve
    katarro "Now go meet the Archmage, she is in her room"
    scene v2204
    with dissolve
    katarro "Bye..."
    MC "That guy sure is weird..."

label travelinsidecollegev3g:
    scene collegeblue
    call screen collegebluev3

label collegeportalroomv3:
    scene portalroom
    with dissolve
    MC "There is nothing to do here"
    jump travelinsidecollegev3g

label collegelibraryv3:
    scene library
    with dissolve
    MC "There is nobody here, I wonder where Yisnna is..."
    jump travelinsidecollegev3g

label throneroomcollegev3:
    MC "There is no reason to go there"
    jump travelinsidecollegev3g

label liliroomcollegev3:
    MC "The door is locked, guess she's out"
    jump travelinsidecollegev3g

label classroomcollegev3:
    scene classroommiss
    with dissolve
    MC "There is nobody here, classes must have ended already"
    jump travelinsidecollegev3g

label bathroomcollegev3:
    scene bathhousemiss
    with dissolve
    MC "There is nobody here"
    jump travelinsidecollegev3g


label v2exitroom01v3:
    "That's where I am"
    jump travelinsidecollegev3g

label courtyardv3:
    if gotrobev3good == 0:
        MC "I need to find the Archmage, she's in her room"
        jump travelinsidecollegev3g
    else:
        MC "I'm tired, I need to go to my room"
        jump travelinsidecollegev3g

label mcroomv2:
    if gotrobev3good == 0:
        scene v3g053
        with dissolve
        MC "This is my room. I need to find the Archmage, then I can sleep"
        jump travelinsidecollegev3g
    else:
        scene v3g053
        with dissolve
        MC "Here we are..."
        fannay "So this is where you are"
        scene v3g054
        with dissolve
        MC "Fannay!?"
        fannay "You still remember my name? That's good"
        scene v3g055
        with dissolve
        fannay "Good to know that being the hotshot around here didn't affect your memory"
        MC "Ahaha yeah right..."
        fannay "So tell me where have you been? Most of us are leaving the College now"
        MC "What? why?"
        fannay "Because we've graduated duh..."
        MC "Are you leaving too?"
        fannay "I'm not sure yet, I need to think about that"
        scene v3g056
        with dissolve
        fannay "Anyway I guess you are staying? Look at that fancy robe"
        MC "Yeah I've been training with the Archmage"
        fannay "Awesome, well enough small talk, kiss me!"
        MC "What?"
        scene v3g057
        with dissolve
        menu:
            "Kiss her[ablovecolor] [ablove]":
                fannay "Hmmmm, you are a good kisser"
                scene v3g058
                with dissolve
                "She pushes you to the bed"
                $ fannaylove += 1
                "Fannay love increased"

                MC "Hey wait..."
                scene v3g060
                with dissolve
                fannay "{i}Giggle{/i} you think a kiss is enough for me?"
                scene v3g061
                with dissolve
                amida "[MC] are you here?"
                amida "Oh... Fannay... You're here..."
                fannay "Oh hi cutie"
                scene v3g062
                with dissolve
                fannay "You are such a beauty"
                fannay "No wonder [MC] here doesn't want anything to do with me"
                amida "I..."
                scene v3g063
                with dissolve
                fannay "Look at this face... You are so pretty Mida"
                fannay "I just want to..."
                scene v3g064
                with dissolve
                fannay "... Kiss you"
                menu:
                    "Stop this":
                        MC "Stop it Fannay"
                        scene v3g066
                        with dissolve
                        "Fannay looks a bit surprised"
                        fannay "Very well, I know when I'm not wanted..."
                        scene v3g070
                        with dissolve
                        fannay "Bye..."
                        $ midalove += 1
                        $ fannaylove -= 1

                        "Mida love increased, Fannay love decreased"
                        jump afterfannayv3g
                    "[abgreen]Let her continue":

                        scene v3g064
                        with dissolve
                        if midacorr >=3:
                            scene v3g067
                            with dissolve
                            "Is Mida allowing this?"
                            scene v3g068
                            with dissolve
                            "You can see both girls kissing in front of you"
                            fannay "Hmmm such sweet lips"
                            scene v3g069
                            with dissolve
                            fannay "I bet your boyfriend here got hard watching us..."
                            MC "That was very sexy..."
                            $ midacorr += 1

                            $ fannaycorr += 1
                            "Mida and Fannay corruption increased"
                            fannay "Time to go..."
                            scene v3g070
                            with dissolve
                            fannay "Enjoy the gift you two! Bye!"
                            scene v3g071
                            with dissolve
                            amida "You look like you enjoyed it {i}giggle{/i}"
                            jump afterfannayv3g
                        else:
                            scene v3g065
                            with dissolve
                            amida "Stop it... I only kiss [MC]"
                            scene v3g070
                            with dissolve
                            fannay "Very well I'm leaving..."
                            scene v3g071
                            with dissolve
                            amida "Fannay is crazy..."
                            $ midacorr += 1
                            "Mida corruption increased"
                            jump afterfannayv3g
            "Reject her[abred] [abnoloveidiot]":





                scene v3g056
                with dissolve
                fannay "Ouch... I guess you only have eyes for that princess of yours..."
                $ fannaylove -= 1
                "Fannay Love decreased"

                scene v3g059
                with dissolve
                fannay "Very well, bye"
                "She left"
                scene v3g101
                with dissolve
                amida "Hello [MC], Archmage told me you just arrived"
                MC "That is correct"
                jump afterfannayv3g



label aynaroomv2v3:
    if gotrobev3good == 0:
        scene v3g042
        with dissolve
        "You enter the Archmage's room and she's waiting for you"
        ayna "Hi [MC], I'm glad you're here"
        MC "You wanted to see me?"
        ayna "Yes, I've been preparing a spell for you"
        MC "For me? What kind of spell?"
        scene v3g043
        with dissolve
        ayna "Let me show you"
        ayna "You see this book? Try to read it"
        scene v3g044
        with dissolve
        MC "I can feel some energy coming out of it..."
        ayna "That's good, can you read it?"
        MC "I'm not sure... I don't think I understand that language"
        ayna "Try a bit harder please"
        scene v3g045
        with dissolve
        MC "I'm seeing something different now, it's like..."
        MC "I feel this magic around me..."
        scene v3g046
        with hpunch
        scene v3g046
        with vpunch
        scene black
        with dissolve
        scene v3g047
        with dissolve
        Nonen "Welcome [MC]"
        MC "Where am I? Who are you?"
        scene v3g048
        with dissolve
        Nonen "Poor fool... Don't you remember me?"
        MC "Are you a Lich?"
        Nonen "You know what I am, but do you know who I am?"
        MC "Am I supposed to know?"
        scene v3g049
        with dissolve
        Nonen "Fool! You will pay!"
        scene black
        with dissolve
        scene v3g050
        with dissolve
        MC "STOP!!"
        ayna "Calm down [MC], everything's fine"
        "You find you are lying on Archmage's bed"
        ayna "Care to tell me what you saw?"
        MC "I..."
        scene v3g051
        with dissolve
        "She sits next to you, with a soft voice she says"
        ayna "No pressure, tell me what you feel confortable telling"
        MC "I... Think I saw the Lich you fought many years ago"
        MC "What does it mean?"
        scene v3g052
        with dissolve
        ayna "I'll be honest with you, I'm not sure"
        ayna "But while you went to Jithak with Kitargo I felt your power peak"
        ayna "The only time I've felt such power was when I faced that Lich"
        ayna "Your power doesn't feel evil like his though but somehow it reminds me of him"
        MC "I don't understand..."
        scene v3g051
        with dissolve
        ayna "That makes two of us..."
        ayna "I have no idea of what is happening..."
        MC "My head is a bit fuzzy"
        ayna "You should go to your room and rest"
        scene v3g094
        with dissolve
        MC "Yes... I think you are right"
        ayna "But first let me give you something"
        "She casts a spell and you feel it on your body"
        ayna "Take a look at the mirror"
        scene v3g095
        with dissolve
        ayna "What do you think?"
        ayna "You are no longer a mere student, you are a Mage now after all"
        ayna "As such, it's only right that you look the part"
        MC "Thank you! I do look like a Mage now"
        ayna "Glad you like it, now time to sleep, tomorrow is a new day"
        MC "See you then"
        "You left her room"
        $ gotrobev3good = 1
        jump travelinsidecollegev3g
    else:
        "It's locked"
        jump travelinsidecollegev3g


label afterfannayv3g:
    scene v3g071
    with dissolve
    amida "Is everything ok?"
    MC "Yes, I'm fine"
    amida "Nice robe you got there"
    MC "It was a gift from the Archmage"
    scene v3g072
    with dissolve
    amida "I've missed you, please kiss me!"
    menu:
        "[abgreen]Kiss her":
            amida "mmhmm"
            scene v3g071
            with dissolve
            amida "Now I want more, lie down"
            "You do what you are told"
            scene v3g073
            with dissolve
            "As you lie down Mida removes her dress"
            "You can see her perfect body in front of you"
            amida "You look happy to see me naked"
            MC "Who wouldn't? But you are still overdressed"
            scene v3g074
            with dissolve
            "She removes her panties"
            amida "What about now?"
            MC "Better..."
            scene v3g075
            with dissolve
            "She starts to move and puts her pussy on your face"
            scene v3g076
            with dissolve
            "You start to lick it"
            amida "Ah! yes..."
            amida "Keep going!! Yes! Don't stop!"
            "You give it your best, you can taste her bittersweet fluids"
            amida "Time to return the favor!"
            scene v3g078
            with dissolve
            "She gets on her knees in front of you, grabbing you dick"
            scene v3g077

            show v03ehj idle
            "She starts to stroke your dick"
            MC "Hmmmm yes...."
            scene v3g078
            with dissolve
            MC "That feels so good..."
            scene v3g077

            show v03ehj2 idle
            MC "Ahhh...."
            amida "You like this?"
            MC "I love it!"
            scene v3g078
            with dissolve

            scene v3g077
            show v03ehj3 idle
            MC "Ahhhh.... that's it keep going..."
            amida "You look so cute like this"
            amida "Lie down please"

            scene v3g080
            with dissolve
            "You lie down and she starts to lick you dick"
            MC "Ahh... Yes..."
            scene v3g081
            with dissolve
            "You can feel her soft lips kissing the tip of your cock"
            amida "Hmmmmm"
            amida "I think it's wet enough to try something else"
            scene v3g083
            with dissolve
            MC "I like the way you think"
            "She strokes you dick a couple more times"
            scene v3g084
            with dissolve
            "After that she points it into her pussy"
            "You grab her left breast"
            scene v3g085
            with dissolve
            "You then help her slide down you cock"
            amida "Ahhhh.... Yes... So big..."
            MC "Humf... Ah..."
            scene v3g096
            with dissolve
            "You start to move"
            amida "Ah... yes..."
            scene v3g097
            with dissolve
            "You are going faster and deeper"
            amida "Ah... Yes!! keep going!!"
            amida "I'm cumming!!! Ahhhh!"
            scene v3g096
            with dissolve
            MC "We are not stopping yet!"
            amida "Ah... Yes..."
            scene v3g097
            with dissolve
            amida "Keep going!"
            MC "Turn around!"
            scene v3g086
            with dissolve
            "You turn her around and put you dick all the way in"
            amida "Ahhh!!! Yes!!"
            "You start to pound her, she starts moving all around"
            scene v3g079
            with dissolve
            "But you won't release your grip"
            amida "Oh my God!! Yes!"
            scene v3g082
            show v03eds idle
            amida "Ahhhh!!!!! I'm cumming again!"
            amida "Ahhhhhhhhh!"
            MC "Turn around again!!"
            amida "I.. Can't..."
            scene v3g087
            with dissolve
            "You turn her around again and keep going harder and faster"
            amida "Ahhhh!"
            scene v3g088
            with dissolve
            MC "Ahhh! I'm.... Cumming"
            $ sexwithmidav26 = 1
            menu:
                "Cum inside":
                    show shot
                    with hpunch
                    scene v3g089
                    with dissolve
                    MC "Ahhhh!! Fuck!!"
                    amida "Ahhhh! Yes!! I can feel you filling me. So warm..."
                    "You collapse on the bed"
                    $ renpy.end_replay()
                    jump aftersexmidav3good
                "Pull out":


                    show shot
                    with hpunch
                    scene v3g090
                    with dissolve
                    MC "Ahhhh!! Fuck!!"
                    amida "Ahhhh! So much..."
                    scene v3g091
                    with dissolve
                    amida "This was so awesome baby"
                    "You collapse on the bed"
                    $ renpy.end_replay()
                    jump aftersexmidav3good
        "Tell her you need to rest":


            scene v3g071
            with dissolve
            amida "Oh... Ok... I'll leave you then"
            $ midacorr -= 1
            $ midalove -= 1
            "Mida love and corruption decreased"
            "She left"
            scene v3g082
            with dissolve
            MC "Time to sleep at last..."
            $ renpy.end_replay()
            jump devilsv3all

label aftersexmidav3good:
    scene v3g092
    with dissolve
    MC "Damn... I'm drained..."
    amida "Are you ok?"
    MC "You bet I am... I need to rest now"
    scene v3g093
    with dissolve
    amida "Me too... I'm so relaxed now..."
    jump devilsv3all
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
