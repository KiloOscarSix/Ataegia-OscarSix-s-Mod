

label v02:

    scene meanwhile
    with dissolve
    scene v2001
    with dissolve
    Bredita "It's ok my dear"
    lili "Who... who were they?"
    lili "What did they want from us?"
    scene v2002
    with dissolve
    Bredita "Those were the Devil Lords"
    lili "Devil Lords?"
    lili "What does that mean?"
    scene v2003
    with dissolve
    Bredita "It means that they are very dangerous"
    Bredita "It also means that if you are found alone"
    Bredita "Goggos will try to rape you... If you are lucky..."
    scene v2004
    with dissolve
    lili "What? I...."
    Bredita "Yes, he saw you... And Goggos aggressiveness..."
    Bredita "Can only be matched by his sexual drive"
    Bredita "He's a wicked creature..."
    scene v2003
    with dissolve
    Bredita "And his sister... Zegladar..."
    Bredita "She's even more dangerous..."
    Bredita "Unlike Goggos, she is smart and unpredictable"
    lili "But they were afraid of you mistress..."
    lili "You are more powerful than them"
    Bredita "That's not true..."
    scene v2004
    with dissolve
    lili "What? But they... ran from you..."
    Bredita "They did... But only because of where we are"
    Bredita "They get weaker the closer they get to Allesterium"
    lili "Really?"
    scene v2003
    with dissolve
    Bredita "Yes, like how Mages in general feel stronger near Allesterium"
    Bredita "Devils, demons and other devilish creatures"
    Bredita "Get weaker when close to it"
    Bredita "Of course, that doesn't mean they are weak even in that state"
    Bredita "Only a handful of Mages can face a 'weakened' Devil..."

    Bredita "And when we are talking about Goggos and Zegladar..."
    Bredita "Well.... Maybe three..."
    lili "Three? Who else beside you mistress?"
    scene v2004
    with dissolve
    Bredita "Ayna obviously, and Suntako..."
    lili "I understand..."
    lili "That's why you wanted Suntako out of the College"
    Bredita "Exactly, having the two of them together"
    Bredita "Unbalanced the distribution of power in the world"
    lili "I understand..."
    Bredita "Now, I need you to go to the College and stay there"
    Bredita "That's the safest place for you to stay right now"
    lili "But... what about my training?"
    Bredita "Are you questioning me?!"
    lili "No.. I'm sorry..."
    Bredita "Leave now!"
    lili "Yes mistress..."
    scene v2005
    with dissolve
    lili "...."
    Bredita "Don't leave the College until I say so"
    lili "Yes mistress"
    scene v2006
    with dissolve
    Bredita "Ok...now that Liliana is gone"
    Bredita "It's time I had a chat with... 'her'"
    scene v2007
    with dissolve
    "...."
    scene v15mission001
    with dissolve
    ayna "What is this feeling?"
    ayna "it's like..."
    Bredita "Ayna..."
    scene v2008
    with dissolve
    ayna "Bredita?"
    Bredita "Oh... You remember me dear... I'm flattered..."
    ayna "How could I forget..."
    scene v2009
    with dissolve
    ayna "What do you want?"
    Bredita "Wow, just like that?"
    Bredita "Not even a 'Long time, no see'?"
    Bredita "Or 'How's the family'?"
    ayna "Cut the crap, what do you want?"
    Bredita "... Goggos and Zegladar..."
    scene v2008
    with dissolve
    ayna "What about them?!"
    Bredita "They want to make a deal with me"
    ayna "And?"
    Bredita "...It concerns you"
    ayna "..."
    ayna "Go ahead..."
    Bredita "I want to talk with you personally"
    scene v2009
    with dissolve
    ayna "Do you think me so stupid?"
    ayna "How do I know it's not a trap?"
    Bredita "Well, you don't..."
    Bredita "But you do feel it, don't you?"
    Bredita "You felt Goggos presence didn't you?"
    scene v2008
    with dissolve
    ayna "Yes..."
    Bredita "So... Meet me tomorrow morning"
    Bredita "I'll tell you where then"
    Bredita "So you won't prepare some way to capture me"
    scene v2009
    with dissolve
    ayna "No way!"
    ayna "You will choose 3 places now"
    ayna "Tomorrow I choose one of them and we meet"
    ayna "So you choose the time, I choose the place"
    Bredita "Hmmm, I like you..."
    Bredita "You're smarter than I remember..."
    Bredita "Very well, it's a deal"
    Bredita "Let's see..."
    scene v015001
    show blink3
    show blink2
    hide blink3
    with dissolve
    show blink1
    hide blink2
    with dissolve
    hide blink1
    with dissolve
    MC "Yawn!"
    MC "Another day...."
    MC "Time to get out of the bed"
    scene mcroombg01
    with dissolve
    MC "What now?"
    $ darkelftalk = 0
    $ readbookv2 = False
    $ foundgoldv2 = False
    $ foundbookv2 = False
    $ liliroomv2 = False
    $ talkwithkat = 0
    $ talkwithenainia = False
    $ talkwithrev = False

    $ talkwithstrangev2 = 0
    $ thugvillagev2 = 0
    $ farmgirlv2 = 0
    $ dwarfv2 = 0
    $ citygatev2 = 0
    $ nextstagev2 = 0
    $ hannatalk = 0
    $ hannadealv2 = 0
    $ hannamiss1 = 0
    $ hannamiss2 = 0
    $ elderv2 = 0
    $ helpjackv2 = 0
    $ foundwalletv2 = 0
    $ helpthugv2 = 0


label v2roomselect01:
    scene mcroombg01
    with dissolve

    call screen collegemcroom1


label v2mirror01:
    scene mcroombg01
    with dissolve
    MC "I don't need to sit right now"

    jump v2roomselect01


label v2bed01:
    scene mcroombg01
    with dissolve
    MC "I just got out of bed..."
    MC "Can't be lazy and go back already"

    jump v2roomselect01

label v2books01:
    scene mcroombg01
    with dissolve
    if readbookv2 == False:
        MC "Should I read some skill book?"
        menu:
            "[abgreen]Yes":
                "What will you read?"
                menu:
                    "Battlemagic[abgreen] [abdestpoint]":
                        "You spend a couple of hours studying Battlemagic"
                        $ Destpoints += 1
                        "Battlemagic increased by 1"
                        $ readbookv2 = True
                        jump v2roomselect01
                    "Illusion[abgreen] [abiluspoint]":
                        "You spend a couple of hours studying Illusion"
                        $ Iluspoints += 1
                        "Illusion increased by 1"
                        $ readbookv2 = True
                        jump v2roomselect01
                    "Healing[abgreen] [abhealpoint]":
                        "You spend a couple of hours studying Healing"
                        $ Healpoints += 1
                        "Healing increased by 1"
                        $ readbookv2 = True
                        jump v2roomselect01
                    "Mysticism[abgreen] [abmystpoint]":
                        "You spend a couple of hours studying Mysticism"
                        $ Mystpoints += 1
                        "Mysticism increased by 1"
                        $ readbookv2 = True
                        jump v2roomselect01
                    "Alteration[abgreen] [abaltepoint]":
                        "You spend a couple of hours studying Alteration"
                        $ Altepoints += 1
                        "Alteration increased by 1"
                        $ readbookv2 = True
                        jump v2roomselect01
                    "Summoning[abgreen] [absummpoint]":
                        "You spend a couple of hours studying Summoning magic"
                        $ Summpoints += 1
                        "Summoning increased by 1"
                        $ readbookv2 = True
                        jump v2roomselect01
            "No":
                jump v2roomselect01
    else:
        MC "I'm tired of reading, let's do something else"
        jump v2roomselect01


label v2openbook01:
    scene mcroombg01
    with dissolve
    MC "Those are books about magic schools..."
    MC "It explains the schools of magic and spells"
    "Do you want to read it?"
    menu:
        "[abgreen]Yes":
            MC "Let's read a bit about that"
            MC "I want to check..."
            menu:
                "Battlemagic":
                    "Battle magic focuses on combat spells, it uses elements like fire or lightning"
                    "Fireball, Thunder or Ice spike are typical spells of this school"
                    "Masters of this school are feared because of their raw destructive power"
                    jump v2roomselect01
                "Healing":
                    "Healing Magic focuses on the restoration of your own health, as well as others"
                    "Healing can also be used in combat versus some kinds of undead opponents"
                    "Masters of this school are highly loved and regarded for saving so many lives"
                    jump v2roomselect01
                "Summoning":
                    "Summoning focuses on magically creating creatures or objects to aid you"
                    "Lizards, Wolfs, Cats, Swords, you name it..."
                    "Masters of this school can summon giant creatures and create massive objects"
                    jump v2roomselect01
                "Illusion":
                    "Illusion Magic focuses on tricking the mind, feelings and senses of others"
                    "Fear, invisibility, mind control fall on this school specialities"
                    "Masters of this school can trick and control weaker opponents"
                    jump v2roomselect01
                "Alteration":
                    "Alteration Magic focuses on converting raw magical energy into useable forms"
                    "Using energy to create floating light sources and powerful magical barriers"
                    "Masters of this school can infuse energy into anything and change their nature"
                    jump v2roomselect01
                "Mysticism":
                    "Mysticism focuses on spells that defy the laws of physics"
                    "Telekinesis, teleporting and time manipulation are just some examples"
                    "Masters of this school can create walls of pure force and manipulate gravity"
                    jump v2roomselect01
        "No":


            MC "I'm not going to read it..."
            jump v2roomselect01

label v2window01:
    scene mcroombg01
    with dissolve
    if darkelftalk == 0:
        MC "Let's take a look outside"
        scene v2011
        with dissolve
        MC "Is that Professor Rerlvam and Mistress Silvana?"
        MC "What are they talking about?"
        "You try to listen to them"
        prof "But it's our people..."
        silvana "I know..."
        silvana "You think it's easy for me?"
        scene v2012
        with dissolve
        silvana "To have those bastards killing our kind?"
        silvana "But we made a choice, we decided to be part of the College"
        silvana "We don't interfere with other nations politics or wars"
        scene v2011
        with dissolve
        silvana "I know it's hard, I've been here for a long time"
        silvana "Many things have happened, some of them very hard..."
        prof "But... Those Slayers... They are hunting our people down"
        prof "Surely the extinction of the Dark Elves should concern the College"
        silvana "Yes... Not to mention the Elves and the other races..."
        scene v2012
        with dissolve
        silvana "I will talk with the Archmage, maybe we can do something"
        silvana "I will look for her right away"
        prof "I saw her leave the college earlier, I don't think you will find her now"
        silvana "She left the college? Was she with someone?"
        prof "Not that I saw... I think she was alone"
        silvana "That's strange... Maybe she went somewhere to meditate"
        "Continue to listen? They might notice you"
        $ darkelftalk = 1
        menu:
            "Yes":
                prof "Yes that's probably it"
                silvana "Maybe Katarro knows something"
                $ darkelftalk = 2
                silvana "I...."
                scene v2011
                with dissolve
                prof "What?"
                scene v2013
                with dissolve
                prof "Is that..."
                MC "Oh shit..."
                "You leave the window"
                scene mcroombg01
                with dissolve

                jump v2roomselect01
            "[abgreen]No, it's to risky":
                scene mcroombg01
                with dissolve
                "You leave the window"
                jump v2roomselect01
    else:
        MC "Let's check if they are still outside"
        scene v2014
        with dissolve
        MC "Nobody's outside..."
        jump v2roomselect01



label v2exitroom01:


    scene hall
    with dissolve
    MC "Where should I go now?"
    menu:
        "Return to my room":
            MC "Did I forget to do something inside?"
            jump v2roomselect01
        "[abgreen]Explore the college":

            MC "Let's look around"
            jump hallv2

label hallv2:
    scene collegeblue
    with dissolve
    call screen collegebluev2


label collegeportalroomv2:
    scene portalroom
    with dissolve
    MC "Nobody's here..."
    "Search the room?"
    menu:
        "[abgreen]Yes":
            if foundgoldv2 == False:
                $ dice = renpy.random.randint(10, 25)
                show goldcoins
                with dissolve
                play sound "sounds/Coin.ogg"
                "You found [dice] gold coins"

                $ Gold = Gold + dice
                $ foundgoldv2 = True
                MC "Nice, some gold for me"
                MC "Let's get out of here"
                jump hallv2

            if foundgoldv2 == True:
                MC "I found nothing this time..."
                MC "Let's get out of here"
                jump hallv2
        "No, let's go back":


            jump hallv2

label bathroomcollegev2:
    scene bathhousemiss
    with dissolve
    "You enter the Baths"
    MC "There is nobody here"
    MC "Should I look around?"
    menu:
        "Yes":
            "You look around but you find nothing"
            MC "Nothing to see here"
            MC "Let's go"
            jump hallv2
        "[abgreen]No, let's get out":
            jump hallv2

label collegelibraryv2:
    scene v18055
    with dissolve
    yisnna "Hey [MC] everything ok with you?"
    MC "Yes, I'm fine"
    yisnna "Did you came to learn something"
    yisnna "Or to refresh your memory?"
    yisnna "What do you want to learn?"

label v2library:
    scene v18055
    with dissolve
    menu:
        "Creatures":

            jump storycreaturesv2
        "College":

            jump storycollegev2
        "The Elite":

            jump storyelitev2
        "The World":

            jump storyworldv2
        "Nothing I'm leaving":

            jump hallv2




label storycreaturesv2:
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
            jump storycreaturesv2
        "Werewolves":
            scene v18060
            with dissolve
            yisnna "Werewolves"
            yisnna "Brutish creatures, very strong and very fast"
            yisnna "Like real wolves, they travel in packs"
            yisnna "They have a high resistance to magic"
            yisnna "A fierce opponent for a common mage"
            jump storycreaturesv2
        "Minotaurs":
            scene v18061
            with dissolve
            yisnna "Minotaurs"
            yisnna "Very strong creatures"
            yisnna "They are not very smart, but usually pretty friendly"
            yisnna "Just don't start trouble with them"
            yisnna "Unless you're ready for a fight"
            jump storycreaturesv2
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
            jump storycreaturesv2
        "Lizard folk":
            scene v18063
            with dissolve
            yisnna "Lizard folk"
            yisnna "They call themselves Gokthians..."
            yisnna "With all the wars, Gokthians are near extinction"
            yisnna "You can probably still find some of them in Tanzani though"
            yisnna "They usually live near swamps"
            yisnna "They are very aggressive"
            jump storycreaturesv2
        "I want to ask something else":
            if libraryv39 == 0:
                jump v2library
            else:
                jump v39libraryknow

label storycollegev2:
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
    if libraryv39 == 0:
        jump v2library
    else:
        jump v39libraryknow


label storyelitev2:
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
    if libraryv39 == 0:
        jump v2library
    else:
        jump v39libraryknow

label storyworldv2:
    scene v18054
    with dissolve
    yisnna "The world"
    yisnna "Very well, let me show you something"
    "She shows you a map"
    scene worldmap
    with dissolve
    yisnna "First of all this map is outdated"
    yisnna "Some of the borders might gave changed"
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
    if libraryv39 == 0:
        jump v2library
    else:
        jump v39libraryknow

label throneroomcollegev2:
    scene throne
    with dissolve
    MC "Nothing to see here"
    MC "Let's go back"
    jump hallv2

label classroomcollegev2:
    scene classroommiss
    with dissolve
    if foundbookv2 == False:
        scene classroommiss
        with dissolve
        MC "Nobody's here, is it lunch time?"
        MC "Should I look around?"
        menu:
            "[abgreen]Yes":
                $ foundbookv2 = True
                "You search around the classroom"
                $ dice = renpy.random.randint(1, 6)

                if dice == 1:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Magic and Fire?"
                    "Your Battlemagic increased"
                    $ Destpoints += 1
                    jump classroomcollegev2

                elif dice == 2:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of the Illusionist?"
                    "Your Illusion increased"
                    $ Iluspoints += 1
                    jump classroomcollegev2

                elif dice == 3:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of the Cure?"
                    "Your Healing increased"
                    $ Healpoints += 1
                    jump classroomcollegev2

                elif dice == 4:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Dispel?"
                    "Your Mysticism increased"
                    $ Mystpoints += 1
                    jump classroomcollegev2

                elif dice == 5:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Creatures of the void?"
                    "Your Summoning increased"
                    $ Summpoints += 1
                    jump classroomcollegev2

                elif dice == 6:
                    show openbook
                    with dissolve
                    "You found a book"
                    MC "Manual of Transmutation?"
                    "Your Alteration increased"
                    $ Altepoints += 1
                    jump classroomcollegev2
            "No, let's get out":

                jump hallv2
    else:
        scene classroommiss
        with dissolve
        MC "I have nothing else to do here"
        jump hallv2

label aynaroomv2:
    scene collegeblue
    with dissolve
    MC "I shouldn't go there"
    MC "It's the Archmage's private quarters"
    jump hallv2

label liliroomcollegev2:
    if liliroomv2 == False:
        $ liliroomv2 = True
        scene v2015
        with dissolve
        "You arive at Liliana's room"
        "She looks scared, or sad maybe, you can't tell"
        MC "Is everything ok?"
        scene v2016
        with dissolve
        "With a surprised look"
        lili "Oh.. I didn't see you there"
        MC "Are you ok?"
        lili "Yes, I'm fine, why wouldn't I be?"
        MC "You look worried, I was concerned"
        scene v2017
        with dissolve
        lili "Do I? I'm fine thank you"
        lili "I was just... Thinking of something"
        MC "Nothing bad I hope"
        lili "No, it's ok"
        lili "Some stuff that happened to me"
        menu:
            "Well a pretty girl looks prettier with a smile[ablovecolor] [abaffection]":
                scene v2018
                with dissolve
                "Her expression changed to a smile"
                lili "What a charming young man you are"
                "Liliana affection increased"
                $ lili_affection = 1
                MC "Well I don't like to see pretty girls sad"
                lili "Thank you..."
                lili "I'll be alright. Now could I ask you to leave?"
                scene v2020
                with dissolve
                lili "I think I need to be alone for a while"
                MC "Sure... See you around"
                jump hallv2
            "Well, they say everyone get what they deserve":
                scene v2019
                with dissolve
                "Her expression changed"
                lili "I... You..."
                lili "You should leave now"
                $ lili_affection = 0
                "Liliana affection decreased"
                scene v2020
                with dissolve
                MC "Ok..."
                jump hallv2
    else:
        scene v2020
        with dissolve
        MC "I should leave her alone for now"
        jump hallv2



label courtyardv2:
    scene v2courtyard
    with dissolve
    "You arrive at the courtyard"
    MC "There are some people around here"
    call screen courtyardv2

label katrionav2:
    scene v2022
    with dissolve
    if talkwithkat == 0:
        katriona "Hello [MC], good job again on bringing that girl here"
        $ talkwithkat = 1
        MC "Hi Katriona"
        MC "Does that mean you realize how great I am now?"
        katriona "Hehehe, you've gained a lot of confidence, that's good for a Mage"
        katriona "Nothing like that scared little kid I brought home with me"
        katriona "Just don't let it get out of control"
        MC "Of course, I know my limits. By the way"
        MC "Do you happen to know where the Archmage is?"
        scene v2022a
        with dissolve
        "Her expression changed"
        katriona "I... Don't know..."
        MC "I was hoping that she would have something new for me to do"
        katriona "I haven't seen her since yesterday"
        menu:
            "[abgreen]I heard that she left the college early this morning" if darkelftalk == 1:
                MC "I heard that she left the college early this morning"
                katriona "Really? Maybe she went to meditate somewhere"
                katriona "Strange..."
                MC "What?"
                scene v2022
                with dissolve
                katriona "Oh, nothing..."
                katriona "Until she shows up you could go explore Allesterra"
                katriona "Or study magic and improve your skills..."
                MC "Yeah, thanks for your help"
                $ talkwithkat = 2
                jump courtyardv2

            "[abgreen]I heard that she left the college early this morning" if darkelftalk == 2:
                MC "I heard that she left the college early this morning"
                katriona "Really? Maybe she went to meditate somewhere"
                katriona "Strange..."
                MC "What?"
                scene v2022
                with dissolve
                katriona "Oh, nothing..."
                katriona "Until she shows up you could go explore Allesterra"
                katriona "Or study magic and improve your skills..."
                MC "Yeah, thanks for your help"
                $ talkwithkat = 2
                jump courtyardv2
            "Me neither":

                MC "I have no ideia where she is"
                katriona "Maybe she's meditating somewhere"
                MC "Then why are you worried?"
                scene v2022
                with dissolve
                katriona "I'm not hehehe"
                katriona "Until she shows up you could go explore Allesterra"
                katriona "Or study magic and improve your skills..."
                MC "Yeah, I should do that"
                jump courtyardv2

    elif talkwithkat == 2:
        scene v2022
        with dissolve
        katriona "Hey, you're back"
        katriona "I asked around and you were right"
        katriona "The Archmage went out this morning"
        MC "And everything is fine?"
        katriona "Yeah she probably left the college to meditate"
        MC "Ok, I should go"
        katriona "See you around"
        $ talkwithkat = 3
        jump courtyardv2
    else:

        scene v2022
        with dissolve
        katriona "Hey, you're back"
        katriona "Have you started to explore Allesterra?"
        MC "Not yet"
        katriona "Are you afraid of the outside world?"
        katriona "Ahahaha"
        MC "No... I'm just looking around here first"
        katriona "Sure sure..."
        MC "I should go"
        katriona "See you around"
        jump courtyardv2

label enainav2:
    scene v2023
    with dissolve
    MC "That's the elven princess"
    MC "What did Ynissa say her name was? Enainia?"
    MC "Should I try to speak with her?"
    MC "I remember what she did to Jessica at the presentation..."
    menu:
        "[abgreen]Yes":
            if talkwithenainia == False:
                MC "Come on [MC] what's the worst that could happen?"
                MC "Hello..."
                scene v015095
                with dissolve
                MC "(Holy shit, she's beautiful)"
                enainia "Hello"
                MC "Are you enjoying your stay here at the College?"
                enainia "It's alright, but there is too much stone and smoke for my tastes"
                MC "Is the enviroment much different in your homeland?"
                enainia "My homeland...Yes... What's left of it anyway..."
                enainia "Damned Slayers..."
                enainia "Hmm... What's your name?"
                MC "I'm [MC] pleasure to meet you"
                enainia "I'm Princess Enainia, ruler of Lilmehil"
                MC "Lilmehil? Is that a nation?"
                enainia "No, it's one of the seven kingdoms of Elvaria"
                enainia "I mean... Was..."
                enainia "Each of them were ruled by my brothers and sisters"
                enainia "And my Mother, Queen Lufina, was the ruler of the nation"
                MC "It sounds wonderful...but you said it's not like that anymore?"
                enainia "More than half of Elvaria has been lost to the Slayers"
                enainia "They have been attacking us for about 20 years now"
                enainia "Us... and so many others... I guess"

                MC "Well... I should probably be on my way now"
                MC "With your permission Princess"
                enainia "Of course, good day [MC]"
                $ talkwithenainia = True
                jump courtyardv2
            else:
                scene v015095
                with dissolve
                enainia "Hello again, [MC]"
                enainia "Was there something that you needed?"
                MC "Oh no, I was just passing by"
                enainia "Ok farewell then"
                jump courtyardv2
        "No":


            MC "Maybe I should stay away from her"
            MC "I don't want a pissed elf princess after me"
            jump courtyardv2

label rerlvamv02:
    scene v2021
    with dissolve
    if talkwithrev == False:
        prof "Hi there [MC]"
        MC "Hi professor"
        if darkelftalk == 2:
            prof "I saw you earlier"
            MC "Yes I saw you too"
            MC "You were with Mistress Silvana in the garden"
            MC "Are you trying to seduce her?"
            scene v015093
            with dissolve
            prof "What?! no..."
            MC "Oh come on, don't tell me you feel nothing for her"
            MC "I mean, she's quite attractive"
            scene v2021
            with dissolve
            prof "How dare you insinuate such a thing?"
            prof "I think you should leave now [MC]"
            $ talkwithrev = True
            jump courtyardv2
        else:
            prof "How is our top student today?"
            MC "I'm fine Professor"
            MC "See you around"
            prof "Have a good day"
            $ talkwithrev = True
            jump courtyardv2
    else:
        scene v2021
        with dissolve
        MC "I shouldn't bother him again"
        jump courtyardv2

label stairsv2:
    scene v2courtyard
    with dissolve
    MC "That's the entrance for the Mages quarters"
    MC "I shouldn't go there without a reason"
    jump courtyardv2

label alesterramapv2:
    scene v2courtyard
    with dissolve
    "You are about to leave the college"
    "Do you want to leave now?"
    menu:
        "[abgreen]Yes":
            jump v2islandmap
        "No":
            jump courtyardv2

label v2islandmap:
    scene allesterra
    call screen allesterramapv2

label collegeallesterrav2:
    "Back to the college"
    jump courtyardv2

label shipallesterrav2:
    "I need to pass through the city before I can reach the docks"
    jump v2islandmap

label villageallesterrav2:
    "You're at the village"
    if thugvillagev2 == 0:
        scene v2villagethug00
        with dissolve
        MC "There are some villagers around"
        call screen villagethugv2
    else:
        scene v2villagenothug00
        with dissolve
        MC "There are some villagers around"
        call screen villagenothugv2


label hannawritterv2:
    if hannatalk == 0:
        scene v2044
        with dissolve
        MC "Who is that?"
        MC "Hello"
        hanna "Hello"
        MC "Is everything ok?"
        hanna "Yes... Why do you ask?"
        MC "Well, you don't look like you're from around here"
        MC "I thought you might be lost or stranded"
        scene v2045
        with dissolve
        hanna "I am not from around here... Good eye"
        hanna "I'm Hanna Roinestad, have you heard about me?"
        MC "Sorry, but no..."
        scene v2044
        with dissolve
        hanna "I'm a famous writer, I came here so I could get away from the city"
        hanna "And to write a new book, I thought that the peace and calm here would help..."
        MC "You don't seem convinced..."
        scene v2047
        with dissolve
        hanna "Hehehe, you are right, I lack ideas..."
        hanna "But hey, you don't seem to belong here either"
        MC "I don't... I'm [MC] and I'm a mage..."
        scene v2046
        with dissolve
        hanna "A mage?! From the College of Allesterra?"
        MC "Yes, exactly"
        $ hannatalk = 1
        $ nextstagev2 += 1
        scene v2047
        with dissolve
        hanna "That's great! Maybe you can tell me about your life"
        hanna "It might be just what I need to brainstorm ideas"
        MC "I...Don't know..."
        hanna "I'll even pay you for your time, what do you say?"
        menu:
            "[abgreen]It's a deal!":
                $ hannadealv2 = 1
                $ nextstagev2 += 1
                scene v2045
                with dissolve
                hanna "That's great!!"
                jump hannastoriesv2
            "I'm sorry but no":

                scene v2044
                with dissolve
                hanna "Oh...Ok..."
                hanna "Maybe some other time?"
                jump villageallesterrav2
    else:
        scene v2044
        with dissolve
        hanna "Hello again [MC]"
        if hannadealv2 == 0:
            hanna "Have you changed your mind?"
            hanna "Want to tell me some stories?"
            menu:
                "[abgreen]Yes I will":
                    $ hannadealv2 = 1
                    $ nextstagev2 += 1
                    scene v2045
                    with dissolve
                    hanna "That's great!!"
                    jump hannastoriesv2
                "No, sorry":
                    scene v2044
                    with dissolve
                    hanna "Oh...Ok..."
                    hanna "Maybe some other time?"
                    jump villageallesterrav2
        else:
            jump hannastoriesv2

label hannastoriesv2:
    scene v2045
    with dissolve
    menu:
        "Tell her about your village and the attack[abgreen] [abgold10]" if hannamiss1 == 0:
            "You tell her what happened to your village, well as much you know"
            $ hannamiss1 = 1
            $ nextstagev2 += 1
            scene v2046
            with dissolve
            hanna "That's terrible! How did you survive?"
            MC "The Mages at the College found me"
            MC "But I can't really remember what happened"
            MC "That's just what I've been told..."
            scene v2047
            with dissolve
            hanna "I'm glad things turned out so well for you"
            scene v2045
            with dissolve
            hanna "As promised here is your payment"
            $ Gold += 10
            play sound "sounds/Coin.ogg"
            "You received 10 Gold"
            MC "Thank you"
            jump hannastoriesv2

        "Tell her about the imp that possessed the farmer[abgreen] [abgold10]" if hannamiss2 == 0:
            "You tell her about the mission and the imp"
            $ hannamiss2 = 1
            $ nextstagev2 += 1
            scene v2046
            with dissolve
            hanna "That's amazing! Imps...."
            MC "Yeah... Weird creatures"
            hanna "That gives me an idea..."

            scene v2047
            with dissolve
            hanna "That's really got me thinking, thank you"
            scene v2045
            with dissolve
            hanna "As promised here is your payment"
            play sound "sounds/Coin.ogg"
            $ Gold += 10
            "You received 10 Gold"
            MC "Thank you"
            jump hannastoriesv2

        "Tell her about your village (Lie)[abgreen] [abgold10]" if hannamiss1 == 0:
            "You tell her a lie about your origins"
            $ hannamiss1 = 1
            $ nextstagev2 += 1
            scene v2046
            with dissolve
            hanna "That's amazing! So you were born to be a Mage?"
            MC "Yes, as soon as I could walk the Mages started to train me"
            MC "I've fought so many creatures already..."
            MC "Maybe I can tell you about it some other time"
            scene v2047
            with dissolve
            hanna "Wow, you must be amazing"
            scene v2045
            with dissolve
            hanna "As promised here is your payment"
            play sound "sounds/Coin.ogg"
            $ Gold += 10
            "You received 10 Gold"
            MC "Thank you"
            jump hannastoriesv2

        "Tell her about the imp (Lie)[abgreen] [abgold10]" if hannamiss2 == 0:
            "You tell her a lie about the imp"
            $ hannamiss2 = 1
            $ nextstagev2 += 1
            scene v2046
            with dissolve
            hanna "That's amazing! Imps...."
            MC "Yeah... Weird creatures, but no match for me"
            hanna "That gives me an idea..."

            scene v2047
            with dissolve
            hanna "That's really got me thinking, thank you"
            scene v2045
            with dissolve
            hanna "As promised here is your payment"
            play sound "sounds/Coin.ogg"
            $ Gold += 10
            "You received 10 Gold"
            MC "Thank you"
            jump hannastoriesv2
        "Ask about her":

            MC "Can you tell me more about you?"
            scene v2046
            with dissolve
            hanna "About me? ok..."
            scene v2047
            with dissolve
            hanna "I'm Hanna Roinestad and I'm a writer"
            hanna "I like to travel all around Ataegina"
            hanna "Discover new cultures and Nations"
            hanna "Write real stories about real people"
            scene v2045
            with dissolve
            hanna "I was starting to think that coming here was a mistake"
            hanna "But thank God you showed up"
            jump hannastoriesv2
        "Leave":

            MC "I need to go"
            hanna "Bye!"
            jump villageallesterrav2

label villageelderv2:
    if elderv2 == 0:
        scene v2048
        with dissolve
        $ elderv2 = 1
        $ nextstagev2 += 1
        MC "Let's talk with that old woman"
        MC "Hello"
        elder "Hello young man"
        elder "What brings you to our village?"
        MC "I'm exploring Allesterra"
        scene v2049
        with dissolve
        elder "Ah... young people..."
        elder "When I was younger I also enjoyed traveling"
        scene v2048
        with dissolve
        elder "Now... I'm too old..."
        MC "I'm sure you can still travel if you really want"
        MC "No age should stop you from doing what you love"
        scene v2049
        with dissolve
        elder "Yes...Not only are you cute but you're also charming"
        elder "I wish I was younger, I would take very good care of you"
        elder "If you know what I mean.... Hehehe"
        MC "Uhmm... Right..."
        elder "I'm serious, I was the best at sucking cock"
        elder "I'm sure I can still do it"
        elder "What do you say?"
        MC "I... Uhm... Maybe another time..."
        elder "Hehehe, don't get all flushed on me"
        scene v2050
        with dissolve
        elder "Look around the village"
        elder "I'm sure there are plenty of people who can tell you all about me"
        MC "Thanks... Bye..."
        MC "(What the fuck was that?)"
        jump villageallesterrav2
    else:
        scene v2049
        with dissolve
        elder "Hello again young man"
        elder "Have you returned because of my offer?"
        MC "Hi... Uhmm... maybe another time..."
        jump villageallesterrav2

label villagethugv2:
    scene v2038
    with dissolve
    MC "Those guys seem to be in a discussion"
    MC "Should I get closer?"
    menu:
        "[abgreen]Yes":
            MC "Let's see if I can eaves drop"
            scene v2038
            with dissolve
            thug "That's my last warning!!"
            thug "If you want to keep your hands, you shall give me the gold"
            jack "But I don't have it yet..."
            thug "I don't care! Lord Runar wants his gold back"
            thug "You... What?"
            scene v2039
            with dissolve
            thug "What are you looking at asshole?!"
            menu:
                "Nothing, sorry to intrude":
                    thug "Get lost!!"
                    jump villageallesterrav2
                "[abgreen]Some kind of animal I'm sure...":

                    $ thugvillagev2 = 1
                    $ nextstagev2 += 1
                    thug "Some kind of.... What?! Do you know who I am?"
                    thug "Do you have a death wish?"
                    MC "Do you think it wise to talk that way to a Mage?"
                    scene v2040
                    with dissolve
                    "They look surprised"
                    thug "A Mage? Mages don't bother with other people's business"
                    MC "Do you really want to find out?"
                    thug "I... "
                    scene v2038
                    with dissolve
                    thug "I'll be back for the gold"
                    menu:
                        "Say nothing to the thug":
                            scene v2041
                            with dissolve
                            "The thug went away"
                            scene v2042
                            with dissolve
                            jack "Thank you, he was about to break my hands"

                            jack "What is your name my savior?"
                            MC "I'm [MC]"
                            jack "[MC] the Great Mage!!"
                            jack "Are you really a Mage?"
                            MC "Yes I am, so what was that about? Something about gold?"
                            scene v2043
                            with dissolve
                            jack "I... Asked for gold from Lord Runar to buy equipment..."
                            jack "But some thieves stole my equipment"
                            jack "Now I can't work to pay him back..."
                            menu:
                                "[abgreen]I will help you":
                                    MC "I will help you get your equipment back"
                                    $ helpjackv2 = 1
                                    scene v2042
                                    with dissolve
                                    jack "You will? Thank you!"
                                    MC "You have any idea where those thieves are?"
                                    jack "No I'm sorry. One day I arrived home and everything was gone"
                                    MC "Hmmm alright, and where can I find that Lord Runar?"
                                    jack "He lives in the city, Allesterra city"
                                    MC "Ok I will return when I have news"
                                    jack "Goodbye and thank you"
                                    jump villageallesterrav2
                                "That's too bad":

                                    MC "That's too bad"
                                    jack "What will I do now?"
                                    jump villageallesterrav2
                        "[abgreen]Gold you say?":

                            scene v2039
                            with dissolve
                            $ helpthugv2 = 1
                            thug "Yes... Gold...Are you interested?"
                            MC "I might be... "
                            thug "Meet Lord Runar at the city, I'm sure he will...hmm"
                            thug "Have a job for someone like you..."
                            MC "Great, I'll meet him later then"
                            thug "Yeah great, see you there..."
                            scene v2041
                            with dissolve
                            "The thug went away"
                            scene v2042
                            with dissolve
                            jack "Thank you, he was about to break my hands"

                            jack "What is your name my savior?"
                            MC "I'm [MC]"
                            jack "[MC] the Great Mage!!"
                            jack "Are you really a Mage?"
                            MC "Yes I am, so what was that about? Something about gold?"
                            scene v2043
                            with dissolve
                            jack "I... Asked for gold from Lord Runar to buy equipment..."
                            jack "But some thieves stole my equipment"
                            jack "Now I can't work to pay him back..."
                            menu:
                                "[abgreen]I will help you":
                                    MC "I will help you get your equipment back"
                                    $ helpjackv2 = 1
                                    scene v2042
                                    with dissolve
                                    jack "You will? Thank you!"
                                    MC "You have any idea where those thieves are?"
                                    jack "No I'm sorry. One day I arrived home and everything was gone"
                                    MC "Hmmm alright, and where can I find that Lord Runar?"
                                    jack "He lives in the city, Allesterra city"
                                    MC "Ok I will return when I have news"
                                    jack "Goodbye and thank you"
                                    jump villageallesterrav2
                                "That's too bad":

                                    MC "That's too bad, and it's not my problem"
                                    jack "What will I do now?"
                                    jump villageallesterrav2
        "No, let's get back":


            MC "I don't want any problems"
            jump villageallesterrav2


label villagenothugv2:
    if helpjackv2 == 1:
        scene v2042
        with dissolve
        jack "So, have you found my stuff?"
        MC "No not yet"
        jack "Ok, thank you for helping me"
        jump villageallesterrav2
    else:
        scene v2043
        with dissolve
        jack "What will I do now? They will kill me..."
        menu:
            "[abgreen]I will help you":
                MC "I will help you get your equipment back"
                $ helpjackv2 = 1
                scene v2042
                with dissolve
                jack "You will? Thank you!"
                MC "You have any idea where those thieves are?"
                jack "No I'm sorry. One day I arrived home and everything was gone"
                MC "Hmmm alright, and where can I find that Lord Runar?"
                jack "He lives in the city, Allesterra city"
                MC "Ok I will return when I have news"
                jack "Goodbye and thank you"
                jump villageallesterrav2
            "That's too bad":

                MC "That's too bad and it's not my problem"
                jack "What will I do now?"
                jump villageallesterrav2



label cityallesterrav2:
    scene v2051
    with dissolve
    "You are at the city gates"
    menu:
        "[abgreen]Talk with the guard":
            MC "Let's talk with the guard"
            if citygatev2 == 0:
                scene v2052
                with dissolve
                $ citygatev2 = 1
                $ nextstagev2 += 1
                sol "Hail citizen"
                sol "What is your business in the city?"
                menu:
                    "Just visiting":
                        sol "Only people with official documentation can pass"
                        sol "Do you have any?"
                        MC "No..."
                        sol "Goodbye then"
                        jump cityallesterrav2
                    "I want to talk to Lord Runar":

                        sol "Do you have official documentation?"
                        MC "No..."
                        sol "Goodbye then"
                        jump cityallesterrav2
                    "I have an important mission in the city":

                        sol "Do you have official documentation?"
                        MC "No..."
                        sol "Goodbye then"
                        jump cityallesterrav2
                    "Nothing I'm leaving":

                        jump cityallesterrav2
            else:
                scene v2052
                with dissolve
                sol "You again!"
                sol "What is your business in the city?"
                menu:
                    "Just visiting":
                        sol "Only people with official documentation can pass"
                        sol "Do you have any?"
                        MC "No..."
                        sol "Goodbye then"
                        jump cityallesterrav2

                    "I want to talk to Lord Runar" if helpjackv2 == 1:
                        sol "Do you have official documentation?"
                        MC "No..."
                        sol "Goodbye then"
                        jump cityallesterrav2
                    "I have an important mission in the city":

                        sol "Do you have official documentation?"
                        MC "No..."
                        sol "Goodbye then"
                        jump cityallesterrav2
                    "Nothing I'm leaving":

                        jump cityallesterrav2
        "[abgreen]Look around":

            if foundwalletv2 == 0:
                $ dice = renpy.random.randint(10, 25)
                show goldcoins
                with dissolve
                play sound "sounds/Coin.ogg"
                "You found a lost wallet with [dice] goldcoins"
                $ Gold = Gold + dice
                MC "Nice"
                $ foundwalletv2 = 1
                $ nextstagev2 += 1
                jump cityallesterrav2
            else:
                MC "I found nothing here..."
                jump cityallesterrav2
        "Leave":

            MC "I should leave"
            jump v2islandmap

label craterallesterrav2:
    scene crater
    with dissolve
    MC "There's nothing to see here."
    MC "At least I'm not fainting this time"
    jump v2islandmap


label farmallesterrav2:
    scene farmmission1
    with dissolve
    "You are at the farm"
    scene v2024
    with dissolve
    "You see the old man and his daughter"
    menu:
        "[abgreen]Go talk with them":
            if farmgirlv2 == 0:
                scene v2024
                with dissolve
                MC "Hello there"
                $ farmgirlv2 = 1
                $ nextstagev2 += 1
                oldman "Hello Young Mage"
                oldman "Glad to see you back and that you're ok"
                oldman "I have to thank you Mages for bringing my little girl back"
                karelia "You are one of the Mages?"
                if savedgirl == True:
                    karelia "I remember... You saved me from a bear..."
                    MC "You remember that?"
                    MC "Weren't you unconscious?"
                    karelia "I was... But somehow I do remember..."
                    karelia "I saw you arrive and shout, but then everything went blank"
                    karelia "Until I woke up in the College"
                    MC "I'm just glad you're ok"
                    scene v2027
                    with dissolve
                    karelia "I'm great, thanks to you"
                    karelia "My savior..."
                    karelia "Dad, can you get something for him to eat?"
                    oldman "Sure sure...."
                    scene v2028
                    with dissolve
                    "The old man left you and the girl alone"
                    scene v2029
                    with dissolve
                    karelia "They told me that your name is [MC]"
                    MC "That's correct"
                    karelia "My savior [MC]! I have a reward for you"
                    scene v2031
                    with dissolve
                    karelia "Come with me please"
                    MC "Ok..."
                    scene v2032
                    with dissolve
                    karelia "I think that your reward should be a kiss, what do you think?"
                    menu:
                        "[abgreen]I'm sorry I have a girlfriend":
                            karelia "And? I'm not going to tell anyone"
                            scene v2033
                            with dissolve
                            karelia "Kiss me!"
                            menu:
                                "[abgreen]Kiss her":
                                    MC "Ok"
                                    scene v2034
                                    with dissolve
                                    "You kiss her lips, you can taste something sweet"
                                    "Like blackberries or something"
                                    scene v2032
                                    with dissolve
                                    karelia "You are a good kisser"
                                    karelia "Don't worry, I won't tell your girlfriend"
                                    karelia "Let's get back before my dad comes looking for us"
                                    MC "I should probably get going actually"
                                    scene v2037
                                    with dissolve
                                    karelia "Sure come visit me again"
                                    karelia "Bye"
                                    $ farmgirlv2 = 2
                                    jump v2islandmap
                                "Don't kiss her":

                                    MC "I can't, I have a girlfriend and I respect her"
                                    karelia "She is a lucky girl"
                                    MC "I guess, I should leave"
                                    karelia "Sure come visit me again"
                                    karelia "Bye"
                                    jump v2islandmap
                        "I think it's a good idea":

                            scene v2033
                            with dissolve
                            karelia "Then come here!"
                            MC "Ok"
                            scene v2034
                            with dissolve
                            "You kiss her lips, you can taste something sweet"
                            "Like blackberries or something"
                            scene v2032
                            with dissolve
                            karelia "You are a good kisser"
                            karelia "We'll have to do that again later"
                            karelia "Let's get back before my dad comes looking for us"
                            MC "I should probably get going actually"
                            scene v2037
                            with dissolve
                            karelia "Sure come visit me again"
                            karelia "Bye"
                            $ farmgirlv2 = 2
                            jump v2islandmap
                else:

                    karelia "I've been told that someone named Katarro found me"
                    menu:
                        "I'm Katarro[abred] [abnoalignment]":
                            $ Points -= 1
                            "You got -1 Point"
                            karelia "They said Katarro is an elf"
                            menu:
                                "He is, I was kidding":
                                    karelia "Oh... Ok..."
                                    MC "I should leave"
                                    jump v2islandmap
                                "Use Illusion to charm her[abred] [abnoalignment]":

                                    $ Points -= 1
                                    "You got -1 Point"
                                    if Iluspoints >= 3:
                                        "Your spell is a success"
                                        karelia "Yes... I think I... Remember you..."
                                        karelia "Yes... You saved me!"
                                        scene v2027
                                        with dissolve
                                        karelia "Dad, leave us now"
                                        oldman "Hmm.. OK.."
                                        scene v2030
                                        with dissolve
                                        karelia "I... Need to thank you"
                                        MC "Yes... Let's go somewhere else"
                                        scene v2031
                                        with dissolve
                                        karelia "Come with me"
                                        scene v2035
                                        with dissolve
                                        karelia "You want a kiss my savior?"
                                        menu:
                                            "Yes, I deserve it":
                                                scene v2034
                                                with dissolve
                                                "She kissed you"
                                                scene v2035
                                                with dissolve
                                                karelia "You are my savior, I owe you..."
                                                scene v2032
                                                with dissolve
                                                karelia "My head hurts..."
                                                karelia "I... Need to go..."
                                                "You decided to leave the farm too"
                                                $ farmgirlv2 = 3
                                                jump v2islandmap
                                            "A kiss? don't you have some gold?[abgreen] [abgold2]":


                                                karelia "Gold? Yes... I have some gold..."
                                                MC "Then give it to me"
                                                karelia "Of course... Here, it's all I have"
                                                play sound "sounds/Coin.ogg"
                                                "You received 2 gold coins"
                                                $ Gold += 2
                                                MC "That's it? 2 gold coins?"
                                                scene v2032
                                                with dissolve
                                                karelia "My head hurts..."
                                                karelia "I... Need to go..."
                                                "You decided to leave the farm too"
                                                $ farmgirlv2 = 4
                                                jump v2islandmap
                                    else:



                                        "Your spell failed"
                                        karelia "I'm sure I heard it right"
                                        MC "Damn..."
                                        MC "I should leave"
                                        jump v2islandmap
                        "In fact I'm the one who saved you":


                            karelia "They said it was an elf who saved me"
                            menu:
                                "Yes Katarro is an elf, I was kidding":
                                    karelia "Oh...Ok..."
                                    MC "I should leave"
                                    jump v2islandmap
                                "Use Illusion to charm her[abred] [abnoalignment]":

                                    $ Points -= 1
                                    "You got -1 Point"
                                    if Iluspoints >= 3:
                                        "Your spell is a success"
                                        karelia "Yes... I think I... Remember you..."
                                        karelia "Yes... You saved me!"
                                        scene v2027
                                        with dissolve
                                        karelia "Dad, leave us now"
                                        oldman "Hmm.. OK.."
                                        scene v2030
                                        with dissolve
                                        karelia "I... Need to thank you"
                                        MC "Yes... Let's go somewhere else"
                                        scene v2031
                                        with dissolve
                                        karelia "Come with me"
                                        scene v2035
                                        with dissolve
                                        karelia "You want a kiss my savior?"
                                        menu:
                                            "Yes, I deserve it":
                                                scene v2034
                                                with dissolve
                                                "She kissed you"
                                                scene v2035
                                                with dissolve
                                                karelia "You are my savior, I owe you..."
                                                scene v2032
                                                with dissolve
                                                karelia "My head hurts..."
                                                karelia "I... Need to go..."
                                                "You decided to leave the farm too"
                                                $ farmgirlv2 = 3
                                                jump v2islandmap
                                            "A kiss? don't you have gold?[abgreen] [abgold2]":


                                                karelia "Gold? Yes... I have some gold..."
                                                MC "Then give it to me"
                                                karelia "Of course... Here, it's all I have"
                                                play sound "sounds/Coin.ogg"
                                                "You received 2 gold coins"
                                                $ Gold += 2
                                                MC "That's it? 2 gold coins?"
                                                scene v2032
                                                with dissolve
                                                karelia "My head hurts..."
                                                karelia "I... Need to go..."
                                                "You decided to leave the farm too"
                                                $ farmgirlv2 = 4
                                                jump v2islandmap
                        "Yes Katarro found you on the forest":

                            MC "Master Katarro found you and then Katriona healed you"
                            scene v2026
                            with dissolve
                            karelia "Yes I remember her, she is so sweet and funny"
                            MC "Well, I should go"
                            karelia "Bye"
                            oldman "See you Young Mage"
                            jump v2islandmap
            else:


                scene v2025
                with dissolve
                oldman "Oh, you're back"
                oldman "You need something?"
                MC "No I'm fine, just passing by"
                "You left the farm"
                jump v2islandmap
        "Leave":




            jump v2islandmap


label dockallesterrav2:
    scene v2053
    with dissolve
    "You are at a small dock"
    if dwarfv2 == 0:
        MC "Is that a dwarf?"
        "You get closer"
        scene v2054
        with dissolve
        dwarf "Who the fuck are ya?"
        dwarf "And what the fuck are ya doing here?"
        MC "I'm [MC], I was just passing by"
        dwarf "Passing by? What the fuck? "
        dwarf "Don't bother me, I need to concentrate on me fishin"
        MC "Do you live here?"
        $ dwarfv2 = 1
        $ nextstagev2 += 1
        scene v2055
        with dissolve
        dwarf "What do ya think? Of course I fucking live here"
        dwarf "Why the stupid question?"
        MC "I just find it unusual to find a dwarf here"
        dwarf "I just find it unusual bla bla bla..."
        scene v2056
        with dissolve
        dwarf "If those fucking bastards hadn't destroyed our city..."
        dwarf "I wouldn't be here in this fucking place"
        dwarf "A great blacksmith like me is now a lowly fisherman..."
        dwarf "Fucking Slayers...."
        MC "Slayers?"
        dwarf "Yeah yeah.... Fucking Slayers, they found the entrance to our mountain"
        dwarf "And destroyed our city, only a few of us managed to escape"
        dwarf "I have no idea where the survivors are though"
        dwarf "Haven't seen another dwarf for about 20 years"
        MC "20 years? When was your mountain attacked?"
        scene v2055
        with dissolve
        dwarf "About 25 years ago I guess..."
        MC "I never heard of such thing"
        dwarf "That's because nobody cares about us, nor do we care about them."
        dwarf "I need to get me lunch, ya should leave now"
        MC "Ok then..."
        "You left the small dock"
        jump v2islandmap
    else:

        scene v2054
        with dissolve
        dwarf "What do ya want?"
        dwarf "I'm busy ya know?"
        MC "Sorry, I'll return later"
        dwarf "Yeah yeah... Fucking kids..."
        "You left the small dock"
        jump v2islandmap


label forestallesterrav2:
    scene forestmap
    with dissolve
    "You are at the forest"
    menu:
        "Look around":
            "You look around, being careful to watch for bears."
            "There's nothing here"
            jump forestallesterrav2
        "[abgreen]Leave":

            jump v2islandmap

label montainallesterrav2:
    "Let's check Mount frost"

    if nextstagev2 <= 9:

        if talkwithstrangev2 == 0:
            scene v2057
            with dissolve
            MC "That's the Mage from before"
            MC "Should I go talk to him?"
            menu:
                "[abgreen]Yes":
                    $ talkwithstrangev2 = 1
                    scene v2057
                    with dissolve
                    MC "Well, he asked me to come here..."
                    scene v2058
                    with dissolve
                    stman "So... You decided to meet me"
                    MC "Yes, last time you said I could find you here"
                    stman "I did..."
                    stman "And if what if this was a trap?"
                    MC "Um..."
                    stman "Don't worry, it's not"
                    stman "You... I..."
                    scene v2059
                    with dissolve
                    stman "I feel a great power hidden in you"
                    stman "And I feel that you..."

                    if Points >= 3:
                        stman "Follow the path of good"
                    elif Points <= -3:
                        stman "Follow the path of evil"
                    else:
                        stman "Are quite neutral in your actions"

                    MC "Is that a problem?"
                    scene v2058
                    with dissolve
                    stman "No, I don't really care what you do"
                    stman "Your destiny is already written"
                    stman "So, it is what it is..."
                    MC "Ok, so... What now?"
                    stman "Now I'm going to leave"
                    stman "You can find me at the top of the mountain"
                    stman "There, I will teach you how to use your power"
                    MC "My power?"

                    scene v2060
                    with dissolve
                    "Before saying anything else, the Mage disappeared"
                    MC "Where did he go?"
                    MC "I'll return later when I'm ready"
                    $ nextstagev2 += 1

                    jump v2islandmap
                "No, I'm out of here":


                    MC "This is probably a trap"
                    jump v2islandmap
        else:

            scene v2061
            with dissolve
            MC "Damn there is a blizzard around the mountain"
            MC "What a bizarre phenomenon, is this magic?"
            MC "I'll should turn back"
            jump v2islandmap
    else:

        scene v2060
        with dissolve
        MC "The blizzard is over"
        MC "Should I try to find that mage?"
        "By trying to find the mage you will go to the next part of the game"
        "If you want to keep exploring do not go yet"
        "Do you want to look for the mage?"
        menu:
            "[abgreen]Yes":
                MC "Let's try to find him then"
                jump mountainclimbv2
            "No":
                MC "Nah... There is something else I need to do"
                jump v2islandmap




label mountainclimbv2:
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v2060
    with dissolve
    "You decide to look around for a while"
    MC "Wow look at those caves"
    scene v2062
    with dissolve
    MC "They're made from pure ice..."
    "You start to feel a chill"
    MC "Is it starting to snow?"
    scene v2063
    with dissolve
    MC "It is... Let's hope that storm doesn't start up again"
    "As soon as you finished your sentence..."
    scene v2064
    with dissolve
    MC "Shit... I can't see a thing, I need to find shelter"
    MC "Or I will freeze to death out here"
    menu:
        "[abgreen]Get inside the cave":
            MC "I should take cover inside"
            jump caveinteriorv2
        "Keep walking around":
            MC "Let's keep looking"
            scene v2061
            with dissolve
            MC "I think I'm lost... I'm... So... cold..."
            MC "Shit I'm...freezing... I think that... I'm not going to..."
            show youaredead
            with dissolve
            "You froze to death, better luck next time"
            return
