
screen mcroomschool:
    imagemap:
        ground "mckidroom.jpg"
        hover "mckidroom01.jpg"

        hotspot (860, 390, 190, 100) clicked Jump ("Books")
        hotspot (1300, 260, 600, 750) clicked Jump ("sleeping")
        hotspot (0, 670, 350, 410) clicked Jump ("Chest")

screen mcroomrobe:
    imagemap:
        ground "mckidroom.jpg"
        hover "mckidroom01.jpg"

        hotspot (860, 390, 190, 100) clicked Jump ("Books01")
        hotspot (1300, 260, 600, 750) clicked Jump ("sleeping01")
        hotspot (0, 670, 350, 410) clicked Jump ("Chest01")

screen kidscorridor:
    imagemap:
        ground "Studentskids.png"
        hover "Studentskids01.png"

        hotspot (0, 0, 1010, 1080) clicked Jump ("Badguys")
        hotspot (1011, 0, 1920, 1080) clicked Jump ("Goodguys")



label lessons:

    $ booksschool = False
    scene hall
    with dissolve
    hide k001
    show k002
    with dissolve
    katarro "So, do you know where you are?"
    MC "I have no idea..."
    katarro "As expected"
    katarro "Well..."
    hide k002
    show k003
    with dissolve
    katarro "You are in the College of Allesterra"
    MC "College of Allesterra?"
    show k001
    with dissolve
    hide k003
    katarro "Yes..."
    katarro "You were brought here"
    katarro "The Archmage believes that you have great magic in you"
    katarro "So you will be attending classes here"
    menu:
        "{color=#1BBB20}Ok.. if you think so..":
            katarro "Good"
            jump lessons01
        "What if I don't want to?":
            show k002
            with dissolve
            hide k001
            katarro "Ahahah"
            katarro "Well... do you want to try to live on your own?"
            katarro "Where will you go?"
            show k003
            with dissolve
            hide k002
            katarro "Are you sure that's what you want?"
            MC "You're right..."
            jump lessons01

label lessons01:
    hide k001
    show k001
    with dissolve
    hide k003

    MC "So what can you tell me about this place?"
    MC "And about you?"
    katarro "Well... I'm Master Katarro"
    katarro "I'm one of the Elite Mages of the College"
    katarro "I'm the highest mage of the Mysticism school"
    show k003
    with dissolve
    hide k001
    katarro "There are 6 Elite Mages"
    katarro "One of each school"
    katarro "And Anya, the Archmage, is our leader"
    MC "That's the lady that was in the bath.. {i}cough{/i}"
    MC "I mean... the lady that talked to me earlier"
    show k002
    with dissolve
    hide k003
    katarro "Probably yes.."
    katarro "She has golden hair and is very attractive"
    katarro "For your kind"
    MC "What do you mean, my kind?"
    show k001
    with dissolve
    hide k002
    katarro "I mean humans"
    katarro "As you can see I'm an Elf"
    MC "I've... never met an elf before"
    MC "But hey... I don't even remember who I am so..."
    katarro "Very well"
    katarro "Let me take you to your room"
    katarro "Follow me"
    show k004
    with dissolve
    hide k001
    hide k004
    with dissolve
    show k005
    with dissolve
    katarro "Are you coming?"
    MC "Yes... sure"
    scene mckidroom
    with dissolve
    show k006
    with dissolve
    katarro "This is your room"
    katarro "You will stay here as long as you remain a novice student"
    show k007
    with dissolve
    hide k006

    MC "What do you mean?"
    katarro "Don't worry about it now... Get some rest"

    katarro "You also have some books there, you can use them to study"

    katarro "Tomorrow morning you'll start having classes"
    katarro "I'll be leaving you now"
    hide k007
    with dissolve
    MC "Ok..."
    jump sowhat

label sowhat:

    call screen mcroomschool

label Books:
    if booksschool == True:
        MC "There's nothing else to read.."
        jump sowhat
    else:
        MC "What is this?"
        MC "Some kind of spell?"
        MC "Invisibility?"
        "You spend some time reading the book"
        "You have gained 1 point in Illusion school"
        $ Iluspoints += 1
        $ booksschool = True
        jump sowhat
label Chest:

    MC "There is nothing inside.."
    jump sowhat
label sleeping:

    MC "Well..."
    MC "I guess it's time to sleep"
    "You lay down on the bed and fall asleep"
    scene black
    with dissolve
    fvoice "Did you miss me?"
    scene black01
    with dissolve
    scene black02
    with dissolve
    MC "You..."
    $ metdark = False
    if cheaterfix == 1:
        fvoice "Did you enjoy the last dream I gave you?"
        MC "Well... It ended at the best part.."
        fvoice "Ahaha"
        fvoice "You know..."
        fvoice "Maybe I can redeem myself?"
        MC "That would be nice"
        fvoice "Maybe another time..."
        fvoice "Now let me tell you"
        fvoice "This is going to be our last encounter like this"
        fvoice "But I'm sure you'll achieve great things"
        fvoice "Let me give you a nice gift"
        "You gained 1 point in Healing"
        $ Healpoints += 1
        MC "Thank you"
        fvoice "No need to thank me..."
        fvoice "And I'm sure we'll meet again in the future"
        fvoice "Now it's time to wake up"
        fvoice "You have a long day ahead of you...."
        scene black
        with dissolve
        jump schoolday01
    else:
        fvoice "I'm a little disappointed with you"
        MC "Why is that?"
        fvoice "Because of your decision"
        fvoice "To see your mother suffer"
        fvoice "Why would you do that?"
        menu:
            "I do what I want!!{color=#FF0000} (-1 Alignment/+1 Necropoint)":
                $ Points -= 1
                "You received -1 Alignment"
                fvoice "I'm sad to hear that..."
                nar "Time to leave..."
                nar "I'll take care of this from here"
                scene black
                with dissolve
                show narface
                MC "Who are you?"
                $ metdark = True
                nar "That doesn't matter now..."
                nar "I'm glad...."
                nar "I see great things in your future"
                nar "If you keep on this path..."
                nar "There are many things"
                nar "That you will have to learn by yourself"
                MC "What do you mean?"
                nar "Don't you like power?"
                MC "...Yes..."
                nar "Don't you want to be free to do whatever you want?"
                MC "...Yes..."
                nar "Good......"
                nar "Our paths will cross at some point"

                nar "Here's a gift..."
                hide narface
                with dissolve
                $ Necropoints += 1
                "You gained 1 point in Necromancy"
                nvl clear
                n "The figure disappeared"
                MC "Wow, that was strange..."
                jump schoolday01
            "I'm sorry... forgive me I didn't mean to...{color=#1BBB20} (+1 Alignment/Healpoint)":

                $ Points = 0
                "You received +1 Alignment"
                fvoice "That's good"
                fvoice "Let's leave it in the past"
                fvoice "Since you repented"
                fvoice "Let me give you a nice farewell gift"
                "You gained 1 point in Healing"
                $ Healpoints += 1
                MC "Thank you, but what do you mean farewell?"
                fvoice "No need to thank me..."
                fvoice "This is our last encounter like this"
                fvoice "Now it's time to wake up"
                fvoice "You have a long day ahead of you...."
                scene black
                with dissolve
                jump schoolday01


label schoolday01:
    nvl clear
    scene mckidroom
    with dissolve
    "You wake up and it's morning"
    nvl clear
    MC "Well I guess I have to go to classes or something"
    MC "But... how do I get there?"
    MC "Am I supposed to wait here?"
    MC "Or should I go look for someone?"
    menu:
        "Stay in the room":
            MC "I'll wait for someone to pick me up here"
            katriona "Hey.."
            show katriona001
            with dissolve
            katriona "What are you waiting for?"
            MC "Uhmm"
            MC "I don't know where I am so..."
            katriona "Right...."
            katriona "Let me take you to class then"
            hide katriona001
            jump schoolday02
        "{color=#1BBB20}Leave the room":

            scene hall
            with dissolve
            MC "Now what?"
            katriona "Hey"
            show katriona004
            with dissolve
            katriona "Curious boy"
            MC "Hi..."
            hide katriona004
            show katriona001
            with dissolve
            katriona "Ready for Magic class?"
            MC "I guess.."
            katriona "Ahahah"
            katriona "Let's go"
            jump schoolday02

label schoolday02:

    scene hall
    with dissolve
    show katriona002
    with dissolve
    katriona "We're almost there"
    katriona "Here we are"
    scene classroom001
    with dissolve
    show katriona003
    katriona "Here you go"
    katriona "You're on your own now"
    katriona "Bye..."
    hide katriona003
    with dissolve
    "You look at the class"
    "And everybody looks back at you..."
    "You see the professor"
    "A woman dressed in pink"
    "And other kids, all looking at you"

    fprof "Please take a seat"
    MC "Ok..."
    scene classroom002
    with dissolve
    MC "Hi, I'm [MC]"
    MC "Is this seat taken?"
    mida "Hello, I'm Mida"
    mida "Yes you can sit there, it's not taken"
    MC "Thank you"
    scene classroom003
    with dissolve
    mida "Let me guess, are you a Nord?"
    MC "Well I..."
    fprof "Am I interrupting your conversation?"
    scene classroom005
    with dissolve
    fprof "Can I continue todays lesson?"
    fprof "Very well"
    scene classroom006
    with dissolve
    fprof "We are going to learn some History and Geography"
    "You are a bit confused..."
    "Isn't this supposed to be a magic school?"
    scene classroom005
    with dissolve
    fprof "I know what you're all thinking"
    fprof "Aren't we supposed to learn magic here?"
    scene classroom006
    with dissolve
    fprof "Yes... But you will also learn other things"
    fprof "A great mage or wizard loves knowledge"
    nvl clear
    n "You can skip this part of the lesson if you want"
    n "But if you are interested in the plot of the game"
    n "Don't skip"
    nvl clear
    n "If you're in it for the porn"
    n "By skipping you lose some of the game's plot"
    n "But no sex scenes"
    nvl clear
    n "Do you want to skip or keep listening to this lesson?"
    nvl clear
    menu:
        "Skip the history and geography part":
            "You decided to skip history and geography"
            "Some of the game's plot maybe be harder to understand now"
            jump magiclesson001
        "{color=#1BBB20}Listen to the whole lesson":
            scene classroom006
            with dissolve
            fprof "So let's start"
            fprof "Here you can see where we are"
            fprof "This Blue island is Allesterra"
            fprof "Our College is located here"
            fprof "We are known to the world as the Mages"
            fprof "We usually look for children with the potential for magic"
            fprof "And we bring them here to the College"
            fprof "With their parents permission of course "
            fprof "You are all examples of that"
            fprof "With one or two exceptions..."
            scene classroom005
            with dissolve
            fprof "Any questions?"
            fprof "Let's continue"
            scene classroom006
            with dissolve
            fprof "A little lower we have Tanzani"
            fprof "The natives of Tanzani are usually dark skinned"
            fprof "They are a peaceful people that have a lot of knowledge in alchemy and plants"
            fprof "The one represented in green is Highgard, the land of the Nords"

            fprof "They are a tall and strong people, with a light complexion "
            scene classroom005
            with dissolve
            fprof "Is everyone following?"
            mida "I have a question!"
            scene classroom004
            with dissolve
            mida "What is that Uky island?"
            mida "I've never heard of it"
            scene classroom010
            with dissolve
            fprof "Well, let's just say you should never try to go there"
            fprof "Nobody knows what's in there"
            fprof "All those who have tried to go to Uky have never returned"
            fprof "So people mostly just don't talk about it"
            "It seems that's a dangerous place"

            "But it only made everyone in the room curious about what's there"
            fprof "Well, Then you have Orciash and Okchorg"
            fprof "These are orc lands"
            fprof "Over here we have Irokumata and Nagatashi"
            fprof "Normally these people are a bit smaller"
            fprof "And their skins are a bit yellow toned"
            fprof "They are also the oldest known civilizations"
            fprof "And probably the most advanced ones in terms of technology"
            fprof "On the top of the map"
            fprof "We see what was once is Arfam"
            fprof "That land no longer exists..."
            fprof "The Slayers conquered them recently"
            "For some reason that sent a chill up your spine"
            scene classroom007
            with dissolve
            fprof "Speaking of which"
            fprof "The Slayers"
            "And more chills"
            fprof "They are the most aggressive civilization"
            fprof "They are very strong in the art of war"
            fprof "And they hate all the other races"
            fprof "Nord, black, yellow, orc, cat, elf..."
            fprof "You name it..."
            scene classroom009
            with dissolve

            fprof "They are at war with Elvaria and Darkaria"
            fprof "The kingdoms of the elves and the dark elves"
            fprof "Here we have Mythrial"
            fprof "This island is home to many kinds of creatures"
            fprof "You can find centaurs, minotaurs and other creatures"
            mida "Really?"
            scene classroom004
            with dissolve
            mida "That's so cool"
            mida "Can we visit it some time?"
            scene classroom009
            with dissolve
            fprof "Maybe you can all visit it on your last year of College"
            fprof "Ahaha"
            scene classroom008
            with dissolve
            MC "Wow look at those boobs..."
            fprof "To finish up"
            scene classroom008
            with dissolve
            fprof "We have Jithak, land of the cat people"
            fprof "And since I'm late"
            fprof "Let's jump to into a little magic"
            "You look at everyone getting excited"
            jump magiclesson001

label magiclesson001:
    scene classroom011
    with dissolve
    fprof "I'm not only the History and Geography professor"
    fprof "I'm also a master at healing magic"
    fprof "So... let me choose one of you..."
    fprof "How... about... you [MC]?"
    MC "Me?"
    fprof "Yes, come here"
    scene classroom012
    with dissolve
    fprof "I promise it won't hurt"
    MC "Very well"
    "You rise from your chair and face the professor"
    scene classroom016
    with dissolve
    fprof "Try to do this"
    play sound "sounds/spell01.mp3"
    show heal001
    with dissolve
    MC "Uhmm... Ok"
    hide heal001
    with dissolve
    MC "Let me try then"
    show handsheal01
    with dissolve
    fprof "Do your best"
    if Healpoints == 1:
        MC "I can feel something"
        MC "I...."
        play sound "sounds/spell01.mp3"
        show handsheal02
        with dissolve
        scene classroom013
        with dissolve
        show handsheal02
        "With a shocked look, the professor says"
        fprof "How did you do that?"
        fprof "Have you had lessons before?"
        "You feel very tired"
        hide handsheal02
        with dissolve
        "And your magic fades away"
        MC "I... pfew... this is hard..."
        MC "No... I never had any lessons.."
        MC "Not that I know of..."
        scene classroom014
        with dissolve
        fprof "Well, you have a gift then..."
        $ Healpoints +=1
        "You gained 1 point in healing"
        jump endlesson001
    else:
        MC "I...."
        MC "Can't... "
        scene classroom014
        with dissolve
        fprof "That's normal, you've never had lessons before"
        fprof "But it was a nice try, keep practicing and you will get it someday."
        "You gained 1 point in healing"
        $ Healpoints +=1
        jump endlesson001


label endlesson001:
    scene classroom012
    with dissolve
    fprof "Today's lesson is over"
    fprof "From tomorrow on"
    fprof "You will all dress in your school robes"
    fprof "You will find them already placed in your bedrooms"
    n "You leave the classroom"
    n "And return to your room"
    nvl clear
    scene mckidroom
    with dissolve
    MC "So... She said I should look for a school robe or something"
    MC "Maybe in that chest?"
    $ Robeschest = False
    jump robesintheroom

label robesintheroom:

    call screen mcroomrobe

label Books01:
    if booksschool == True:
        MC "I believe these are the same books that I read yesterday"
        MC "Theres nothing else to learn.."
        jump robesintheroom
    else:
        MC "What is this?"
        MC "Some kind of spell?"
        MC "Invisibility?"
        "You spend some time reading the book"
        "You have gained 1 point in Illusion school"
        $ Iluspoints += 1
        $ booksschool = True
        jump robesintheroom

label Chest01:

    if Robeschest == False:
        scene mckidroom
        with dissolve
        MC "Let's check the chest"
        scene classroom015
        with dissolve
        MC "This is what they want us to wear?"
        "You got the school robes"
        $ Robeschest = True
        jump robesintheroom
    else:
        scene mckidroom
        with dissolve
        MC "There is nothing else in here..."
        jump robesintheroom



label sleeping01:
    if Robeschest == False:
        scene mckidroom
        with dissolve
        MC "I should search for the robes first"
        MC "Maybe in that chest?"
        jump robesintheroom
    else:
        scene mckidroom
        with dissolve
        stop music fadeout 5.0
        MC "I guess I should get some sleep"
        MC "I'm pretty tired"
        "You fall asleep"
        jump schoolday03

label schoolday03:
    play music "<loop 0.0>dark.mp3" fadein 6.0
    scene meanwhile
    with dissolve
    scene bredita001
    with dissolve
    Nonen "And that's it Mistress Bredita"
    Bredita "You're saying that he can become very powerful?"
    Nonen "Yes... Even the Archmage believes that he has the potential"
    Nonen "To become one of the most powerful mages ever seen"
    Bredita "Humm... That's good news"
    Bredita "I could use some more power... Maybe he will join me some day"

    Bredita "If he doesn't.... well... we'll see..."
    Nonen "Should we do something different this time?"
    scene bredita002
    with dissolve
    Bredita "I remember last time... How long has it been? 60 years?"

    Nonen "Yes Mistress"
    Nonen "They were lucky..."
    Bredita "No... I didn't want to kill Katriona"
    Bredita "Or any of them...."
    Bredita "You know that some day I will need them all alive"
    scene bredita001
    with dissolve
    Bredita "But if that boy has even half the power you all believe"
    Bredita "Some of those things may change"
    Bredita "Ahahah"
    Nonen "What should I do Mistress?"
    Bredita "For now.... Just keep a close eye on them"

    Bredita "Tell me everything that happens"
    Bredita "Oh... and keep bringing me playthings like you always do"
    Bredita "You're dismissed"
    Nonen "Very well Mistress"
    scene bredita003
    with dissolve
    Bredita "Well well well..."
    Bredita "I believe that things are about to change soon"
    Bredita "Now... Time to play with my new toy"
    scene bredita004
    with dissolve
label galleryScene1:
    Bredita "Hello puppet"
    profmys "Argh..."
    profmys "Where?... am... I?"
    Bredita "That doesn't really matter now"
    scene bredita005
    with dissolve
    profmys "You... Who?.."
    profmys "I sense... are you a necromancer?!"
    scene bredita006
    with dissolve
    Bredita "Bravo... And you are a Mysticism professor"
    Bredita "At Allesterra College, Professor Hishigo..."
    profmys "You... I shall defeat you"
    scene bredita007
    with dissolve
    "Professor Hishigo used his power to attack the Dark Mistress"
    profmys "I shall stop your evil here and now..."
    Bredita "Ahahahah"
    Bredita "With that measley power??!!"
    Bredita "Ahahahaha"
    Bredita "Let me show you true power"
    "Bredita used only one finger and with no effort at all"
    "Dominated Hishigo's will...."
    scene bredita008
    with dissolve
    scene bredita009
    with dissolve
    scene bredita010
    with dissolve
    scene bredita011
    with dissolve
    scene bredita012
    with dissolve
    Bredita "You were saying??"
    profmys "Uhmmm"
    Bredita "Really? Aahahah"
    Bredita "Come on, let's play a bit"
    scene bredita013
    with dissolve
    profmys "Uhmmmm"
    Bredita "When I'm done with you, you'll know what real power is"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene meanwhile
    with dissolve
    play music "<loop 0.0>ingame.mp3"
    scene meet002
    with dissolve
    katarro "And that's it"
    katarro "Another disappearance..."
    ayna "Can't you sense him anywhere?"
    katarro "No... I don't have a clue where Hishigo is..."
    scene meet001
    with dissolve
    suntako "Aren't you Mysticism Masters all connected?"
    suntako "You're supposed to know where he is!"
    scene meet003
    with dissolve
    silvana "Hey... We're all on the same side"
    silvana "It's not like he's the first one"
    Qa "Or the second...."
    scene meet001
    with dissolve
    ayna "I know... This is happening more and more"
    ayna "We need to do something to prevent this"
    suntako "No shit!"
    suntako "I believe we all need to rethink if you're still the best choice to lead us"

    scene meet002
    with dissolve
    ayna "Well, that's your opinion"
    ayna "If it matters that much to you maybe we could vote... Again..."

    katriona "Again?? Last time you had the majority of the votes"
    katarro "Exactly... I don't see the point in voting again"
    stop music fadeout 2.0

    scene meanwhile
    with dissolve
    play music "<loop 0.0>dark.mp3" fadein 4.0
    scene bredita014
    with dissolve
    Bredita "Yes... lick your Mistress"
    profmys "Uhmmm"
    scene bredita015
    with dissolve
    scene bredita016
    with dissolve
    Bredita "Yes..."
    Bredita "Use your tongue"
    Bredita "Like a good slave"
    Bredita "Uhmmm that's it"
    Bredita "You are another nice specimen for my collection"
    Bredita "Time to show me what you've got"
    scene bredita017
    with dissolve
    Bredita "That's it?"
    Bredita "Ahahahaha"
    Bredita "I hope you have stamina at least"
    Bredita "Now, lick my shoe, Professor Small Dick"
    scene bredita018
    with dissolve
    profmys "Uhmmmm"
    Bredita "Time to show me if you have stamina"
    scene bredita019
    with dissolve
    Bredita "That's it"
    Bredita "Put it in"
    Bredita "Is it even in yet?"
    Bredita "Ahahaha"
    scene bredita020
    with dissolve
    Bredita "What are you..."
    scene bredita021
    with dissolve
    Bredita "Really?!"
    Bredita "You're finished?"
    Bredita "Bah... Disappointing... I hoped you'd be worthwhile..."
    stop music fadeout 2.0
    scene black
    with dissolve
    play music "<loop 0.0>ingame.mp3"
    scene mages002
    with dissolve
    ayna "That Suntako gets on my nerves.."
    ayna "Why is he always like this?"
    katarro "Don't mind him..."
    katarro "It's because he doesn't like that he's no longer Archmage"
    scene mages003
    with dissolve
    ayna "I know, but the Elite voted for me over him"
    katarro "And a lot of things improved after"
    ayna "I don't know... Bad things happened as well"
    ayna "Bredita happened..."
    scene mages002
    with dissolve
    katarro "But many good things happened"
    katarro "I've been wondering... if Suntako..."
    katarro "Nah.. nevermind."
    ayna "What? tell me!"
    katarro "I've... been wondering if Suntako is somehow responsible"
    katarro "For the bad things that are happening..."
    ayna "I.... I don't believe that..."
    ayna "He's a pain in the ass"
    scene mages003
    with dissolve
    ayna "But he wouldn't do that..."
    ayna "Would he?"
    katarro "I don't know... But I think we should keep an eye on him"
    ayna "I don't believe we're doing this..."
    scene mages002
    with dissolve
    ayna "But if he is responsible for this I'm gonna !!!"
    show rageayna001
    with dissolve
    katarro "Calm down please..."
    hide rageayna001
    with dissolve
    ayna "You're right..."
    ayna "Thank you for being at my side"
    katarro "I believe in you"
    scene black
    with dissolve
    scene bredita022
    with dissolve
    Bredita "Now you look a lot better"
    Bredita "I removed that pathetic power you had"
    Bredita "And gave you real power"
    Bredita "Show it to me"
    profmys "Yes... Mistress"
    show bredita023
    with dissolve
    show bredita024
    with dissolve
    show bredita025
    with dissolve
    show bredita026
    with dissolve
    Bredita "Yes...That's a good boy..."




    scene black
    with dissolve
    if metdark == True:
        "You start to feel strange things in your dream"
        "You can't see anything..."
        "But you start to hear voices"
        mom "Why?"
        mom "What are you becoming?"
        mom "Please stop this..."
        MC "I... who are you?"
        sis "You monster!"
        MC "..."
        ayna "You are not what I expected..."
        katriona "Please don't do this..."
        katarro "No! he's unstoppable"
        fvoice "I failed...."
        nar "Ahahaha good!!!"
        nar "Now we shall rule them all!!!"
        scene mckidroom
        with dissolve
        MC "Damn...."
        MC "What just happened?"
    else:
        "You feel good and warm"
        "You can't see a thing, but start to hear voices"
        mom "That's my son!"
        mom "The greatest champion this land has ever seen"
        sis "I can't believe you are so powerful little brother"
        MC "I...are you my family?"
        ayna "I knew it, you are now one of us"
        katriona "So we have a new member, I'm no longer the newbie"
        fvoice "That's it! You are bound for success"
        katarro "Hello Master [MC]"
        scene mckidroom
        with dissolve
        MC "Wow..."
        MC "That was quite a dream"
        MC "Is it morning already?"
        MC "I should go to classes then"

label kidscorridor00:

    call screen kidscorridor


label Badguys:
    scene rivals001
    with dissolve
    MC "Hello"
    hatoshi "What are you looking at?!"
    fannay "Hey, he looks like a lost puppy"
    fannay "Ahahah"
    hatoshi "Get lost.... puppy"
    MC "What the hell..."
    jump kidscorridor00



label Goodguys:
    scene friends001
    with dissolve
    MC "Hi..."
    mida "Hello again"
    koneko "Hi..."
    kitargo "You is Nord? Right?"
    MC "I think so, yes"
    kitargo "Yes.. You Nord"
    kitargo "Kitargo Jithak"
    kitargo "Magic good!!"
    mida "He just arrived from Jithak"
    mida "He is still adapting to our language"
    kitargo "Me speaks good"
    kitargo "He understand me right??"
    menu:
        "Yes sure, you're quite good actually":
            kitargo "Me knows heehee"
            mida "Now he is all pumped up"
            kitargo "Kitargo is good"
            mida "We should go to class now guys"
            jump summonclass
        "{color=#1BBB20}Nah... you suck, keep trying though":

            kitargo "You is mean person"
            mida "Aahhahaah"
            kitargo "Kitargo will be best mage"
            mida "Time to go to class guys"
            jump summonclass

label summonclass:
    scene summonclass001
    with dissolve
    prof "Welcome students"
    prof "I'm Professor Rerlvam"
    prof "Today you will learn a bit of the History of Magic"
    prof "And after that we will practice a bit of Summoning Magic"
    menu:
        "Skip the history part":
            "You decided to skip the history part"
            "Some of the game plot may be harder to understand"
            jump class2summon
        "{color=#1BBB20}Listen to the whole lesson":
            prof "So, do any of you have a clue where Magic came from?"
            scene summonclass002
            with dissolve
            prof "Yes, you there.. What's your name?"
            scene summonclass003
            with dissolve
            kitargo "Me, Kitargo"
            scene summonclass002
            with dissolve
            prof "So can you tell me what you know?"
            scene summonclass003
            with dissolve
            kitargo "My father tell me magic from Gods"
            kitargo "Gods gave magic to us"
            scene summonclass002
            with dissolve
            prof "That's one of the theories, yes"
            prof "But unfortunately we don't have theology classes"
            scene summonclass004
            with dissolve
            hatoshi "Ahahaha"
            hatoshi "It appears that language is not his only problem"
            fannay "Ahahah"
            klathu "Ahahah"
            scene summonclass002
            with dissolve
            prof "Well Hatoshi, perhaps you can enligten us"
            prof "On the origin of Magic?"
            prof "And can you please explain it in Kitargo's language? Jithak..."
            "Everyone stopped laughing"
            scene summonclass005
            with dissolve
            prof "I'm waiting..."
            scene summonclass004
            with dissolve
            hatoshi "....."
            scene summonclass002
            with dissolve
            prof "That's what I thought…."
            scene summonclass006
            with dissolve
            mida "Ahahah... take that"
            scene summonclass007
            with dissolve
            kitargo "Kitargo is smart"
            kitargo "hehehe"
            scene summonclass005
            with dissolve
            prof "Can we proceed with the class?"
            prof "Here in the College we follow the scientific theory of Magic's origin"
            prof "It doesn't mean other theories are wrong"
            prof "But this is what we believe is more accurate"
            scene summonclass008
            with dissolve
            prof "In the beginning of time, Magic didn't exist"
            prof "Not on our world at least"
            prof "But about 50,000 years ago a meteor crashed into our planet"
            show summonclass009
            with dissolve
            hide summonclass009
            show summonclass010
            with dissolve
            hide summonclass010
            show summonclass011
            with dissolve
            hide summonclass011
            show summonclass012
            with dissolve
            scene summonclass013
            with dissolve
            prof "This meteor had a specific element called Allesterium"
            scene summonclass005
            with dissolve
            prof "And yes... Our College and Realm were named after it"
            prof "This element reacted with certain people"
            prof "Giving them abilities, or as it's better known: Magic"
            prof "Any questions so far?"
            prof "Yes?"
            scene summonclass006
            with dissolve
            mida "What kind of people are we talking about?"
            scene summonclass005
            with dissolve
            prof "That's an excellent question!"
            prof "But we honestly don't know... "
            prof "Some people seem to react to the element"
            prof "And others don't"
            prof "Our Archmage is believed to be the strongest mage alive"
            prof "But of course there could be other unknown mages around the world"
            prof "A little curiosity"
            prof "The next time you see the Archmage, look at her crown"
            prof "It's made of pure Allesterium"
            jump class2summon

label class2summon:
    scene summonclass001
    with dissolve
    prof "Now, it's time for some Summoning Magic instruction"
    prof "I imagine this is what you've all been waiting for"
    prof "To start with, you first need to envision what you want to summon"
    prof "Let me show you"
    scene summonclass014
    with dissolve
    play sound "sounds/spell01.mp3"
    show summonclass015
    with dissolve
    show summonclass016
    with dissolve

    scene summonclass017
    show summonclass018
    "Everyone in the room looked in awe of the creature!"
    hide summonclass018
    prof "This is a Summon"
    show summonclass007
    with dissolve
    kitargo "Oh!!"
    kitargo "Is that.. Dragon?"
    scene summonclass017
    with dissolve
    prof "Ahahah"
    prof "No... I don't have that kind of power"
    prof "But there is one person in the College capable of Summoning a Dragon"
    "Everyone stared at the Professor with curiosity"
    scene summonclass005
    with dissolve
    prof "Only Master Suntako can summon a Dragon"
    prof "As he is the highest ranked Summoner of Allesterra"
    scene summonclass006
    with dissolve
    mida "What about the Archmage?"
    mida "Can't she Summon one too?"
    scene summonclass005
    with dissolve
    prof "Honestly, I don't know"
    prof "I've never seen her do it"
    prof "But Master Suntako was my Master for years"
    prof "And when we battled Bredita he summoned a Dragon"
    prof "And that was a turning point in the battle"
    prof "We lost many people, but we won that day"
    menu:
        "{color=#1BBB20}Ask who Bredita is":
            scene summonclass005
            with dissolve
            show hand002
            with dissolve
            MC "Professor, who is Bredita"
            hide hand002
            with dissolve
            "Professor Rerlvam's face suddenly turned serious"
            prof "That's something you will learn in your History classes"
            prof "But only in your later years here"
            jump praticesummon001
        "Say nothing":

            scene summonclass006
            with dissolve
            mida "Who is Bredita Professor?"
            scene summonclass005
            with dissolve
            "Professor Rerlvam's face suddenly turned serious"
            prof "That's something you will learn in your History classes"
            prof "But only in your later years here"
            jump praticesummon001

label praticesummon001:
    scene summonclass005
    with dissolve
    prof "Now, let's see what you're all capable of Summoning"
    prof "Kitargo, do you want to start?"
    scene summonclass003
    with dissolve
    kitargo "Kitargo is good"
    kitargo "Will show great summon of Dragon!!!"
    kitargo "Watch Kitargo!!"
    scene summonclass019
    with dissolve
    kitargo "Ahmmm"
    play sound "sounds/spell01.mp3"
    show summonclass020
    with dissolve
    hide summonclass020
    show summonclass021
    with dissolve
    kitargo "That's....not..."
    scene summonclass004
    with dissolve
    hatoshi "Ahahah a Dragon...fly..."
    scene summonclass006
    with dissolve
    mida "Do you think you can do better?"
    "Mida then started her attempt"
    scene summonclass024
    with dissolve
    play sound "sounds/spell01.mp3"
    scene summonclass022
    with dissolve
    mida "This is difficult to hold...."
    scene summonclass023
    with dissolve
    mida "Phew.."
    scene summonclass002
    with dissolve
    prof "Wow that's really good Mida"
    hatoshi "Meh..."
    scene summonclass025
    with dissolve
    hatoshi "Let me show you how it's done!!"
    play sound "sounds/spell02.mp3"
    show summonclass026
    with dissolve
    hide summonclass026
    show summonclass027
    with dissolve
    hide summonclass027
    show summonclass028
    with dissolve
    "You feel an amazing amount of power coming from Hatoshi"
    hatoshi "And..."
    scene summonclass029
    with dissolve
    hatoshi "You see? This is how it's done!"
    hatoshi "Hehehe"
    scene summonclass002
    with dissolve
    prof "Amazing..."
    "While everyone was distracted by Hatoshi's bragging"
    scene summonclass030
    with dissolve
    "You notice that Hatoshi's wolf is staring at Mida's cat"
    "It looks like it's going to attack"
    MC "Oh shit!!"
    MC "Should I do something?"

    "You feel as though someone is giving you power"
    scene summonclass031
    with dissolve
    "A great amount of power"
    play sound "sounds/spell02.mp3"
    show summonclass032
    with dissolve
    show summonclass033
    with dissolve
    show summonclass034
    with dissolve
    scene summonclass035
    with dissolve
    "You Summon a Panther next to the Wolf"
    $ Summpoints +=1
    "You gained 1 point in summoning"
    "A fight between the animals was about to begin when.."
    play sound "sounds/spell02.mp3"
    scene summonclass014
    with dissolve
    show summonclass015
    with dissolve
    show summonclass016
    with dissolve
    "Professor Revlan cast some spell that made all the Summons vanish"
    scene summonclass005
    with dissolve
    prof "And this is why we should all be very careful with Magic"
    prof "Anyway you are an impressive group, I must say"
    scene summonclass036
    with dissolve
    hatoshi "Were you trying to attack my wolf?"
    MC "Your wolf was going to attack Mida's cat"
    hatoshi "I will teach you a lesson, you asshole!"
    MC "Oh Yeah?!"
    scene summonclass037
    with dissolve
    MC "Bring it!!"
    prof "Stop this right now!!"
    scene summonclass005
    with dissolve
    prof "The two of you will be having a long conversation with the Archmage"
    MC "But.."
    prof "Class dismissed"
    prof "You two follow me"
    scene summonclass038
    with dissolve
    "You and Hatoshi follow Professor Rerlvam"
    "And arrive at some kind of waiting room"
    scene summonclass039
    with dissolve
    prof "[MC] you wait here"
    scene summonclass040
    with dissolve
    prof "Hatoshi, you go right in"
    prof "She's waiting..."
    play sound "sounds/door.mp3"
    scene summonclass041
    with dissolve
    "The next moment you are alone"
    "Waiting for your turn to go inside"
    "..."
    "After a while you see the door moving"
    "And Hatoshi coming out"
    play sound "sounds/door.mp3"
    show summonclass042
    with dissolve
    hide summonclass042
    show summonclass043
    with dissolve
    hatoshi "Good luck with the sermon...."
    hatoshi "Asshole...."
    scene summonclass041
    with dissolve
    MC "Well, I guess I should go in..."
    scene summonclass044
    with dissolve
    play sound "sounds/door.mp3"
    "You enter the room and see the Archmage"
    "She's sitting on an armchair surrounded by books"
    ayna "So.... [MC]..."
    ayna "Already causing trouble?"
    menu:
        "It's not my fault! Hatoshi started it":
            ayna "You know it's not nice to tell on other students"
            jump Archsermon
        "{color=#1BBB20}I'm very sorry Archmage...":
            ayna "No harm done..."
            jump Archsermon


label Archsermon:
    scene summonclass044
    with dissolve
    ayna "So... do you want to tell me what happened?"
    "You explain what happened in class"
    ayna "So, you're saying you're innocent...?"
    MC "Yes..."
    ayna "And why should I believe you?"
    MC "Because I'm telling the truth"
    scene summonclass045
    with dissolve
    ayna "So you're saying you haven't done anything wrong?"
    MC "Exactly!"
    ayna "Tell me something then..."
    scene summonclass046
    with dissolve
    ayna "Isn't it wrong to spy on other people while they are bathing?"
    scene summonclass046
    with hpunch
    MC "Um...."
    MC "I..."
    ayna "You are dismissed"
    ayna "And try to stay out of trouble, ok?"
    "You leave the room"
    scene hall
    with dissolve
    MC "Does that mean she knows?"
    MC "But if she knows, why didn't she punish me?"
    MC "I should probably go to my room"
    MC "I've had enough problems for today..."
    "You hear a female voice in a distance"
    lili "Hey, you know what I want?"
    suntako "Be quiet... What if someone hears us?"
    "You discretely try to find out who is talking"
    scene sunlili001
    with dissolve
    "You see a pretty girl and some old bald guy"
    scene sunlili002
    with dissolve
    lili "You are one of the Elite, honey"
    lili "And probably the most powerful"
    lili "Do you think anyone will want to mess with you?"
    scene sunlili003
    with dissolve
    suntako "You are right my pretty flower, I'm Master Suntako"
    suntako "But that's not the point"
    suntako "That slut that calls herself Archmage is always on my back"
    suntako "I should be the Archmage, like I was before"
    scene sunlili002
    with dissolve
    lili "Don't worry about it my dear"
    lili "I bet that someday you will be the Archmage again"
    lili "Like you deserve"
    MC "Are they conspiring something?"
    MC "What's going on here?"
    scene sunlili003
    with dissolve
    suntako "Yeah... It doesn't matter right now"
    suntako "What matters now is what I want to do to you"
    scene sunlili002
    with dissolve
    lili "Hmmm... I like the sound of that"
    lili "Shall we go to your room?"
    scene sunlili003
    with dissolve
    suntako "Yes..."
    scene sunlili004
    with dissolve
    "You see them leaving"
    MC "Should I follow them?"
    menu:
        "Follow them{color=#1BBB20} (Some scenes)":
            MC "I'll see what they're up to"
            jump sunbanglili001
        "Go to your room":
            MC "I should go to my room"
            MC "I don't want to be part of this"
            jump roomdps

label sunbanglili001:
    scene sunlili004
    with dissolve
    MC "They've entered some room"
    "Luckily they left the door unlocked"
    "And you are able to silently open it a take a peek"
    "They are so into each other that they don't even notice you"
    scene sunlili005
    with dissolve
    suntako "This ass of yours.. Hmm"
    scene sunlili006
    with dissolve
    lili "Is it only my ass you like?"
    suntako "It's everything..."
    suntako "Kiss me!!"
    scene sunlili007
    with dissolve
    lili "Hmmm"
    scene sunlili008
    with dissolve
    lili "Is it just a kiss that you want?"
    lili "Or should I take off this coat of yours?"
    suntako "Don't let me stop you!"
    scene sunlili009
    with dissolve
    lili "Ahaha"
    suntako "It's a bit unfair that I'm the only one half naked here, don't you think?"
    "In a blink of an eye Liliana removes her top"
    "And Suntako doesn't hesitate a second"
    scene sunlili010
    with dissolve
    lili "Hmmm baby.. that's it..."
    suntako "You like this?"
    scene sunlili011
    with dissolve
    lili "Come with me over there"
    lili "I want to show you something"
    suntako "Oh I will"
    "You see the old guy take off his pants and sit on the bench"
    scene sunlili012
    with dissolve
    lili "Are you ready for what comes next?"
    "Suntako nods in approval"
    "And Liliana get fully naked"
    "And starts dancing"
    scene sunlili013
    with dissolve
    lili "So do you like what you see?"
    suntako "No... I love it"
    lili "That's a good answer"
    scene sunlili014
    with dissolve
    lili "Let me show you something"
    MC "Shit... Is she going to suck him?"
    scene sunlili015
    with dissolve
    suntako "Oh yes my dear..."
    scene sunlili016
    with dissolve
    MC "How can such a pretty girl suck an old guy like that?"
    lili "Do you like it?"
    scene sunlili017
    with dissolve
    scene sunlili018
    with dissolve
    scene sunlili017
    with dissolve
    scene sunlili018
    with dissolve
    scene sunlili017
    with dissolve
    scene sunlili018
    with dissolve
    suntako "Oh yes baby that feels amazing!!"
    suntako "But let's try something else!"

    scene sunlili019
    with dissolve
    suntako "I want you to ride me!"
    lili "Hmm... It's going in..."
    scene sunlili020
    with dissolve
    scene sunlili021
    with dissolve
    scene sunlili020
    with dissolve
    scene sunlili021
    with dissolve
    scene sunlili020
    with dissolve
    scene sunlili021
    with dissolve
    lili "Oh yes... keep going!"
    suntako "I want to fuck you from behind now!"
    lili "Yes... fuck me like a bitch"
    scene sunlili022
    with dissolve
    suntako "Turn around you little slut"
    lili "Yes Master"
    scene sunlili023
    with dissolve
    scene sunlili024
    with dissolve
    scene sunlili023
    with dissolve
    scene sunlili024
    with dissolve
    scene sunlili023
    with dissolve
    scene sunlili024
    with dissolve
    lili "Don't stop!"
    scene sunlili023
    with dissolve
    suntako "I won't!!"
    "You hear a strange noise behind you"
    MC "Shit... what was that?"
    MC "I should get the fuck out of here"
    "You leave and go to your room"
    $ renpy.end_replay()
label roomdps:
    scene mckidroom
    with dissolve
    MC "That was strange to say the least"
    scene xibokatarro001
    with dissolve
    katriona "So... Master Katarro..."
    katriona "Why did you call us all here?"
    silvana "Yeah... I was busy..."
    ayna "I'm sure there is a good reason"
    katarro "Yes there is..."
    katarro "Look at my mirror please"
    scene xibokatarro002
    with dissolve
    katriona "What the ...?"
    silvana "Is that Master Suntako??"
    ayna "It....Is..."
    ayna "But why are you showing this to us?"
    katarro "Look closer please"
    scene xibokatarro003
    with dissolve
    ayna "Is that?"
    katriona "That girl Liliana"
    scene xibokatarro004
    with dissolve
    katarro "Yes..."
    silvana "But it's forbidden to have sex with students"
    scene xibokatarro005
    with dissolve
    katarro "Now you understand why I'm showing you this"
    katarro "So that all of you can see his actions"
    scene xibokatarro006
    with dissolve
    ayna "That.... Bastard..."
    ayna "Did he enchant her? Is she doing this of her own will?"
    scene xibokatarro007
    with dissolve
    katarro "Does that matter Archmage?"
    scene xibokatarro008
    with dissolve
    ayna "I guess not..."
    ayna "He knows it's not allowed..."
    ayna "He will pay for this..."
    scene xibokatarro007
    with dissolve
    ayna "Please Master Katarro"
    ayna "Organize a meeting with all the Elite"
    ayna "With Master Suntako included!"
    katarro "Yes Archmage, It shall be done"
    scene mckidroom
    with dissolve
    stop music fadeout 4.0
    MC "I should get some sleep, I’m really tired"
    "You fall asleep"
    scene black
    with dissolve
    play sound "sounds/burning.mp3"
    "In your sleep, you start to feel something"
    "And you start hearing voices"
    dad "Look at this Sven"
    scene fatherquest001
    with dissolve
    sven "What the hell happened here?"
    dad "Such destruction..."
    dad "And where is everybody?"
    sven "Who dares to attack our land like this?"
    scene fatherquest002
    with dissolve
    sven "Hey... look..."
    sven "What is that?"
    dad "Is that a....?"
    scene fatherquest003
    with dissolve
    dad "Demon??!!"
    scene fatherquest004
    with dissolve
    scene fatherquest005
    with dissolve
    scene fatherquest006
    with dissolve
    play sound "sounds/demonooh.wav"
    demon "Ooh.... fear..."
    scene fatherquest007
    with dissolve
    demon "I smell fear..."
    play sound "sounds/burning.mp3"
    demon "Two puny humans..."
    demon "I guess you are the last..."
    scene fatherquest001
    with dissolve
    dad "What have you done evil creature?"
    dad "Why did you come here?"
    dad "Why did you kill everyone?"
    scene fatherquest007
    with dissolve
    demon "So many questions..."
    demon "But since you are about to die..."
    demon "Let me tell you..."
    demon "I'm looking for something..."
    demon "Something very powerful..."
    demon "Something so powerful that I was drawn here to this place"
    demon "Are you hiding it?"
    scene fatherquest001
    with dissolve
    sven "Nonsense..."
    sven "There isn't such an artifact here"
    scene fatherquest007
    with dissolve
    demon "Ahahah I never said it was an artifact"
    demon "But... That means that you know nothing"
    demon "Or you are very stupid..."
    demon "Either way, I will kill you both!!"
    demon "Ahahaha"
    scene fatherquest001
    with dissolve
    dad "How dare you?!"
    sven "You are the one who's going to die"
    scene fatherquest008
    with dissolve
    dad "Ahhhhhhh"
    sven "Ahhhhh"
    scene fatherquest009
    with dissolve
    demon "Is that supposed to scare me?"
    demon "Ahahahaha"
    demon "Come on!!"
    scene fatherquest010
    with dissolve
    demon "You will go down first"
    play sound "sounds/hit.mp3"
    scene fatherquest011
    with dissolve

    sven "Arghhh"
    play sound "sounds/beat.mp3"
    dad "Sven!!"
    demon "And you are the next!"
    scene mckidroom
    with dissolve
    MC "Noooo!"

    MC "Another nightmare..."
    MC "When are these going to end?"
    "You calm down a little..."
    stop sound
    MC "I should try to get some sleep"
    scene nextday
    with dissolve
    play music "<loop 0.0>ingame.mp3"
    scene mckidroom
    with dissolve
    MC "Yawn!!"
    MC "Time for class..."
    scene hall
    with dissolve

    scene friends001
    with dissolve
    mida "Hey look who's coming!"
    "Everyone stares at you"
    MC "Hi guys.."
    scene hall
    show mida001
    with dissolve
    mida "Hey, tell us what happened yesterday"
    mida "Did you really get to see the Archmage?!"
    MC "Yes.."
    mida "So you talked to her??"
    mida "You are so lucky!!!"
    mida "She must be amazing"
    scene friends001
    with dissolve
    kitargo "Kitargo wants speak to Archmage"
    kitargo "So Kitargo learns new spell"
    kitargo "You learn new spell?"
    kitargo "Archmage teach new spell?"
    MC "Nah... She just told me to keep out of trouble"
    scene hall
    show mida001
    with dissolve
    mida "And that's it?"
    mida "Didn't you ask her anything?"
    mida "Like how it feels to be the Archmage?"
    mida "How it feels to be the most powerful woman in the world?"
    mida "And probably the most powerful being?"
    MC "Uhmm ... No... "
    mida "You have the honor of seeing and talking to her"
    mida "And you didn't ask anything?"
    MC "That's... right..."
    mida "What a..."
    play sound "sounds/bell.mp3"
    "You hear bells tolling"
    MC "What's going on?"
    mida "Don't you know anything?"
    mida "It means that the Elite will be having a meeting today"
    mida "And shouldn't be bothered"
    mida "Well, time for class"
    MC "Right.. Let's go"
    stop sound fadeout 1.0
    scene alterclass001
    with dissolve
    profalter "Welcome students"
    profalter "I'm Professor Abaashi"
    profalter "I'm the professor of Alteration magic"
    scene alterclass002
    with dissolve
    profalter "I bet all of you have heard of Alteration"
    profalter "Like changing your skin to iron?"
    profalter "It's really nice, hehehe"
    profalter "But today I want you to meet someone"
    profalter "She is one of the top students of this last year"
    profalter "And was the best student at Summoning"
    profalter "Far better than me, heheh"
    profalter "This is Liliana"
    scene alterclass003
    with dissolve
    lili "Thank you Professor"
    lili "Hello everybody"
    "You look at the girl"
    MC "Is that the girl from yesterday?"
    MC "The one that was hanging with that old fart?"
    MC "It is her..."
    scene alterclass004
    with dissolve
    lili "I just want to say that"
    lili "Any of you can become a great Mage"
    scene classroom004
    with dissolve
    mida "Can you show us some spells??"
    mida "Please...."
    scene alterclass004
    with dissolve
    lili "Well..."
    lili "Ok, watch this"
    play sound "sounds/spell02.mp3"
    scene alterclass005
    with dissolve
    show alterclass005a
    with dissolve
    show alterclass005b
    with dissolve
    show alterclass005c
    with dissolve
    scene alterclass006
    show alterclass005c
    lili "Adornankh Mareum"
    scene alterclass007
    with dissolve
    "A horse just appeared"
    MC "Holy shit..."
    MC "She's good"
    scene classroom004
    with dissolve
    mida "Oh my God!!"
    mida "It's a horse"
    scene alterclass008
    with dissolve
    lili "So... Do you like it?"
    "All the students look in amazement"
    "Except for Hatoshi"
    "Who for some reason didn't come to the class"
    scene alterclass009
    with dissolve
    lili "Well that's all"
    lili "Remember, if you work hard"
    lili "You may even become better than me"

    scene alterclass010
    with dissolve
    profalter "Well that's a big task, heheh"
    profalter "but it's true"
    scene alterclass009
    with dissolve
    lili "Keep practicing kids"
    lili "Bye"
    "Everyone said goodbye"
    "And she left"
    scene alterclass002
    with dissolve
    profalter "Well"
    profalter "Who's ready for the second surprise?"
    profalter "We are going on a field trip"
    MC "Field trip?"
    profalter "Yes we are going to see the place"
    profalter "Where we believe magic started"
    scene meanwhile
    with dissolve
    scene meanwhile
    with dissolve
    scene alterclass013
    with dissolve
    ayna "And for that reason, you're out!!"
    suntako "What?? You dare do this to me?!"
    silvana "It's not just her"
    silvana "We've all voted on this"
    suntako "Where is Bojay?"
    Qa "He's on a quest"
    Qa "But it doesn't matter a bit"
    ayna "The rest of us voted you out"
    ayna "So it's 5 out of 7 against you"
    scene alterclass015
    with dissolve
    suntako "Where is the proof of what you are saying?"
    suntako "You say I'm involved with a student..."
    scene alterclass013
    with dissolve
    katarro "We all saw it..."
    katarro "You having sex with Liliana"
    katarro "One of the top students from the senior class"
    scene alterclass014
    with dissolve
    suntako "I... You don't understand"
    suntako "You can't do this..."
    scene alterclass016
    with dissolve
    ayna "It is done..."
    ayna "Leave... And you won't be humiliated publically"
    scene alterclass014
    with dissolve
    suntako "You will all regret this day..."
    scene alterclass012
    with dissolve
    profalter "And this is the crater left by the meteor"
    profalter "That brought Allesterium to our planet"
    "While the professor is explaining some stuff"
    "You start to feel weird"
    profalter "This place still has a lot of magic"
    profalter "There are some people that feel dizzy when near this place"
    profalter "And all Mages feel stronger"
    "It's like the professor is reading your feelings"
    "You feel dizzy and stronger at the same time"
    "But nobody else seems to have a problem"
    stop music fadeout 8.0
    "You start to lose your balance"
    MC "Wow... I...I'm..."
    scene alterclass011
    with dissolve
    profalter "Hey! are you ok??"
    show blink1
    with dissolve
    show blink2
    with dissolve
    show blink3
    with dissolve
    profalter "Grab him!!"
    profalter "Before he fain...blawadsf.."
    scene black
    with dissolve
    "You don't understand that last sentence"
    "But all of a sudden"
    scene alterclass017
    with dissolve
    MC "What the..."
    play sound "sounds/spell02.mp3"
    MC "Who are those guys??"
    play sound "sounds/explosionayna.wav"
    scene alterclass018
    with dissolve
    scene alterclass019
    with dissolve
    scene alterclass020
    with dissolve
    MC "Shit!!!"
    scene black
    with dissolve
    $ Destpoints += 1
    $ Iluspoints += 1
    $ Healpoints += 1
    $ Mystpoints += 1
    $ Summpoints += 1
    $ Altepoints += 1
    $ Necropoints += 1
    "All your powers improved"
    play music "<loop 0.0>ingame.mp3"
    katriona "Hey [MC]... wake up"
    scene wakealter001
    show blink3
    with dissolve
    hide blink3
    show blink2
    with dissolve
    hide blink2
    show blink1
    with dissolve
    hide blink1
    MC "Where?... What?.."
    scene wakealter002
    with dissolve
    katriona "Hey, it's all ok..."
    katriona "You're safe now"
    MC "I... Saw some incredibly powerful mages"
    katriona "I bet you did.. In your dreams... Ahahaha"
    MC "What happened?"
    katriona "Well... You fainted while you were on a field trip"
    katriona "Tomorrow your friends will probably tease you all day... Hehehe"
    katriona "And probably will call you a delicate flower... hehehe"
    katriona "But let me tell you a secret..."
    scene wakealter001
    with dissolve
    katriona "Fainting means that you have a lot of hidden potential"
    katriona "Those who possess great Magic are more affected by Allesterium"
    scene wakealter002
    with dissolve
    katriona "And since you fainted... You must have a lot of Magic"
    MC "Really?!"
    katriona "Or... you're a delicate little flower.. Hehehe"
    MC "Hey!!"
    katriona "Hehehe"
    scene wakealter003
    with dissolve
    katriona "Well, since you're ok"
    katriona "Time to move to your room"
    katriona "There are some important things happening"
    katriona "And I have to attend to them"
    katriona "So.... bye for now"
    MC "Thanks... I guess"
    "You leave her room"
    scene hall
    with dissolve
    "This place is getting weirder by the day"
    "But somehow I feel stronger everyday..."
    "I should go to my room..."
    scene meanwhile
    with dissolve
    scene meanwhile
    with dissolve
    scene suntakoout002
    with dissolve
    suntako "I'm glad you're here"
    suntako "I have something very important to tell you"
    scene suntakoout004
    with dissolve
    lili "Hehehe don't look like that"
    lili "It can't be that bad"
    scene suntakoout001
    with dissolve
    suntako "I wish it wasn't..."
    suntako "But it is..."
    suntako "I have been exiled by the Elite"
    scene suntakoout003
    with dissolve
    lili "Those bastards..."
    lili "Do they know your power?"
    lili "Who the hell do they think they are?!"
    lili "It's that bitch’s fault I'm sure"
    scene suntakoout004
    with dissolve
    lili "But tell me love"
    lili "Why did they exile you?"
    scene suntakoout005
    with dissolve
    suntako "Well....They..."
    suntako "They... Found out about us..."
    lili "What??!!"
    suntako "Yes... But don't worry.."
    suntako "I convinced them it was my fault"
    lili "But...."
    suntako "I told them I used my Magic to seduce you"
    suntako "So you are safe"
    lili "But everyone will know about it..."
    lili "I...."
    scene suntakoout006
    with dissolve
    lili "Oh my god... The shame..."
    lili "I need to go...."
    suntako "Wait!!"
    scene suntakoout007
    with dissolve
    suntako "They will pay for this!!"
    suntako "Someday they will need me..."
    suntako "Then they'll see..."
    suntako "But I must leave for now.."
    scene suntakoout008
    with dissolve
    suntako "Time to call Rarvayrrinth"
    suntako "Hytomihall!! Adhorxicus!! Rarvayrrinth!!"
    play sound "sounds/spell02.mp3"
    show suntakoout008a
    with dissolve
    hide suntakoout008a
    show suntakoout008b
    with dissolve
    hide suntakoout008b
    show suntakoout008c
    with dissolve
    scene suntakoout009
    with dissolve
    play sound "sounds/dragon.mp3"
    "A massive armored black dragon appeared"
    suntako "Welcome Rarvayrrinth"
    "In a repulsive voice the Dragon answered"
    rarva "You called me...Master.."
    suntako "Yes..."
    suntako "I need to leave this place..."
    suntako "Take me out of here"
    rarva "Hmph... Very well"
    scene suntakoout010
    with dissolve
    suntako "Those bastards..."
    scene suntakoout011
    with dissolve
    suntako "Let's go!!"
    rarva "Hmph..."
    "The Dragon reluctantly followed the order"
    scene suntakoout012
    with dissolve
    suntako "Take me to Mythrial"
    rarva "Hmph..."
    scene suntakoout013
    with dissolve
    lili "The plan worked perfectly!!"
    lili "Suntako is out"
    scene suntakoout014
    with dissolve
    lili "I understand why we should lay low now"
    lili "So that they don't find out"
    lili "I still can't believe it worked so well"
    lili "The Mistress will be pleased"
    scene mckidroom
    with dissolve
    MC "Yawn, I need to sleep"
    scene black
    with dissolve
    nvl clear
    n "10 years have passed"

    n "You are now a senior year student"

    nvl clear
    $ favmagic = "none"
    n "During your college years"
    n "You learn magic to:"
    nvl clear
    menu:
        "Be strong enough to help people{color=#1BBB20} (+1 Alignment)":
            "You are always ready to help others with your skills"
            "+1 alignment point"
            $ Points += 1
            jump question02
        "So that nobody can tell me what to do":
            "You follow your own path, you help and or kill who you want"
            "No alignment change"
            jump question02
        "So that nobody can stop me from ruling the world{color=#FF0000} (-1 Alignment)":
            "You have the ambition to rule over everyone, like you deserve"
            "-1 alignment point"
            $ Points -= 1
            jump question02

label question02:

    n "One of your colleagues was attacked"
    n "By a bear, so you.."
    nvl clear
    menu:
        "Used fear on the bear and healed my colleague{color=#1BBB20} (+1 Alignment/Heal/Iluspoints)":
            "You didn't want to kill the animal and saved your colleague"
            "+1 alignment point, +1 Healing point, +1 Ilusion point"
            $ Points += 1
            $ Iluspoints += 1
            $ Healpoints += 1
            jump question03
        "Used ironskin on myself and flames to scare the bear":
            "As long as you don't get hurt..."
            "Everybody should be able to defend themselves.."
            "+ 1 Battlemagic point, +1 Alteration point"
            $ Altepoints += 1
            $ Destpoints += 1
            jump question03
        "I summoned a creature to fight the bear and experimented on my dead colleague’s body{color=#FF0000} (-1 Alignment/+1 Necro/Summpoints)":
            "The bear is dead, no more problems from it"
            "And since there was a dead body... why not?"
            "-1 alignment point, +1 Summoning point, +1 Necromancy point"
            $ Points -= 1
            $ Summpoints += 1
            $ Necropoints += 1
            jump question03

label question03:
    "Your favorite school of magic in college is"
    menu:
        "Battlemagic{color=#1BBB20} (+3 Destpoints) {image=001battle}":

            "You love Battlemagic, and you practice it a lot"
            "+3 Battlemagic points"
            $ Destpoints += 3
            $ favmagic = "destruction"
            jump question04
        "Illusion{color=#1BBB20} (+3 Iluspoints) {image=001illusion}":
            "You love Illusion, and you practice it a lot"
            "+3 Illusion points"
            $ Iluspoints += 3
            $ favmagic = "illusion"
            jump question04
        "Healing{color=#1BBB20} (+3 Healpoints) {image=001heal}":

            "You love Healing, and you practice it a lot"
            "+3 Healing points"
            $ Healpoints += 3
            $ favmagic = "heal"
            jump question04
        "Mysticism{color=#1BBB20} (+3 Mystpoints) {image=001myst}":
            "You love Mysticism, and you practice it a lot"
            "+3 Mysticism points"
            $ Mystpoints += 3
            $ favmagic = "myst"
            jump question04
        "Summoning{color=#1BBB20} (+3 Summpoints) {image=001summon}":
            "You love Summoning, and you practice it a lot"
            "+3 Summoning points"
            $ Summpoints += 3
            $ favmagic = "summ"
            jump question04
        "Alteration{color=#1BBB20} (+3 Altepoints) {image=001alteration}":
            "You love Alteration, and you practice it a lot"
            "+3 Alteration points"
            $ Altepoints += 3
            $ favmagic = "alt"
            jump question04

label question04:
    "Your second favorite school of magic in college is"
    menu:

        "Battlemagic{color=#1BBB20} (+2 Destpoints) {image=001battle}" if favmagic != "destruction":
            "+2 Battlemagic points"
            $ Destpoints += 2
            jump question05
        "Illusion{color=#1BBB20} (+2 Iluspoints) {image=001illusion}" if favmagic != "illusion":
            "+2 Illusion points"
            $ Iluspoints += 2
            jump question05
        "Healing{color=#1BBB20} (+2 Healpoints) {image=001heal}" if favmagic != "heal":
            "+2 Healing points"
            $ Healpoints += 2
            jump question05
        "Mysticism{color=#1BBB20} (+2 Mystpoints) {image=001myst}" if favmagic != "myst":
            "+2 Mysticism points"
            $ Mystpoints += 2
            jump question05
        "Summoning{color=#1BBB20} (+2 Summpoints) {image=001summon}" if favmagic != "summ":
            "+2 Summoning points"
            $ Summpoints += 2
            jump question05
        "Alteration{color=#1BBB20} (+2 Altepoints) {image=001alteration}" if favmagic != "alt":
            "+2 Alteration points"
            $ Altepoints += 2
            jump question05

label question05:
    "You started dating Mida a couple months ago"
    $ midacorr = 0
    $ midalove = 0
    "Why?"
    menu:
        "Because I like her{color=#1BBB20} (+1 Alignment/Mida's Love)":
            "Mida's love increased"
            "+1 alignment point"
            $ Points +=1
            $ midalove +=1
            jump question06
        "Because I'm a guy and I like to bang girls":
            "Those who tell the truth..."
            jump question06
        "Because I can use her for my plans{color=#FF0000} (-1 Alignment/+1 Mida's Corruption)":
            "Mida's corruption increased"
            "-1 alignment point"
            $ Points -=1
            $ midacorr +=1
            jump question06

label question06:
    $ Racist = False
    "Last question I promise :P"
    "What do you think about the other races (Orcs, Elves, Jithaks etc..)?"
    menu:
        "All races deserve the same respect and I will defend it{color=#1BBB20} (+1 Alignment)":
            "+1 alignment point"
            "Some game choices may be different because of your racial preferences"
            $ Points +=1
            jump adulthood
        "I don't really care about that, I let them do what they want..":
            "As long as nobody bothers you, right?"
            jump adulthood
        "There is only one real race!! Orcs, Jithaks, Elves... They are all shit{color=#FF0000} (-1 Alignment/Racist= True)":
            "-1 alignment point"
            "Some game choices may be different because of your racial preferences"
            $ Points -=1
            $ Racist = True
            jump adulthood
