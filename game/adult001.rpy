
label adulthood:
    scene black
    "You are now an adult"
    $ GNE = "Neutral"
    if Points <= -3:
        $ GNE = "Evil"
    elif Points >= -2:
        if Points <= 2:
            $ GNE = "Neutral"
        else:
            $ GNE = "Good"

    "Based on your choices you are [GNE]"


    scene black
    stop music
    play music "<loop 0.0>ingame.mp3"
    play sound "sounds/knock.mp3"
    "Knock knock knock"
    scene v015001
    with dissolve
    MC "There is someone knocking on my door already..."
    play sound "sounds/knock.mp3"
    "Knock knock"
    kitargo "Hey [MC] Kitargo want to show trick"
    MC "... And you couldn't wait until the presentation?"
    kitargo "Open door to Kitargo please"
    scene v015002
    with dissolve
    kitargo "Hi"
    MC "Hello"
    scene v015002a
    with dissolve
    kitargo "Kitargo want to show trick yes?"
    scene v015003
    with dissolve
    kitargo "Nobody want to see Kitargo trick"
    MC "Well I guess..."
    scene v015004
    with dissolve
    kitargo "Yes.. Kitargo will show you"
    kitargo "Look!!"
    "You start to feel some energy coming out of Kitargo"
    scene v015005
    with dissolve
    "He starts to change his appearance"
    scene v015006
    with dissolve
    "A moment later he looks like Master Katarro"
    MC "You look like Katarro"
    kitargo "Yes.. hehehe"
    kitargo "Kitargo is good!"
    MC "You forgot your tail...."
    scene v015007
    with dissolve
    kitargo "wha..?"
    kitargo "Kitargo must improve"
    scene v015006
    with dissolve
    kitargo "Thank you"
    "He returns to normal"
    scene v015008
    with dissolve
    kitargo "Kitargo is pleased"
    kitargo "Bye"
    "Kitargo left"
    scene v015009
    with dissolve
    MC "Well since I'm already up..."
    amida "Hey"
    "That is a very familiar voice"
    "You turn around"
    scene v015010
    with dissolve
    amida "I came to wake you up"
    amida "But I see it wasn't necessary"
    scene v015011
    with dissolve
    MC "Yeah.. Kitargo got that pleasure today.."
    amida "Hehe"
    amida "Well in that case..."
    MC "You can always have the pleasure of kissing me first"
    "She closed her eyes"
    scene v015012
    with dissolve
    "And kissed you"
    scene v015013
    with dissolve
    amida "We don't want Kitargo to be the first one kissing you today"
    MC "Or ever..."
    amida "Hehehe"
    scene v015011
    with dissolve
    amida "Come on, we need to go to the presentation"
    MC "Alright... Let me just get my robe..."
    amida "For the last time.. we'll finally be rid of these"
    scene v015014
    with dissolve
    amida "I'm going on ahead, see you there"
    MC "See you soon"
    scene v015015
    with dissolve
    MC "Let's get that robe"
    fannay "Hey pretty boy"
    MC "Again...What is happening today??"
    scene v015016
    with dissolve
    fannay "Hey now, you're the one changing your clothes with the door open..."
    MC "..."
    scene v015017
    with dissolve
    fannay "Not that I mind"
    fannay "Ahaha"
    scene v015018
    with dissolve
    fannay "See you at the presentation!"
    fannay "Good luck... You're going to need it"
    fannay "Ahahah"
    "As she leaves, you close the door"
    scene v015015
    with dissolve
    play sound "sounds/door.mp3"
    MC "Let's see..."
    scene v015019
    with dissolve
    "You start changing into your robe"
    "And as soon as you're prepared to leave"
    stop music fadeout 4.0
    "You feel a presence"
    "And a terrible pain runs down your spine"
    play sound "sounds/shock.ogg"
    scene v015019
    with hpunch
    ".. You start to faint"
    play music "<loop 0.0>epic.mp3" fadein 6.0
    scene v015020
    show blink1
    with dissolve
    "As you fall you can see that someone was behind you.."
    "But..."
    show blink2
    with dissolve
    show blink3
    with dissolve
    scene black
    with dissolve
    scene v015021
    with dissolve
    demon "And now it's your turn!!"
    scene v015022
    with dissolve
    demon "Are you ready to die?"
    demon "Puny human"
    scene v015023
    with dissolve
    demon "I'm going to drink your blood"
    scene v015024
    with dissolve
    demon "DIE!!"

    scene v015025
    with dissolve
    demon "What the.."
    scene v015026
    with dissolve
    demon "AHH!! My eye!!"
    scene v015027
    with dissolve
    mom "Take that evil creature!"
    mom "Leave!"
    scene v015028
    with dissolve
    mom "I've got more for you"
    scene v015029
    with dissolve
    mom "Take this!"
    scene v015030
    with dissolve
    demon "YOU FUCKING WHORE!!"
    demon "You think that will stop me??"
    demon "I'm going to kill you"
    dad "Yahhhh"
    scene v015031
    with dissolve
    demon "AHHHH!!"
    demon "My back!!"
    scene v015032
    with dissolve
    demon "You fucking bastards!!"
    demon "You will pay for this..."
    scene v015033
    with dissolve
    demon "Someday..."
    scene v015034
    with dissolve
    dad "The demon is gone"
    scene v015035
    with dissolve
    dad "You saved me my dear"
    mom "Again..."
    dad "You are the best archer of the realm..."
    dad "So that's bound to happen..."
    mom "Heheh"
    play sound "sounds/babycry.mp3"
    scene v015036
    with dissolve

    mom "Did you hear that?"
    dad "What is that?"
    mom "Sounds like... A baby?"
    dad "Look.. There"
    scene v015037
    with dissolve
    mom "It's a baby..."
    mom "But... how?"
    scene v015038
    with dissolve
    mom "Poor thing..."
    play sound "sounds/babycry.mp3"
    dad "I would say the opposite.."
    dad "Since he's the only survivor.."
    scene v015039
    with dissolve
    mom "Calm down little one"
    mom "We will take care of you"
    mom "As a family"
    scene v015038
    with dissolve
    dad "Let's get out of here"
    dad "I'm worried about our daughter"
    stop music fadeout 2.0
    scene black
    with dissolve
    scene v015009
    with dissolve
    play music "<loop 0.0>ingame.mp3"
    MC "Shit..."
    MC "That dream again..."
    MC "But what happened?"
    MC "Shit.. The presentation!!"
    "You leave your room in a hurry"
    "Not stopping until you reach the College courtyard"
    scene v015040
    with dissolve
    amida "You're late"
    amida "Where were you?"
    amida "You missed my presentation"
    MC "I... I'm not sure what happened"

    "You look around the courtyard"
    scene v015041
    with dissolve
    "You see many professors, the Elite members, many students..."
    "You can't see the Archmage though.."
    "And you see an Elf woman that you've never seen before"
    scene v015042
    with dissolve
    MC "Who is that?"
    amida "Pretty isn't she?"
    amida "She's an elven princess or something"
    MC "Why is she here?"
    amida "I have no idea..."
    profalter "And next"
    scene v015043
    with dissolve
    profalter "We have one of the best students"
    profalter "To ever study in our College"
    profalter "Hatoshi!!"
    scene v015044
    with dissolve
    amida "That asshole..."
    "You see Hatoshi assuming a basic stance"
    "And out of nowhere"
    scene v015045
    with dissolve
    play sound "sounds/quake.ogg"
    "He unleashes a high level spell"
    "You have no idea what he is even casting"

    scene v015046
    with dissolve
    "Then he stops... And starts to do something else..."
    play sound "sounds/ward.ogg"
    scene v015047
    with dissolve
    MC "What the??!"
    profalter "That is amazing!!"
    scene v015048
    with dissolve
    profalter "He summoned a copy of himself!"
    scene v015049
    with dissolve
    profalter "And that was Hatoshi everyone"
    scene v015050
    with dissolve
    "As he is leaving Hatoshi passes by you"
    hatoshi "Try to beat that... asshole..."
    hatoshi "Ahahaha"
    "He leaves the courtyard, ignoring the remaining presentations"
    scene v015043
    with dissolve
    profalter "And next we have Kitargo"
    profalter "Let's see what he prepared for us today"
    scene v015051
    with dissolve
    "The majority of students were cheering Kitargo"
    "But it was in a joking tone"
    kitargo "Yes, Kitargo is good"
    scene v015052
    with dissolve
    "Kitargo raises his arms"
    "You start to feel energy coming out of him"
    scene v015053
    with dissolve
    play sound "sounds/ward.ogg"
    "He starts to change"

    scene v015054
    with dissolve
    "Into... Hatoshi..."
    "Then starts to dance.."
    "All of the students start laughing"
    amida "Hehehe"
    MC "Ahaha"
    kitargo "Hello I'm Hatoshi"
    kitargo "Kitargo is much better than me!"
    kitargo "I act tough but I'm scared of everything"
    "After saying that he returns to normal"
    scene v015055
    with dissolve
    "You hear laughs everywhere"
    "And Kitargo looks satisfied"
    kitargo "Kitargo is good"
    "Kitargo approaches you"
    scene v015056
    with dissolve
    kitargo "Thank you for helping me earlier"
    MC "Your show was better than I expected"
    MC "Too bad Hatoshi left... I would have loved to see his face"
    kitargo "Yes... Hatoshi face.."
    kitargo "Hehehe"
    MC "Let's see who's next"
    scene v015057
    with dissolve
    profalter "And now..."
    "You notice the Archmage arriving to the presentation and joining the others"
    profalter "Koneko please show us your skills"
    "You see Koneko move to the center of the courtyard"
    scene v015058
    with dissolve
    "She looks a bit overwhelmed with everyone staring at her"
    akoneko "..."
    scene v015059
    with dissolve
    "She looks at you, maybe looking for some encouragement"
    "You..."
    $ konekolove = 0
    $ konekocorr = 0
    menu:
        "Nod at her with a confident smile{color=#1BBB20} (+1 Koneko's Love)":
            scene v015060
            with dissolve
            $ konekolove = 1
            "With a shy smile she nods back"
            "Koneko now likes you more"
            jump konekoshow
        "Ignore her":
            "You see Mida nod and smile to Koneko"
            scene v015060
            with dissolve
            "That seems to boost Koneko’s confidence"
            jump konekoshow

label konekoshow:
    scene v015060
    with dissolve
    "With her new confidence"
    scene v015061
    with dissolve
    "Koneko starts to do something"
    play sound "sounds/ward.ogg"
    "You feel a considerable amount of energy around her"

    MC "Is she enchanting herself?"
    scene v015062
    with dissolve
    "You keep watching"
    "She looks at the stone pedestal"
    scene v015063
    with dissolve
    "And she grabs it... with one hand"
    "People around start to clap"
    scene v015064
    with dissolve
    "Which seems to boost Koneko’s morale even more"
    akoneko "Thank you..."
    scene v015065
    with dissolve
    akoneko "Thank you so much"
    scene v015043
    with dissolve
    profalter "That was very good"
    profalter "A perfect example of the spell 'Strength' "
    profalter "Next we have Jessica"
    profalter "Come on Jessica"
    scene v015066
    with dissolve
    jessica "Hello everybody"
    jessica "Let me show you something I've been working on"
    scene v015067
    with dissolve
    jessica "Mexerium Agilus!!"
    play sound "sounds/fear.ogg"
    scene v015068
    with dissolve
    MC "She's... fading?"
    scene v015069
    with dissolve
    MC "She disappeared..."
    "You look around but fail to find her"
    jessica "Hello"
    scene v015070
    with dissolve
    "She reappears in the same spot"
    MC "Is that a staff?"
    jessica "This staff is...."
    jessica "..."
    jessica "......"
    MC "Is she frozen?"
    MC "What is happening?"
    scene v015071
    with dissolve
    "The elf woman approaches Jessica, who is still frozen"
    scene v015072
    with dissolve
    "The elf woman removes the staff from Jessica's hand"
    "And returns to her previous position"
    scene v015073
    with dissolve
    "But Jessica is still not moving at all"
    scene v015074
    with dissolve
    "Is she ok?"
    "Was it the elf who did this to her?"
    scene v015075
    with dissolve
    jessica "What the?"
    jessica "What happened?"
    scene v015077
    with dissolve
    MC "Yeah, that was definitely her..."
    scene v015076
    with dissolve
    "Jessica runs away, ashamed and confused by what has happened"
    scene v015078
    with dissolve
    profalter "Well, she learned a lesson..."
    profalter "Never steal from an elf princess"
    profalter ".."
    profalter "Let' see... who's next?"
    profalter "Oh yeah, [MC] !"
    profalter "Come on [MC] , show us why you're one of the best!"
    "You move to the center of the courtyard"
    scene v015079
    with dissolve
    nvl clear
    n "From now on"
    n "Some options will be based on your skills"
    n "In the next choice, the options available"
    n "Will depend on your skills"
    nvl clear
    n "Only skills over 3 points"
    n "Will be able to be chosen"
    n "But that will not happen all the time"
    n "In some future choices "
    n "You need to keep that in mind"
    nvl clear
    n "If you use a weak skill"
    n "To fight a powerful opponent"
    n "You can count on a game over"
    nvl clear
    n "To help you choose"
    n "The respective skill symbol"
    n "Will appear in front of the choice"
    nvl clear
    "Everyone is staring at you curiously"
    "You decide to start"
    $ impressed = 0
    "The first spell you use is"

    menu:
        "Use Flames {image=001battle}" if Destpoints >= 4:
            scene v015081
            with dissolve
            "You start to cast Flames"
            play sound "sounds/flames.wav"
            scene v015084
            with dissolve
            "In the next second, very hot waves of heat leave your hands"
            scene v015095
            with dissolve
            "You look at the elf princess"
            MC "Is she smiling at me?"
            MC "That's a first..."
            $ impressed = "elf"
            jump afterpresentaion

        "Summon a Reptilian {image=001summon}" if Summpoints >= 4:
            scene v015081
            with dissolve
            "You start to summon a Reptilian"
            play sound "sounds/summon.ogg"
            scene v015087
            with dissolve
            "It's a success"
            "The reptilian starts to scare the viewers"
            scene v015096
            with dissolve
            "Liliana looks very impressed with your spell"
            $ impressed = "lili"
            jump afterpresentaion

        "Use Minor Ward {image=001alteration}" if Altepoints >= 4:
            scene v015081
            with dissolve
            "You start to cast Minor Ward"
            play sound "sounds/ward.ogg"
            scene v015085
            with dissolve
            "In the next second you have a ward in front of you"
            scene v015098
            with dissolve
            "After you break your spell, you notice that Professor Abaashi"
            "Looks very impressed"
            $ impressed = "abaa"
            jump afterpresentaion

        "Use Darkness {image=001illusion}" if Iluspoints >= 4:
            scene v015081
            with dissolve
            "You start to cast Darkness"
            play sound "sounds/fear.ogg"
            scene v015086
            with dissolve
            "In the next moment it's like the night arrived sooner"
            scene v015097
            with dissolve
            "After you return everything to normal"
            "You notice that the Archmage looks surprised with your skill"
            $ impressed = "arch"
            jump afterpresentaion

        "Use Telekinesis {image=001myst}" if Mystpoints >= 4:
            scene v015081
            with dissolve
            "You will cast Telekinesis"
            scene v015089
            with dissolve
            "And you choose Professor Rerlvam as your test subject"
            play sound "sounds/force.ogg"
            scene v015091
            with dissolve
            "And lift him in the air"
            scene v015093
            with dissolve
            "You then put him down"
            "And he looks very impressed"
            $ impressed = "rerl"
            jump afterpresentaion

        "Use Mass Bless {image=001heal}" if Healpoints >= 4:
            scene v015081
            with dissolve
            "You cast Mass Bless"
            play sound "sounds/spell01.mp3"
            scene v015092
            with dissolve
            "Your spell targets everyone"
            "Everyone looks more comfortable or even happier"
            scene v015094
            with dissolve
            "And you notice that Mistress Katriona looks very impressed"
            $ impressed = "kat"
            jump afterpresentaion



label afterpresentaion:
    scene v015078
    with dissolve
    profalter "And that ends the presentations today"
    profalter "We had some great spells shown off today"
    profalter "All students may return to their rooms"
    profalter "You have the rest of the day to yourselves"
    profalter "Celebrate and have fun!"
    "As you are about to leave"
    ayna "Hey [MC] wait a minute"
    scene v015090
    with dissolve
    MC "Archmage..."
    ayna "I need to ask you something"
    MC "Of course"
    ayna "I need to talk to you in private"
    ayna "Can you meet me in about two hours please?"
    MC "Hmm... Sure..."
    ayna "Then for now, go and celebrate your graduation"
    "She left"
    scene v015040
    with dissolve
    amida "What was that?"
    MC "I have no idea..."
    amida "But you know where to meet her right?"
    MC "Ugh, now that you say that.."
    amida "Hehehe, she didn't say, and you didn't ask..."
    amida "I just imagined that you knew what she was talking about"
    MC "Yeah.. I have no idea.."
    amida "Shall we go to your room and celebrate?"
    amida "We have about two hours hehehe"
    MC "Well then what are we waiting for?"
    scene v015009
    with dissolve
    "You and Mida enter your empty room"
    scene v015099
    with dissolve
    "Mida gets in your bed"
    amida "I want to show you something"
    MC "I can't wait"
    scene v015100
    with dissolve
    "She removes her robe"
    scene v015101
    with dissolve
    amida "Finally!!"
    amida "We won't need these ugly robes anymore"
    MC "Yeah.. that's a definite improvement"
    amida "How about a kiss?"
    scene v015102
    with dissolve
    MC "You don't have to ask me twice"

    "You kiss her"
    "You can feel her body shiver"
    "That makes yours shiver too"

    amida "Hmmm..."
    scene v015101
    with dissolve
    amida "[MC] my love"
    amida "You were so great today"
    if impressed == "elf":
        amida "That flames spell was amazing"
        amida "Even the Elf princess looked impressed with you"
        amida "And believe me, she was stone faced up all day"
        amida "But then you appeared..."
        MC "What can I say... [MC] is good!"
        amida "Ahahaha"
    else:

        if impressed == "lili":
            amida "That Reptilian you summoned was amazing"
            amida "Where did you learn that spell?"
            amida "Come on, tell me! We never learned that spell"
            MC "To be honest I'm not sure..."
            "You can only remember using that spell"
            "In one of your dreams, but you can't learn spells in your dreams.."
            "Or can you?"
            amida "Typical you... Amazing at magic..."
            amida "But everything else is a mess in that head of yours"
            amida "Ahahaha"
        else:
            if impressed == "abaa":
                amida "That Ward was amazing"
                amida "I think professor Abaashi felt weak at the sight of it"
                amida "You could see what he was thinking by looking at his face"
                amida "'How can a senior year student cast professor level spells?'"
                MC "What can I say.. [MC] is good!"
                amida "Ahahaha"
            else:
                if impressed == "arch":
                    amida "That Darkness spell was impressive"
                    amida "And scary..."
                    amida "All of a sudden it was as dark as night..."
                    amida "I think that even the Archmage was impressed"
                    MC "What can I say... [MC] is good!"
                    amida "Ahahaha"
                else:
                    if impressed == "rerl":
                        amida "You scared the shit out of Professor Rerlvam"
                        amida "Moving him around like a doll"
                        amida "He sure looked scared..."
                        amida "Still I think you impressed everyone"
                        MC "What can I say... [MC] is good!"
                        amida "Ahahaha"
                    else:
                        amida "I can't believe you casted Mass Blessing"
                        amida "You took a big risk with that choice"
                        amida "Still, everyone could feel your power"
                        amida "And Mistress Katriona looked impressed"
                        amida "Since that's her speciality"
                        amida "You were so great!"
                        MC "What can I say... [MC] is good!"
                        amida "Ahahaha"
    amida "How about another kiss as a reward?"
    MC "A reward for me or for you?"
    amida "You didn't see my presentation..."
    MC "Yeah, I'm really sorry about that..."
    MC "Now that you mention it..."
    MC "What did happen to me before the presentation?"
    amida "Forget about it and kiss me"
    scene v015102
    with dissolve
    "You kissed her"
    "She kissed you back passionately"
    scene v015103
    with dissolve
    "And started to remove your robe"
    scene v015103
    with dissolve
    amida "Mmmm"
    "As your robe hits the ground"
    scene v015104
    with dissolve
    "Your erect penis is exposed"
    amida "Wow"
    amida "Is that all because of me?"
    MC "What can I say..."
    amida "Hehehe I guess I should take care of it then"
    scene v015105
    with dissolve
    "She grabs your dick"
    "And starts stroking it"
    amida "You like it?"
    MC "Oh yes..."
    scene v015106
    with dissolve
    "She takes the tip up to her lips and into her mouth"
    "You feel the warmth and wetness of her mouth around your dick"
    play sound "sounds/knock.mp3"
    "*Door Knock"
    scene v015107
    with dissolve
    amida "Are you expecting someone?"
    MC "No..."
    amida "Let me get dressed"
    MC "Shit..."
    scene v015108
    with dissolve
    play sound "sounds/knock.mp3"
    "*Door knock"
    fannay "Hey open the door you two"
    amida "Is that Fannay?"
    "After both of you dress, you open the door"
    scene v015109
    with dissolve
    "Fannay enters the room"
    fannay "What were you doing? Fucking?"
    "Mida was rendered speechless, which almost never happens"
    amida "..."
    MC "Almost... but then you interrupted.."
    scene v015110
    with dissolve
    fannay "Hmmm... you little perverts"
    fannay "But hey... I love perverts.."
    scene v015111
    with dissolve
    fannay "And this beauty you have"
    fannay "I can imagine how easily you seduced [MC] Mida"
    scene v015112
    with dissolve
    fannay "Even I feel attracted to you"

    menu:
        "Let her continue":
            "You decide to see what is going to happen{color=#1BBB20} (+1 Mida's Love)"
            amida "Hey..."
            amida "Stop it!"
            scene v015113
            with dissolve
            fannay "Ok ok.."
            fannay "It was a compliment"
            scene v015110
            with dissolve
            fannay "I'll let you two continue"
            fannay "But hey, if you ever feel the need to try something else"
            fannay "Just call me, either of you"
            fannay "Bye, heheh"

            scene v015013
            with dissolve
            amida "What the hell was that?"
            amida "Was she asking to have sex with us?"
            MC "It sure seems like it..."
            "You look at her face and she doesn't look mad"
            "More like... happy?"
            amida "..."
            "Mida corruption increased"
            $ midacorr += 1
            scene v015014
            with dissolve
            amida "I... Should go..."
            amida "And you should meet the Archmage"
            amida "Cya later... aligator"
            MC "In a while... crocodile"
            scene v015015
            with dissolve
            "She leaves you alone"
            MC "I should go look for the Archmage"
            $ liliseen = False
            jump Archmagemission
        "Stop her{color=#FF0000} (+1 Mida's Corruption)":

            "You decide to interrupt Fannay"
            MC "Hey!!"
            scene v015114
            with dissolve
            MC "That's my girl, if you want one"
            MC "Go find another"
            scene v015110
            with dissolve
            fannay "I was just kidding"
            fannay "You know I only like guys"
            fannay "I should go"
            fannay "Bye"
            scene v015013
            with dissolve
            amida "What the hell was that?"
            amida "Thank you for stopping her"
            MC "It was nothing my dear"
            amida "I was about to punch her face"
            MC "Forget it baby, we have each other"
            amida "Ohh..."
            "Mida love increased"
            $ midalove += 1
            scene v015014
            with dissolve
            amida "I... Should go..."
            amida "And you should meet the Archmage"
            amida "Cya later... aligator"
            MC "In a while... crocodile"
            scene v015015
            with dissolve
            "She leaves you alone"
            MC "I should go look for the Archmage"
            $ liliseen = False
            jump Archmagemission

label Archmagemission:

    scene hall
    with dissolve
    MC "Where should I look for her?"
    call screen collegeblue


label collegeportalroom:

    scene v15mission001
    with dissolve
    MC "There she is"
    MC "What is she doing?"
    MC "I can feel... a lot of power..."
    play sound "sounds/spell01.mp3"
    scene v15mission002
    with dissolve
    ayna "Ahmmm Hummm"

    "You can feel her power growing"
    play sound "sounds/spell01.mp3"
    scene v15mission003
    with dissolve
    MC "Wow... So much power..."
    ayna "Ahmmmm"
    scene v15mission004
    with dissolve
    "You can't even fathom the amount of power generated"
    "And all of a sudden"
    scene v15mission005
    with dissolve
    "She stops..."
    ayna "You are right on time"
    ayna "I need to prepare you for the travel"
    MC "Travel? What Travel?"
    ayna "Hold still"
    scene v15mission007
    with dissolve
    ayna "So you'll be able to use it"
    MC "Can you explain what's going on? Why did you need me?"
    ayna "Yes, give me a moment, I need to finish this"
    ayna "There, all done"
    scene v15mission005
    with dissolve
    ayna "So I called you because I want you to do something"
    MC "Ok... And what is it?"
    ayna "Apparently the daughter of a farmer"
    ayna "Here on Allesterra disappeared"
    ayna "And he sent me a letter asking for help"
    MC "Go on..."
    ayna "I was planning to send an established Mage to check this out"
    ayna "But since I was very impressed with your skills today"
    ayna "I'd like you to go instead"
    MC "Me?"
    scene v15mission006
    with dissolve
    ayna "Yes, you"
    ayna "Don't tell me you're afraid?"
    MC "Of course not!"
    scene v15mission005
    with dissolve
    ayna "So what do you say?"
    ayna "You'll be paid the same as any other Mage would be"
    MC "Count me in"
    scene v15mission008
    with dissolve
    ayna "Here, take this"
    play sound "sounds/Coin.ogg"
    "You received 5 gold"
    $ Gold += 5
    scene v15mission005
    with dissolve
    MC "Thank you"
    ayna "Go ahead, the portal is open for you"
    scene v15mission009
    with dissolve
    ayna "Follow the stairs and"
    ayna "Just pass through it"
    MC "Very well"
    scene v15mission010
    with dissolve
    MC "Let's go then!!"
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    stop music fadeout 2.0
    play music "dark.mp3" fadein 2.0
    scene meanwhile
    with dissolve
    scene bredita001
    with dissolve
    Nonen "He was very impressive Mistress"
    Bredita "Hmmm"
    Bredita "That's good news.."
    Bredita "And Ayna continues her charades?"
    Nonen "Yes, but I don't believe she will for much longer"
    Nonen "After all [MC] is already the best student of the college"
    scene bredita002
    with dissolve
    Bredita "Ahh... Memories..."
    Bredita "You can go now"
    Nonen "Very well Mistress"
    scene bredita003
    with dissolve
    Bredita "Looks like I need to start planning"
    Bredita "Ahahah"
    stop music fadeout 2.0
    jump oldmanmission1


label collegelibrary:

    scene library
    with dissolve
    MC "Maybe she's here"
    MC "This is the library"
    MC "Nobody's here"
    MC "She must be somewhere else"
    MC "Maybe I should return later"
    MC "There is a lot of knowledge here..."
    jump Archmagemission


label throneroomcollege:

    scene throne
    with dissolve
    MC "Maybe she's here"
    MC "No... She's not here"
    MC "It's a throne... "
    MC "With a statue of a soldier with some creature behind it"
    MC "No clues about where she is though"
    jump Archmagemission

label liliroomcollege:
    if liliseen == False:


        scene v15mission011
        with dissolve

        lili "Ahh... that's relaxing"
        MC "Oh... she's naked with the door open..."
        MC "Now I see why the college kept her as a teacher... ahahah"
        scene v15mission012
        with dissolve
        lili "Time to take a good hot bath.."
        scene v15mission013
        with dissolve
        lili "Hey... [MC] right?"
        MC "Hummmm yes..."
        lili "I need to ask you something"
        MC "Hmm ok..."
        lili "Why the hell are you spying on me?"
        MC "Sorry... I was looking for the Archmage..."
        scene v15mission014
        with dissolve
        lili "She's in the portal room..."
        lili "Now go... I want to take a bath..."
        "Now that was crazy"
        $ liliseen = True
        jump Archmagemission
    else:
        MC "I shouldn't mess with Liliana again..."
        jump Archmagemission


label classroomcollege:

    scene classroommiss
    with dissolve
    MC "Maybe she's here"
    MC "This is the classroom..."
    MC "Nothing to see here..."
    jump Archmagemission

label bathroomcollege:

    if liliseen == True:

        scene v15mission015
        with dissolve

        lili "Ahh.. this is going to be great..."
        MC "Damn..."
        MC "Her again..."
        MC "I should leave..."
        jump Archmagemission
    else:
        scene bathhousemiss
        with dissolve

        MC "These are the baths.."
        MC "She's not here.."
        jump Archmagemission




label oldmanmission1:
    play music "ingame.mp3" fadein 2.0
    scene farmmission1
    with dissolve
    MC "Wow that was awesome!!"
    MC "What am I suppose to look for?"
    oldman "Hey! You there!"
    scene v15mission016
    with dissolve
    "You look around to see who's talking"
    "And you see an old man."
    oldman "Who are you?"
    oldman "What are you doing here?"
    MC "I'm looking for a farmer that needs help"
    scene v15mission017
    with dissolve
    oldman "What do you mean?"
    MC "We got a letter asking for help"
    MC "A farmer's daughter seems to be missing"
    scene v15mission019
    with dissolve
    "The man's face suddenly lit up"
    oldman "Ah yes... My... Daughter.."
    MC "Are you sure it's your daughter"
    scene v15mission017
    with dissolve
    "His face changed back..."
    oldman "Yes..."
    oldman "Of course I'm sure..."
    scene v15mission018
    with dissolve
    oldman "She went to the forest looking for firewood"
    oldman "And never returned..."
    MC "How long has it been?"
    scene v15mission017
    with dissolve
    oldman "About a week ago..."
    oldman "I really need help..."
    MC "I will look for her"
    scene v15mission019
    with dissolve
    oldman "Thank the Gods"
    oldman "And the Mage College"
    MC "Don't worry, I shall leave at once"
    $ mclocation = "farm"
    jump maptravel1st


label maptravel1st:
    scene farmmission1
    with dissolve
label callmapnow:
    call screen allesterramap


label montainallesterra:
    MC "I'm supposed to look for her in the forest..."
    MC "And how am I supposed to go to the mountain?"
    MC "Walking?"
    jump maptravel1st

label collegeallesterra:
    MC "I'm supposed to look for her in the forest..."
    MC "I'll return to the college"
    MC "As soon as I find the girl."
    jump maptravel1st

label craterallesterra:
    MC "I'm supposed to look for her in the forest..."
    MC "Why should I go to the crater?"
    jump maptravel1st


label villageallesterra:
    scene villagedesert
    with dissolve
    MC "This village is empty..."
    MC "Where is everybody?"
    MC "This is very strange..."
    MC "But I need to find the girl first."
    jump maptravel1st


label farmallesterra:
    if mclocation == "farm":
        MC "That's where I am..."
        jump maptravel1st
    else:
        $ mclocation = "farm"
        jump maptravel1st

label dockallesterra:
    MC "I'm supposed to look for her in the forest..."
    MC "The docks may be useful in the future."
    jump maptravel1st

label cityallesterra:
    MC "I'm supposed to look for her in the forest..."
    MC "Still, I can't wait to visit the city"
    MC "but now I need to find the girl."
    jump maptravel1st

label shipallesterra:
    MC "I'm supposed to look for her in the forest..."
    MC "I'll be sure to visit the docks when I travel to the city."
    jump maptravel1st

label forestallesterra:
    scene forestmap
    with dissolve
    if mclocation == "farm":
        MC "Here we are..."
        $ mclocation = "forest"
        MC "Now what?"
        MC "Should I go deeper into the forest or return?"
        call screen forest
    else:
        MC "That's where I am"
        call screen forest


label nada01:
    "You return to the map"
    jump callmapnow

label nada02:
    "You decide to go deeper into the forest."
    scene v15mission020
    with dissolve
    MC "Damn... it's cold here"
    MC "How could that anyone could survive in this forest for a week...?"
    "You keep walking..."
    scene v15mission021
    with dissolve
    MC "How am I supposed to find her in here?"
    if GNE == "Evil":
        MC "Come on [MC], how can you conquer the world"
        MC "If I can't even find some girl..?"
    else:
        if GNE == "Neutral":
            MC "Come on [MC], you need to find the girl"
            MC "That will show my skills to the Archmage"
        else:
            MC "Come on [MC], the girl must be scared"
            MC "I promised to help everyone in need"

    MC "Where should I look? "
    play sound "sounds/screamwoman.wav"
    "You hear a scream"
    MC "What was that??"
    "You run in the direction of the scream"

    scene v15mission022
    with dissolve
    "You see a massive bear about to attack a girl"
    play sound "sounds/bear.ogg"
    "Probably the one you are looking for"
    MC "She's alive... I have to do something..."
    "What should you do?"
    $ savedgirl = False
    menu:
        "Run away and leave the girl behind{color=#FF0000} (-2 Alignment)":
            MC "I should get the hell out of here"
            MC "I'm not risking my life for some farm girl!"
            "You run away"
            $ Points -= 2
            "You gained -2 Points"
            jump killedgirlmission1
        "Shout to provoke the bear{color=#1BBB20} (+2 Alignment)":
            "You decide to shout in order to provoke the bear"
            "You gained 2 Points"
            $ Points += 2
            MC "AHHHH"
            scene v15mission023
            with dissolve
            "Both the girl and the bear look a bit confused"
            play sound "sounds/bear.ogg"
            scene v15mission025
            with dissolve
            "But it only took the bear a second to start running after you"
            nvl clear
            n "You should save the game now"
            n "You can die in this battle"
            n "I will not warn you again"
            n "Hint* Use your best skills"
            nvl clear

            "What should you do?"



            menu:
                AB "Choose the ones you have >= 3 or that leads to no new points/{color=#FF0000}game over{/color}."
                "Cast fear on the bear{color=#1BBB20} (+1 Iluspoint) {image=001illusion}":
                    "You decide to cast fear"
                    if Iluspoints >= 3:
                        scene v15mission026
                        with dissolve
                        play sound "sounds/fear.ogg"
                        scene v15mission026f
                        with dissolve
                        "The spell is a success"
                        scene v15mission027
                        with dissolve
                        "The bear ran away"
                        "Illusion increased by 1"
                        $ Iluspoints += 1
                        $ savedgirl = True
                        jump savedgirlmission1
                    else:
                        scene v15mission026
                        with dissolve
                        "You failed to cast Fear"
                        "The bear attacked you"
                        play sound "sounds/slash2.ogg"
                        scene v15mission026die1
                        with dissolve
                        MC "Ahhhhrgg"
                        scene v15mission026die2
                        with dissolve
                        scene v15mission026die3
                        with dissolve
                        show youaredead
                        with dissolve
                        "Game over"
                        return
                "Cast lightning on the bear{color=#1BBB20} (+1 Destpoint) {image=001battle}":

                    "You decide to cast lightning"
                    if Destpoints >= 3:
                        scene v15mission026
                        with dissolve
                        play sound "sounds/shock.ogg"
                        scene v15mission026l
                        with dissolve
                        "The spell is a success"
                        scene v15mission027
                        with dissolve
                        "The bear runs away"
                        "Battlemagic increased by 1"
                        $ Destpoints += 1
                        $ savedgirl = True
                        jump savedgirlmission1
                    else:
                        scene v15mission026
                        with dissolve
                        "You failed to cast Lightning"
                        "The bear attacks you"
                        play sound "sounds/slash2.ogg"
                        scene v15mission026die1
                        with dissolve
                        MC "Ahhhhrgg"
                        scene v15mission026die2
                        with dissolve
                        scene v15mission026die3
                        with dissolve
                        show youaredead
                        with dissolve
                        "Game over"
                        return
                "Summon something to fight the bear{color=#1BBB20} (+1 Summpoint) {image=001summon}":
                    "You decide to summon a Reptilian"
                    if Summpoints >= 3:
                        scene v15mission026
                        with dissolve
                        play sound "sounds/summon.ogg"
                        scene v15mission026r
                        with dissolve
                        "The spell is a success"
                        scene v15mission027
                        with dissolve
                        "Your Reptilian manages to scare the bear"
                        "Summoning increased by 1"
                        $ Summpoints += 1
                        $ savedgirl = True
                        jump savedgirlmission1
                    else:
                        scene v15mission026
                        with dissolve
                        "You failed to summon a creature"
                        "The bear attacks you"
                        play sound "sounds/slash2.ogg"
                        scene v15mission026die1
                        with dissolve
                        MC "Ahhhhrgg"
                        scene v15mission026die2
                        with dissolve
                        scene v15mission026die3
                        with dissolve
                        show youaredead
                        with dissolve
                        "Game over"
                        return
                "Use telekinesis on the bear{color=#1BBB20} (+1 Mystpoint) {image=001myst}":
                    "You decide to throw the bear to the air"
                    if Mystpoints >= 3:
                        scene v15mission026
                        with dissolve
                        play sound "sounds/force.ogg"
                        scene v15mission026t
                        with dissolve
                        "The spell is a success"
                        scene v15mission027
                        with dissolve
                        "The bear is sent flying through the air"
                        "Mysticism increased by 1"
                        $ Mystpoints += 1
                        $ savedgirl = True
                        jump savedgirlmission1
                    else:
                        scene v15mission026
                        with dissolve
                        "You failed to push the bear away"
                        "The bear attacks you"
                        play sound "sounds/slash2.ogg"
                        scene v15mission026die1
                        with dissolve
                        MC "Ahhhhrgg"
                        scene v15mission026die2
                        with dissolve
                        scene v15mission026die3
                        with dissolve
                        show youaredead
                        with dissolve
                        "Game over"
                        return
                "Use a ward to protect yourself and the girl{color=#1BBB20} (+1 Altepoint) {image=001alteration}":
                    "You decide to cast a ward"
                    if Altepoints >= 3:
                        scene v15mission026
                        with dissolve
                        play sound "sounds/ward.ogg"
                        scene v15mission026w
                        with dissolve
                        "The spell is a success"
                        scene v15mission027
                        with dissolve
                        "The bear gives up attacking and leaves"
                        "Alteration increased by 1"
                        $ Altepoints += 1
                        $ savedgirl = True
                        jump savedgirlmission1
                    else:
                        scene v15mission026
                        with dissolve
                        "You failed to cast Ward"
                        "The bear attacks you"
                        play sound "sounds/slash2.ogg"
                        scene v15mission026die1
                        with dissolve
                        MC "Ahhhhrgg"
                        scene v15mission026die2
                        with dissolve
                        scene v15mission026die3
                        with dissolve
                        show youaredead
                        with dissolve
                        "Game over"
                        return


label savedgirlmission1:
    scene v15mission027
    with dissolve
    MC "I should check the girl quickly"
    scene v15mission028
    with dissolve
    MC "There..."
    MC "How did she survive for so long?"
    MC "And dressed like that..."
    MC "I need to take her to the College"
    scene v15mission029
    with dissolve
    "You pick her up"
    MC "She's so cold..."
    MC "There's no way I'm skilled enough to heal her"
    scene v15mission030
    with dissolve
    MC "I need to take her to Katriona as soon as possible"
    MC "I really wish I could teleport like Katarro..."
    MC "Let's go"
    scene v15mission031
    with dissolve
    "You start to move through the snowy forest"
    MC "I have a long way to walk..."
    MC "Let's hope I get there in time"
    scene meanwhile
    with dissolve
    jump bredfan


label killedgirlmission1:
    scene v15mission021
    with dissolve
    "As you were escaping the forest"
    "You noticed it was getting colder"
    scene v15mission021snow
    with dissolve
    "It started to snow"
    "Wind became stronger"
    MC "I have to continue..."
    scene v15mission021s
    with dissolve
    "As you continued walking"
    "The weather became worse"
    "Suddenly you were in the middle of a blizzard"
    MC "Shit... I need to find a shelter... Fast.."
    scene meanwhile
    with dissolve
    jump bredfan
