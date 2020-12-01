
init:
    $ cerealove = 0
    $ cereacorr = 0
    $ cereadiscount = 0
    $ v42spellbookcount = 0
    $ lvl1v42altspell = 0
    $ lvl5v42desspell = 0
    $ lvl5v42sumspell = 0
    $ lvl5v42illspell = 0
    $ lvl5v42mysspell = 0
    $ lvl5v42heaspell = 0
    $ v42pricetag = 20
    $ v42pricetag2 = 50
    $ v42grabstone = 0
    $ v42firsttimespell = 0

label v42brothel:
    scene v4131
    with dissolve
    "You get close to the door"
    "It's locked"
    fvoice "What's the password?"
    MC "Phoenix"
    fvoice "Welcome"
    scene v4180
    with dissolve
    "You are inside the brothel"
    "You see Calessa inside and wonder if you should talk with her"
    show shotr
    with hpunch
    hide shotr
    Nonen "I like pussy as much as you do but we have other things to do"
    MC "Can't we..."
    show shotr
    with hpunch
    hide shotr
    MC "Hmmff... Ok..."
    Nonen "Good"
    "You leave the brothel"
    jump v4slayerplaza_1


label v42all:
    stop music
    play music "<loop 0.0>ingame.mp3"
    $ v42check = 1
    $ tavernhanna = 1
    scene v42013
    with dissolve
    if v4spentthenight == "tavern":
        scene black
        with dissolve
        scene v42000
        with dissolve
        MC "Yawn!"
        MC "Where the ...? Right... I'm in the tavern..."
        MC "My head... Damn... Also really I'm hungry..."
        MC "I should probably get going now"
        "You leave the room"
        scene v4141
        with dissolve
        MC "Looks exactly the same as yesterday"
        MC "Let's see if I can find something to eat"
        scene v4145
        with dissolve
        keeper "Morning"
        MC "Hi..."
        keeper "You got pretty drunk last night, how are you feeling?"
        MC "Good... I guess"
        keeper "Here, eat something. It'll help"
        MC "Thank you"
        scene black
        with dissolve
        scene v4145
        with dissolve
        "You eat some bread and cheese and you are ready to go"
        keeper "This one is on me, are you staying again?"
        MC "Thanks, I'm not sure yet, do you know if there are ships leaving today?"
        keeper "I don't know, if you wait long enough I'm sure you be able to get one"
        MC "Well, thank you anyway. See you later on"
        "You leave the tavern"
        jump cityv42
    else:


        scene black
        with dissolve
        scene v42013
        with dissolve
        MC "Yawn!"
        MC "Where the ...? Right... I'm in Hanna's place..."
        MC "My head... Damn... Also I'm really hungry..."
        MC "Where is she? She's not home?"
        scene v42014
        with dissolve
        MC "Hmm that looks good, did she left this here for me?"
        MC "There's also a note with something written"
        "You sit at the table and eat while reading the note"
        scene v42015
        with dissolve
        "{i}Dear [MC] I had to leave for a while to do research for my story."

        if v4spentthenight == "hannain" or v4spentthenight == "hannaout":
            "{i}I loved last night, we should try it again soon"
            MC "You're not the only one"
        else:
            "{i}You were very drunk last night, I hope you're feeling better"

        "{i} Don't forget to visit the docks, you never know when a ship will set sail"
        "{i} Hope to see you again soon, Hanna"
        MC "Well, let's finish this and take a look around the docks"
        "You finish your breakfast and leave the house"
        jump cityv42

label cityv42:
    jump v4slayercitymap


label v42slayerdocks:
    if v42dockvisit == 0:
        scene v42001
        with dissolve
        "When you arrive at the docks, you can see an old man talking with a Guard"
        "There is also a small boat, but it's definitely not large enough to get you home"
        "Since the ship is out of the question, you decide to listen in on the conversation"
        scene v42002
        with dissolve
        sol "Listen, it's not my fault your wares were kept this long."
        sol "We had orders from the capitol to delay your processing."
        oldman "Ah yes, I have no doubt..."
        oldman "I can just imagine that her magnificent bitchiness wanted to stop my business."
        sol "Watch yourself old man!!"
        sol "You will not speak ill of our Empress again..."
        sol "Or I will remove your tongue through your neck."
        scene v42003
        with dissolve
        oldman "No, peon, it's you who should watch who you're speaking to."
        "The old man waves his hand. You can see the ethereal light of a spell in his palm"
        oldman "Now... as you were saying?"
        scene v42004
        with dissolve
        sol "Oh... please forgive me sire"
        sol "I can't believe I could be so foolish as to talk to you in that way"
        oldman "You're forgiven, this time...."
        oldman "Now out of my sight you piece of Slayer filth."
        sol "Of course sir, please forgive me again..."
        scene v42005
        with dissolve
        "The old man turns his attention to his wares"
        "When suddenly he looks up, as if he noticed something, and turns your direction"
        scene v42006
        with dissolve
        "Adjusting his glasses, he peers at you as if he were looking through you"
        "A smirk crosses the old man's face as he waves you over"
        oldman "Well aren't you an interesting one. Quite powerful too it would seem"
        MC "I'm not sure what you mean"
        oldman "Oh... you don't fool me one bit."
        oldman "Not only are you powerful, you're also quite well trained"
        oldman "I'd wager you're from the Allesterian College. You're a long way from home"
        MC "How could you tell?"
        oldman "Oh, well when you have seen and done as much as I have..."
        oldman "You get to know quite a few things..."
        MC "So I saw. What was that spell you used on the Guard just now?"
        scene v42007
        with dissolve
        oldman "Caught that did you? Of course you did..."
        oldman "Hmm just a little Charm. He thought I was the Emperor"
        MC "It seemed more powerful than just a charm, I wouldn't mind learning that"
        oldman "Well then you happen to be in luck..."
        oldman "But before that, would you mind loading these crates into my cart?"
        scene v42008
        with dissolve
        "You nod and begin helping the old mage load his wares"
        oldman "So, tell me, what is your name?"
        MC "It's [MC], sir"
        scene v42009
        with dissolve
        bairn "Interesting. Well... my name is Bairn. I run the potion shop in town."
        bairn "I provide potions and tonics to the normal people of town"
        bairn "Just a hint of magic in them, not like any of them would know"
        bairn "But for someone as....unique as you..."
        bairn "There are much more useful things I could sell you..."
        bairn "Including some spell books you won't find anywhere else"
        MC "Well then, I'll be sure to stop by later while I'm still in town"
        scene v42010
        with dissolve
        "Bairn laughs a little to himself"
        bairn "Yes, you make sure you do"
        scene v42011
        with dissolve
        "Bairn begins pulling his cart away with strength someone his age shouldn't possess"
        scene v42012
        with dissolve
        MC "What a weird old man..."

        Nonen "Familiar...a familiar presence..."
        MC "What?!"
        MC "Hello....?"
        MC "Not sure why I keep trying to rely on you for help..."
        MC "Wait.... where'd that guard go? Huh... Oh well..."
        MC "Time to go I guess"
        $ v42magicshop = 1
        "As you get ready to leave..."
        mvoice "Hey you!! Stop!"
        scene v42135
        with dissolve
        MC "Hmm? Who are these guys now?"
        mvoice "Didn't you hear me? Stop!"
        scene v42136
        with dissolve
        thug "You have to pay the city toll"
        MC "City toll?"
        thug2 "Yes! City toll! You just arrived right? On a boat? So you pay the toll"
        MC "And you guys are what? Collection agents?"
        thug "Well of course, that's why we're here"
        MC "And the masks are for?"
        thug "None of your business. Now just shut up and pay or else"
        MC "Or else what exactly?"
        thug2 "We beat you senseless, and take the 50 Gold and whatever else we want"
        MC "You want me to pay you 50 gold!?"
        $ v42dockvisit = 1
        menu:
            "Pay them 50 gold" if Gold >= 50:
                MC "Sure..."
                scene v42137
                with dissolve
                $ Gold -= 50
                MC "There you go"
                play sound "sounds/coin.ogg"
                "You lost 50 gold"
                thug "Ahah see, glad you can be a reasonable fellow"
                thug2 "Yes... Let's go"
                scene v42138
                with dissolve
                thug "What a chump"
                thug2 "Ahahah"
                jump v4slayercitymap

            "Use illusion to mind trick them[abgreen] [abgold50]" if Iluspoints >= 0:
                MC "I think you should give me 50 gold"
                thug "We should... Give... You"
                scene v42137
                with dissolve
                thug "Yes... Here take it"
                $ Gold += 50
                play sound "sounds/coin.ogg"
                "You gained 50 gold"
                thug "Thank you"
                thug2 "Yes... thank you"
                MC "Now run around the city screaming -Punch me if you can-"
                scene v42140
                with dissolve
                thug "Punch me if you can!!"
                thug2 "Punch me first!!"
                MC "Wow, criminals are always so weak minded..."
                jump v4slayercitymap
            "Reason with them":


                MC "If you know what's good for you, you'll back off. I'm a Mage"
                thug "A mage?! Crap..."
                thug2 "Yeah... but if we beat him down and turn him in..."
                thug "Then they'll probably give us a reward... GET HIM!"
                scene v42141
                with dissolve
                $ companion = 0
                $ enemy = "v42thugs"
                jump combat
    else:
        scene v42012
        with dissolve
        "The dock is empty, there's nothing to do here"
        jump v4slayercitymap

label v42deadthugs:
    stop music
    play music "<loop 0.0>ingame.mp3"
    hide screen companions
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    scene v42139
    with dissolve
    MC "Greedy thugs, I tried to tell you..."
    $ Gold += 50
    play sound "sounds/coin.ogg"
    "You find 50 gold"
    jump v4slayercitymap

label v42magicshop:
    $ churchreadyv42 = 1
    if bairnform == 0:
        scene v42024
        with dissolve
        "You enter the magic shop"
        scene v42025
        with dissolve
        bairn "Oh it's you, come in my boy, come in."
        bairn "Now then, let me show you my unique collection of spells"
        jump spellchoice_shopv42
    else:
        jump checkbairnformv42


label spellchoice_shopv42:
    menu:
        "Level 1 spells":


            menu:
                "Alteration Spell, [v42pricetag] Gold {image=001alteration}" if lvl1v42altspell == 0:
                    if Gold >= v42pricetag:
                        $ lvl1v42altspell = 1
                        $ v42spellbookcount += 1
                        $ Gold -= v42pricetag
                        play sound "sounds/coin.ogg"
                        if v42firsttimespell == 0:
                            $ v42firsttimespell = 1
                            jump endspellchoice_shopv42
                        elif bairnform >= 2:
                            scene v42017
                            with dissolve
                        else:
                            scene v42026
                            with dissolve
                            jump endspellchoice_shopv42
                    else:
                        "You don't have enough gold"
                        jump spellchoice_shopv42
                "Back":
                    jump spellchoice_shopv42
        "Level 5 spells":



            menu:
                "BattleMagic Spell, [v42pricetag2] Gold {image=001battle}" if lvl5v42desspell == 0:
                    if Gold >= v42pricetag:
                        $ lvl5v42desspell = 1
                        $ v42spellbookcount += 1
                        $ Gold -= v42pricetag2
                        play sound "sounds/coin.ogg"
                        if v42firsttimespell == 0:
                            $ v42firsttimespell = 1
                            jump endspellchoice_shopv42
                        elif bairnform >= 2:
                            scene v42017
                            with dissolve
                            jump endspellchoice_shopv42_2
                        else:
                            scene v42026
                            with dissolve
                            jump endspellchoice_shopv42
                    else:

                        "You don't have enough gold"
                        jump spellchoice_shopv42

                "Summon Spell, [v42pricetag2] Gold {image=001summon}" if lvl5v42sumspell == 0:
                    if Gold >= v42pricetag:
                        $ lvl5v42sumspell = 1
                        $ v42spellbookcount += 1
                        $ Gold -= v42pricetag2
                        play sound "sounds/coin.ogg"
                        if v42firsttimespell == 0:
                            $ v42firsttimespell = 1
                            jump endspellchoice_shopv42
                        elif bairnform >= 2:
                            scene v42017
                            with dissolve
                            jump endspellchoice_shopv42_2
                        else:
                            scene v42026
                            with dissolve
                            jump endspellchoice_shopv42
                    else:
                        "You don't have enough gold"
                        jump spellchoice_shopv42

                "Illusion Spell, [v42pricetag2] Gold {image=001illusion}" if lvl5v42illspell == 0:
                    if Gold >= v42pricetag:
                        $ lvl5v42illspell = 1
                        $ v42spellbookcount += 1
                        $ Gold -= v42pricetag2
                        play sound "sounds/coin.ogg"
                        if v42firsttimespell == 0:
                            $ v42firsttimespell = 1
                            jump endspellchoice_shopv42
                        elif bairnform >= 2:
                            scene v42017
                            with dissolve
                            jump endspellchoice_shopv42_2
                        else:
                            scene v42026
                            with dissolve
                            jump endspellchoice_shopv42
                    else:
                        "You don't have enough gold"
                        jump spellchoice_shopv42

                "Mysticism Spell, [v42pricetag2] Gold {image=001myst}" if lvl5v42mysspell == 0:
                    if Gold >= v42pricetag:
                        $ lvl5v42mysspell = 1
                        $ v42spellbookcount += 1
                        $ Gold -= v42pricetag2
                        play sound "sounds/coin.ogg"
                        if v42firsttimespell == 0:
                            $ v42firsttimespell = 1
                            jump endspellchoice_shopv42
                        elif bairnform >= 2:
                            scene v42017
                            with dissolve
                            jump endspellchoice_shopv42_2
                        else:
                            scene v42026
                            with dissolve
                            jump endspellchoice_shopv42
                    else:
                        "You don't have enough gold"
                        jump spellchoice_shopv42

                "Healing Spell, [v42pricetag2] Gold {image=001heal}" if lvl5v42heaspell == 0:
                    if Gold >= v42pricetag:
                        $ lvl5v42heaspell = 1
                        $ v42spellbookcount += 1
                        $ Gold -= v42pricetag2
                        play sound "sounds/coin.ogg"
                        if v42firsttimespell == 0:
                            $ v42firsttimespell = 1
                            jump endspellchoice_shopv42
                        elif bairnform >= 2:
                            scene v42017
                            with dissolve
                            jump endspellchoice_shopv42_2
                        else:
                            scene v42026
                            with dissolve
                            jump endspellchoice_shopv42
                    else:
                        "You don't have enough gold"
                        jump spellchoice_shopv42
                "Back":

                    jump spellchoice_shopv42
        "Exit":
            if bairnform >= 1:
                jump aftercheckbairnformv42
            else:
                jump endspellchoice_shopv42

label endspellchoice_shopv42_2:
    if bairnform >= 2:
        scene v42017
        with dissolve
        cerea "That's a good spell... Once you've mastered it"
    else:
        scene v42027
        with dissolve
        bairn "That's a good spell... Once you've mastered it"
    jump spellchoice_shopv42


label endspellchoice_shopv42:
    if bairnform >= 1:
        jump endspellchoice_shopv42_2

    if v42spellbookcount >= 1:
        bairn "Hmm there we are. Knowledge is everything my boy."
        bairn "The more knowledge you have, the better equipped you are."
        MC "Wait... What language is this? I can't even begin to decipher it."
        scene v42027
        with dissolve
        bairn "Ah yes... that will be a problem."
        bairn "Clearly you don't know the language of the Devils"
    else:
        bairn "Oh.. nothing you see interest you?"
        MC "What language are those spells in? I couldn't even read the names"
        scene v42027
        with dissolve
        bairn "Well, my wares are a bit unique it's true"
        bairn "That's the language of the Devils"

    MC "Devils? This is Demonic Magic?"
    bairn "Oh no.. no.."
    scene v42026
    with dissolve
    bairn "Simply knowledge that was recorded by the Devils and Demons..."
    bairn "Of course it's going to be written in their own tongue.."
    Nonen "I knew it.... I knew I felt this presence before"
    Nonen "This old man is not what he seems..."
    MC "What?"
    Nonen "This magic of his, it's.... "
    Nonen "Quickly, use my power, break the illusion..."
    MC "I..."
    Nonen "I'll even let you do it for free this time..."
    MC "For free? What do you mean?"
    Nonen "Hurry now, break the illusion before we're noticed..."
    scene v42027
    with dissolve

    menu:
        "[abgreen]Use the stone's power":
            $ bairnform = 2
            "Suddenly the image of the old man begins to waver then crack entirely"
            scene v42027a
            with dissolve
            scene v42027b
            with dissolve
            scene v42027c
            with dissolve
            scene v42017
            with dissolve
            "Before you stands a beautiful female demon"
            "Bearing a mark on her face and still wearing the same glasses she had on as Bairn"
            demon "What?! How?! How could you....?"
            scene v42023
            with dissolve
            "The demon adjusts her glasses and stares at you"
            demon "Clearly you are more powerful than I gave you credit for..."
            MC "You're a demon?!"
            scene v42021
            with dissolve
            demon "Figure that out on your own did you?"
            demon "What gave it away? The massive horns? Maybe the red skin?"
            MC "Are you one of Lust's Succubi?"
            scene v42020
            with dissolve
            demon "How dare you? I have nothing in common with those Sluts and their Whore Queen."
            scene v42017
            with dissolve
            cerea "I am Cerea, I am... was a Demon of Pride"
            cerea "Until I was exiled..."
            MC "How do I know you're telling me the truth?"
            cerea "You don't. But if you were a demon you'd know by looking at my face"
            cerea "This mark tells all demons that I am an exile"
            cerea "To make matters worse, they marred my face with it, soiling my pride..."
            MC "Why where you exiled?"
            scene v42018
            with dissolve
            cerea "For not helping in this war of genocide"
            cerea "You probably already know this, but this whole Slayer war is Lust's doing"
            cerea "She is pretending to be the Emperor's wife and whispers in his ear"
            cerea "She sent their armies on this 'Murder and Fuck' spree all over the world"
            scene v42023
            with dissolve
            "She pauses, thinking"
            scene v42022
            with dissolve
            cerea "Excuse my language, but thinking about that cunt pisses me off"
            cerea "She's the reason I'm here. At a certain point, she asked my Lord Pride"
            cerea "For his help in conquering the races of the world"
            cerea "He then came to me, looking for knowledge that could speed it along... I refused"
            MC "Why you?"
            scene v42021
            with dissolve
            cerea "Because of Knowledge..."
            cerea "I was the keeper of the Grand Library of the Nine Hells"
            cerea "Knowledge is what I take pride in most of all"
            cerea "If I had helped... if I had given him what he wanted..."
            cerea "Do you know what happens when one race rules over every other?"
            cerea "Dogma.... Stagnation..."
            scene v42018
            with dissolve
            cerea "Old knowledge would be destroyed, new knowledge would never be born."
            cerea "In order for the world to continue to evolve..."
            cerea "In order for old knowledge to be able to be found"
            scene v42017
            with dissolve
            cerea "The world must continue on with all the races free to develop in their own way"
            cerea "But the knowledge in my library would have been used..."
            cerea "To give the Slayers the ability to stomp all that out"
            scene v42022
            with dissolve
            cerea "Then my race would have killed all of them, once the dirty work was done."
            cerea "So I refused, then I was branded and exiled"
            cerea "But I escaped my library with a horde of knowledge hidden away"
            cerea "And sealed it with a forgotten spell they'll never break"
            cerea "Then I was forced to live here..."
            cerea "Right near that Whore Lust and her pawns so I could be... monitored"
            MC "You can't leave?"
            scene v42023
            with dissolve
            cerea "No... currently there's a spell in place..."
            cerea "That has me stuck here put so I don't cause trouble for them"
            jump questionsmenuv42
        "Leave Bairn alone":

            $ bairnform = 1
            scene v42025
            with dissolve
            bairn "Everything ok over there boy?"
            MC "Yes, sorry, just had a minor headache, I dealt with it"
            scene v42024
            with dissolve
            bairn "Ah good, yes, well as to your problem..."
            bairn "Hmmm is Yisnna still at your College?"
            MC "Yes, she is."
            bairn "Then there are no worries. A smart one that girl"
            bairn "She'll have no problem deciphering this for you."
            MC "She'll probably even be happy to have new books..."
            bairn "As I said, smart girl she is"
            MC "Well, fare well Bairn, thank you"
            "You leave the magic shop"
            jump v4slayercitymap




label questionsmenuv42:
    menu:
        "Why were you disguised as an old man?":
            scene v42022
            with dissolve
            cerea "Because he's inconspicuous..."
            cerea "Bairn, the old potion shop owner. Bairn the old feeble mage"
            cerea "Who would look at him and see a danger?"
            cerea "Besides, a woman was out of the question, I got hit on enough in Hell"
            jump questionsmenuv42
        "Why help me?":
            scene v42021
            with dissolve
            cerea "You have a bit of Destiny shining on you."
            cerea "So I figured it'd serve in the interest of Knowledge to help you"
            cerea "But obviously not for free, I do have to eat... we aren't immortal monsters"
            jump questionsmenuv42
        "How can I even use these spells?":
            scene v42023
            with dissolve
            cerea "Of all you human mages, there is one I actually rather respect."
            cerea "Her name is Yisnna, I believe you would know her"
            MC "Yes, she's in charge of the library at the College"
            scene v42022
            with dissolve
            cerea "Ah... the College of Allestria's famous library"
            cerea "What I wouldn't give to be able to get in there..."
            MC "I don't see that happening..."
            scene v42021
            with dissolve
            cerea "You'd be surprised..."
            cerea "However, simply give the books to her"
            cerea "She'll be able to translate Demonic Script for you"
            MC "Why can't you do it?"
            cerea "Because knowledge must be earned"
            cerea "So earn it by making the trek back to your school"
            jump questionsmenuv42
        "No More Questions":
            scene v42017
            with dissolve
            cerea "So... what now? Going to fight me? Kill me?"
            cerea "Turn me in to the Slayer Guards? Blackmail me into lowering my prices?"
            stop music
            play music "<loop 0.0>sounds/beat.mp3"
            show shotr
            with hpunch
            Nonen "Enslave her... use my power, make her your slut!"
            Nonen "Take the knowledge from her"
            Nonen "And you'll no longer need to spend your gold on this whore!"
            hide shotr
            jump questionsmenuv42_2

label questionsmenuv42_2:

    menu:
        "You have nothing to fear from me[abgreen] [abalignmentlove]":

            stop music
            play music "<loop 0.0>ingame.mp3"
            scene v42021
            with dissolve
            $ Points += 1
            "You gain 1 point"
            MC "I'd much rather continue the friendly relationship we were forming"
            MC "Back when you were still Bairn"
            MC "I don't see a good reason to threaten you"
            scene v42022
            with dissolve
            cerea "You might be a bit too trusting. I mean I am a Demon"
            MC "Yes, but even though I'm pretty sure you'd have no problem defeating me..."
            MC "You haven't been hostile at all or tried to kill me..."
            MC "Making you the first demon ever who hasn't"
            scene v42023
            with dissolve
            cerea "Hmm, I do see how that would be convincing evidence"
            cerea "Fine as further proof of our new friendship"
            cerea "I'll take 20 percent off my store prices for you"
            $ v42pricetag = 16
            $ v42pricetag2 = 40
            scene v42021
            with dissolve
            cerea "I see great potential in you"
            cerea "So I want to help you succeed in ruining the Devils' plans"
            cerea "Especially that whore..."
            cerea "Also, if you come back in on another day"
            cerea "I'll pull out some higher level spells for you to purchase"
            MC "That sounds like a good deal"
            MC "It'd be nice to have a demon who isn't trying to kill me for once"
            MC "Let alone having one as a friend..."
            $ cerealove += 1
            "Cerea likes you more now"
            scene v42018
            with dissolve
            cerea "Then I hope to see you again soon [MC]..."
            cerea "Perhaps in the future I can do more for you than simply sell you spells"
            MC "Farewell Cerea"
            MC "I am sorry you were exiled from your library, but I am glad to have met you"
            jump v4slayercitymap
        "Blackmail her[abred] [abnoalignment]":

            stop music
            play music "<loop 0.0>ingame.mp3"
            $ bairnform = 3
            $ Points -=1
            "You lose one point"
            scene v42017
            with dissolve
            MC "Fine... I won't turn you in... if you do lower your prices for me"
            cerea "I should have figured. Fucking humans, all the same..."
            MC "Or maybe you could offer something... more carnal?"
            scene v42018
            with dissolve
            cerea "Only if you're into demon girls biting it off"
            MC "Fine... then just the discount then"
            cerea "Alright, I'll give you 5 percent off my books"
            MC "20 percent"
            scene v42017
            with dissolve
            cerea "10 percent or go fuck yourself and I'll go into hiding from you"
            $ v42pricetag = 18
            $ v42pricetag2 = 45
            MC "Fine... pleasure doing business with you"
            cerea "Fucking humans...."
            "Cerea hates you"
            "You leave the shop"
            jump v4slayercitymap
        "Use the stone to corrupt her[abred] [abnoalignment2]":

            $ bairnform = 4
            $ Points -= 2
            "You lose 2 points"
            scene v42019
            with dissolve
            "Cerea groans as she holds her head"
            cerea "Ahhh..."
            scene v42020
            with dissolve
            cerea "Now I get it... how you broke my illusion... how you knew..."
            scene v42017
            with dissolve
            cerea "You're him... Well fuck you, you won't get me..."
            cerea "I will not become some dark power's fucktoy!!"
            scene v42030
            with dissolve
            cerea "I am Cerea of Knowledge, Demon of Pride and I hope you burn in Hell !!!"
            "Cerea resists the stone's power..."
            scene v42031
            with dissolve
            scene v42031a
            with dissolve
            scene v42031b
            with dissolve
            "Pulls an item from her robes and vanishes in bright light"
            scene v42029
            with dissolve
            MC "What the fuck was that?"
            show shotr
            with hpunch
            Nonen "How did she resist? That bitch knows things she shouldn't..."
            hide shotr
            stop music
            play music "<loop 0.0>ingame.mp3"
            MC "Like what?"
            MC "Hello? Urgh...."
            scene v42032
            with dissolve
            "You notice a lone book left on the ground, a spellbook that you hadn't purchased"
            MC "Well I may not have been able to acquire her, but I did get this for free"
            $ lvl1v42altspell = 1
            "Cerea knows you can use the Stone's power, you'll never see her again."
            "Hope it was worth it..."
            "You leave the shop"
            jump v4slayercitymap

label checkbairnformv42:
    if bairnform == 1:
        scene v42028
        with dissolve
        bairn "Come in my boy, see what I have to offer you"
        jump spellchoice_shopv42
    elif bairnform == 2:
        scene v42028
        with dissolve
        "Bairn stands before you.."
        scene v42016
        with dissolve
        "But only for as second until Cerea breaks the illusion"
        scene v42017
        with dissolve
        cerea "Hello again, [MC]. What can I interest you in?"
        jump spellchoice_shopv42
    elif bairnform == 3:
        scene v42028
        with dissolve
        "Bairn stands there"
        MC "Well?"
        scene v42016
        with dissolve
        cerea "*scoffs* Well, what do you want?"
        MC "You could stand to be a little nicer"
        scene v42017
        with dissolve
        cerea "You could stand to go jump in a flame pit"
        MC "That doesn't sound like talk from someone who wants me to keep their secret"
        cerea "Fine... Good day sir, what can I offer you for purchase?... jackass"
        jump spellchoice_shopv42
    else:
        scene v42029
        with dissolve
        "Nobody's here, you made her run away remember?"
        "You leave the shop"
        jump v4slayercitymap



label aftercheckbairnformv42:
    if bairnform == 1:
        scene v42027
        with dissolve
        bairn "Take care, come again"
        "You leave the shop"
        jump v4slayercitymap
    elif bairnform == 2:
        scene v42021
        with dissolve
        cerea "Take care, come back soon"
        MC "Thanks Cerea, I will"
        "You leave the shop"
        jump v4slayercitymap
    elif bairnform == 3:
        scene v42018
        with dissolve
        cerea "You done? Then get out"
        MC "I'm sorry, what was that?"
        scene v42017
        with dissolve
        cerea "Get the fuck out of my shop..."
        cerea "Before we see if I am strong enough to kill you or not"
        MC "Ahah sure... Bye bye..."
        "You leave the shop"
        jump v4slayercitymap


label v42church:
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    scene v42033
    with dissolve
    "As you walked by the previously closed Church, you felt a sort of pull"
    "Before you know what you're doing, you walk in main hall"
    MC "What is this? Why was I drawn here?"
    show shotr
    with dissolve
    hide shotr
    MC "Damn it... When will you stop this?"
    Nonen "Yes... I can feel it... it's close"
    MC "What do you mean?"
    scene v42034
    with dissolve
    "You look around the church for a bit more"
    MC "This place is empty... There is nobody here"
    MC "I wonder why I felt I had to come here..."
    scene v42035
    with dissolve
    MC "I have a strange feeling... I should leave this place"
    fvoice "Going somewhere?"
    scene v42036
    with dissolve
    MC "What the?"
    Nonen "Oh... so she's the one responsible"
    lust "I knew you would come here eventually"
    MC "You..."
    scene v42037
    with dissolve
    lust "Did you miss me? I'm sure you did"
    MC "I don't understand..."
    lust "What don't you understand?"
    scene v42038
    with dissolve
    lust "Come on... Tell me, don't be shy now"
    MC "If you wanted me, why did you let me go last time?"
    lust "Well... What's the difference between then and now?"
    MC "The difference?"
    lust "Yes... You have something I want..."
    lust "And I knew he would give it to you but never to me"
    MC "You mean..."
    scene v42039
    with dissolve
    lust "Yes... The missing piece..."
    MC "Is that..."
    stop music
    play music "<loop 0.0>sounds/beat.mp3"
    show shotr
    with hpunch
    hide shotr
    Nonen "Yes... It's more of me"
    lust "Come on, Cari my dear, give it to me"
    scene v42040
    with dissolve
    lust "See how it reacts to you? It loves you..."
    lust "I'm so glad... It took some time..."
    lust "But we are about to rule everything..."
    "You start to feel your essence pulling the stone to you"
    MC "I...This..."
    scene v42041
    with dissolve
    lust "Yes... Take it... Savor it... Drain it!"
    lust "Do you feel it? The power"
    show shotr
    with hpunch
    hide shotr
    Nonen "Ahhh yes... I feel it..."
    MC "Ahhh... Damn you..."
    scene v42042
    with dissolve
    lust "Feel the power! Taste the power!"
    show shotr
    with hpunch
    hide shotr
    show shotr
    with vpunch
    hide shotr
    $ Destpoints += 5
    $ Iluspoints += 5
    $ Healpoints += 5
    $ Mystpoints += 5
    $ Summpoints += 5
    $ Altepoints += 5
    $ Necropoints += 5
    "All your powers increased by 5"
    scene v42043
    with dissolve
    lust "Feel it? Feels great right?"
    Nonen "Yes!! I need more!"
    MC "No... Wait..."
    lust "Four pieces left to go my dear, imagine the power"
    "You feel like you are about to faint..."
    MC "I..."
    stop music
    scene v42043a
    with dissolve
    scene v42043b
    with dissolve
    scene black
    with dissolve
    MC "Can't...."
    mvoice "Come on... You need to fight this"
    MC "I... Can't..."
    mvoice "Of course you can!"
    scene v37129
    with dissolve
    stman "I know you can, that's why I gave you the stone"
    stman "You can't let her have it, fight back!"
    scene black
    with dissolve
    stman "NOW!"
    scene v42044
    with dissolve
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    "You open your eyes and see Lust and Carilielle in front of you"
    "You can feel your body moving by itself"
    "But you can't control it..."
    MC "{i} What's going on... I can't even move my mouth"
    scene v42045
    with dissolve
    lust "So... Are you ready?"
    Nonen "Yes I am, let's get this going"
    lust "Excellent!"
    MC "{i} What? No... I... "
    Nonen "This young body is impressive, and his will is amazing"
    Nonen "Even now he's still trying to fight me, ahahaha"
    scene v42046
    with dissolve
    lust "Only the best for you father!"
    MC "{i} Father? what is she talking about? Ahh.. My head... I'm..."
    lust "What do you say of a little fun with Cari here?"
    "You push with all the power you can muster to break free"
    "Until you finally succeed"
    scene v42047
    with dissolve
    MC "Ahhhhh! NO!!!"
    lust "Why you... How dare you interrupt? You insignificant mortal worm"
    lust "To the ground with you filthy mortal scum"
    scene v42047
    with hpunch
    scene black
    with dissolve
    "She slaps you to the ground and you black out"
    cari "Hmmm he's so big..."
    lust "Father did say he was a great vessel"
    "You force your eyes open"
    scene v42048
    with dissolve
    "You can see Carilielle stroking your dick"
    MC "I can't move... Stop..."
    scene v42049
    with dissolve
    cari "Are you sure?"
    "She starts to swallow your dick"
    cari "Hmmm... So good..."
    "Even though you didn't agree with this, it feels great"
    MC "Ah... Wait..."
    cari "Nuh uh..."
    scene v42050
    with dissolve
    "She goes even deeper"
    MC "Ah... Shit..."
    "It's like you are about to cum but you aren't allowed to"
    scene v42051
    with dissolve
    cari "Time to have you try another part of me"
    "She rubs herself onto your penis"
    "Then grabs it and points it towards her pussy"
    scene v42052
    with dissolve
    cari "Ah... Yes... What a marvelous cock"
    "You feel like cumming, but you still can't"
    "The pleasure becomes pain, the urge to cum is overwhelming"
    "Is this some sort of torture? Are you under a spell?"
    cari "Yes!! More!"
    MC "Ahhrgg... I can't take this anymore, stop it!"
    scene v42053
    with dissolve
    cari "We're almost done, don't worry"
    lust "Yes we are, come on girls, let's help Father rise again"
    MC "Ahhhh... SHIT!!"
    scene v42054
    with dissolve
    "You see some of the girls you know were missing"
    MC "Is my mind playing tricks on me now?"
    cari "Yes... Keep going, I'll let you cum in a moment"
    lust "There girls, each of you grab a stone and get ready to be with father forever"
    scene v42055
    with dissolve
    "You see that the girls are getting closer with more of those stones"
    "Your mind can't process anything anymore"
    cari "Get ready to cum pretty boy, we're almost ready"
    scene v42056
    with dissolve
    "You are now surrounded by all the girls and stones"
    cari "Yes!! I'm cumming!!"
    MC "I..."
    menu:
        "Resist, give your best to fight back[abgreen] [abendings]":
            MC "I will not allow this.... I can't..."
            scene v42059
            with dissolve
            lust "Quiet now... It's almost over my boy"
            lust "You are about to reborn into the most powerful being ever"
            menu:
                "Try to cast a mind spell on Carilielle":
                    "You start to get inside Carilielle's mind"
                    "You find out that she is being controlled just like the others"
                    "You try your best to break that spell"
                    cari "I..."
                    jump v42fightback
                "Try to cast a mind spell on the girls[abgreen] [abendings]":

                    "You are not powerful enough to mess with their minds"
                    jump thethingthatshouldnotbe
                "Give up to the temptation and power[abgreen] [abendings]":

                    jump thethingthatshouldnotbe
        "Give up to the temptation and power":

            jump thethingthatshouldnotbe

label thethingthatshouldnotbe:
    scene v42057
    with dissolve
    "You can't fight anymore"
    "You see the Stones surrounding you, empowering you"
    scene v42057
    with dissolve
    scene v42057a
    with dissolve
    scene v42057b
    with dissolve
    scene v42057c
    with dissolve
    scene v42057d
    with dissolve
    scene black
    with dissolve
    $ Destpoints = 999
    $ Iluspoints = 999
    $ Healpoints = 999
    $ Mystpoints = 999
    $ Summpoints = 999
    $ Altepoints = 999
    $ Necropoints = 999
    $ Points = -99
    "All your powers increased and your points lowered"
    lust "Now rise Father! Rise to rule the world!"
    scene v42058
    with dissolve
    Nonen "Lust... My dear, I'm back, after all this time..."
    Nonen "Thanks to you... I'm at my greatest! Ahahaha"
    show text "{color=#f00}{b}Ending 2: The thing that should not be{/b}{/color}" with dissolve
    $ renpy.pause(3, hard=True)
    scene v42131
    with dissolve
    lust "And you have a start for your harem"
    Nonen "You did great Lust... You did great..."
    Nonen "We can now take over this world and wipe out all who oppose us"
    Nonen "Are you ready girls?"
    scene v42132
    with dissolve
    "The girls nod with joy"
    "They are happy to be owned by such a powerful being"
    scene v42133
    with dissolve
    "You... Well... Your body had sex whenever he wanted"
    "It had all the girls, power, and land he wanted"
    "But in the end... Was it really you in command?"
    "Thank you for playing, try different choices to find different endings"
    jump endversion


label v42fightback:
    scene v42060
    with dissolve
    cari "AHHHHHHH!!"
    "Carilielle launches some powerful force in all directions"
    "Sending everyone aside, you included"
    lust "What the hell?!"
    scene v42061
    with dissolve
    "You see her transform in front of your eyes"
    "Wings... Horns... A tail and tattoos covering her body"
    "And a massive power surrounding her"
    lust "What are you doing? Stop!"
    scene v42062
    with dissolve
    "You and the girls have been pushed away by her power"
    "Only Lust stands next to her"
    "Carilielle casts some destructive spell with Lust being the target"
    lust "You really think you can face me?"
    scene v42063
    with dissolve
    "It doesn't take long before Lust's power overcomes Carilielle"
    lust "How dare you attack me? Me? Your queen!"
    scene v42064
    with dissolve
    "You feel can feel that Carilielle is drained of her power"
    lust "Why... Why would you do this to me? Why?"
    scene v42065
    with dissolve
    lust "What should I do to you now? I can't kill such a beauty"
    lust "My most valuable asset... I just can't"
    lust "You... This is all your fault..."
    scene v42066
    with dissolve
    lust "You'll pay for this, believe me..."
    lust "I was trying to do everthing painlessly"
    lust "But you give me no choice..."
    scene v42067
    with dissolve
    "She snaps her fingers and Carilielle returns to her human form"
    MC "I can't move..."
    lust "You can try... But you are done"
    scene v42068
    with dissolve
    lust "Father only needs your body anyway, your mind can go"
    fvoice "Looks like we are right on time brother"
    mvoice "Yes... And look.. So many girls for me"
    scene v42069
    with dissolve
    zegladar "Hello, I hope we're not interrupting something"
    goggos "Hmmm hi Lust..."
    lust "Just what I needed... More distractions... The usurpers"
    scene v42070
    with dissolve
    lust "What are you two doing here?"
    goggos "Whatever you want me to do... Hehe"
    zegladar "Forgive my brother... His libido is uncontrollable..."
    zegladar "Are you sure he is not{i} your {/i}brother?"
    lust "What do you want and why should I let you live?"
    scene v42071
    with dissolve
    zegladar "First we just want him, second because you used a lot of your power..."
    zegladar "And there's two of us..."
    goggos "But... I want to have some fun too"
    zegladar "Not now, Goggos"
    scene v42072
    with dissolve
    lust "Pfff.... Ahahahaha... Ahahahah"
    lust "You.... Ahahahah"
    zegladar "What's so funny bitch?"
    lust "I thought you were supposed to be the smart one Zegladar"
    zegladar "What?"
    scene v42073
    with dissolve
    lust "You really think you can come here and tell ME what to do?"
    scene v42072
    with dissolve
    lust "Ahahaha"
    "You can move you body again... Looks like you regained control of it"
    "She must be getting ready to fight"
    scene v42073
    with dissolve
    lust "I can give you one thing though..."
    goggos "What?"
    lust "Death!"
    scene v42074
    with dissolve
    "You feel Lust's power everywhere"
    "Now would be a great time to get the hell out of here"
    scene v42075
    with dissolve
    "You notice that the girls assembled near the wall"
    MC "Are you ok? Girls?"
    scene v42076
    with dissolve
    lili "What happened? Where are we? Who are these girls? Why are we naked?"
    MC "You were being mind controlled I believe... But there's no time to explain"
    scene v42087
    with dissolve
    MC "See what is happening over there? We need to go! Now!"
    scene v42077
    with dissolve
    "The girls get up, looking dazed and confused"
    isabella "My head... I... "
    scene v42077
    with hpunch
    MC "We should leave, come on!"
    scene v42078
    with dissolve
    lili "Come on girls, we'll figure out what happened later on"
    scene v42078
    with vpunch
    MC "Hurry up, come on!"
    scene v42079
    with dissolve
    lili "I'm not sure what is happening but I want an explanation"
    MC "Sure, I promise"
    "The girls leave"
    scene v42087
    with dissolve
    "Lust is still fighting with the other devils"
    scene v42087
    with vpunch
    "Their power is something else"
    scene v42080
    with dissolve
    "Before you leave you notice that Carilielle is still there"
    "In the same exact position she was before"
    "There is also one of the stones present"
    MC "What should I do now?"
    menu:
        "Get the hell out of here":
            MC "I'm out of here"
            jump v42afterescape
        "Grab the stone and leave[abred] [abnoalignment]":

            scene v42081
            with dissolve
            MC "I'm sure this will be useful"
            $ Points -=1
            "You lost 1 point"
            MC "I'm out of here"
            $ v42grabstone = 1
            jump v42afterescape
        "Try to help Carilielle[abgreen] [abalignment]":

            scene v42082
            with dissolve
            MC "I can't leave her like this..."
            $ Points +=1
            "You gain 1 point"
            MC "Hey... Can you hear me? Let me help you"
            scene v42083
            with dissolve
            "She looks surprised by your words"
            MC "Come on, you need to get out of here, fast"
            scene v42084
            with dissolve
            "She grabs your hand and you help her get up"
            scene v42085
            with dissolve
            cari "Why are you helping me?"
            MC "I'm not sure... But I think I should..."
            scene v42085
            with vpunch
            MC "Now please can you run before this whole place falls apart?"
            scene v42086
            with dissolve
            cari "Ok..."
            cari "Thank... You..."
            scene v42087
            with dissolve
            "She left and the devils are still fighting"
            scene v42087
            with vpunch
            MC "Now I should leave too"
            scene v42088
            with dissolve
            "What about the stone? Should you take it with you? "
            scene v42088
            with vpunch
            "Maybe Ayna or Bredita can help you with it?"
            menu:
                "[abgreen]Grab the stone and go":
                    $ v42grabstone = 2
                    scene v42081
                    with dissolve
                    MC "I'm sure this will be useful"
                    jump v42afterescape
                "Forget the stone and leave":

                    $ v42grabstone = 3
                    MC "Fuck that! I'm out of here!"
                    jump v42afterescape

label v42afterescape:
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v42098
    with dissolve
    "You are now outside the church"
    zordruza "I'm Zordruza, Queen of the Dark Elves, you can trust me"
    katla "I'm Katla, I would like to say a pleasure to meet you..."
    katla "But in these circumstances..."
    lili "Any of you know where we are, and why we're naked?"
    scene v42099
    with dissolve
    zordruza "I can fix the naked part..."
    isabella "Wow..."
    scene v42100
    with dissolve
    katla "You know magic!?"
    MC "Are you all ok?"
    if my_path_is == "good":
        scene v42101
        with dissolve
        zordruza "We're fine, can you tell us what's going on?"
        MC "I wish I knew... Really..."
        scene v42104
        with dissolve
        zordruza "The last thing I remember was the invasion..."
        zordruza "Now... We're here..."
        MC "We'll be fine"
        jump v42talkportal

    elif my_path_is == "evil":
        scene v42103
        with dissolve
        lili "We're fine, can you tell us what's going on?"
        MC "I wish I knew... Really..."
        scene v42105
        with dissolve
        lili "The last thing I remember was that we were traveling"
        lili "Now... We're here..."
        MC "We'll be fine"
        jump v42talkportal
    else:

        scene v42102
        with dissolve
        isabella "We're fine, can you tell us what's going on?"
        MC "I wish I knew... Really..."
        scene v42106
        with dissolve
        isabella "The last thing I remember was that we were traveling"
        isabella "You, me, my mother and Irgodon..."
        isabella "Now... We're here..."
        MC "We'll be fine"
        jump v42talkportal

label v42talkportal:
    MC "All of you come here please"
    scene v42107
    with dissolve
    MC "I know you must still be confused with all this"
    MC "And I promise I'll tell you everything I know"
    MC "But we need to leave now"
    scene v42108
    with dissolve
    MC "Do any of you know how to use this..?"
    zordruza "A teleporting crystal, let me see"
    MC "Yes, the Archmage gave it to me, but I haven't been able to get it to function"
    katla "Teleporting?"
    scene v42109
    with dissolve
    zordruza "Yes, the crystal has an engraved location..."
    zordruza "And still appears to have some charge..."
    MC "Can you take us out of here with it?"
    zordruza "I can try, but with 5 people, the Crystal may not be strong enough.."
    lili "We need to try anyway, I don't want to stay here"
    lili "I feel observed somehow..."
    scene v42110
    with dissolve
    zordruza "Let's begin then, put your hands on the crystal"
    stop music
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    scene v42111
    with dissolve
    "You teleport to what appears to be the Portal Room in the College"
    MC "You did it! It worked!"
    zordruza "We did it!"
    scene v42112
    with dissolve
    "You can see the happiness in their faces"
    MC "We did it... We actually did it..."
    scene meanwhile
    with dissolve
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    scene v42087
    with dissolve
    lust "You really think you can hold on much longer?"
    scene v42088
    with dissolve
    lust "Bad news... You can't!!"
    scene v42089
    with dissolve
    lust "I told you... And now, time to end your miserable lives"
    lust "Damn you for ruining my plans like this!!"
    scene v42090
    with dissolve
    lust "DIE!!!"
    scene v42090
    with vpunch
    lust "...."
    scene v42091
    with dissolve
    lust "Are you enjoying the cozy fire?"
    goggos "Ahhh"
    scene v42092
    with dissolve
    goggos "I'm going to fuck you so hard when this is over!!"
    zegladar "Fucking bitch..."
    lust "Oh... Did I hurt you...? Are you enjoying the view Gluttony?"
    scene v42093
    with dissolve
    zegladar "What?"
    goggos "No way..."
    lust "Come on now... Don't be shy"
    scene v42094
    with dissolve
    lust "Are you hungry? I brought you something"
    gluttony "Heheheh yes!! Food! I'm hungry!"
    lust "Go ahead, eat them. I even started to cook them, see?"
    gluttony "Heheheh"
    scene v42095
    with dissolve
    lust "Have fun kids, mommy needs to do something"
    zegladar "Get ready..."
    goggos "This fat fuck had to show up..."
    scene v42096
    with dissolve
    lust "Bye bye..."
    gluttony "FOOD!!!"
    scene v42096
    with vpunch
    gluttony "Hehehe"
    scene v42097
    with dissolve
    gluttony "I will swallow you both now!!"
    gluttony "You'll be in my belly soon hehehe"
    scene v42117
    with dissolve
    lust "Now where did they go... They can't have gotten far..."
    lust "These bastards had to show up and ruin everything..."
    scene v42118
    with dissolve
    aelia "But I will find them..."
    aelia "They can't run from me forever"
    scene v42119
    with dissolve
    aelia "Hmmm?"
    aelia "Oh... You're here..."
    scene v42120
    with dissolve
    aelia "What's going on here? Why are you here my King?"
    aelia "And with all these soldiers?"
    scene v42121
    with dissolve
    tiberius "Shut it demon!! I saw it all!"
    tiberius "You've blinded me for long enough"
    tiberius "Get her!!"
    scene v42122
    with dissolve
    lust "You too? Why is everyone defying me today?"
    lust "You think you can stop me? ME?!"
    lust "With something as pitiful as this?"
    scene v42123
    with dissolve
    cpt "Now soldiers!! Move!"
    scene v42124
    with dissolve
    tiberius "Kill her Brutus!!"
    tiberius "Now!"
    scene v42125
    with dissolve
    lust "Poor Brutus... Following a limp dick man like you"
    lust "You really think you can face me here and now?"
    lust "You should have sided with me Brutus, goodbye..."
    scene v42126
    with dissolve
    lust "Now it's your turn..."
    tiberius "Ahhrrgg... {i}cough cough"
    tiberius "Soldiers... Kill... her..."
    lust "Let me tell you a secret... I'm going to kill them all"
    scene v42127
    with dissolve
    tiberius "Ahhhhhh!!"
    lust "But you get to go first..."
    lust "And they get to watch..."
    sol "Run... I'm not facing that..."
    sol2 "Holy shit..."
    cpt "You cowards, attack!!"
    lust "Do you hear that? Your soldiers? See how much they love you now?"
    lust "It must be so painful for your heart... Let me help you"
    scene v42128
    with dissolve
    tiberius "......."
    lust "There...See? Like I promised, all the pain is gone"
    lust "Now"
    lust "For the rest of you..."
    stop music
    play music "<loop 0.0>ingame.mp3"

    if my_path_is == "good":
        scene v42114
        with dissolve
        zordruza "So what do we do now?"
        MC "We should talk with the Archmage"
        zordruza "Where is my sister?"
        MC "Last I knew she was in Darkaria looking for you"
        zordruza "Very well, then let's see if Ayna can help"
        MC "Let's collect the others first..."


    elif my_path_is == "evil":
        scene v42115
        with dissolve
        lili "So what do we do now?"
        MC "We should talk with the Archmage"
        MC "Bredita was here earlier, but I'm not sure if she's come back yet"
        lili "Bredita was here?! At the College?"
        MC "Desperate times, I guess. Anyway, let's collect the others"
    else:


        scene v42113
        with dissolve
        isabella "So what do we do now?"
        MC "We should talk with the Archmage"
        isabella "I trust you, lead the way"
        MC "I promise we'll get this sorted out"
        MC "Let's get the others together first though"

    scene v42116
    with dissolve
    MC "Ok we're safe here ladies, and I'm thankful for that"
    MC "You had a lot of people looking for you"
    MC "Still I think Katriona should take a look at you all"
    MC "Liliana knows the way to her lab, she can take you there"
    scene v42129
    with dissolve
    lili "Yes, I agree. We should be checked out for any further problems..."
    lili "Katriona is the best healer I know, she's an Elite after all"
    lili "She will be able to tell if we're still under the influence of anything"
    scene v42130
    with dissolve
    "You can't believe that you are back in the College safe and sound"
    "Especially after what almost happened..."
    jump v43version
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
