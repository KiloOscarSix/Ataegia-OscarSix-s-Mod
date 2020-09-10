
label v018:


    scene farmmission1
    with dissolve
    MC "I should return to the College and speak with the Archmage"
    oldman "Fuck you mage!!!"
    "You turn around to see the creature casting some spell"
    scene v18001
    with dissolve
    MC "Shit, I need to do something!"
    scene v18002
    with dissolve
    "What should you do?"
    menu:
        "Cast Fear{color=#1BBB20} (+1 Iluspoint) {image=001illusion}" if Iluspoints >= 4:
            "You decide to cast fear"
            play sound "sounds/fear.ogg"
            scene v18006ilu
            with dissolve
            $ Iluspoints += 1
            "Your Illusion increased"
            oldman "Ahhh!"

            jump impfight
        "Cast Flames{color=#1BBB20} (+1 Destpoint) {image=001battle}" if Destpoints >= 4:
            "You decide to cast Flames"
            play sound "sounds/flames.wav"
            scene v18006des
            with dissolve
            $ Destpoints += 1
            "Your Battlemagic increased"
            oldman "Ahhh!"

            jump impfight
        "Summon Something{color=#1BBB20} (+1 Summpoint) {image=001summon}" if Summpoints >= 4:
            "You decide to summon a Reptilian"
            play sound "sounds/summon.ogg"
            scene v18006sum
            with dissolve
            $ Summpoints += 1
            "Your Summoning increased"
            oldman "Ahhh!"

            jump impfight
        "Use Telekinesis{color=#1BBB20} (+1 Mystpoint) {image=001myst}" if Mystpoints >= 4:
            "You used telekinesis"
            play sound "sounds/force.ogg"
            scene v18006mys
            with dissolve
            $ Mystpoints += 1
            "Your Mysticism increased"
            oldman "Ahhh!"

            jump impfight
        "Use a ward{color=#1BBB20} (+1 Altepoint) {image=001alteration}" if Altepoints >= 4:
            "You decide to cast a ward"
            play sound "sounds/ward.ogg"
            scene v18006alt
            with dissolve
            $ Altepoints += 1
            "Your Alteration increased"
            oldman "Ahhh!"

            jump impfight

label impfight:
    scene v18007
    with dissolve
    oldman "Ok, ok stop!"
    oldman "Hold on!"
    "You realize that something weird is happening"
    scene v18008
    with dissolve
    "A winged creature exits the Old Man's body"
    MC "Who.. what are you?!"
    imp "You've never seen an Imp, Young Mage?"
    imp "Let's talk, shall we?"
    scene v18009
    with dissolve
    imp "As you can see I own this Old Man's body"
    imp "If you keep attacking me"
    scene v18010
    with dissolve
    imp "You will kill him"
    imp "Do you want that?"
    imp "You should let me go..."
    scene v18011
    with dissolve
    imp "I'll even make a deal with you"
    imp "You let me go, you can keep the old man"
    imp "And I'll even give a boost to one of your skills"
    scene v18010
    with dissolve
    imp "It's a good deal!"
    imp "Everybody wins"
    imp "What do you say?"
    $ dealimp = False
    menu:
        "Seems good to me{color=#1BBB20} (Deal= True)":
            scene v18011
            with dissolve
            imp "I knew you were a smart one"
            imp "A deal is a deal"
            imp "Here you go"
            scene v18012
            with dissolve
            "You see him doing some movements with his hands"
            imp "It's done, bye"
            scene v18015
            with dissolve
            "the imp flies away"
            scene v18016
            with dissolve
            oldman "What just happened?"
            oldman "My head is killing me"
            scene v18017
            with dissolve
            oldman "Who are you?"
            MC "Calm down, don't you remember anything?"
            scene v18018
            with dissolve
            oldman "I... yes..."
            oldman "I couldn't control my actions"
            oldman "My... daughter..."
            scene v18019
            with dissolve
            oldman "Where is she?"
            MC "She's fine, she's in the College"
            "You start to feel strange..."
            "Like if you are paralyzed"
            $ dealimp = True
            jump postimp
        "I don't think so":

            scene v18011
            with dissolve
            imp "I knew you were stupid"
            scene v18012
            with dissolve
            "You see him doing some movements with his hands"
            scene v18013
            with dissolve
            "The imp enters the old man's mouth"
            MC "That's disgusting..."
            scene v18014
            with dissolve
            oldman "Cough cough... ahww"
            scene v18018
            with dissolve
            MC "You shall..."
            oldman "Tell me something Young Mage..."
            MC "I... can't..."
            oldman "Can you move at all?"
            "You realize that you are paralyzed"
            jump postimp

label postimp:
    MC "I...."
    scene v18020
    with dissolve
    oldman "Ahahaha"
    oldman "Are you stupid?"
    oldman "How the fuck did you expect to beat an imp?"
    oldman "When you're so weak?"
    "You fall to the ground"
    scene v18021
    with dissolve
    oldman "You have a young body"
    oldman "And I feel a lot of magic potential in you"
    oldman "Maybe I should take your body instead"
    stman "Stop right there, devilish creature!"
    scene v18022
    with dissolve
    oldman "What?"
    oldman "Who the..??"
    scene v18023
    with dissolve
    oldman "Ahhhh"
    oldman "Stop this!!"
    scene v18024
    with dissolve
    imp "Who are you?!"
    "You turn you head to see..."
    scene v18025
    with dissolve
    "A hooded man in a robe"
    "He's using some kind of magic"
    scene v18026
    with dissolve
    "He pulls the Imp out of the Old Man, directly to his hand"
    imp "Who are you??"
    imp "Let me go!!"
    imp "Let's make a deal!"
    scene v18027
    with dissolve
    play sound "sounds/spell02.mp3"
    stman "Adornak Solium!"
    imp "What are you..."
    scene v18028
    with dissolve

    "You feel a lot of energy being transfered"
    "From the creature to this man"
    scene v18029
    with dissolve
    stman "Now it's your turn"
    MC "My turn? What do you mean?"
    scene v18030
    with dissolve
    stman "Soltaret encarium"
    scene v18031
    with dissolve
    stman "There... You're both free"
    MC "Thanks... but.."
    MC "Who are you?"
    scene v18032
    with dissolve
    stman "Who I am doesn't matter"
    scene v18031
    with dissolve
    stman "But you..."
    stman "I feel that..."
    stman "Humm"
    MC "What?"
    stman "Nevermind..."
    MC "What? You were going to say something about me..."
    scene v18033
    with dissolve
    stman "Yes I was..."
    stman "But I'll leave it for a later date..."
    MC "Where can I find you?"
    stman "When the time is right"
    stman "Look for me on Mount Frost"
    stman "Bye"

    oldman "We are free!"
    scene v18018
    with dissolve
    oldman "I could see and feel everything..."
    oldman "That damn creature..."
    oldman "It even made my daughter run away..."
    scene v18016
    with dissolve
    oldman "It made her think I'm a pervert..."
    oldman "He tried to rape my daughter... with my body.."
    scene v18019
    with dissolve
    oldman "You will tell her the truth right?"
    oldman "That it wasn't me..."
    MC "Sure, don't worry"
    MC "I need to return to the College now"
    stop music fadeout 2.0
    scene meanwhile
    play music "<loop 0.0>dark.mp3" fadein 2.0
    with dissolve
    label galleryScene8:
    scene v18034
    with dissolve
    Bredita "That's it! Keep going"
    lili "It's... Hard..."
    scene v18035
    with dissolve
    Bredita "You are good at Summoning"
    Bredita "This is almost the same thing"
    lili "I'm...doing...it.."
    scene v18036
    with dissolve
    Bredita "Great, There is you first real summon"
    lili "I...did it!"
    scene v18037
    with dissolve
    Bredita "Looks good"
    Bredita "You still have a lot to learn"
    Bredita "But it's a good try"
    scene v18038
    with dissolve
    Bredita "Now that got me excited"
    Bredita "Playing with life and death excites me"
    Bredita "You know what to do"
    scene v18039
    with dissolve
    lili "Yes Mistress"
    Bredita "That's it! Lick it"
    scene v18040
    with dissolve
    Bredita "Hmm..."
    lili "Slurp..."
    scene v18041
    with dissolve
    Bredita "Come on"
    Bredita "I need more that this now"
    lili "Hmm?"
    Bredita "And bring your skeleton"
    scene v18042
    with dissolve
    Bredita "Now that we're here"
    Bredita "I'm waiting..."
    scene v18043
    with dissolve
    Bredita "Time to please my pussy"
    lili "Yes Mistress, it's my pleasure"
    scene v18044
    with dissolve
    Bredita "Hmm... Your skeleton is enjoying this"
    lili "I don't think.."
    scene v18045
    with dissolve
    Bredita "Shush girl!! Lick my pussy!"
    lili "..."
    scene v18046
    with dissolve
    Bredita "Ahhh... yes..."
    lili "Slurp...lick..."
    scene v18047
    with dissolve
    Bredita "That's it! Keep going"
    Bredita "AH!"
    scene v18048
    with dissolve
    Bredita "Get the fuck out of here!"
    lili "What??"
    scene v18049
    with dissolve
    Bredita "I didn't tell you to stop!"
    Bredita "Lick it!!"
    Bredita "That's it my little girl"
    Bredita "Don't you dare to stop!"
    stop music fadeout 2.0
    scene v15mission048
    with dissolve
    play music "<loop 0.0>ingame.mp3" fadein 2.0
    ayna "[MC]!! There you are, welcome back"
    ayna "I was beginning to wonder where you were"
    scene v15mission050
    with dissolve
    ayna "So have you spoken with the farmer?"
    ayna "Does he know that his daughter is with us?"
    MC "Well...He does...but"
    MC "There was a weird creature commanding him"
    scene v15mission049
    with dissolve
    ayna "A weird creature?"
    MC "Yes, it was an Imp I believe"
    scene v15mission050
    with dissolve
    ayna "An Imp?"
    ayna "Those are tricky creatures"
    ayna "Always trying to fool you with false deals"
    if dealimp == True:
        MC "Now you tell me..."
        MC "I almost got killed by that thing"
        ayna "You made a deal with it?"
        MC "Yes... If it wasn't for a mysterious Mage, I wouldn't be here"
        ayna "A Mage?"
        ayna "Who was he?"
        jump strangemage
    else:
        MC "He tried to make a deal"
        MC "But I rejected it"
        MC "Still, I almost got killed"
        MC "If it wasn't for a mysterious Mage I wouldn't be here"
        ayna "A Mage?"
        ayna "Who was he?"
        jump strangemage

label strangemage:
    MC "Well, I can't say much"
    MC "But he beat the Imp so easily"
    MC "That he must be a very powerful Mage"
    scene v18050
    with dissolve
    ayna "And he helped you.."
    ayna "That's good to know"
    yisnna "Hello you two"
    scene v18051
    with dissolve
    ayna "Oh, hello Yisnna"
    scene v18052
    with dissolve
    yisnna "Good day Archmage"
    yisnna "Hello... [MC]"
    MC "Hello"
    MC "You know my name?"
    yisnna "Of course I know your name"
    yisnna "You impressed me with your presentation"
    if impressed == "elf":
        yisnna "Those flames made the whole courtyard blazing hot"
        yisnna "I haven't seen a student do something so impressive since.."
        yisnna "Our Archmage here"
        MC "Really?"
        scene v18052
        with dissolve
        ayna "Well..."
    else:

        if impressed == "lili":
            yisnna "That reptilian was very fierce and impressive"
            yisnna "I haven't seen a student do something so impressive since.."
            yisnna "Our Archmage here"
            MC "Really?"
            scene v18052
            with dissolve
            ayna "Well..."
        else:

            if impressed == "abaa":
                yisnna "Your Ward looked impenetrable "
                yisnna "I haven't seen a student do something so impressive since.."
                yisnna "Our Archmage here"
                MC "Really?"
                scene v18052
                with dissolve
                ayna "Well..."
            else:
                if impressed == "arch":
                    yisnna "Your Darkness blotted out the very sun"
                    yisnna "I haven't seen a student do something so impressive since.."
                    yisnna "Our Archmage here"
                    MC "Really?"
                    scene v18052
                    with dissolve
                    ayna "Well..."
                else:
                    if impressed == "rerl":
                        yisnna "Professor Rerlvam looked quite funny flying through the air.."
                        yisnna "Ahaha, I know I shouldn't laugh but..."
                        yisnna "I haven't seen a student do something so impressive since.."
                        yisnna "Our Archmage here"
                        MC "Really?"
                        scene v18052
                        with dissolve
                        ayna "Well..."
                    else:
                        yisnna "You casted Mass Blessing"
                        yisnna "At first I tought it was a bad choice"
                        yisnna "But it was impressive, everyone could feel your power"
                        yisnna "I haven't seen a student make such an potetent impression since.."
                        yisnna "Our Archmage here"
                        MC "Really?"
                        scene v18052
                        with dissolve
                        ayna "Well..."
    scene v18053
    with dissolve
    ayna "Yisnna, I'm glad you're here actually"
    ayna "[MC], You should go with Yisnna"
    ayna "She knows a lot about the world"
    scene v18052
    with dissolve
    yisnna "I like to think almost everything, hehe"
    MC "I don't think that's possible..."
    scene v18053
    with dissolve
    ayna "Anyway, she can teach you about creatures you are unaware of, like that imp"
    ayna "As well as about various factions, magic, and even about yourself"
    MC "Myself?"
    scene v18052
    with dissolve
    yisnna "Yes, what we believe we know about you at least"
    yisnna "Where you came from, about your homeland..."
    MC "Very well, let's go!"
    scene v18053
    with dissolve
    ayna "[MC] pay good attention to Yisnna"
    ayna "She can teach you alot about this world"
    scene v18052
    with dissolve
    yisnna "Shall we go?"
    stop music fadeout 2.0
    scene black
    with dissolve
    play music "<loop 0.0>dark.mp3" fadein 2.0
    scene v18049
    with dissolve
    Bredita "Hmmm that's..."
    scene v18070
    with dissolve
    Bredita "...."
    Bredita "You've got a lot of nerve to show up here"
    scene v18071
    with dissolve
    lili "???"
    Bredita "Show yourself!"
    Bredita "I'll only ask once"
    scene v18072
    with dissolve
    zegladar "Well well well"
    zegladar "Impressive as always, my dear Bredita"
    zegladar "Even while having fun with your puppets"
    zegladar "You are able to detect me"
    scene v18071
    with dissolve
    lili "Oh my..."
    Bredita "I'm also impressed..."
    Bredita "You were quite good actually..."
    Bredita "But your brother..."
    lili "Brother?"
    scene v18072
    with dissolve
    zegladar "Hahah"
    scene v18073
    with dissolve
    zegladar "Goggos, come on, she knows you're there.."
    scene v18074
    with dissolve
    goggos "Hmmm I was just enjoying the view..."
    goggos "Who is your new puppet Bredita?"
    scene v18075
    with dissolve
    goggos "Can I have a turn with her?"
    goggos "I like her!"
    scene v18071
    with dissolve
    lili "I.. what..?"
    scene v18076
    with dissolve
    goggos "Come now, my dear..."
    goggos "I won't hurt you.... much..."
    scene v18077
    with dissolve
    Bredita "So... Goggos..."
    Bredita "Does that mean you don't want me?"
    goggos "Oh, I can fuck you both, hehehe"
    Bredita "Ahaha You're forgetting something you, big meatball"
    goggos "What?"
    scene v18078
    with dissolve
    Bredita "That you are no match for me"
    goggos "Ahhhrg"
    Bredita "So... Which of us is going to end up fucked, I wonder?"
    Bredita "Maybe I should summon a gigantic cock"
    Bredita "And put it inside your ass?"
    goggos "...."
    scene v18079
    with dissolve
    zegladar "Now Bredita, as much as I would enjoy"
    zegladar "To see my brother learn a lesson"
    zegladar "That's not why we are here"
    scene v18080
    with dissolve
    Bredita "Ok, speak"
    zegladar "You know that the Allesterra Mages have something we want"
    zegladar "And I know that you want it too"
    Bredita "So...?"
    zegladar "Can we work together to get it?"
    zegladar "We just need a part of it's power"
    zegladar "The rest is all yours, once we're done"
    scene v18081
    with dissolve
    zegladar "Can we make a deal?"
    Bredita "Hmmm"
    Bredita "You've reminded me of something my mother once told me"
    scene v18082
    with dissolve
    zegladar "Hmm what??"
    Bredita "That you should never make a deal with a devil"
    scene v18083
    with dissolve
    zegladar "I see..."
    scene v18084
    with dissolve
    zegladar "Hahaha"
    zegladar "She sounds like a smart woman"
    zegladar "However, this time we are actually serious"
    Bredita "Ok, let's make a deal then"
    Bredita "You leave now, and I won't kill you both"
    zegladar "Very well"
    scene v18085
    with dissolve
    zegladar "Goggos!"
    zegladar "We have to go..."
    goggos "But you said.."
    zegladar "Let's go"
    scene v18086
    with dissolve
    goggos "Oh, I won't forget you, my lovely girl"
    scene v18087
    with dissolve
    goggos "You will beg me to fuck that pussy someday"
    scene v18088
    with dissolve
    goggos "Bye Bredita...."
    goggos "Bye... Bredita's pretty puppet.."
    stop music fadeout 2.0
    scene black
    with dissolve
    play music "<loop 0.0>ingame.mp3" fadein 2.0
    scene v18054
    with dissolve
    yisnna "So [MC] have you ever been in this library?"
    MC "I guess I came here once or twice for my classes"
    yisnna "Isn't this place great?"
    scene v18055
    with dissolve
    yisnna "There is so much knowledge here, waiting to be learned"
    MC "Have you read many of these books?"
    scene v18056
    with dissolve
    yisnna "Well... actually I've read all of them"
    MC "All?"
    scene v18054
    with dissolve
    yisnna "Yes, all of them"
    MC "But how?"
    yisnna "Well I like to read, and I have lots of time, so.."
    yisnna "But hey, do you want to learn something or what?"
    scene v18057
    with dissolve
    $ talklibrary = False
    $ talkmyself = False
    $ talklibraryyou = False
    $ yisnnaafect = 0
    $ yisnnabooks = 0

    MC "Ok"
    yisnna "Shall we?"

    jump libraryknows

label libraryknows:
    if talklibrary == False:

        yisnna "So what do you want to learn first?"
        $ talklibrary = True
        jump librarychoices

    if talklibrary == True:
        yisnna "Like what you learned?"
        yisnna "What do you want to know next?"
        jump librarychoices

label librarychoices:
    MC "I want to learn about"
    menu:
        AB "Choose all."
        "Myself" if talkmyself == False:
            jump storymyself
        "You" if talklibraryyou == False:
            jump storyyourself
        "Creatures":
            jump storycreatures
        "College":
            jump storycollege
        "The Elite":

            jump storyelite
        "The World":
            jump storyworld
        "Nothing else" if talkmyself == True:
            jump postlibrarystory

label storymyself:
    scene v18054
    with dissolve
    $ talkmyself = True
    yisnna "You want to learn what the College knows about you?"
    yisnna "Very well"
    yisnna "10 years ago Katriona and Katarro"
    yisnna "Brought you here from your town in Arfam"
    yisnna "We are not sure what happened before their arrival"
    scene mages010
    with dissolve
    yisnna "When they arrived, the whole town was burning"
    yisnna "It was total carnage. There were no survivors... Just you"
    scene v18054
    with dissolve
    MC "So.. Someone attacked the town and killed everyone?"
    yisnna "Yes... And no.."
    MC "What do you mean?"
    yisnna "We know that the Slayers attacked your village"
    yisnna "But that kind of destruction could only be done by magic"
    MC "Magic?"
    yisnna "The Archmage believes that you..."
    yisnna "Were the one responsible for that"
    MC "What me? For destroying my village?"
    yisnna "Well, you were probably trying to defend yourself"
    yisnna "Or your family and friends"
    yisnna "You've lost your memories so we can't really know why"
    yisnna "We have no idea if you already knew magic"
    yisnna "Or if the danger somehow awakened your powers"
    MC "That can't be true"
    MC "How can you be sure about this?"
    yisnna "That's the thing.. We're not..."
    yisnna "But when Katriona and Katarro arrived"
    yisnna "There was a lot of burnt Slayer soldiers"
    yisnna "More than the town defenses could have done"
    yisnna "And the center of the explosion"
    yisnna "Was the exact place where you were found"
    MC "Well... If that is true..."

    jump libraryknows

label storyyourself:
    $ talklibraryyou = True
    scene v18058
    with dissolve
    yisnna "You want to know about me?"
    MC "Yes"
    $ yisnnaafect += 1
    "Yisnna affection increased"
    yisnna "Oh...Ok"
    scene v18056
    with dissolve
    yisnna "I'm Yisnna, the Librarian"
    yisnna "I'm the one responsible for maintaining the College Library"
    yisnna "And I've been here for a long time"
    MC "What do you mean by a long time?"
    yisnna "More than a 100 years"
    MC "Ok, that's a lot"
    yisnna "Yes, you know that some of the mages here are very old"
    yisnna "So am I"
    MC "Ok, please continue"
    yisnna "I studied here at the College many years ago"
    yisnna "And I could learn all the theories and knowledge easily"
    yisnna "Still, I was never a good Mage"
    yisnna "Everyone has a certain limit of power"
    yisnna "And mine... Well... Mine is not that high"
    yisnna "Master Suntako, the Archmage at the time"
    yisnna "Saw my abillity and love for books"
    yisnna "So he asked me to take care of the Library"
    yisnna "And told me as long as I remained here, I wouldn't age a day"
    scene v18054
    with dissolve
    yisnna "So here I am"
    MC "You never get bored?"
    yisnna "Sometimes yes..."
    yisnna "But since we receive new books from time to time..."
    yisnna "Hey, that gives me an idea"
    yisnna "If while on your travels you find any books"
    yisnna "Bring them to me"
    yisnna "I'll pay you with gold"
    MC "Sound's great, it's a deal"
    "You will find books on your travels that you can bring to Yisnna for gold"
    jump libraryknows

label storycreatures:
    scene v18054
    with dissolve
    yisnna "You want to learn about creatures?"
    yisnna "What do you want to know?"

    yisnna "There are so many..."
    menu:
        "Vampires":
            scene v18059
            with dissolve
            yisnna "Vampires"
            yisnna "Vampirism is a kind of disease"
            yisnna "That you get from blood contact with vampires"
            yisnna "Vampires gain an increase to some of their skills"
            yisnna "But they also gain new weaknesses"
            yisnna "Like the sun or fire..."
            jump storycreatures
        "Werewolves":
            scene v18060
            with dissolve
            yisnna "Werewolves"
            yisnna "Brutish creatures, very strong and very fast"
            yisnna "Like real wolves, they travel in packs"
            yisnna "They have a high resistance to magic"
            yisnna "A fierce opponent for a common mage"
            jump storycreatures
        "Minotaurs":
            scene v18061
            with dissolve
            yisnna "Minotaurs"
            yisnna "Very strong creatures"
            yisnna "They are not very smart, but usually pretty friendly"
            yisnna "Just don't start trouble with them"
            yisnna "Unless you're ready for a fight"
            jump storycreatures
        "Giant Spiders":
            scene v18062
            with dissolve
            yisnna "Giant Spiders"
            yisnna "Well, they are just like common spiders..."
            yisnna "Only much bigger"
            yisnna "There are many kinds of spiders"
            yisnna "For example, the Giant Frost Spider"
            yisnna "The most common one we see here on Allesterra"
            yisnna "Due to their nature they are immune to cold"
            jump storycreatures
        "Lizard folk":
            scene v18063
            with dissolve
            yisnna "Lizard folk"
            yisnna "They call themselves Gokthians..."
            yisnna "With all the wars, Gokthians are near extinction"
            yisnna "You can probably still find some of them in Tanzani though"
            yisnna "They usually live near swamps"
            yisnna "They are very aggressive"
            jump storycreatures
        "I want to ask something else":
            jump libraryknows

label storycollege:
    scene v18054
    with dissolve
    yisnna "The College hmm..."
    yisnna "I guess you already know this but"
    yisnna "Children with magic potential"
    yisnna "Are brought here to study magic"
    yisnna "The College is ruled by The Elite"
    yisnna "And Archmage Ayna is the head of the College"
    yisnna "Students like you can become great Mages"
    yisnna "Though some do fail..."
    jump libraryknows

label storyelite:
    scene v18054
    with dissolve
    yisnna "The Elite"
    yisnna "They're are usually seven of them"
    yisnna "The six best of the best in each school of magic"
    yisnna "And then the Archmage as the central leader"
    yisnna "The Archmage is choosen by the others"
    yisnna "But don't let that fool you"
    yisnna "Ayna is probably the strongest Mage I've ever seen"
    yisnna "And with Master Suntako gone, she is the strongest here for sure"
    MC "Why did Master Suntako leave?"
    yisnna "I'm not sure... I've only heard that he decided to leave on his own"
    MC "(Hmmm... It was because of Liliana for sure)"
    MC "Will someone be replacing him as member of The Elite?"
    yisnna "I believe so, Enainia being here can't be a coincidence"
    MC "Enainia?"
    yisnna "Yes, the Elf princess that was at the students' presentation"
    scene v015095
    with dissolve
    MC "Yes... I remember seeing her"
    MC "You think she'll become one of The Elite?"
    scene v18054
    with dissolve
    yisnna "It's just my best guess"
    yisnna "But who knows?"
    jump libraryknows

label storyworld:
    scene v18054
    with dissolve
    yisnna "The world"
    yisnna "Very well, let me show you something"
    "She shows you a map"
    scene worldmap
    with dissolve
    yisnna "First of all this map is outdated"
    yisnna "Some of the borders might have changed"
    yisnna "With all the wars..."

    yisnna "This Blue island is Allesterra"
    yisnna "Our college is located here"
    yisnna "We are known in the world as the Mages"
    yisnna "And we don't usually interfere"
    yisnna "With the affairs of other nations"

    yisnna "A little lower we have Tanzani in grey"
    scene v18054
    with dissolve
    yisnna "I'm an example of a Tanzanian, hehehe"
    yisnna "The natives of Tanzani are usually dark skinned"
    yisnna "We are a peaceful people"
    yisnna "that have alot of knowledge in alchemy and plants"
    scene worldmap
    with dissolve
    yisnna "The one represented in green is Highgard"
    yisnna "This is the land of the Nords"
    yisnna "Tall and strong people, with a light complexion"
    yisnna "That description was true for Arfam, your homeland..."
    yisnna "Sadly they no longer exist..."

    yisnna "The little dark island is Uky"
    yisnna "Nobody knows what's there"
    scene v18054
    with dissolve
    yisnna "I believe that demons and such live there"
    MC "Demons?"
    yisnna "Yes... Demons, devils, imps... You name it"
    scene worldmap
    with dissolve
    yisnna "Then you have Orciash and Okchorg"
    scene v18064
    with dissolve
    yisnna "These are orc lands"
    yisnna "Orcs are warriors, they love war"
    yisnna "Luckily they are not very smart..."
    scene worldmap
    with dissolve
    yisnna "We have Irokumata and Nagatashi"
    yisnna "Normally these people are a bit smaller"
    yisnna "And their skins are a bit yellow toned"
    scene v18069
    with dissolve
    yisnna "Like your classmate Koneko"
    yisnna "They are also the oldest known civilizations"
    yisnna "And probably the most advanced ones in technology"
    scene worldmap
    with dissolve
    yisnna "The Slayers"
    yisnna "They have the biggest territory due to conquest and war"
    yisnna "And are the most aggressive civilization,"
    yisnna "Even the lowest soldiers are well equiped"
    yisnna "And know how to fight"

    yisnna "Of course we have here Elvaria and Darkaria"
    yisnna "Kingdoms of the elves and the dark elves"
    scene v18068
    with dissolve
    yisnna "Our own Master Katarro would be an example of the Elves"
    scene v18066
    with dissolve
    yisnna "And Mistress Silvana would be an example of a Dark Elf"
    scene worldmap
    with dissolve
    yisnna "To finish up, we have Mythrial"
    yisnna "This island is home to many kinds of creatures"
    jump libraryknows

label postlibrarystory:
    yisnna "Well, I hope I was able to teach you something today"
    yisnna "Come back and see me any time"
    MC "Thank you, good night Yisnna"
    "You leave the library and head to your room to sleep"
    scene meanwhile
    with dissolve
    scene v18090
    with dissolve
    goggos "Look how they left me sister"
    zegladar "Ahahha"
    zegladar "You are always the same"
    zegladar "Is it only pussy you think about?"
    goggos "Yes...."
    goggos "Can you do something to help me?"
    zegladar "Ok... Now that I've seen your cock, well..."

    scene v18091
    with dissolve
    goggos "Can I ask you something?"
    zegladar "What?"
    goggos "Can you transform into that girl?"
    scene v18090
    with dissolve
    zegladar "What girl? Bredita's new puppet?"
    goggos "Yes!! Yes!! That one"
    zegladar "Hmmm"
    goggos "I'll do whatever you want next"
    scene v18091
    with dissolve
    zegladar "It's a deal..."
    scene v18092
    with dissolve
    scene v18093
    with dissolve
    scene v18094
    with dissolve
    scene v18095
    with dissolve
    lili "Is this what you wanted?"
    goggos "Oh... Yes little girl"
    goggos "Look what I've got here for you"
    scene v18096
    with dissolve
    lili "Oh my... Such a big cock..."
    lili "Is this all for me?"
    goggos "Yes! let me get my pants out of the way"
    scene v18097
    with dissolve
    goggos "So what do you say?"
    lili "I've never seen such a big cock"
    goggos "Play with it"
    scene v18098
    with dissolve

    lili "I'm not sure I can"
    lili "It's too big for me"
    scene v18099
    with dissolve
    lili "But it looks so tasty"
    goggos "Come on then, taste it"
    scene v18100
    with dissolve
    goggos "That's it use you tongue"
    goggos "Move it!"
    scene v18101
    with dissolve
    lili "Hmmmm"
    lili "Lick, lick"
    goggos "Ah... Yes..."
    goggos "Now put it in your mouth!"
    scene v18102
    with dissolve
    goggos "Yes! Suck it!"
    goggos "Much better than Bredita's pussy, right?"
    lili "Hmmm hmmm"
    goggos "Let's continue this upstairs"
    scene v18103
    with dissolve
    lili "Ok"
    goggos "Come with me, little puppet"
    scene v18104
    with dissolve
    goggos "These are mine and my sister's thrones"
    lili "Wow, you are so powerful"
    scene v18105
    with dissolve
    goggos "Shut it bitch!"
    goggos "Your mouth is only good for one thing!"
    scene v18106
    with dissolve
    goggos "Use it!"
    goggos "Yes! Deeper!"
    goggos "Turn around, I want to fuck you!"
    scene v18107
    with dissolve
    lili "Yes, oh great and powerful master"
    goggos "I'll fuck you hard"
    scene v18108
    with dissolve
    goggos "Ahhh... So good"
    goggos "Such a nice pussy"
    scene v18107
    with dissolve
    goggos "Shit... I'm going to cum"
    goggos "Get on your knees slut!"
    scene v18109
    with dissolve
    goggos "I want to cover your face!"
    goggos "Get ready!"
    goggos "Open wide!"
    scene v18110
    with dissolve
    goggos "Ahhhhh!"
    goggos "Take it all!"
    scene v18111
    with dissolve
    goggos "Such a pretty face..."
    goggos "Covered with my devil seed"
    goggos "Lick my cock clean!"
    scene v18112
    with dissolve
    lili "Hmmm hmmm"
    lili "Slurp, lick"
    scene v18113
    with dissolve
    zegladar "So much cum, brother..."
    zegladar "Hmmm this girl sure excites you"
    goggos "Yes... It was great..."
    $ renpy.end_replay()
    scene v015001
    with dissolve
    MC "I think I'm gonna lie down and sleep a bit"
    scene v015009
    with dissolve
    "As you are getting ready to sleep"
    "Someone knocks on the door"
    "And you hear Mida whispering"
    amida "[MC] are you awake?"

    menu:
        "{color=#1BBB20}Answer her":
            scene v015001
            with dissolve
            MC "Yes I am"
            "She enters the room"
            scene v18142
            with dissolve
            amida "I was thinking we could have some fun"
            menu:
                "{color=#1BBB20}I'm always ready for fun!":
                    amida "Great!"
                    amida "Let me show you what I have under this dress"
                    scene v18124
                    with dissolve
                    amida "Surprise.. Nothing! Ahahah"
                    MC "You got me..."
                    MC "Can I see more?"
                    "She rotates a bit"
                    scene v18125
                    with dissolve
                    "Showing her ass"
                    amida "Is this what you want to see?"
                    MC "Oh yes..."
                    "She bends a little"
                    scene v18126
                    with dissolve
                    "Showing her ass even more"
                    amida "Do you like it?"
                    menu:
                        "I love it{color=#1BBB20} (+1 Mida's Love)":
                            $ midalove += 1
                            "Mida's love increased"
                            amida "Let me show you more"
                            jump v18midasex
                        "Bring that ass here!{color=#FF0000} (+1 Mida's Corruption)":
                            $ midacorr += 1
                            "Mida's corruption increased"
                            amida "Giggle"
                            jump v18midasex
                "I'm too tired, maybe tomorrow{color=#FF0000} (-1 Mida's Corruption/Love)":




                    amida "OK then..."
                    $ midalove -= 1
                    $ midacorr -= 1
                    "She left"
                    scene v015001
                    with dissolve
                    "Mida's love and corruption decreased"
                    jump sleepv18
        "Pretend you are sleeping":

            amida "Love?"
            amida "..."
            amida "Sweet dreams..."
            jump sleepv18

label v18midasex:
    $ firstgoingv18 = 0
    scene v18127
    with dissolve
    MC "Good..."
    "You start to play with her ass"
    scene v18129
    with dissolve
    scene v18128
    with dissolve
    amida "Lie on the bed please"
    menu:
        "Ignore her and put a finger in her pussy{color=#FF0000} (+1 Mida's Corruption)":
            scene v18130
            with dissolve
            amida "Oh! I wasn't expecting that"
            MC "Was it bad?"
            amida "No..."
            $ midacorr += 1
            "Mida's corruption increased"
            MC "Good"
            "You use your finger for a few seconds"
            MC "Now it's time for something bigger"
            "Before she could say anything"
            "You turned her around with hands on the bed"
            scene v18131
            with dissolve
            "You started to rub your cock on her pussy"
            MC "Do you like this?"
            amida "Yes..."
            MC "Let's continue then"
            "You then started to push your cock inside her pussy"
            scene v18132
            with dissolve
            amida "Ah.... Go easy..."
            "You start to slide your cock inside"
            scene v18133
            with dissolve
            amida "Ah... Yes..."
            MC "Hummm"
            "You feel her walls pressing against your cock"
            amida "You can move..."
            scene v18134
            with dissolve
            "You push your cock deeper"
            amida "Ah... Yes keep going.."
            "You start go gain some pace"
            amida "Yes that's it... More..."
            scene v18133
            with dissolve
            MC "Oh.... Yes"
            "You give it more and more"
            amida "Ah... This is great but..."
            amida "Can we try something else?"
            MC "I..."
            scene v18135
            with dissolve
            "She turns around to face you"
            jump v18midasex2
        "Lie on the bed{color=#FF0000} (More points in the next choice)":


            "You lied on the bed"
            scene v18135
            with dissolve
            amida "You are so hard already!"
            menu:
                "That's because I love you{color=#1BBB20} (+1 Mida's Love)":
                    $ midalove += 1
                    "Mida's love increased"
                    amida "Oh... I love you too"
                    jump v18midasex2
                "That's because you're so hot{color=#FF0000} (+1 Mida's Corruption)":
                    $ midacorr += 1
                    "Mida's corruption increased"
                    amida "You naughty boy..."
                    jump v18midasex2



label v18midasex2:
    scene v18135
    with dissolve
    $ midaorder = 0
    amida "So now I'm going to..."
    menu:
        "I give the orders here{color=#FF0000} (+1 Mida's Corruption/Order)" if midacorr >= 2:
            amida "Uhmm ok..."
            amida "I... Like this..."
            $ midaorder = 1
            $ midacorr += 1
            "Mida's corruption increased"
            jump v18midachoicessex



        "Smile and let her finish{color=#1BBB20} (+1 Mida's Love)" if midalove >= 2:
            amida "Let you choose what you want"
            amida "Since you are so lovely"
            $ midalove += 1
            "Mida's love increased"
            jump v18midachoicessex
        "Listen silently":

            amida "Start to please you with my mouth"
            scene v18114
            with dissolve
            "She then gets on her knees"
            "And grabs your cock"
            scene v18115
            with dissolve
            amida "So hard..."
            "She is grabbing you very hard"
            scene v18116
            with dissolve

            amida "Do you like this?"
            amida "This hard?"
            "You can't even speak"
            scene v18115
            with dissolve
            "She then starts to stroke you"
            "The sensation is ovewhelming"
            scene v18117
            with dissolve
            amida "Time to taste it"
            "And she puts your cock in her mouth"
            scene v18118
            with dissolve
            MC "Ahh.."
            amida "Hmmmm"
            "You can only watch her movements"
            "Going up and down on your dick"
            MC "Ah... Yes..."

            scene v18119
            with dissolve
            "And then she goes deeper"
            scene v18120
            with dissolve
            MC "Ahhh"
            MC "Fuck yeah..."
            amida "Hmmm"
            scene v18117
            with dissolve
            amida "Everything ok?"
            MC "Yes..."


            amida "Good, time to play with my boobs"
            scene v18121
            with dissolve
            "She places your cock between her boobs"
            "They are so soft, yet firm..."
            scene v18122
            with dissolve
            "She smiles at you"
            "You must be doing some weird faces"
            scene v18123
            with dissolve
            "She's stops"
            scene v18122
            with dissolve


            amida "Time for the main dish"
            scene v18135
            with dissolve
            MC "..."
            scene v18136
            with dissolve
            amida "You are absolutely ready"
            amida "Look at this cock"
            "She starts to slide you in"
            scene v18140
            with dissolve
            MC "Ahhh... yes..."
            amida "Ah.... It's so big..."
            scene v18138
            with dissolve
            amida "Hmm, so good..."
            amida "Move a little bit"
            "You obey"
            scene v18139
            with dissolve
            amida "Ah! Yes!"
            scene v18138
            with dissolve
            amida "I'm about to..."
            scene v18137
            with dissolve
            amida "Cuuuum!!"
            "She screamed so loud"
            "That if someone was outside they would hear her"
            scene v3g093
            with dissolve
            amida "That was great!"
            $ renpy.end_replay()
            jump v02






label v18midachoicessex:
    scene v18135
    with dissolve

    if firstgoingv18 == 0:
        amida "So... What do you want me to do?"
    else:
        amida "So... What do you want to do next?"
    menu:
        "Suck my cock!" if midaorder == 1:
            amida "Yes..."
            scene v18114
            with dissolve
            "She gets on her knees"
            "And grabs your cock"
            scene v18115
            with dissolve
            amida "So hard..."
            scene v18116
            with dissolve
            amida "Do you like this?"
            MC "Hmmm"
            "She starts to stroke you"
            scene v18117
            with dissolve

            MC "I said suck it"
            amida "..."
            "She puts your cock in her mouth"
            scene v18118
            with dissolve
            MC "Ahh.."
            amida "Hmmmm"
            "You can only watch her movements"
            "Going up and down on your dick"
            MC "Ah... Yes..."

            scene v18119
            with dissolve

            "And the she goes deeper"
            scene v18120
            with dissolve
            MC "Ahhh"
            MC "Fuck yeah..."

            scene v18117
            with dissolve
            amida "Hmmm"
            $ firstgoingv18 = 1
            jump v18midachoicessex

        "Use your mouth please" if midaorder == 0:
            amida "Yes..."
            scene v18114
            with dissolve
            "She gets on her knees"
            "And grabs your cock"
            scene v18115
            with dissolve
            amida "So hard..."
            scene v18116
            with dissolve
            amida "Do you like this?"
            MC "Hmmm"
            "She starts to stroke you"
            scene v18117
            with dissolve
            MC "Oh... Yes..."
            amida "Hmmm"
            "She puts your cock in her mouth"
            scene v18118
            with dissolve
            MC "Ahh.."
            amida "Hmmmm"
            "You can only watch her movements"
            "Going up and down on your dick"
            MC "Ah... Yes..."
            scene v18119
            with dissolve
            "And the she goes deeper"
            scene v18120
            with dissolve

            MC "Ahhh"
            MC "Yes..."
            scene v18117
            with dissolve
            amida "Hmmm"
            $ firstgoingv18 = 1
            jump v18midachoicessex

        "Use your tits!" if midaorder == 1:
            amida "Of course"
            scene v18121
            with dissolve
            "She places your cock between her boobs"
            "They are so soft, yet firm..."
            scene v18122
            with dissolve
            "She smiles at you"
            "You must be doing some weird faces"
            scene v18123
            with dissolve
            "She's stops"
            scene v18122
            with dissolve
            $ firstgoingv18 = 1
            jump v18midachoicessex

        "Can you use your boobs?" if midaorder == 0:
            amida "Of course"
            scene v18121
            with dissolve
            "She places your cock between her boobs"
            "They are so soft, yet firm..."
            scene v18122
            with dissolve
            "She smiles at you"
            "You must be doing some weird faces"
            scene v18123
            with dissolve
            "She's stops"
            scene v18122
            with dissolve
            $ firstgoingv18 = 1
            jump v18midachoicessex

        "Ride my cock!" if midaorder == 1:
            amida "So you want the main dish"
            scene v18135
            with dissolve
            MC "..."
            scene v18136
            with dissolve
            amida "Look at this cock"
            "She starts to slide you in"
            scene v18140
            with dissolve
            MC "Ahhh... yes..."
            amida "Ah.... It's so big..."
            scene v18138
            with dissolve
            amida "Hmm, so good..."
            MC "Move faster!"
            amida "Yes.."
            scene v18139
            with dissolve
            amida "Ah! Yes!"
            "You give it everthing you got"
            "Fast and hard until..."
            amida "I'm about to..."
            scene v18137
            with dissolve
            amida "Cuuuum!!"
            "She screamed so loud"
            "That if someone was outside they would hear her"
            scene v18138
            with dissolve
            amida "Ah! Yes!"
            scene v3g093
            with dissolve
            amida "That was great!"
            $ renpy.end_replay()
            jump v02

        "Do you want to ride me?" if midaorder == 0:
            amida "So you want the main dish?"
            scene v18135
            with dissolve
            MC "..."
            scene v18136
            with dissolve
            amida "Look at this cock"
            "She starts to slide you in"
            scene v18140
            with dissolve
            MC "Ahhh... yes..."
            amida "Ah.... It's so big..."
            scene v18138
            with dissolve
            amida "Hmm, so good..."
            MC "Yes faster"
            amida "Yes.."
            scene v18139
            with dissolve
            amida "Ah! Yes!"
            "You give it everthing you got"
            "Fast and hard until..."
            amida "I'm about to..."
            scene v18137
            with dissolve
            amida "Cuuuum!!"
            "She screamed so loud"
            "That if someone was outside they would hear her"
            scene v18138
            with dissolve
            amida "Ah! Yes!"
            scene v3g093
            with dissolve
            amida "That was great!"
            $ renpy.end_replay()
            jump v02






label sleepv18:
    scene black
    with dissolve
    "You lay on the bed and fall asleep"
    jump v02
