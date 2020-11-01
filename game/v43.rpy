
init:
    $ v43check = 0
    $ v43dormant = 0
    $ v43stone = 0
    $ v43bookpay = 0
    $ v43cashforbooks = 0
    $ v43speakryo = 0
    $ v43timeforroom = 0
    $ v43bathfannay = 0
    $ v43visitroomcheck = 0
    $ v43endsexwith = 0
    $ v43lilidom = 0
    $ v43nobooks = 0

label v43version:
    $ v43check = 1
    MC "I guess I should look for the Archmage"
    MC "She's probably in the hall"
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    scene meanwhile
    with dissolve
    scene v43072
    with dissolve
    zegladar "I've got him, kill him now!!"
    goggos "You don't have to tell me twice"
    scene v43073
    with hpunch
    play sound "sounds/hit.mp3"
    goggos "Take that you fat bastard!"
    gluttony "Hmfff..."
    zegladar "Kill him!! I can't hold it much longer"
    scene v43074
    with vpunch
    play sound "sounds/hit.mp3"
    gluttony "Ahhh... "
    goggos "Get ready to die you ugly piece of shit!!"
    scene v43075
    with dissolve
    zegladar "Now!!"
    goggos "Take that! DIE!!!"
    play sound "sounds/explosionayna.wav"
    scene v43076
    with dissolve
    zegladar "You got him!"
    goggos "{i} pant pant pant"
    goggos "Yeah... I got him..."
    goggos "{i} pant pant pant"
    gluttony "AHHHHHH!!!!!"
    zegladar "Shit..."
    scene v43077
    with dissolve
    gluttony "You make me more hungry! Me hungry! You food!!"
    goggos "How the fuck!? What kind of monster is this?"
    zegladar "His power... Is... Rising..."
    goggos "What?!"
    scene v43078
    with dissolve
    gluttony "I'm going to eat you... Eat you all!!"
    zegladar "Run...."
    goggos "What?"
    scene v43079
    with dissolve
    zegladar "RUN!! Now!!"
    gluttony "FOOD!!!"
    play sound "sounds/horror.ogg"
    scene v43080
    with dissolve
    zegladar "No way..."
    goggos "What?"
    zegladar "His power..."
    scene v43081
    with dissolve
    zegladar "Is still rising..."
    gluttony "Feed me!!"
    goggos "Fuck...."

    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v43001
    with dissolve
    "You reach the hall and you can see Ayna and Katarro near the throne"
    "They are looking at you suspiciosly"
    scene v43002
    with dissolve
    "You get closer to them"
    MC "Hmm... Hello?"
    ayna "Hi... [MC]"
    katarro "..."
    MC "You would not believe what I've been through..."
    MC "Or maybe you would... hmm... Is everything ok?"
    ayna "No, [MC], not really"
    MC "Why?"
    scene v43007
    with dissolve
    ayna "We can feel it..."
    MC "You can feel What?"
    ayna "The darkness inside you..."
    scene v43002
    with dissolve
    MC "What do you mean?"
    katarro "I'm pretty sure you know, we can feel his presence in you"
    MC "So you know who this is?"
    MC "Now, wait, I've been struggling hard against him for a while now"
    scene v43007
    with dissolve
    ayna "Don't worry, we also know that you somehow are still in control"
    ayna "And to be honest... that's incredible"
    ayna "We're not even sure if any of us would be able to contain it"
    scene v43002
    with dissolve
    katarro "We still need to discuss what we should do about this"
    ayna "And we need to gather all the information we can"
    if v42grabstone == 1 or v42grabstone == 2:
        $ v43stone = 1
        scene v43003
        with dissolve
        MC "Here, maybe this can help?"
        ayna "That's..."
        katarro "..."
        MC "So... Do you want to take a look at it?"
        scene v43004
        with dissolve
        "Ayna takes the blood colored stone from your hands"
        katarro "No doubt... That's one of the soul stones we used years ago"
        ayna "The power inside this stone is incredible... I forgot how much"
        menu:
            "[abgreen]But it looks like it's dormant now":
                scene v43005
                with dissolve
                ayna "What do you mean?"
                MC "Those things have some sort of affinity with me..."
                MC "Up until now, just touching one would cause it to absorb into me..."
                MC "But for some reason that's not happening right now"
                ayna "I'm glad you brought this to us"
                scene v43008
                with dissolve
                ayna "Katarro please take the stone and examine it"
                ayna "[MC] let's go to Kat, I want her to take a look at you"
                $ v43dormant = 1
                jump v43katlab
            "Say nothing":


                scene v43008
                with dissolve
                ayna "Katarro please take the stone and examine it"
                ayna "[MC] let's go to Kat, I want her to take a look at you"
                jump v43katlab
    else:

        scene v43006
        with dissolve
        ayna "Katarro, try to find out what's going on please"
        ayna "[MC] let's go to Kat, I want her to take a look at you"
        MC "Sure..."
        jump v43katlab

label v43katlab:
    scene v43009
    with dissolve
    "You and Ayna arrive at the lab"

    if my_path_is == "neutral":
        "You can see Isabella and her mother talking with Katriona"
        "You can only wonder what happened to them"
        "Since you were split up by those mages in black"
    else:

        "You can see Isabella and Katla talking with Katriona"
        "You wonder what happened with them"
        "Since you met Isabella in the city some weeks ago"

    "Right now Katriona must be checking if they are healthy"

    scene v43010
    with dissolve
    katla "There is our hero now"
    isabella "Hello again, [MC]"
    MC "Hello ladies, is everything alright?"
    katla "Yes, we're doing fine"
    scene v43011
    with dissolve
    ayna "Katriona, is everything alright with these two?"
    katriona "Yes, everything seems to be perfectly ok"
    katriona "I didn't find any lasting physical effects from the spell they were under"
    katriona "I made sure to give them a small dose this potion just to make sure though"
    scene v43012
    with dissolve
    MC "That's not the scale one, right?"
    katriona "No, I only torture you"
    MC "Yeah, lucky me"
    scene v43011
    with dissolve
    ayna "Katriona, will you please do a thorough examination of [MC]?"
    ayna "He's been through a lot with those Devils, and I need to know"
    ayna "If anything is wrong with him or if they did something lasting to him...."
    scene v43013
    with dissolve
    ayna "Ladies, if you would come with me"
    ayna "There are some things I would like to discuss with you"
    ayna "Also, there are some free rooms you can use to rest and relax"
    katla "Of course, lead the way"
    isabella "I'll see you later [MC]"
    MC "Looking forward to it Isabella"
    scene v43014
    with dissolve
    katriona "Boy you move fast, do you have a thing with that cutie?"
    katriona "Should I tell Mida?"
    if my_path_is == "neutral":
        MC "It's not like that, she's a good friend"
        katriona "Ah yes, of course, you're just friends with that gorgeous girl"
    else:
        MC "It's not like that, I barely know her"
        katriona "Right..."

    scene v43015
    with dissolve
    katriona "Anyway, the Archmage asked me to check you out so.... let me just"
    "You notice where her gaze is directed"
    katriona "Check you out....."
    MC "What are you..... see something you like Kat?"
    katriona "Mmmmm maybe..."
    katriona "Then again, girls do talk and Mida has said some interesting things..."
    MC "And you're what? Jealous?"
    scene v43016
    with dissolve
    katriona "HAHAHAHAHAHA! Maybe.... maybe not.... which would you prefer?"
    MC "I'm not answering that, I know your traps well enough not to walk into one"
    katriona "Well I'll get the truth out of you one way or another..."
    scene v43017
    with dissolve
    katriona "Maybe I'll just have to use one these potions to help"
    MC "Aren't you supposed to be healing me instead of poisoning me?"
    scene v43018
    with dissolve
    katriona "You dummy, don't you know how worried I was?"
    katriona "You were here, then suddenly poof..."
    katriona "You're gone through the portal and no one knows why"
    katriona "Then the Archmage told us you were in Slayer territory, surrounded by demons..."
    katriona "You could have been killed, you idiot"
    katriona "What am I supposed to do then?"
    MC "I'm sorry I worried you Katriona, please forgive me"
    scene v43014
    with dissolve
    katriona "Just promise to be more careful from now on..."
    katriona "And if something weird is going on, tell me about it"
    MC "I will, and I'd tell you more now..."
    MC "But I think I'd need to ask the Archmage if I should."
    katriona "Fine... anyway, lets get to your exam."
    katriona "Trust me, if I find anything terrible has happened, I'll kill you myself"
    MC "Understood"
    "She examines you for a moment"
    katriona "Everything looks fine... at least physically"
    scene v43019
    with dissolve
    katriona "Now... Tell me all about Isabella...."
    MC "{i}sigh"
    MC "Not happening... Bye, see you later"
    katriona "Joy killer..."
    jump afterorcv39

label v43demonspells:
    if v43bookpay == 0:

        $ v43bookpay = 1
        scene v43082
        with dissolve
        yisnna "Demon spells? What are you talking about?"
        MC "Here..."
        scene v43083
        with dissolve
        yisnna "No way... you're kidding"
        MC "I take it these would count toward me finding rare books for you?"
        scene v43084
        with dissolve
        yisnna "Ha ha, show it to me I'll decide about that"
        MC "Oh you don't belive me... Here"
        scene v43085
        with dissolve
        yisnna "Oh my... This is... Do you even know what this is?"
        MC "I know what I was told, but not what's written exactly"
        yisnna "This is demonic language... Incredible..."
        MC "Is there a problem with it?"
        yisnna "How did you get your hands on this? No way"
        yisnna "I... This is a spell book..."
        MC "..."
        scene v43086
        with dissolve
        yisnna "Right... Sorry, I'm just... Surprised"
        yisnna "And no, there's no problem with it"
        yisnna "Knowledge is never an issue..."
        yisnna "The way you use it, is"
        scene v43085
        with dissolve
        yisnna "I'll need some time to translate this.."
        yisnna "I still can't believe this..."
        MC "..."
        scene v43086
        with dissolve
        yisnna "Right... Your reward... Here"
        $ Gold += 50
        play sound "sounds/coin.ogg"
        "You got 50 gold"
        scene v43084
        with dissolve
        yisnna "Good reward right? Bring me more..."
        yisnna "And I'll reward you more"

        if v42spellbookcount >= 2:
            MC "Actually..."
            MC "I have more..."
            scene v43083
            with dissolve
            yisnna "What?"
            MC "I have [v42spellbookcount] of those demonic books..."
            yisnna "No way..."
            MC "Here..."
            scene v43085a
            with dissolve
            yisnna "I can't believe this..."
            yisnna "I'll work on a translation as soon as possible"
            MC "I hope it won't cause you too much trouble"
            scene v43084
            with dissolve
            yisnna "Are you kidding? You made my day"
            yisnna "So... [v42spellbookcount] books..."
            $ v43cashforbooks = v42spellbookcount * 50
            yisnna "[v43cashforbooks] Gold it is"
            $ Gold += v43cashforbooks
            play sound "sounds/coin.ogg"
            "You got [v43cashforbooks] gold"



        scene v43084
        with dissolve
        yisnna "Let me tell you... You made my whole year with this... Hahaha"
        $ yisnalove += 1
        "Yisnna now likes you more"
        yisnna "Visit me later, I may have the translation ready for you"
        MC "Great thanks, see you later Yisnna!"
        jump afterorcv39

    elif v43bookpay == 1:
        scene v43082
        with dissolve
        yisnna "Sorry I haven't finished the translation yet"
        yisnna "Come back later please"
        MC "Sure, see you later"
        jump afterorcv39

label v43courtryo:
    scene v38163
    with dissolve
    "You reach the courtyard and you see Princess Ryo"
    if v43speakryo == 0:

        $ v43speakryo = 1
        scene v38164
        with dissolve
        ryo "Hey [MC] where have you been?"
        MC "It's a long story..."
        scene v38165
        with dissolve
        ryo "I have the time..."
        menu:
            "[abgreen]Talk with her about what happened before":
                scene v38167
                with dissolve
                ryo "Look I... wanted to apologize my behavior from before..."
                ryo "I felt this sudden, overwhelming attaction to you but I had to stop..."
                ryo "Because I felt like I would dishonor myself..."
                scene v38164
                with dissolve
                ryo "If later I asked for your help with my country's affairs..."
                ryo "I didn't want to make it seem like I was using my body to..."
                ryo "To... Get what I wanted from you"
                scene v38165
                with dissolve
                MC "Then I should apologize too..."
                ryo "You do?"
                MC "It was partly my fault as well... I can explain.."
                MC "But not yet..."
                MC "Maybe soon I can tell you, also... The attraction is mutual"
                scene v38166
                with dissolve
                ryo "I would like to have that conversation when you feel like you're ready"
                MC "Great, can we go back trying to be friends and go from there?"
                ryo "Yes, I would like that very much, I like you so far, [MC]"
                ryo "And I would like to continue our friendship"
                ryo "If you do choose to help us, help me..."
                ryo "Then I can accept with a clear conscience"
                $ v43speakryo = 2
                ryo "It was great to talk to you, see you later?"
                MC "Yeah, we certainly will"
                ryo "Thanks for the talk"
                MC "No problem, bye"
                jump afterorcv39
            "Tell her you don't have the time right now":

                scene v38167
                with dissolve
                ryo "Oh... Ok... See you later then"
                MC "Bye"
                jump afterorcv39
    else:
        jump afterorcv39

label v43mcroom:
    if v43visitroomcheck == 1:
        MC "I should look around the college a bit more"
        jump afterorcv39
    if v43nobooks == 1 and v43speakryo >= 1:
        $ v43visitroomcheck = 1
        scene v43043
        with dissolve
        MC "I think I need a rest now..."
        show blink1
        with dissolve
        show blink2
        with dissolve
        show blink3
        with dissolve
        scene black
        with dissolve
        stop music
        play music "<loop 0.0>dark.mp3"
        if Points >= 0:
            jump v43goodside
        else:
            jump v43badside
    if v43bookpay == 1 and v43speakryo >= 1:
        $ v43visitroomcheck = 1
        scene v43043
        with dissolve
        MC "I think I need a rest now..."
        show blink1
        with dissolve
        show blink2
        with dissolve
        show blink3
        with dissolve
        scene black
        with dissolve
        stop music
        play music "<loop 0.0>dark.mp3"
        if Points >= 0:
            jump v43goodside
        else:
            jump v43badside
    else:

        MC "I should look around the college a bit more"
        jump afterorcv39

label v43labkat:
    scene v43018
    with dissolve
    katriona "You're back little flower, what is it? Feeling ill?"
    MC "You..."
    scene v43019
    with dissolve
    katriona "I'm busy you know, I don't just spend all day plotting pranks against you"
    MC "Could have fooled me"
    katriona "Psh, get out of here, let me work"
    jump afterorcv39

label v43goodside:
    Nonen "And you think you can beat me? Really?"
    MC "Uhmm...What?"
    scene v43020
    with dissolve
    Nonen "I told you brother... There is no way you can defeat me now"
    MC "What do you mean?"
    Nonen "Ahahaha embrace all your sins... You'll know true power"
    scene v43021
    with vpunch
    scene v43021
    with hpunch
    MC "Brother? You... What have you done?"
    Nonen "Don't worry, I'll make sure to use your essence"
    scene v43022
    with dissolve
    Nonen "Take that!!!"
    MC "Oh no you won't!"
    scene v43023
    with dissolve
    Nonen "Yes... I'm glad you're fighting back"
    Nonen "Wouldn't be fun otherwise"
    MC "AHH!!"
    scene v43024
    with dissolve
    Nonen "Oh... You're better than I expected brother"
    Nonen "Take this!!"
    scene v43025
    with dissolve
    MC "I got you now!"
    Nonen "You think this will stop me?! Ahaha"
    play sound "sounds/hit.mp3"
    scene v43026
    with hpunch
    Nonen "Hmmmf..."
    Nonen "You bastard... Take this"
    play sound "sounds/hit.mp3"
    scene v43027
    with hpunch
    MC "Ahhh..."
    Nonen "Ahahah.... I told you... Embrace your sins!"
    play sound "sounds/hit.mp3"
    scene v43042
    with vpunch
    MC "Ughhh..."
    Nonen "Ahhh..."
    scene v43027
    with dissolve
    Nonen "You think you can stop me? Nobody can!"
    MC "I will!"
    Nonen "No... You will die!"
    scene v43028
    with dissolve
    MC "Shit..."
    Nonen "Ahaha See?"
    MC "You're coming with me then!!"
    scene v43029
    with dissolve
    Nonen "What??!!"
    MC "Your reign ends now!"
    scene v43030
    with dissolve
    Nonen "DIE!!!!"
    MC "Never!!"
    scene v43031
    with hpunch
    scene v43031
    with vpunch
    Nonen "AHHHH!!!"
    scene v43031
    with vpunch
    scene v43031
    with hpunch
    MC "Be gone!!"
    jump v43postdream


label v43badside:
    Nonen "Stop this at once brother!"
    MC "Uhmm...What?"
    scene v43032
    with dissolve
    Nonen "I told you brother..."
    Nonen "If you kept feeding on sins I would come for you"
    MC "You... Want to stop me?"
    MC "Bring it on then!!"
    scene v43033
    with dissolve
    MC "Get ready to die!!"
    Nonen "I see... There's no way to reason with you anymore"
    Nonen "The sins have rotted your mind, fine!"
    scene v43034
    with dissolve
    MC "Good... You're fighting back... Wouldn't be fun otherwise"
    play sound "sounds/hit.mp3"
    scene v43036
    with hpunch
    MC "Ahhh..."
    Nonen "Weren't expecting that right?!"
    MC "You bastard!! Take that!"
    play sound "sounds/hit.mp3"
    scene v43040
    with dissolve
    Nonen "Uhmff..."
    MC "Like it?!"
    play sound "sounds/hit.mp3"
    scene v43041
    with hpunch
    MC "Argh..."
    Nonen "Two can play this game you know?"
    play sound "sounds/hit.mp3"
    scene v43042
    with hpunch
    MC "Ahaha get away weakling!"
    Nonen "I will never give up!"
    MC "Then DIE!!"
    scene v43037
    with dissolve
    MC "Ahahaha"
    Nonen "You're coming with me!!"
    scene v43038
    with dissolve
    MC "What??!"
    Nonen "You think I can't stop you?!"
    scene v43039
    with hpunch
    scene v43039
    with vpunch
    MC "AHHHH!!!"
    scene v43039
    with vpunch
    scene v43039
    with hpunch
    Nonen "Be gone!!"
    jump v43postdream

label v43postdream:
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v43043
    with dissolve
    MC "AHHHHH!!"
    MC "{i} pant pant pant..."
    MC "Shit... What the hell?"
    play sound "sounds/knock.mp3"
    "Knock Knock"
    isabella "[MC]! Everything ok? I'm coming in"
    scene v43044
    with dissolve
    MC "Isabella?"
    isabella "Are you ok? I was passing by and I heard you scream"
    MC "I'm... Fine... It was a nightmare..."
    scene v43045
    with dissolve
    isabella "Are you sure?"
    MC "Yes... Thank you..."
    scene v43046
    with dissolve
    isabella "Can you stand up? Want me to call someone?"
    MC "I'm fine..."
    scene v43047
    with dissolve
    "You stand up in front of her"
    MC "See? I'm great!"
    isabella "If you say so... There's something I want to tell you..."
    scene v43048
    with dissolve
    isabella "Thank you for saving me and my mother... I..."
    isabella "I don't know what happened to the other hunters..."
    scene v43049
    with dissolve
    isabella "I mean... I have you here... And since that time"
    isabella "That time I saw you... I... Feel..."
    play sound "sounds/knock.mp3"
    "Knock Knock"
    scene v43050
    with dissolve
    lili "Is everything ok in there? [MC]?"
    scene v43051
    with dissolve
    lili "Oh... This is unexpected..."
    MC "Hey Liliana..."
    isabella "Hi..."
    scene v43052
    with dissolve
    lili "So... I heard this screaming and come here running..."
    lili "This is not what I expected to find... "
    isabella "Well this is..."
    menu:
        "Nothing that concerns you Liliana":
            scene v43057
            with dissolve
            lili "Oh ok... I'm leaving then..."
            lili "Have fun you two..."
            scene v43058
            with dissolve
            MC "So you were saying..."
            isabella "That was a bit harsh... She was concerned with you"
            MC "You think?"
            scene v43059
            with dissolve
            "Isabella caress your face"
            isabella "You don't understand women right?"
            MC "What?"
            isabella "Can you take me to the Archmage? I want to talk to her"
            MC "She must be in the throne room or the hall"
            MC "I'll dress in something more appropriate and meet you there"
            scene v43060
            with dissolve
            isabella "Thanks..."
            MC "I'll be right there"
            jump v43findcari
        "[abgreen]Isabella got here first":


            scene v43053
            with dissolve
            MC "Yeah... Isabella beat you to it..."
            MC "She was passing by and was concerned with my scream..."
            lili "So... You saw a mouse or something?"
            MC "Ahah funny..."
            lili "The Archmage wants to talk with you [MC]"
            scene v43052
            with dissolve
            isabella "Oh... Can I go? I want to talk with her too"
            lili "I think that should be fine... Let's go"
            scene v43054
            with dissolve
            lili "You're coming?"
            MC "Yeah... Sure... Let me get dressed in something first"
            scene v43055
            with dissolve
            lili "Or you could come just with your pants like that"
            MC "Ahaha funny"
            scene v43056
            with dissolve
            lili "Let's go Isabella"
            isabella "Thank you"
            jump v43findcari

label v43findcari:
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    scene meanwhile
    with dissolve
    scene v43087
    with dissolve
    man "What happened here?"
    man2 "The church is gone... And some of the surrounding buildings too"
    man "What could have caused this?"
    scene v43088
    with dissolve
    man2 "I would say an enemy invasion, but there's only city soldiers corpses"
    man "Magic?"
    man2 "Let's look around, Calessa told us to look for clues"
    scene v43089
    with dissolve
    man "The destruction... It's unbelievable"
    man2 "Hey what is that?"
    scene v43090
    with dissolve
    man2 "It's a woman..."
    man "A woman? Is she alive?"
    scene v43091
    with dissolve
    man2 "Lady? Can you hear me? Are you ok?"
    man "How is she?"
    scene v43092
    with dissolve
    man2 "She's alive... But she needs to be treated"
    man "Let's take her to the Nest"
    man2 "I agree"
    man "Hey look who's there..."
    scene v43093
    with dissolve
    man2 "Damn... Isn't that Brutus?"
    man "Looks like he never had a chance"


label v43archmagetalk:
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v43061
    with dissolve
    "You arrive to the throne room"
    "Ayna and Yotul are talking, looks like Isabella just got here"
    scene v43062
    with dissolve
    "They notice you"
    ayna "Hey [MC], hope you had a nice rest"
    ayna "What about you Isabella, everything good with your room?"
    scene v43063
    with dissolve
    isabella "Yes thank you... Just bumped into [MC] on the way here"
    MC "Yeah sort of..."
    "You notice that Yotul is not looking very friendly..."
    yotul "What you mean bumped? You're [MC] female?"
    scene v43064
    with dissolve
    isabella "What?"
    MC "What?"
    yotul "Yotul challenge you for [MC]!"
    ayna "Hey, let's calm down please, this is no time or place for this"
    ayna "Isabella, come with me please dear"
    scene v43065
    with dissolve
    "Ayna takes Isabella away and gives you a concerned look"
    MC "Umm... Yotul..."
    scene v43066
    with dissolve
    MC "You can't go around and challenge people like that"
    yotul "No? How you get what you want then?"
    yotul "You don't fight for things you want?"
    MC "Well... Yes... But not like that..."
    scene v43067
    with dissolve
    yotul "Is because Yotul is too strong for little girl?"
    MC "She may be smaller than you"
    MC "But I'm pretty sure she would give a nice fight"
    yotul "Want to see Yotul and little girl fight?"
    menu:
        "Not really":
            scene v43068
            with dissolve
            yotul "[MC] like little girl more than Yotul"
            yotul "[MC] will see, Yotul will make [MC] like her"
            scene v43070
            with dissolve
            yotul "Yotul will train more now"
            yotul "Goodbye"
        "[abgreen]Maybe some day":

            scene v43069
            with dissolve
            yotul "[MC] like Yotul"
            yotul "[MC] can have Yotul when [MC] want"
            MC "That's good to know"
            scene v43071
            with dissolve
            yotul "Yotul will visit [MC] soon"
            scene v43070
            with dissolve
            yotul "Yotul will train more now"
            yotul "Goodbye"

    scene throne
    with dissolve
    "She left, you are now alone"
    MC "I guess I should go too..."
    MC "I need to relax a bit, maybe I should go train a bit?"
    MC "Or maybe a nice bath?"
    $ v43bathfannay = 1
    jump afterorcv39

label v43bathfannay:
    scene v43177
    with dissolve
    "You're in the baths"
    MC "Nobody is here, perfect time to relax a bit"
    MC "Time to try the water"
    scene v43178
    with dissolve
    MC "Ahhh.... Perfect as usual... Pfew..."
    MC "I don't know what spell or enchantment they use here"
    MC "But this water always feels like heaven"
    fannay "I was pretty sure I saw you coming here..."
    scene v43179
    with dissolve
    MC "Fannay?"
    fannay "[MC]?"
    MC "What are you doing here?"
    scene v43180
    with dissolve
    fannay "Same as you probably... Taking a bath"
    if my_path_is == "evil" and sexv038 <= 5:
        MC "You got a lot of nerve... After what you did..."
        scene v43181
        with dissolve
        fannay "What did I do? Tell Mida we fucked?"
        MC "You little bitch..."
        if midacorr >= 3:
            fannay "I like it when you treat me like that..."
            fannay "And you will thank me later"
            fannay "Wouldn't it be fun to fuck me and your pretty Mida together?"
            MC "What?"
            scene v43182
            with dissolve
            fannay "Yes... I can see it in you face..."
            fannay "And probably your dick too..."
        else:
            fannay "I like it when you treat me like that..."
            MC "Now Mida is pissed... I'm not sure I can turn that around"
            scene v43182
            with dissolve
            fannay "I didn't force you to fuck me..."
    else:

        MC "And you choose now to do it?"
        scene v43181
        with dissolve
        fannay "What better time than when you're here?"
        MC "Uhm..."

    menu:
        "Get the fuck out![abred] [abnocorruptionlove]":
            scene v43180
            with dissolve
            fannay "Jeez... Ok... I'll leave you and you bath alone"
            MC "..."
            $ fannaylove -= 1
            $ fannaycorr -= 1
            "Fannay's love and corruption decreased"
            scene v43185
            with dissolve
            fannay "Bye Bye then..."
            scene v43178
            with dissolve
            "You are alone in the bath again"
        "You're here just for the bath?[abcorruptioncolor] [abcorruptionlove]":

            scene v43183
            with dissolve
            fannay "Do you have other... Plans?"
            MC "Maybe..."
            fannay "Hmmm... Really?"
            scene v43184
            with dissolve
            fannay "Would those plans involve my lips?"
            fannay "{i} Muaw"
            "She kissed you"
            "You start to feel your cock rising..."
            MC "What lips are we talking about?"
            scene v43183
            with dissolve
            fannay "Ahahah... Maybe you'll find out later..."
            MC "What?"
            fannay "You don't want people to catch us here..."
            $ fannaylove += 1
            $ fannaycorr += 1
            "Fannay's love and corruption increased"
            scene v43186
            with dissolve
            fannay "Bye bye... See you later..."
            fannay "Oh and stay in the water for a while..."
            scene v43185
            with dissolve
            fannay "You don't want everybody to see that hard on"
            MC "..."
            scene v43178
            with dissolve
            "You are alone in the bath again"

    "You relaxed in the water for some time before returning to your room"
    jump v43roomsexscene

label v43roomsexscene:
    scene v43043
    with dissolve
    MC "Ah... I feel so relaxed now..."
    "You remove your clothes and lie down in bed with your underwear"
    MC "It's not night yet but that nightmare earlier..."
    MC "I haven't rested that much yet"
    play sound "sounds/knock.mp3"
    "Knock Knock"

    if my_path_is == "neutral":
        isabella "[MC]?"
        MC "Isabella?"
        menu:
            "[abgreen]Come on in":
                jump v43isasex
            "Go away, I need to rest":

                isabella "Oh... Sorry"
                $ v43endsexwith = "rejisa"

                jump v43breditanecro


    elif my_path_is == "evil":
        lili "[MC]?"
        MC "Liliana?"
        menu:
            "[abgreen]Come on in":
                jump v43lilisex
            "Go away, I need to rest":

                lili "Ok then..."
                $ v43endsexwith = "rejlili"
                jump v43breditanecro
    else:

        zordruza "[MC]?"
        MC "Zordruza?"
        menu:
            "[abgreen]Come on in":
                jump v43zorsex
            "Go away, I need to rest":

                zordruza "Oh fine!"
                $ v43endsexwith = "rejzor"
                jump v43breditanecro


label v43isasex:
    scene v43044
    with dissolve
    isabella "I'm sorry to bother you..."
    MC "No problem at all"
    scene v43045
    with dissolve
    isabella "Isn't it a bit early to..."
    isabella "Be in your underwear in bed...? "
    MC "Well... I just came out of the baths, I'm just relaxing a bit"
    scene v43046
    with dissolve
    isabella "You mean... Oh.. Sorry to bother you then..."
    "You get up"
    scene v43047
    with dissolve
    MC "No need to apologize... Actually I'm glad you're here"
    isabella "You are?"
    scene v43094
    with dissolve
    MC "Yes, is everything ok with you?"
    isabella "Yes... Considering everything that happened"
    isabella "And thanks to you obviously"
    MC "That's good to know"
    menu:
        "Well, I need to rest now. See you later?":
            scene v43096
            with dissolve
            isabella "Oh... Sure... See you later"
            $ v43endsexwith = "rejisa"
            scene v43043
            with dissolve
            "She left the room and you are alone again"
            play sound "sounds/door.mp3"
            $ renpy.end_replay()
            jump v43breditanecro
        "Tell her you're there for her{color=#1BBB20} (+1 Isabella's Love)":
            scene v43095
            with dissolve
            MC "I would do everything to keep a smile on you face"
            $ isabellalove += 1
            "Isabella likes you more"
            if isabellalove <=3:
                scene v43096
                with dissolve
                isabella "I... I need to go... Sorry..."
                MC "Wait..."
                scene v43060
                with dissolve
                isabella "I'm so sorry... I need to go"
                play sound "sounds/door.mp3"
                scene v43043
                with dissolve
                "She left and you are alone in the room again"
            else:
                isabella "{i} giggle"
                isabella "I'm so glad you found us..."
                scene v43096
                with dissolve
                isabella "I don't even know how long it has been.."
                isabella "Or what we did..."
                scene v43095
                with dissolve
                MC "Don't worry about it now, everything is ok now"
                isabella "Yes..."
                scene v43097
                with dissolve
                isabella "And it's all thanks to you"
                "You notice that her face is getting closer to yours.."
                "Is she trying to kiss you?"
                scene v43098
                with dissolve
                "She kisses you, you can feel her tremble"
                "You can taste her soft lips"
                scene v43097
                with dissolve
                isabella "Did you like it?"
                MC "Yes..."
                MC "I always like kissing you"
                MC "Do you remember that night?"
                isabella "What night?"
                MC "The night we got a bit drunk and..."
                scene v43095
                with dissolve
                isabella "Actually to be honest I don't remember much..."
                MC "Oh..."
                scene v43097
                with dissolve
                isabella "Did something happen?"
                MC "Hmmm..."
                scene v43099
                with dissolve
                "Isabella sits in your bed"
                isabella "Do you not remember either or what?"
                "Maybe you should pretend you don't remember either"
                MC "Yeah... I was pretty drunk too..."
                scene v43100
                with dissolve
                isabella "You know... I'm not drunk now... So I'll remember"
                "Did she just gave you a hint to make a move?"
                MC "I can sense that we are on the same page on that matter"
                isabella "And...?"
                scene v43101
                with dissolve
                MC "You know... I think you are gorgeous... Your face... Your eyes"
                MC "Your Lips..."
                scene v43100
                with dissolve
                isabella "Nothing about my body? Really?"
                MC "I...That's..."
                isabella "Maybe you need to take a better look?"
                scene v43102
                with dissolve
                "She takes her top off, exposing her breasts"
                isabella "So? Have something else to say? "
                MC "Wow... Yes..."
                "You move your hands closer to her chest"
                scene v43103
                with dissolve
                MC "They are beautiful... Perfect..."
                isabella "Hummm... Your hands... Ah..."
                "You start to stimulate her right nipple"
                isabella "Ah... Yes..."
                scene v43102
                with dissolve
                isabella "I... Need something more..."
                "You can't agree more with her words"
                scene v43104
                with dissolve
                "She removes her skirt and gives you a shy look"
                "It's like she's waiting for you to say or do something"
                MC "You look like a Goddess right now..."
                scene v43105
                with dissolve
                "Your words made her relax a little"
                isabella "Oh really? {i} giggle"
                isabella "Is there something you want to do to please your Goddess?"
                "You waste no time"
                scene v43106
                with dissolve
                "You move towards her, and you start to rub her pussy"
                isabella "Ah... Your hand... Feels great"
                MC "Then I'll show you something more"
                scene v43107
                with dissolve
                "You then procced to lick her pussy"
                isabella "Ah... That's so good... Ah"
                "You can feel and taste her juices coming out"
                isabella "Yes....."
                scene v43108
                with dissolve
                "You give it a little more speed"
                "You notice that she is now fondling her own breast"
                isabella "AHHH!! YES!"
                "Looks like she's enjoying herself"
                "Maybe it's time to use other parts of you?"
                scene v43109
                with dissolve
                "You rest your dick close to her pussy"
                MC "Is everything ok?"
                isabella "Yes... Listen... this is my first time..."
                isabella "But my hymen already broke a long time ago..."
                isabella "So please believe me..."
                MC "Of course I do, I'm happy I get to be your first...."
                "She nods at you signaling that she is ready"
                scene v43110
                with dissolve
                "So you start to push your dick inside her"
                isabella "Ah.... it's so big..."
                "She feels so tight..."
                MC "Humm... You feel amazing..."
                isabella "Come here, get closer to me"
                scene v43111
                with dissolve
                "She grabs your arms a pulls you down on her"
                "You keep moving your hips, now face to face with Isabella"
                isabella "Ah... Yes... Keep going"
                MC "Ah... Ah... "
                isabella "You can go faster now if you want"
                "That's all you needed to hear and start to go faster"
                isabella "Ahhh... YES!"
                scene v43112
                with dissolve
                "You can see that she is enjoying herself..."
                "So you go even faster and harder"
                isabella "AH! Yes... Yes... I'm..."
                "You feel her clamping your dick harder"
                "You decide to stop and move her on top of you"
                scene v43113
                with dissolve
                "Before she can even say anything, you're going at it again"
                isabella "Ah... This is so good..."
                "You decide to give it all you got"
                scene v43114
                with dissolve
                isabella "AH!!! YES!!! I'm.... "
                isabella "AHHHHHHH!!!"
                "You feel her orgasm hitting her hard"
                "Your cock is now being completely squeezed by her lower lips"
                scene v43115
                with dissolve
                "Her climax is so strong that she can't even maintain her balance"
                isabella "YEEES!!!"
                "You start to feel yourself getting closer"
                "Should you try to pull it out?"
                scene v43117
                with dissolve
                MC "Isabella... I..."
                isabella "Don't worry about it... Keep going!"
                "Does she even realize that you are about to cum?"
                scene v43115
                with dissolve
                "She presses harder against you..."
                "You can't hold it anymore"
                scene v43116
                with dissolve
                "She notices that you are about to cum and presses even harder"
                isabella "Yes... Cum for me..."
                $ v43endsexwith = "isabella"
                "Those words were the last trigger"
                MC "AHHHH!!! I'm..."
                show shot
                with hpunch
                scene v43115a
                with dissolve
                show shot
                with vpunch
                hide shot
                "You feel your dick filling her up"
                MC "Uhmmm... damn... That... Was..."
                scene v43118
                with dissolve
                isabella "{i} Muwa"
                isabella "Thank you"
                scene v43119
                with dissolve
                "Isabella get's up but you are too tired to move"
                isabella "I... Why do I feel that..."
                MC "What's wrong? Are you ok?"
                isabella "I... Don't know... I..."
                MC "Want to stay here and rest a bit?"
                isabella "Thank you but I need to talk with my mother"
                MC "But..."
                scene v43045
                with dissolve
                "She dresses again"
                isabella "I need to go... I feel strange"
                MC "Wait..."
                scene v43120
                with dissolve
                isabella "Sorry, I need to go..."
                play sound "sounds/door.mp3"
                scene v43043
                with dissolve
                "She left the room and you are alone again"
                MC "...."
                $ renpy.end_replay()
                jump v43breditanecro


label v43lilisex:
    scene v43121
    with dissolve
    lili "Hey, how's our big hero feeling right now?"
    MC "Pretty good actually, just relaxing a bit"
    scene v43122
    with dissolve
    "You get up from bed"
    lili "Relaxing? Hum... You mean... Manual relaxation?"
    lili "I could help with that you know?"
    menu:
        "You should leave now":
            scene v43152
            with dissolve
            lili "Your loss... See you around"
            $ v43endsexwith = "rejlili"
            play sound "sounds/door.mp3"
            scene v43043
            with dissolve
            "She left the room and you are alone again"
            $ renpy.end_replay()
            jump v43breditanecro
        "{color=#1BBB20}Really?":

            $ v43endsexwith = "liliana"
            scene v43123
            with dissolve
            lili "Yes... Do you need a helping hand?"
            "Before you could answer"
            scene v43124
            with dissolve
            "Liliana pushes you to the bed"
            MC "Woah..."
            lili "I'll show you what you get for saving me!"
            scene v43125
            with dissolve
            "Liliana crawls on the bed getting very close to you"
            lili "What should we do about this?"
            "She removes your underwear exposing your erect penis"
            scene v43126
            with dissolve
            lili "Hmmm... So big... I love it..."
            lili "It's twitching in my hand..."
            lili "I think it wants a kiss..."
            scene v43127
            with dissolve
            "Liliana is now kissing and licking you dick"
            MC "Hmmm..."
            lili "Like it? Maybe we can do better..."
            scene v43128
            with dissolve
            "She starts to put the tip of you dick in her mouth"
            "And starts to move up and down on your head"
            MC "Ah... yes... That feels great..."
            scene v43129
            with dissolve
            "Before you can say anything else she goes deeper"
            lili "Mmmmm... {i} Slurp Slurp"
            MC "Oh shit... That feels amazing..."
            scene v43130
            with dissolve
            "She stops sucking and stares at you"
            lili "Who wants to be taken care of?"
            menu:
                "Assume control of the situation[abcorruptioncolor] [abcorruption]":
                    $ v43lilidom = 1
                    scene v43131
                    with dissolve
                    MC "You want to play games? I'll give you games!"
                    lili "Wha...?"
                    scene v43132
                    with dissolve
                    "You push her to the bed with her ass towards you"
                    lili "Oh...."
                    $ lilicorr += 1
                    "Liliana corruption increased"
                    MC "Let's see if you know how to play my game"
                    scene v43133
                    with dissolve
                    "You point your dick into her pussy entrance"
                    lili "Hmmmmm"
                    MC "You like this don't you?"
                    lili "...Yes..."
                    MC "Then take it!"
                    scene v43134
                    with dissolve
                    "You shove your cock all the way in"
                    lili "AHH! Yes!"
                    MC "You like this don't you, you little slut?"
                    lili "Yes! Yes! I love it! Give me more!"
                    MC "Who's my little slut?"
                    lili "I am... I'm your slut master!"
                    MC "Turn around!"
                    scene v43135
                    with dissolve
                    "You flip her around and shove you dick in again"
                    "You can see that she is loving it by the joy on her face"
                    "You go faster and harder on her"
                    scene v43136
                    with dissolve
                    lili "Yes! Don't stop! Make me cum!!"
                    MC "You little slut! Take it all!!"
                    lili "Ah I'm...."
                    scene v43137
                    with dissolve
                    lili "Ahhh!!!"
                    "You feel her trembling as she orgasms"
                    "You feel like you are about to reach climax yourself"
                    MC "Ahh!! I'm..."
                    lili "Ah..."
                    "She loses her balance and falls on the bed"
                    scene v43138
                    with dissolve
                    MC "Ah fuck... I can't hold it anymore..."
                    lili "Cover me master!"
                    menu:
                        "Cum all over her":
                            show shot
                            with hpunch
                            scene v43139
                            with dissolve
                            show shot
                            with vpunch
                            hide shot
                            MC "FUUUUCK!!"
                            "You release all your semen onto her"
                            MC "....."
                            scene v43140
                            with dissolve
                            lili "Ah.... Look at this.... "
                            MC "Shit.... This was great..."
                            "She cleans up"
                            jump v43liliendsex
                        "Put it back inside and cum":
                            scene v43135
                            with dissolve
                            lili "AHHH!!"
                            show shot
                            with hpunch
                            scene v43136a
                            with dissolve
                            show shot
                            with vpunch
                            hide shot
                            MC "FUUUUCK!!"
                            "You release all your semen inside her"
                            MC "....."
                            lili "Ah.... You filled me up.... "
                            MC "Shit.... This was great..."
                            "She cleans up"
                            jump v43liliendsex
                "Let her play her game[ablovecolor] [ablove]":

                    $ v43lilidom = 2
                    scene v43141
                    with dissolve
                    lili "Look at that hard cock..."
                    lili "What does it want? My mouth? My pussy?"
                    MC "..."
                    scene v43142
                    with dissolve
                    "She pushes you and grabs your cock"
                    "Then she starts to stroke it with slow but strong movements"
                    lili "So hard... You're a good boy..."
                    $ lililove += 1
                    "Liliana now likes you more"
                    scene v43143
                    with dissolve
                    "Liliana gets up on bed, places her foot on your chest"
                    lili "Ready to have more fun?"
                    MC "Yes..."
                    scene v43144
                    with dissolve
                    lili "See this pussy here? Hmm?"
                    MC "Yes..."
                    lili "I want your cock all the way in"
                    scene v43145
                    with dissolve
                    "After those words she sit on your dick"
                    "Sliding it all the way inside her"
                    lili "Hmmm... So big.... So good..."
                    MC "Ah.... Shit..."
                    scene v43146
                    with dissolve
                    lili "Now now... Watch your tongue..."
                    lili "Or I'll use it for other things..."
                    "She starts moving fast and hard"
                    scene v43145
                    with dissolve
                    lili "Ah... Yes.... That cock all the way inside..."
                    lili "Feels great... YES!"
                    scene v43146
                    with dissolve
                    "You feel you are about to cum"
                    lili "Yes... Give me all that tasty cum... Give it to me!"
                    MC "Ah... Fuck..."
                    scene v43147
                    with dissolve
                    "She feels you are about to cum and jumps off your dick"
                    "After that she strokes you dick fast and hard"
                    lili "Come on, cover me!"
                    MC "FUUCK!"
                    show shot
                    with vpunch
                    scene v43148
                    with dissolve
                    show shot
                    with vpunch
                    hide shot
                    lili "Yes! Cum for me!"
                    MC "Ahhhh!"
                    scene v43149
                    with dissolve
                    lili "Look at all this mess..."
                    lili "You're a dirty dirty boy..."
                    lili "I should make you clean all this..."
                    scene v43150
                    with dissolve
                    lili "Hmmm tasty... I'll clean it up myself..."
                    "She swallows all the cum on her face"
                    jump v43liliendsex


label v43liliendsex:
    $ renpy.end_replay()
    scene v43151
    with dissolve
    lili "This was great... And you had a lot to give {i} giggle"
    lili "I'm satisfied... I hope you are too"
    MC "{i} pant pant..."
    MC "Oh.. I am..."
    scene v43122
    with dissolve
    "Liliana dresses again"
    lili "Time for me to go... Hope we can do this again"
    MC "Me too!"
    scene v43152
    with dissolve
    lili "Bye bye [MC]"
    MC "Bye...."
    play sound "sounds/door.mp3"
    scene v43043
    with dissolve
    "She left and you are alone in your room"
    MC "That was great..."
    jump v43breditanecro


label v43zorsex:
    scene v43153
    with dissolve
    zordruza "Hello [MC], are you feeling well?"
    MC "Yeah, just relaxing a bit"
    scene v43154
    with dissolve
    zordruza "I just came here to thank you for saving me"
    zordruza "Thanks to you, I'm free again"
    zordruza "And I can start to figure out how to help my people"
    MC "I would always do my best to help"
    scene v43155
    with dissolve
    zordruza "I know... And that's why I like you so much"
    MC "I..."
    zordruza "You know I..."
    scene v43156
    with dissolve
    zordruza "{i} kiss"
    "You feel her lips pressing against yours, they are soft and warm"
    scene v43155
    with dissolve
    zordruza "Do you like me too?"
    menu:
        "[abgreen]Yes I do!":
            $ v43endsexwith = "zordruza"
            scene v43156
            with dissolve
            zordruza "{i} kiss"
            "You are both kissing each other passionatly"
            "One thing takes to another"
            scene v43157
            with dissolve
            "You start to fondle her breast, she doesn't complain..."
            zordruza "Hmmm"
            "Quite the opposite actually..."
            zordruza "I think those clothes are in the way..."
            scene v43158
            with dissolve
            "You got the tip and undress her"
            zordruza "Yes... Play with them... Hmmmm"
            zordruza "You like them?"
            MC "I do..."
            scene v43159
            with dissolve
            zordruza "Take off your underwear... I want to do something for you"
            "She doesn't have to tell you twice"
            scene v43160
            with dissolve
            "She grabs your dick and presses it against her face"
            zordruza "So hard already..."
            MC "I'm happy to see you..."
            zordruza "{i} giggle {/i} Right..."
            zordruza "Let's see if you get happier"
            scene v43161
            with dissolve
            "She is now licking your tip"
            MC "Hmmm...That feels great..."
            zordruza "Mmm Mmm {i} slurp, lick"
            scene v43162
            with dissolve
            "Your dick is now almost all the way inside her mouth"
            MC "Ah..."
            zordruza "Mmmmmm"
            "She starts to go faster and deeper"
            MC "Oh... Fuck..."
            scene v43163
            with dissolve
            zordruza "Fuck? I think it can be arranged"
            "She says it with a lewd look in her face while licking you"
            scene v43164
            with dissolve
            "She moves to the bed"
            zordruza "So you were saying?"
            MC "I... Was saying..."
            zordruza "Bring that big cock here"
            scene v43165
            with dissolve
            "You do as the lady says and get closer to her..."
            zordruza "Good... and now you..."
            scene v43166
            with dissolve
            "You don't let her finish and start sliding your dick in"
            zordruza "Ah.... Hmmm..."
            MC "Oh... You're so tight..."
            zordruza "Come here..."
            scene v43167
            with dissolve
            "She pulls you over her forcing your dick all the way in"
            zordruza "Ah... Yes.... It's all the way in... Hmmm"
            MC "Ah.... Yes..."
            "You both start to move faster and faster"
            zordruza "Let me ride you [MC]"
            scene v43168
            with dissolve
            "You nod and she climbs on top of you"
            zordruza "Ah yes.... I feel it all in!"
            zordruza "Give me more! More!"
            scene v43169
            with dissolve
            "You give it all you got, hard and fast"
            zordruza "YES!!! YES!! MORE!! Don't stop!"
            "You start to feel her getting tighter and tighter"
            scene v43170
            with dissolve
            "That pressure is too much and your orgasm is getting closer"
            zordruza "Yes!! Give me more! I'm... About to..."
            scene v43171
            with dissolve
            zordruza "CUUUUUM!!! AH!!! YES!!!"
            MC "Shit I can't hold it any longer"
            scene v43172
            with dissolve
            zordruza "Yes!! Give it all to me"
            MC "Fuck..."

            menu:
                "Pull out":
                    show shot
                    with vpunch
                    scene v43173
                    with dissolve
                "Cum inside":

                    show shot
                    with vpunch
                    scene v43172a
                    with dissolve
            show shot
            with vpunch
            hide shot
            MC "AHHHHH! SHIT!!!"
            zordruza "Hmmm.... So much..."
            scene v43174
            with dissolve
            MC "{i} pant pant pant..."
            MC "That...{i} pant pant pant..."
            MC "Was great..."
            zordruza "I agree... This some of the best sex I ever had"
            zordruza "We should do it again sometime"
            MC "Definitely..."
            scene v43175
            with dissolve
            zordruza "Now I need to go..."
            zordruza "Don't take me wrong... I loved it"
            zordruza "But I have some matters to take care of"
            MC "Sure..."
            scene v43176
            with dissolve
            "Zordruza gets dressed and walks towards the door"
            zordruza "Bye bye [MC] See you soon"
            MC "Bye"
            play sound "sounds/door.mp3"
            scene v43043
            with dissolve
            "She left and you are alone in your room"
            MC "That was great..."
            jump v43breditanecro
        "I think you should go...":

            $ v43endsexwith = "rejzor"
            scene v43154
            with dissolve
            zordruza "Oh... Ok... "
            scene v43176
            with dissolve
            zordruza "See you later I guess"
            play sound "sounds/door.mp3"
            scene v43043
            with dissolve
            "She left the room and you are alone again"
            jump v43breditanecro


label v43breditanecro:
    $ renpy.end_replay()
    stop music
    play music "<loop 0.0>dark.mp3"
    scene meanwhile
    with dissolve
    scene v43187
    with dissolve
    Bredita "Now let's see if you can be useful to me"
    Bredita "First... You will tell me all you know..."
    Bredita "Yes... Exactly... Your mind is clear"
    Bredita "Thank you... Now..."
    scene v43188
    with dissolve
    Bredita "I shall reward you... With power..."
    Bredita "The greatest power you ever had"
    Bredita "Rise!! Rise!!"
    scene v43189
    with dissolve
    Bredita "Open your eyes..."
    Bredita "And obey!"
    brutus "Ahhhhnnnn..."
    jump v44script
