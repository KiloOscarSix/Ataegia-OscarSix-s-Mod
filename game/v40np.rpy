init:
    $ v4soldiergone = 0
    $ v4midajoined = 0
    $ v4helpdwarf = 0
    $ v4talkwithayna = 0
    $ v40np = 0
    $ v4talklwithrunar = 0
    $ gamblegold = 0
    $ bathadventure = 0
    $ calessapet = 0
    $ hanna3some = 0
    $ tavernhanna = 0
    $ v4spentthenight = 0
    $ v4visiteon = 0
    $ v4katlabvisit = 0
    $ v4calessabrothelfun = 0
    $ midaforgive = 0
    $ fuckmidadouble = 0
    $ midaown = 0
    $ v42check = 0
    $ churchreadyv42 = 0
    $ v42magicshop = 0
    $ bairnform = 0
    $ v42dockvisit = 0


label v40np:
    $ v40np = 1
    if resistsoulstone == 1:
        $ stoneuses += 1
    scene v39165
    with dissolve
    rolf "We should start by travelling to the hunters camp"
    MC "Very well, if you feel that's where we should go, let's go"
    scene v39166
    with dissolve
    rolf "We'll need a boat to get there, unless you have a Mage spell or trick of some sort"
    MC "I wish I could teleport but..."
    MC "I could try to find out how the portal room works..."
    scene v39165
    with dissolve
    rolf "The portal?"
    MC "Yes, we have a portal at the College. With that we could travel instantly"
    scene v39166
    with dissolve
    rolf "That would be great... If you manage that, it will save us days of travel"
    MC "I'll see what can be done"
    scene v39165
    with dissolve
    rolf "Thank you [MC], you truely will make a great hunter."
    rolf "Meanwhile I'll prepare a plan B, just in case"
    MC "Very well, see you soon, with good news I hope"
    scene v39164
    with dissolve
    "As you leave the kitchen, you notice that Rolf still seems very concerned"
    MC "Let's see if I can find a way to use the portal"
    MC "I could ask the Archmage or Master Katarro... Or maybe check the library..."
    jump afterorcv39

label v40portalbooks:
    if v40askedportal == 0:
        $ v40askedportal = 1
        scene v38200
        with dissolve
        yisnna "Portals? That's a very tricky subject you know..."
        yisnna "Even when a Mage knows how to do it"
        yisnna "Portals require a great deal of concentration and power to set them correctly"
        yisnna "You could end up not opening one or go somewhere you didn't mean to"
        MC "I understand that, but is there at least a book about it here?"
        scene v18058
        with dissolve
        yisnna "I just said it's horribly advanced..."
        MC "..."
        scene v18056
        with dissolve
        yisnna "Fine... Let me get you something about it..."
        yisnna "Just don't blame me if you end up in one of the Hells..."
        scene v38203
        with dissolve
        MC "Thank you Yisnna"
        scene v38204
        with dissolve
        yisnna "It should be right... Wait..."
        MC "What's wrong?"
        scene v38205
        with dissolve
        yisnna "It's missing... I don't understand..."
        MC "Missing? Like stolen?"
        yisnna "Probably not... Someone came for it and that's why it's gone"
        yisnna "I wish people would tell me when they take my books so this doesn't happen"
        yisnna "I'm sorry, without the book I really can't help you"
        yisnna "Maybe you can ask Katarro or Ayna about it, or maybe look for the book?"
        if my_path_is == "good":
            MC "I have this gem, but I don't know what to do with it..."
            scene v38200
            with dissolve
            yisnna "Why didn't you said that earlier? Those gems were made by Ayna"
            yisnna "You just need to go to the portal room..."
            yisnna "You'll still need to know where to aim your landing though..."
            "Well... Silvana said to get it ready... I guess going there is enough"
            MC "Thank you Yisnna"
            $ v4talkwithayna = 1
            jump v41portalsil
        elif my_path_is == "evil":
            MC "Thank you anyway Yisnna"
            "Maybe the Archmage can help you, you just need to find her"
            $ v4talkwithayna = 1
            jump afterorcv39

        yisnna "I'm sorry, without the book I really can't help you"
        yisnna "Maybe you can ask Katarro or Ayna about it, or maybe look for the book?"
        MC "Thank you anyway Yisnna"
        $ v4talkwithayna = 1
        jump afterorcv39
    else:
        yisnna "Hey [MC] have you found the book?"
        MC "Not yet, I'll return when I do"
        yisnna "See you later then"
        jump afterorcv39

label v40newspells:
    scene v38200
    with dissolve
    yisnna "New spells? I guess I can show you some spellbooks..."
    MC "Awesome! Thanks"
    yisnna "Follow me please"
    scene v38203
    with dissolve
    "You follow her to another part of the library"
    scene v38204
    with dissolve
    yisnna "Here they are, spellbooks!"


label v40newspells_2:
    scene v38205
    with dissolve
    yisnna "What do you want to learn?"
    menu:
        "Level 1 spells":
            menu:
                "Phantasm {image=001illusion}" if shadow_entity == 0:
                    $ shadow_entity = 1
                    "You create a Shadow Entity that damages the enemy and has a chance of causing Fear"
                    "You can now use {color=#f00} Phantasm {/color}"
                    jump v40newspells_2
                "Life Bloom {image=001heal}" if l_bloom == 0:
                    $ l_bloom = 1
                    "Heal twice with a single spell. Once on cast and then again slightly after."
                    "You can now use {color=#f00} Life Bloom {/color}"
                    jump v40newspells_2
                "Shadow Flames {image=001necro}" if shadow_flames == 0:
                    $ shadow_flames = 1
                    "Cast flames of necrotic darkness"
                    "You can now use {color=#f00} Shadow Flames {/color}"
                    jump v40newspells_2
                "Nothing":
                    jump v40newspells_2
        "Level 5 spells":

            menu:
                "Nothing":

                    jump v40newspells_2
        "Level 10 spells":

            menu:
                "Nothing":
                    jump v40newspells_2
        "Back":

            jump v39libraryknow

label v40archtalk:
    scene v4136
    with dissolve
    ayna "Is there something I can do for you, young man?"
    scene v4137
    with dissolve
    ayna "I can see it in your eyes..."
    if my_path_is == "good":
        jump v41goodarch
    elif my_path_is == "evil":
        jump v41evilarch
    MC "Well... I was hoping to learn how the College Portal works"
    ayna "Are you planning to travel somewhere?"
    MC "Yes..."
    scene v4139
    with dissolve
    ayna "And where would that be?"
    MC "Does it matter where, I just was hoping you'd teach me."
    ayna "Of course it matters"
    ayna "After all, how can I help if I don't know where you need to go?"
    ayna "I need to set the portal correctly or you could end up in the Ocean"
    MC "Yeah, Yisnna said I'd probably end up in a Hell"
    ayna "Well, at least I said somewhere nicer..."
    MC "Anyway, Rolf wants to go check the Hunter's Camp"
    MC "I offered to go with him and suggested we could use the Portal"
    MC "But since I've never learned about it's function, I came to you."
    scene v4137
    with dissolve
    ayna "Oh... Actually, I already knew that. He came to talk me already."
    MC "Then why did you act like that?"
    ayna "Because I was messing with you"
    MC "..."
    ayna "Oh don't be like that, it was fun watching you be flustered"
    MC "You're spending too much time with Kat, she's starting to influence your humor"
    ayna "I've known her longer than you"
    ayna "Maybe I influenced hers and you're just now starting to see it"
    scene v4140
    with dissolve
    ayna "But enough joking around, you are free to depart"
    ayna "Also, take this gem with you."
    ayna "When you concentrate your magic on it, you'll be transported back to the College"
    ayna "And not to worry, I already set the Portal to your destination"
    MC "Really? That's great"
    "She hands you a green gem"
    scene v4139
    with dissolve
    ayna "Is there anything else I can do for you?"
    MC "Hmm.. No... Not that I can think of..."
    scene v4138
    with dissolve
    ayna "Safe travels then"
    MC "Thank you, Archmage"
    "She gives you a friendly wink and turns back"
    $ v40archtalk = 1

label v40qarra:
    "You move to the hall"
    scene v4147
    with dissolve
    "As you are walking through the hall you see Mistress Qa'arra"
    Qa "Hello [MC], how are you?"
    MC "Hi Mistress Qa'arra"
    scene v4149
    with dissolve
    Qa "I've been looking for you"
    MC "For me? But why?"
    Qa "I... Need to ask you a favor"
    MC "Hmmm ok... I guess"
    scene v4150
    with dissolve
    "She is looking around making sure you are alone"
    Qa "So a friend of mine has been locked away by the city guards"
    Qa "And I need you to help him escape"
    MC "What? Why me?"
    scene v4149
    with dissolve
    Qa "I can't do it myself, it would be to suspicious if I went.."
    Qa "I travel to the city and suddenly he gets away...?"
    Qa "With us both being Jithaks and known acquaintances..."
    MC "I see, but why is he in jail?"
    scene v4151
    with dissolve
    Qa "I'm sure he was set up, that Runar fellow can't be trusted..."
    Qa "He was working for Runar, then he was accused of stealing"
    MC "Runar... I remember that nasty guy..."
    MC "Alright Mistress, I'll go there. I want to see Runar anyway"
    MC "But I can't promise that I'll be successful"
    scene v4149
    with dissolve
    Qa "Thank you [MC], here have some gold"
    $ Gold += 50
    play sound "sounds/coin.ogg"
    "You received 50 gold"
    MC "50 gold?"
    Qa "What? Is that not enough?"
    MC "No, that's not what I..."
    Qa "What if I enchant you and your weapon?"
    scene v4151
    with dissolve
    MC "Hmm? What do you mean?"
    Qa "Lest you forget, I am the Elite of the Alteration School..."
    Qa "Let's see...."
    scene v4148
    with dissolve
    "You start to feel something around you..."
    $ meeleeimbue = 1
    Qa "Just a bit more..."
    scene v4149
    with dissolve
    Qa "There... All done"
    MC "What was that spell just now?"
    Qa "I've enchanted you and your weapon"
    Qa "Now when you use your weapon you'll have a special bonus"
    Qa "If your skill with a magic school is above Level 7"
    MC "So my weapon will be empowered with my Magic? Is this like a spell?"
    scene v4151
    with dissolve
    Qa "Not exactly, this will not use your Mana reserves"
    Qa "For example if your Alteration is Level 7 or above"
    Qa "You'll be able to use the{color=#f00} Ether Blade {/color}"
    Qa "When you cut your enemy, you'll also steal Mana from them"
    MC "That sounds amazing!!"
    scene v4149
    with dissolve
    Qa "It's quite useful, especially in lengthy battles"
    Qa "The same is true for your other skills, if they are Level 7 or above"
    Qa "You'll be able to imbue your weapon with your powers"
    MC "That sounds really useful, I'll have to test the others..."
    scene v4150
    with dissolve
    Qa "Now, please make haste and let me know your fare"
    MC "I will"
    if my_path_is == "good" or my_path_is == "evil":
        "Maybe now it's a good time to check on Mida"
        jump afterorcv39
    jump v4portaltime

label v4portaltime:
    scene hall
    with dissolve
    MC "I should talk with Rolf now"
    "You move to the kitchen"
    scene v39163
    with dissolve
    MC "There he is"
    scene v39165
    with dissolve
    rolf "[MC] I spoke with your Mage Leader..."
    MC "Yes I've spoken with her as well"
    MC "The Portal is ready to take us"
    scene v39166
    with dissolve
    rolf "It is?! What are we waiting for then?"
    MC "Let's go!"
    "You both move to the portal room"
    scene v4001
    with dissolve
    rolf "So... How is this supposed to work?"
    MC "Let me see..."
    "As you get closer to the stairs you feel the portal open"
    scene v4002
    with dissolve
    rolf "How did you do that?"
    MC "What a great question..."
    rolf "No time to lose, I fear for the Hunters"
    scene v4003
    with dissolve
    "Rolf moves to the portal without hesitation"
    MC "I guess it's time to go"
    stop music
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    play music "<loop 0.0>huntercamp.mp3"
    scene v4004
    with dissolve
    "As you arrive to your destination..."
    rolf "Oh no! What the!?"
    "All you see is death... Bodies of other Hunters"
    "Laying all over the camp"
    scene v4005
    with dissolve
    rolf "Abilio wake up!! Abilio!"
    MC "Rolf..."
    rolf "I know... He's dead..."
    rolf "Who...."
    scene v4006
    with dissolve
    rolf "Who did this? How dare they?!"
    MC "..."
    rolf "I... How... Could this be..."
    rolf "We could never be surprised by a demon attack"
    rolf "Unless it was not a demon... But what could do this?"
    scene v4007
    with dissolve
    rolf "I... Failed my people..."
    menu:
        "Rolf, it's not your fault[abgreen] [abalignment]":
            MC "We don't know what happened here"
            MC "You can't blame yourself"
            $ Points += 1
            "You gained 1 point"
        "Say nothing":

            MC "..."
        "Yeah, you did[abred] [abnoalignment]":

            MC "Yeah... You should have come here sooner"
            $ Points -= 1
            "You got -1 point"

    scene v4008
    with dissolve
    rolf "I don't deserve to be the leader of the Hunter Clan any more..."
    rolf "A true leader should always be the first to face the danger"
    rolf "I think it's time to pass this honor to the next generation"
    scene v4009
    with dissolve
    rolf "But first I need to find out who did this...And make them pay!"
    rolf "Even if it's the last thing I do..."
    scene v4008
    with dissolve
    rolf "You should return to the Mage College now"
    MC "Aren't you coming with me?"
    rolf "No..."
    scene v4010
    with dissolve
    rolf "I need to bury my friends, and try to find out who did this..."
    MC "But..."
    rolf "It's better if we split up while looking for clues"
    MC "Very well"
    rolf "I will let you know if I find something"
    MC "I'll do the same, Rolf"
    "You focus your magic into the gem as the Archmage told you to"


    scene meanwhile
    with dissolve
    scene v4011
    with dissolve
    brutus "Is there anything else you need my Lord"
    tiberius "No, you can leave me alone for now"
    tiberius "Just keep on guard and call me if anything important happens"
    brutus "Yes my Lord"
    sol "My Lord my Lord!"
    scene v4012
    with dissolve
    tiberius "What's this about!?"
    brutus "Grrr..."
    sol "I apologize... But...I think... We... We found it..."
    scene v4013
    with dissolve
    tiberius "YOU WHAT?!"
    sol "My Lord..."
    tiberius "What are we waiting for? Take me there!"
    sol "Yes... Of course my Lord"
    scene v4014
    with dissolve
    sol "We brought it here to the camp as instructed"
    tiberius "Let's see if you did a good job"
    tiberius "Brutus come with me"
    brutus "Very well my Lord"
    scene v4015
    with dissolve
    sol "We found it in the last cave we looked in"
    tiberius "I hope you are not mistaken..."
    sol "I... I really believe it's what you are looking for my Lord"
    scene v4016
    with dissolve
    tiberius "Come on... Move it.."
    sol "There it is"
    tiberius "Umm?"
    scene v4017
    with dissolve
    sol "See... That's what we've been looking for right?"
    tiberius "It can't be... She was right..."
    sol "Is this the thing my Lord?"
    tiberius "..."
    scene v4018
    with dissolve
    tiberius "It is... Ahahah! Ahahah! Finally! it's mine!"
    tiberius "Ahahah after all this time"
    sol "It's glowing my Lord what does it mean?"
    tiberius "It means... That we've won this war!"
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene black
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    with dissolve
    scene portalroom
    with dissolve
    "You are back in the College"
    MC "What should I do now?"
    $ v40npmida = 1
    jump afterorcv39

label v40midaroom:
    if v4midajoined == 1:
        scene v4158
        with dissolve
        amida "What are we doing here?"
        amida "Shouldn't we get going?"
        jump afterorcv39

    elif v40npmida == 2:
        scene v4159
        with dissolve
        amida "So, are you ready to go?"
        menu:
            "Yes, let's get going":
                $ v4midajoined = 1
                "Mida is now traveling with you"
                jump afterorcv39
            "I'm not ready yet":
                amida "Oh... Ok I'll wait here for you"
                jump afterorcv39
    elif my_path_is == "evil":
        scene v4153
        with dissolve
        "You enter Mida's room and she is looking for something"
        amida "They didn't touch much... But where is my robe?"
        amida "Maybe the chest..."
        MC "Yeah Fannay was trying to steal a book of yours, but I caught her"
        MC "It's in my room now"
        amida "I'll get it back later"
        scene v4154
        with dissolve
        MC "So Mistress Qa'arra wants me to travel to the City for her, want to come along?"
        "She opens the chest by the foot of her bed"
        amida "That sounds fine, let me finish getting ready"
        amida "I have some things I want to look for anyway"
        amida "Ah.... Here it is..."
        "Your vision is drawn to her perfect ass"
        "Should you do something about it?"
        menu:
            "[abgreen]Feel her ass":
                MC "I can't resist..."
                scene v4155
                with dissolve
                "You move your hand to her bottom and give it a nice squeeze"
                if midaown == 2:
                    scene v4157
                    with dissolve
                    amida "Oh come on... Really?"
                    MC "What..?"
                    amida "What?! You told Bredita you had no interest in me"
                    amida "Now you try to grope me, that's what!"
                    "She's right you know"
                    menu:
                        "[abgreen]Apologize":
                            $ midaforgive = 1
                            MC "Look... I'm done nothing but regret it... I made a mistake"
                            scene v4156
                            with dissolve
                            amida "..."
                            amida "I'll think about that..."
                            amida "We should go now"
                            jump v40midapostdress
                        "Fuck it":

                            MC "I don't care, your ass looked great so I grabbed it"
                            amida "Well then keep your hands to yourself"
                            amida "Touch me again and see what happens"
                            amida "I belong to the Mistress now"
                            amida "We're only working together because she made me"
                            $ midalove = 0
                            "Mida love decreased... a lot"
                            jump v40midapostdress

                elif midalove >=3 or midacorr >=3:
                    scene v4156
                    with dissolve
                    amida "Hmmm... You naughty boy... But now is not the time for fun..."
                    MC "No fair, you look so good"
                    amida "We'll never get to the City if I give in"
                    amida "But... maybe later...My love..."
                    jump v40midapostdress
                else:
                    scene v4157
                    with dissolve
                    amida "Oh come on... We don't have time for this"
                    amida "You're always the same... Hands off..."
                    "Your relationship with her is too low, be careful"
                    MC "..."
                    jump v40midapostdress
            "Do nothing":

                jump v40midapostdress
    else:

        scene v4152
        with dissolve
        "You enter Mida's room and she is standing near her hutch"
        amida "Hello [MC]"
        MC "Hi Mida what are you doing?"
        amida "I was getting ready to go to the City"
        MC "To the City? I'm actually going there as well"
        amida "In that case, shall we go together? Let me get changed quick"
        scene v4153
        with dissolve
        "She removes her dress and stares at you"
        MC "Mmm"
        amida "Behave"
        amida "Now where did I put it?"
        "She is looking around the room for something"
        scene v4154
        with dissolve
        "She opens the chest by the foot of her bed"
        amida "Here it is..."
        "Your vision is drawn to her perfect ass"
        "Should you do something about it?"
        menu:
            "[abgreen]Feel her ass":
                MC "I can't resist..."
                scene v4155
                with dissolve
                "You move your hand to her bottom and give it a nice squeeze"
                if midalove >=3 or midacorr >=3:
                    scene v4156
                    with dissolve
                    amida "Hmmm... You naughty boy... But now is not the time for fun..."
                    MC "No fair, you look so good"
                    amida "We'll never get to the City if I give in"
                    amida "But... maybe later...My love..."
                    jump v40midapostdress
                else:
                    scene v4157
                    with dissolve
                    amida "Oh come on... We don't have time for this"
                    amida "You're always the same... Hands off..."
                    "Your relationship with her is too low, be careful"
                    MC "..."
                    jump v40midapostdress
            "Do nothing":

                jump v40midapostdress

label v40midapostdress:
    scene v4158
    with dissolve
    amida "All set, ready to go"
    menu:
        "Wow... That's a badass robe[ablovecolor] [ablove]" if midaown != 2:
            amida "Right?"
            scene v4159
            with dissolve
            amida "I always liked black, so it makes sense to have a black robe"
            MC "Please don't hurt me miss Necromancer..."
            amida "Ahahah!! Prepare for my Ultimate Spell!!!"
            scene v4160
            with dissolve
            amida "The kiss of death..."
            amida "{i} Mwuah"
            MC "Oh no... I feel my powers vanishing..."
            scene v4159
            with dissolve
            amida "Ahahah No one will stop me now..."
            MC "Oh no, I am dying.... but what a great way to go..."
            $ midalove +=1
            "Mida now loves you more"
            $ v40npmida = 2
            jump v40midaroom
        "Yeah... Ok...":


            scene v4159
            with dissolve
            amida "Ok, let's go"
            $ v40npmida = 2
            jump v40midaroom

label v4allesterramap:
    scene allesterra
    call screen v4allesterramap



label v4farmallesterra:
    "Yeah, I don't think I should take Mida there, Karelia might make things awkward"
    jump v4allesterramap

label v4dontgothere:
    "There is no reason to go there"
    jump v4allesterramap

label v4shipallesterra:
    "There is no reason to go there"
    jump v4allesterramap



label v4villageallesterra:
    scene villagedesert
    with dissolve
    "Looks like there's nobody in the streets..."
    MC "weird..."
    $ event_dice = renpy.random.randint(1, 4)
    if event_dice == 1:
        scene v4176
        with dissolve
        thug "Look what we got here..."
        thug2 "And look at that hot chick..."
        thug "Looks tasty..."
        MC "Hey back off!"
        thug "Don't worry baby, we'll show you a good time"
        thug2 "Let's kill him already, we can take our time with her"
        amida "My love, lets show them what they got themselves into"
        MC "With pleasure, Mida"
        $ companion = 1
        $ companion_name = "Mida"
        $ enemy = "v4thugs"
        jump combat
    else:

        MC "Time to go..."
        jump v4allesterramap

label v4collegeallesterra:
    "Time to return to the college"
    jump afterorcv39

label v4dock:
    if v4helpdwarf == 1:
        scene v4173
        with dissolve
        dwarf "Oh... Hello... No more rats here"
        MC "Good to know"
        "You leave"
        jump v4allesterramap
    else:

        scene v2053
        with dissolve
        "You see a small statue man"
        scene v2054
        with dissolve
        dwarf "What the fuck! You... I remember you!"
        dwarf "What are ya doin here?"
        scene v2055
        with dissolve
        dwarf "Came to mock me did you?"
        dwarf "Even brought a pretty girl to mock me more?"
        menu:
            "I don't have time for this...":
                MC "Right... Bye.."
                jump v4allesterramap
            "[abgreen]Mock you? Why would I mock you?":

                scene v2056
                with dissolve
                dwarf "Cause of the fucking rats!!"
                dwarf "Rats everywhere, eatin me food"
                scene v4165
                with dissolve
                amida "Who's this little fellow?"
                dwarf "Little? You..."
                amida "Oh calm down... Tell us what's wrong"
                amida "Maybe we can help you"
                dwarf "I..."
                "Apparently he's having trouble being his normal self around a beauty like Mida"
                scene v4166
                with dissolve
                amida "Right [MC]?"
                menu:
                    "We don't have time for this":
                        MC "Let's go..."
                        jump v4allesterramap
                    "[abgreen]Sure, what's the problem?":

                        $ v4helpdwarf = 1
                        dwarf "You'll help me?"
                        MC "Sure..."
                        scene v4169
                        with dissolve
                        dwarf "Rats... Rats everywhere!"
                        dwarf "I don't know what to do... They won't fucking leave"
                        scene v4165
                        with dissolve
                        amida "Can you show us where?"
                        dwarf "Where??! Everywhere! Look!"
                        scene v4170
                        with dissolve
                        "You see a bunch of rats roaming around"
                        dwarf "See? And this is just a fucking small part of them"
                        dwarf "Fucking rats...."
                        scene v4171
                        with dissolve
                        dwarf "You think you can fucking kill them?"
                        MC "Hmm...I have a better idea..."
                        "You cast Fear on the rats"
                        scene v4172
                        with dissolve
                        "The rats start to run away"
                        dwarf "What the fuck?!"
                        MC "There really was a lot of them..."
                        scene v4173
                        with dissolve
                        MC "There you go, no more rats"
                        dwarf "What the sorcery is this?"
                        MC "Exactly that, sorcery. I made the rats leave with a spell."
                        dwarf "I... Here... Have some payment"
                        menu:
                            "Thank you[abgreen] [abalignment] [abgold10]":
                                $ Points += 1
                                $ Gold += 10
                                play sound "sounds/coin.ogg"
                                "You gained 1 point and 10 gold coins"
                                scene v4175
                                with dissolve
                                amida "See, I told you we could help"
                                MC "Well, time to go"
                                amida "See you litte man"
                                dwarf "Little... You..."
                                jump v4allesterramap
                            "Thank you but keep it, I don't need it[abgreen] [abalignment2]":

                                dwarf "Really?"
                                $ Points += 2
                                "You gained 2 points"
                                scene v4175
                                with dissolve
                                amida "See, I told you we could help"
                                MC "Well, time to go"
                                amida "See you litte man"
                                dwarf "Little... You..."
                                jump v4allesterramap
                            "10 Gold! What is this joke?![abred] [abnoalignment] [abgold17]":

                                MC "You better cough up some more!"
                                dwarf "I... Here, that's... All I have..."
                                $ Points -= 1
                                $ Gold += 17
                                play sound "sounds/coin.ogg"
                                "You lost 1 point and gained 17 Gold coins"
                                MC "Well, time to go"
                                scene v4175
                                with dissolve
                                MC "Let's go Mida we have stuff to do"
                                amida "That was a little harsh..."
                                jump v4allesterramap


label v4forestallesterra:
    scene v15mission020
    with dissolve
    "You're at the forest"
    menu:
        "[abgreen]Look around the forest":
            $ event_dice = renpy.random.randint(1, 3)
            if event_dice == 1:
                "As you are looking around the forest"
                play sound "sounds/bear.ogg"
                scene v15mission025
                with dissolve
                "A wild bear appears"
                scene v4177b
                with dissolve
                MC "Back for more are you?"
                amida "Do you know this bear?"
                MC "Yeah, I ran into him on my first mission"
                amida "I think he's going to attack us!"
                MC "Get ready!"
                $ companion = 1
                $ companion_name = "Mida"
                $ enemy = "v4bear"
                jump combat
            else:

                scene v15mission021
                with dissolve
                "You find nothing unusual"
                jump v4forestallesterra
        "Leave the forest":
            MC "There is nothing to do here"
            jump v4allesterramap


label v4cityallesterra:
    if v4talklwithrunar == 1:
        scene v2052
        with dissolve
        sol "You again? Lord Runar doesn't want to see you know"
        menu:
            "You know I can kill you right?":
                sol "What?! I..."
                scene v4177c
                with dissolve
                amida "Please let's go... Don't cause any problems here"
                MC "Very well..."
                scene v2052
                with dissolve
                MC "You were lucky... This time..."
                jump v4allesterramap
            "[abgreen]Leave":
                jump v4allesterramap
    else:

        scene v2052
        with dissolve
        sol "Welcome to the great Allesterra City"
        sol "What do you want from here?"
        MC "I need to speak with Runar"
        sol "Runar? Lord Runar? And who are you?"
        MC "I... Work for him"
        sol "Hmmm... Follow me then..."
        "You and Mida follow the guard"
        scene black
        with dissolve
        scene v2215
        with dissolve
        sol "Lord Runar, this man is here to speak with you"
        runar "OH? You? I thought you were dead..."
        runar "You can leave us..."
        sol "Very well, sir"
        scene v2216
        with dissolve
        runar "So... You're here... And who's the girl?"
        MC "It doesn't matter, we have some matters to discuss"
        scene v2217
        with dissolve
        runar "Ahahaha, what matters? I lost my ship"
        runar "You were supposed to find it"
        MC "I know what you did..."
        scene v021001
        with dissolve
        runar "Seems we have a smart one here..."
        runar "What do you think we should do?"
        scene v021002
        with dissolve
        runar "Yes... We should teach him a lesson don't you think?"
        MC "You could try... And we would see about that"
        scene v2217
        with dissolve
        "There is a mix of confusion and surprise on Runar's face"
        runar "Hmmm... I like you..."
        runar "So tell me what you want"
        jump v4runartalk

label v4runartalk:
    scene v2217
    with dissolve
    menu:
        "About the Lumberjack..." if helpjackv2 == 1:
            runar "That again... That's settled"
            MC "Settled? How is that?"
            scene v2216
            with dissolve
            runar "That bastard ran away... He's nowhere to be seen"
            runar "If you find him and bring him to me I'll pay you"
            MC "Are you trying to trick me?"
            scene v2217
            with dissolve
            runar "You can think that if you want, what will that help?"
            runar "Find him, I'll pay you"
            "That's odd, you'll need to keep an eye open for clues"
            "There's more to it than what this bastard is saying"
            MC "..."

            $ helpjackv2 = 2
            jump v4runartalk
        "There is someone locked here":

            runar "Someone? There are lots of someones here"
            MC "It's a certain Jithak..."
            runar "Oh... I see... He's not here anymore"
            MC "He's not? Where is he?"
            runar "He left on the last ship... But..."
            MC "But what?"
            runar "Nevermind..."
            MC "Just tell me what I need to know..."
            scene v2216
            with dissolve
            runar "He escaped on a certain ship, I'm getting another ready to go after him"
            runar "You can come with us if you want..."
            "Here we go again..."
            scene v4161run
            with dissolve
            amida "You can't possibly be serious..."
            amida "We should return to the College and consider what to do next"
            MC "Yeah... I agree, this guy is not trustworthy..."
            MC "I need to talk with Mistress Qa'arra about this"
            amida "I want to do something here in the city first"
            MC "Ok... What do you want to do?"
            amida "I'll tell you on the way"
            MC "Very well"
            $ v4talklwithrunar = 1
            scene black
            with dissolve
            scene v2169
            with dissolve
            "You and Mida walk around the city..."
            "You talk a bit about her childhood"
            "She tells you of her family, her heritage"
            "That's why she decided to tag along with you, to look for clues about her aunt"
            "Concentrated on her task, she looks down every street"
            "...Until she decides to enter a shop"
            scene v41076
            with dissolve
            shop "Hello, welcome to my shop do you want to see my wares?"
            amida "Hello thank you, actually I'm looking for someone"
            shop "Oh... Ok... And who would that be?"
            amida "It's a woman, I guess she would look like me..."
            amida "Only older... she would have been here in the City around 15 years ago?"
            shop "I don't think so... I don't recognize your features"
            shop "I do recognize the handsome man you're with though"
            scene v41077
            with dissolve
            amida "You do?"
            if holewallshop == 1:
                shop "I do, he helped me with some rat problems a few weeks ago"
                MC "Yup... Rats... "
                shop "And he was also looking for a missing ship"
            else:

                shop "Yeah he was here some weeks ago looking for the missing ship"

            shop "Did you manage to find it?"
            MC "That's a long story... Maybe I can tell it some other time"
            amida "I... I guess I'll give up for today"
            amida "What should we do now?"
            scene v41078
            with dissolve
            MC "We should return to the College, and give the news to Mistress Qa'arra"
            amida "Very well..."
            scene v41076
            with dissolve
            shop "You said the College? The Mage College?"
            amida "Yes..."
            shop "I do remember a dark haired woman with a young girl some years ago"
            shop "I'm pretty sure she was royalty, and there was a rumor..."
            amida "What rumor?"
            shop "That she left the child in the College"
            scene v41077
            with dissolve
            MC "What makes you say that?"
            shop "We do see strangers with babies and children from time to time"
            shop "They arrive at the docks with the children and leave alone"
            shop "And I know that the Mages accept children gifted with magic"
            scene v41076
            with dissolve
            amida "And that woman you were talking about, why did you mention it?"
            shop "Unlike the others, she arrived with the child... But..."
            amida "But what?"
            shop "She never returned... I never saw her again..."
            shop "With or without the young girl..."
            shop "And now that I look at you, I do see the resemblance"
            amida "Is there anything else you can tell me about her?"
            shop "I'm sorry... That's all I know..."
            amida "What about..."
            scene v41077
            with dissolve
            MC "Mida... we should go, it's getting late. I promise we'll come back again to look for clues"
            shop "You should stay at the tavern for the night"
            shop "There is a storm coming"
            shop "And you'll certainly be caught in it if you try to travel now"
            scene v41076
            with dissolve
            shop "Also, it's the best place to ask around about everything"
            amida "Thank you for everything, good bye"
            scene v41rain
            with dissolve
            "You leave the shop, it's raining a lot outside"
            "You and Mida run to the tavern, luckily it's not too far away"
            scene v41079
            with dissolve
            "You are now in the tavern and it looks pretty empty"
            "With only about one or two other patrons"
            "You see a familiar face, the tavern keeper"
            amida "I'll ask the owner for a room"
            scene v41080
            with dissolve
            amida "Hello sir, do you have any spare rooms for tonight?"
            "You can see by his lustful look that nothing else matters"
            keeper "Oh... Hello cutie... A room for you? Of course..."
            keeper "Do you need company too? I can give you some..."
            MC "Actually..."
            scene v41081
            with dissolve
            keeper "You... I... remember you... You're that Mage..."
            MC "Yes I am... As is she... Do you still want her company?"
            keeper "Well I... I was just messing around hehehe you know..."
            keeper "You know right? {i} gulp"
            scene v41080
            with dissolve
            amida "Do you have a room or not?"
            keeper "I... I... Yes..."
            scene v41082
            with dissolve
            keeper "You just sit on that table, make yourself at home"
            keeper "Eat and drink, I'll get a room ready for you"
            scene v41083
            with dissolve
            "You sit at the table with Mida"
            keeper "It may take a bit... I wasn't expecting more people tonight"
            keeper "But I'll return as soon as the room is ready"
            keeper "Meanwhile eat and drink all you want, please"
            MC "Very well..."
            amida "Thank you, kind sir"
            scene v41084
            with dissolve
            "You and Mida are now alone at the table"
            amida "Why was he so afraid of you? What did you do?"
            MC "Me? I did nothing... I think he is just afraid of Mages"
            amida "Sure... I'll pretend I believe that"
            "You both spend some time drinking mead and talking"
            MC "By the way... You came here looking for a woman"
            MC "Can you tell me more about who you are looking for?"
            scene v41087
            with dissolve
            amida "In fact... I'm looking for my parents..."
            amida "I don't remember them very well... I was about five... I think"
            MC "Do you remember being left at the College?"
            amida "I do remember my aunt, she was the one taking care of me"
            amida "And I think she was the one that left me there"
            scene v41088
            with dissolve
            "You and her drink some more and talk about her first years in College"
            "She had been there for years before you arrived"
            "And had a pretty lonely time back then, being so young"
            "Since classes only start once students are at least ten"
            scene v41087
            with dissolve
            "With the the drinking having some effect"
            "She reveals her secret crush on the Archmage, something you always suspected"
            "Ayna had always acted kindly and lovingly toward her since she was a small girl"
            scene v41086
            with dissolve
            amida "Also she is so pretty... I wish I could be like her {i} hic"
            amida "Powerful and beautiful... {i} giggle... hic"
            scene v41084
            with dissolve
            MC "Yes she is... but you are already beautiful, so you're half way there"
            MC "Thankfully, I am already powerful and beautiful, so I can show you how!"
            scene v41085
            with dissolve
            amida "Ahahah... You're funny.... {i} hic"
            MC "Only when you're drunk.... Ahahaha"
            scene v41086
            with dissolve
            "You are both pretty drunk right now but Mida..."
            "Mida looks a lot more drunk than you..."
            amida "Bottoms up!!"
            scene v41088
            with dissolve
            "You and her get some more drinks"
            keeper "Excuse me..."
            scene v41089
            with dissolve
            MC "Wha... What?"
            keeper "Your room is ready..."
            amida "That's great! I'm horny... {i} hic..."
            scene v41090
            with dissolve
            keeper "Uhmmm... I...."
            amida "I need some cock tonight... {i} giggle"
            "She is very, very drunk..."
            MC "Hey Mida... "
            scene v41091
            with dissolve
            amida "Oh come on! Don't you want to? {i} hic"
            amida "We can take some mead with us right sir?"
            "He doesn't even know what to say"
            keeper "I... I..."
            amida "See? It's ok... Let's go"
            scene v41092
            with dissolve
            MC "Ok.. Ok let's go"
            keeper "The room is just upstairs"
            MC "Thanks"
            keeper "Lucky bastard..."
            scene v41093
            with dissolve
            "You and Mida reach the room upstairs"
            amida "Look... It's not as bad as I expected..."
            MC "Sure..."
            scene v41094
            with dissolve
            amida "{i} giggle"
            amida "I'm horny [MC], and it's all your fault"
            amida "What do you have to say in your defense?"
            menu:
                "I think we should go to sleep now[abred] [abnocorruptionlove]":
                    scene v41095
                    with dissolve
                    amida "I... Ok fine..."
                    $ midacorr -= 1
                    $ midalove -= 1
                    "Mida love and corruption decreased"
                    "You both go to sleep, you share the same bed"
                    "But nothing else happens that night"
                    scene black
                    with dissolve
                    jump v41morningmida
                "[abgreen]I think I'd like to see proof of this horniness":

                    $ fuckmidadouble = 1
                    amida "You do?"
                    scene v41096
                    with dissolve
                    "She pushes you to the bed"
                    amida "Should I take off this robe? I should... Right?"
                    "You just nod"
                    scene v41097
                    with dissolve
                    "She removes her robe and throws it away"
                    amida "That look in your eyes, so predictable... {i} giggle "
                    scene v41098
                    with dissolve
                    amida "What should I do now? {i} hic"
                    amida "Maybe take off some more clothes?"
                    scene v41099
                    with dissolve
                    "She removes her brassiere"
                    amida "Oops... It's off {i} giggle"
                    "Just like she did with her robes, she throws it away"
                    scene v41100
                    with dissolve
                    amida "Oh... The door is open... Were you trying to show me off?"
                    amida "You're naughty..."
                    amida "Sorry, this is a show for an audience of one only"
                    "With as sexy as she was acting, you had actually forgot about the door entirely"
                    scene v41101
                    with dissolve
                    "She closed the door and faced you again"
                    amida "I think you need some extra punishment for this {i} giggle"
                    "You start to feel her casting something"
                    scene v41102
                    with dissolve
                    MC "Wait... What are you doing? Hold on..."
                    amida "Get ready for your punishment"
                    show shot
                    with hpunch
                    hide shot
                    scene v41103
                    with dissolve
                    "You see two Midas in front of you"
                    MC "Wow... I'm either very drunk or this is the best dream ever..."
                    amida "{i} giggle {/i} You are drunk... But this is real"
                    scene v41104
                    with dissolve
                    amida "I've been practicing this spell, what do you think?"
                    MC "Holy shit... Is this an Illusion?"
                    amida "Yes... And no... {i} giggle"
                    MC "What do you mean?"
                    amida2 "Let us show you"
                    scene v41105
                    with dissolve
                    "One of the Midas grabs your cock and starts to stroke it"
                    MC "Oh.... "
                    amida "You like this don't you?"
                    amida2 "Of course you do... Look at you, so hard on my hand"
                    MC "I love it..."
                    amida "{i} Giggle"
                    scene v41106
                    with dissolve
                    "They sit on the bed, the one that was stroking your cock"
                    "Is now licking the tip of your dick"
                    "While the other is playing with her breasts and teasing you"
                    amida "You're so hot right now..."
                    amida "I never imagined I would like to see this so much"
                    amida "It's still me, but it's so hot to see her suck you"
                    amida "Hmmm... I'm so wet... Look..."
                    "You put your fingers near her entrance"
                    "You feel all those fluids oozing out"
                    scene v41107
                    with dissolve
                    "You grab her waist and land her ass on your face"
                    amida "Ahh..... Yes.... Lick my pussy!!"
                    amida2 "Hmmm your balls are so tasty"
                    amida "And your dick... It's so hard... So hot..."
                    "If this is a dream you don't want to wake up"
                    MC "Ah shit.... Mida... This is great!"
                    MC "I can't take it anymore, I need you feel your pussy"
                    scene v41108
                    with dissolve
                    "You grab Mida and force her on all fours"
                    "While the other lies down on her back and keeps licking you"
                    "As if to lubricate your dick for the other Mida"
                    amida "Hmmm so forceful..."
                    scene v41109
                    with dissolve
                    "As you start to bury the tip of you penis into Mida"
                    "The other one moves her face close to the action"
                    "While spreading Midas ass cheeks to give you full access"
                    amida "Ahh.... It's going in... Hmmm so good"
                    MC "You're so wet and hot Mida..."
                    "You don't know if this is the alcohol or not"
                    "But in case this is a one time thing, you decide to enjoy it to the fullest"
                    scene v41110
                    with dissolve
                    "You start to move your hips faster and faster"
                    "Giving her everything you got"
                    "One Mida jumps on top of the one you're fucking"
                    amida2 "Yeah!! Fuck her hard! Kiss me!"
                    "You start to feel your orgasm build up"
                    MC "Ah... This is too good.... I'm..."
                    amida "Don't stop now!! Fuck me more!! Make me cum!!"
                    scene v41111
                    with dissolve
                    "You're doing the best you can, pumping in fast and hard"
                    amida "AHHH!!! YES!!!"
                    amida2 "Yes, give her more... She's about to cum"
                    amida "AHHHHHH.... YEEES!!"
                    "You feel her insides squezing your dick hard"
                    "That makes you even closer to climax"
                    amida2 "Now it's my turn... I want to cum too"
                    MC "But... I..."
                    scene v41112
                    with dissolve
                    "Before you could say anything else she's on top of you"
                    amida2 "Yes... Put his dick inside me"
                    amida "It's great isn't it?"
                    amida2 "Yes...Yes! it's amazing"
                    "She starts to move, in no time she's riding you at full speed"
                    scene v41113
                    with dissolve
                    amida2 "Yes!!! So big... So hard... I'm about to..."
                    amida2 "CUUUUUUUUM!!! AHHH!"
                    amida "Good girl..."
                    "That was you limit you can feel your orgasm comming"
                    amida "Hurry move, he's about to cum"
                    scene v41114
                    with dissolve
                    "The Mida that was on top of you gets of to your side"
                    "While the other puts your dick in her mouth and starts to stroke"
                    MC "AH.... I can't take it any more..."
                    scene v41115
                    with dissolve
                    amida "Yes cum for me, cum all over us"
                    amida2 "Yes, let us taste your cum"
                    MC "Shit I'm about to..."
                    show shot
                    with hpunch
                    hide shot
                    scene v41116
                    with dissolve
                    show shot
                    with vpunch
                    hide shot
                    MC "FUUUCK!! Yeah....."
                    amida "So much... {i} Giggle"
                    amida2 "Hmmm..."
                    scene v41117
                    with dissolve
                    "You feel numb, you don't know if it's the alcohol"
                    "Or if it's because you spent all your energy"
                    "But at least you can still feel the girls lapping the cum out of you"
                    MC "Ah shit.... I can die happy now..."
                    "If this was not the best fuck ever it's near the top"
                    scene v41118
                    with dissolve
                    "The illusion Mida vanishes, but the real one is still close to you"
                    amida "Did you like it?"
                    MC "Fuck... This was the best thing ever..."
                    amida "Do you want me to act more like a slut for you?"
                    menu:
                        "Hell yeah! You're my dirty slut[abcorruptioncolor] [abcorruption]":
                            amida "Hmmm this cum... so tasty"
                            "She cleans all the cum on her face and puts it on her mouth"
                            amida "Your slut loves to swallow your cum"
                            $ midacorr +=1
                            $ fuckmidadouble = 2
                            "Mida corruption increased"
                        "I like the romantic way more[ablovecolor] [ablove]":

                            "She cleans all the cum on her face"
                            scene v41119
                            with dissolve
                            amida "Oh... You're so cute..."
                            $ midalove +=1
                            "Mida love increased"

                    scene v41120
                    with dissolve
                    "After all that, she collapses on the bed with a smile on her face"
                    MC "Mida?"
                    MC "... Mida?... Do you hear me?"
                    MC "She fell asleep..."
                    "You wonder if this was all the booze fault"
                    if midaown == 2:
                        MC "She was pretty pissed earlier because of Bredita thing"
                    MC "We'll see how it works out tomorrow morning..."
                    MC "But this was one hell of a fuck... Damn..."
                    "You start to shut your eyes close"
                    scene black
                    with dissolve
                    "You fall asleep"

label v41morningmida:
    if fuckmidadouble == 0 or midaown == 2:
        amida "Hey, wake up!"
        MC "Hmmm what?"
        amida "Come on, we have stuff to do"
        scene v41124
        with dissolve
        "You open your eyes and see Mida"
        if fuckmidadouble != 0:
            amida "I'm not sure what happened last night"
            amida "But it's time you get dressed and we leave"
            MC "Ok..."
            "Doesn't she remember, or is she pretending?"
        else:
            amida "So, are coming or what?"
            "She's not happy..."
    else:
        amida "Yawn... My head..."
        MC "Hmmmm what?"
        scene v41121
        with dissolve
        "You open your eyes and see Mida, naked"
        MC "Ah... My head..."
        "You head feels like it was slapped by a bear"
        "Mida starts to dress"
        scene v41122
        with dissolve
        amida "Oh... You're awake already, do you remember last night?"
        MC "I think I remember most of it..."
        scene v41123
        with dissolve
        "She dressed her robe"
        amida "{i} Giggle..."
        amida "I'm glad you do... We should return to the College now"
        MC "Right..."
    scene v41125
    with dissolve
    "You get dressed and you both leave the room"
    scene v41080
    with dissolve
    keeper "Did you have a good night?"
    amida "Here, take this for your trouble"
    "You see Mida paying for the tavern services"
    scene v41081
    with dissolve
    amida "Ready to go now?"
    MC "Sure, lead the way"


    if v4sideq == 0:
        "You and Mida travel to the college"
        jump afterorcv39
    else:
        jump v4allesterramap

label v4roomstonecontrol:
    scene mcroombg01
    with dissolve
    MC "Should I lay down a bit and rest?"
    fvoice "Hai!"
    MC "I know this voice... Looks like it's coming from the garden..."
    "You get closer to the window and peek outside"
    scene v41052
    with dissolve
    "You see Koneko and Ryo talking about something... But you don't understand them"
    "Not only they are to far, they are speaking a language you don't understand"
    ryo "{i}Unintelligible"
    scene v41053
    with dissolve
    akoneko "Nani?"
    ryo "{i}Unintelligible"
    akoneko "{i}Unintelligible"
    MC "I can't understand a word... But looks like Ryo is asking for something"
    scene v41054
    with dissolve
    MC "And they seem to have reached some sort of agreement..."
    akoneko "It's a deal!"
    ryo "Arigato Koneko"
    scene v41055
    with dissolve
    "You see Ryo leaving the garden, leaving Koneko there alone"
    MC "I guess this would be a great time to have a talk with Koneko"
    scene black
    with dissolve
    scene v41056
    with dissolve
    "You move to the garden and you can see Koneko practicing some spell"
    "You get closer to her"
    scene v41057
    with dissolve
    MC "Hello Koneko, it's nice to see you again."
    MC "I don't think I've really seen you since Graduation"
    "Except in the bath..."
    scene v41058
    with dissolve
    akoneko "Yes, it's great to see you again..."
    if konekolove >= 1:
        scene v41060
        with dissolve
        akoneko "I can't tell you how much that smile you gave me boosted my confidence"
        MC "Nonsense, you just needed a push, you were impressive on your own"
    scene v41058
    with dissolve
    MC "So are you and Ryo old friends?"
    akoneko "Oh.. no actually we just met. Also... um.. We're from different countries..."
    MC "Oh well now I feel like an ass"
    scene v41060
    with dissolve
    akoneko "No, it's fine."
    akoneko "You wouldn't be able to tell people from either apart, unless they told you"
    akoneko "In fact, the two countries used to be one large empire a long time ago."
    scene v41062
    with dissolve
    akoneko "So you could say we're like cousins of a sort"
    MC "Wow, I had no idea. So what have you been up to lately?"
    scene v41060
    with dissolve
    akoneko "Actually I've been studying with Qa'arra"
    MC "That's great. It seems like quite a few of our class are getting lessons from the Elite"
    scene v41062
    with dissolve
    akoneko "Like there was ever doubt you would, you were the golden boy"
    MC "Stop, it was nothing like that"
    akoneko "But yes, I'm happy to still be here at the school..."
    scene v41065
    with dissolve
    akoneko "It's a far better fate than what I could have had gone through..."
    MC "What do you mean?"
    akoneko "Well, I'm the daughter of a province lord."
    akoneko "My brother is in line to take over the family when my father steps down"
    akoneko "But my sisters have been used for..... political marriages with other lords."
    scene v41061
    with dissolve
    akoneko "Sometimes... to some of the ugliest ancient looking among them."
    akoneko "But as for me, I'm a mage, so I've been saved from that particular fate"
    scene v41062
    with dissolve
    MC "That.... is really horrible. I guess it makes me happy that I'm a nobody with no past."
    MC "I have no family obligations like you do"
    MC "But since you're free of that fate, what will you do when your training is done?"
    MC "Stay here at the College?"
    scene v41061
    with dissolve
    akoneko "Oh...no...I may not need to marry for political reasons, but I'm obligated to return."
    akoneko "Most likely I'll be expected to become a Mage for our Emperor's court."
    scene v41065
    with dissolve
    akoneko "Most likely I will also become his concubine..."
    akoneko "There are worst fates I could imagine..."
    scene v41062
    with dissolve
    MC "Koneko... I understand family must be important to you..."
    MC "But you do remember you're a mage, right?"
    MC "You are more powerful than any of them combined."
    scene v41058
    with dissolve
    MC "You don't have to do anything you don't want to."
    akoneko "[MC]... Obligation is something..."
    scene v41061
    with dissolve
    akoneko "... One must maintain in my culture to honor your parents and your ancestors."

    akoneko "I would dishonor them if I did not live up to what was expected of me."
    scene v41062
    with dissolve
    MC "I'm sorry, but that's bullshit. You weren't raised by them, you were raised with us."
    MC "Mida, Kitargo and I are your siblings too."
    MC "None of us would feel dishonored if you chose your own path."
    scene v41058
    with dissolve
    MC "We would feel proud of you."
    MC "Like you should feel proud of yourself and all you've accomplished"
    MC "Don't make decisions based on people who weren't there for you during all these years."
    MC "Live your own life."
    scene v41060
    with dissolve
    akoneko "Do... do you really see me like that?"
    MC "Of course... we've been friends for my whole life.... well as least these last 10 years of it."
    scene v41058
    with dissolve
    MC "You know Mida feels the same and Kitargo loves everybody..."
    MC "Except Hatoshi, but I can't blame him for that. I hate that prick too."

    scene v41059
    with dissolve
    akoneko "Ahahah... Alright, you got me {i}giggle{/i}....I promise that..."
    scene v41060
    with dissolve
    akoneko "I will definitely reconsider my options..."
    akoneko "Before making any permanent decisions that would affect my family..."
    akoneko "...Either of them"
    MC "That's the spirit. Now, if you'll excuse me I'm going back to my room to rest."
    scene v41058
    with dissolve
    MC "I've been travelling all over recently and could use a rest."
    MC "Make sure it's not as long before I see you again"
    akoneko "I promise... I... Maybe..."
    akoneko "The four of us can go to the City together and get a drink some time soon?"
    menu:
        "I'd like that a lot[ablovecolor] [ablove]":
            scene v41059
            with dissolve
            $ konekolove +=1
            "Koneko love increased"
            scene v41064
            with dissolve
            akoneko "Great, well then take care [MC], rest well"
            MC "Goodbye, Koneko"
        "We'll have to see how things go":

            scene v41065
            with dissolve
            akoneko "Oh.... right, I guess you are really busy with the Slayer war and everything"
            MC "I didn't say never..."
            akoneko "Yeah... I know. Well I'll get back to practice..."
            "Way to go there..."

    scene v41066
    with dissolve
    "As you are leaving the garden you give one last glimpse at Koneko"
    "You can see her casting something to practice"
    scene v41066a
    with dissolve
    scene v41066a
    with dissolve
    scene v41066b
    with dissolve
    "She made the flowers blossom..."
    MC "She's pretty good... {i}Yawn..."
    MC "I really need a nap now... Let's get back to my room"
    scene mcroombg01
    with dissolve
    MC "I think I need to rest a bit... I'm feeling a bit weird"
    MC "Going to lie down a bit"
    stop music
    play music "<loop 0.0>sounds/beat.mp3"
    show shotr
    with hpunch
    show shotr
    with vpunch
    hide shotr
    MC "Ahrghh..."
    Nonen "Do you feel it?"
    MC "What... ?"
    show shotr
    with hpunch
    show shotr
    with vpunch
    hide shotr
    Nonen "It's... Another part of me..."
    Nonen "Do you feel it? Do you feel the power?"
    show shotr
    with hpunch
    show shotr
    with vpunch
    hide shotr
    MC "Ahrghh... Shit... Stop this!"
    Nonen "I'm not the one responsible for it..."
    Nonen "Don't tell me you don't feel stronger?"
    MC "I..."
    $ Destpoints += 1
    $ Iluspoints += 1
    $ Healpoints += 1
    $ Mystpoints += 1
    $ Summpoints += 1
    $ Altepoints += 1
    $ Necropoints += 1
    "All your skills increased"
    Nonen "See... Imagine when we get it..."
    Nonen "How strong we... You could be"
    show shotr
    with hpunch
    show shotr
    with vpunch
    MC "Fuck!!... My head... My body..."
    Nonen "Let me ease the pain"
    hide shotr
    Nonen "Now let's go to the portal room"
    MC "What why?"
    show shotr
    with hpunch
    show shotr
    with vpunch
    hide shotr
    MC "Ahhhh!! Shit..."
    Nonen "Don't you want the pain to end? Don't you want power?"
    Nonen "Let's go to the portal room!"
    menu:
        "Yes I want more power![abkarmacolor] [abstoneuses2]":
            $ stoneuses += 2
            Nonen "Good... To the portal room..."
            stop music
            $ Points -= 1
            "You lost 1 Point"
            scene portalroom
            with dissolve
            "You reach the portal room"
            MC "Now what?"
            Nonen "Let me take care of it"
            scene v37117
            with dissolve
            MC "How did..."
            Nonen "Let's go"
            $ v4resist = 0
            $ renpy.movie_cutscene("opti/portal.webm")
            jump v4slayercity
        "Yes... Make the pain go away[abkarmacolor] [abstoneuses]":

            $ stoneuses += 1
            Nonen "Good... To the portal room..."
            stop music
            scene portalroom
            with dissolve
            "You reach the portal room"
            MC "Now what?"
            Nonen "Let me take care of it"
            scene v37117
            with dissolve
            MC "How did..."
            Nonen "Let's go"
            $ v4resist = 0
            $ renpy.movie_cutscene("opti/portal.webm")
            jump v4slayercity
        "Resist the stone temptation[abgreen] [abalignment]":

            $ Points += 1
            "You gained 1 point"
            Nonen "What makes you think you have a choice?"
            show shotr
            with hpunch
            show shotr
            with vpunch
            MC "Ahhhh!! Fuck you..."
            show blink1
            with dissolve
            show blink2
            with dissolve
            show blink3
            with dissolve
            scene black
            with dissolve
            stop music
            "You faint from unbearable pain"
            $ v4resist = 1
            jump v4slayercity

label v4slayercity:

    play music "<loop 0.0>ingame.mp3"
    scene v4118
    with dissolve
    if v4resist == 1:
        MC "What the? Where am I?"
        MC "Was it the stone?"
        "The pain seems to have passed"
    else:
        MC "Where did you bring me?"
        MC "Where are we? What? You're not speaking now?"
        "The pain seems to have passed"

    "And you start to feel normal again"
    MC "Is that a Slayer soldier? What is this place?"
    MC "Maybe I should ask around... That looks like a tavern"
    scene v4129
    with dissolve
    MC "Always a good place to ask questions..."
    jump v4tavern

label v4slayerplaza_1:
    if v4soldiergone == 0:
        scene v4118
        call screen v4slayerplaza
    else:
        scene v4scityplaza2_idle
        call screen v4slayerplaza2

label v4slayersoldier:
    if v4soldiergone == 0:
        scene v4119
        with dissolve
        "You approach the soldier"
        sol "What are you doing here? Move along"
        menu:
            "Do what he says and leave":
                MC "Fine..."
                jump v4slayerplaza_1
            "Ask where you are":
                sol "What? Poor thing... You don't know where you are?"
                sol "You are on Saciorona! One of our great cities"
                sol "Now move along I don't have time for you"
                jump v4slayerplaza_1
            "Use Fear on the soldier[abgreen] [abgold10]":
                $ v4soldiergone = 1
                "You start to cast fear on the soldier"
                scene v4120
                with dissolve
                sol "What is this?... Spiders??!!"
                sol "I hate spiders!! They're on me!! They're in my helmet!!"
                scene v4121
                with dissolve
                sol "AHHH!!! Help me!!"
                scene v4128
                with dissolve
                "He's gone..."
                MC "Oh! What's that? He dropped some gold"
                play sound "sounds/coin.ogg"
                "You found 10 gold"
                $ Gold += 10

                "He left "
                jump v4slayerplaza_1
    else:
        scene v4128
        with dissolve
        "There's nothing to see here..."
        jump v4slayerplaza_1

label v4Brothel:
    if v42check == 1:
        jump v42brothel

    elif bathadventure == 0:
        "It's locked"
        fvoice "What's the password?"
        MC "What password?"
        "...."
        "Nobody says anything else..."
        MC "Ok then..."
        jump v4slayerplaza_1
    else:

        scene v4131
        with dissolve
        "You get close to the door"
        "It's locked"
        fvoice "What's the password?"
        MC "Phoenix"
        fvoice "Welcome"
        jump v4slayerplaza_1


label v4tavern:
    if bathadventure == 0:
        scene v4129
        with dissolve
        "You get closer to the door and try to open it"
        jump v4tavernday


label v4tavernday:
    scene v4141
    with dissolve
    "It's a tavern"
    menu:
        "[abgreen]Talk with the Tavern keeper":
            if v4visiteon == 0:
                $ v4visiteon = 1
                scene v4145
                with dissolve
                keeper "Hi, you're new here right?"
                keeper "What can I get you? Mead for 1 coin?"
                MC "Actually I'm kind of lost..."
                keeper "Lost? What do you mean?"
                MC "I mean... Where are we? What is this place?"
                scene v4146
                with dissolve
                keeper "I think you need one of these... First one is on me"
                MC "Thanks... I guess..."
                fvoice "I knew I remembered that face..."
                scene v4162d
                with dissolve
                hanna "[MC] right? The Mage student..."
                MC "Oh... You're Hanna, the writer I met in the village back then"
                scene v4163d
                with dissolve
                hanna "Yes, that's me, good memory"
                "It's hard to forget such a figure..."
                MC "Yeah..."
                hanna "So what brings you here to Saciorona?"
                MC "Saciorona?"
                hanna "Yes... One of the greatest Slayer cities"
                "So you are in Slayer territory..."
                MC "Well, a magical experiment went wrong..."
                MC "I teleported myself here, no idea where I was"
                MC "I was wandering clueless and came in here."
                scene v4164d
                with dissolve
                hanna "Teleporting magic? That sounds dangerous..."
                hanna "Tell you what... Come with me, I'll show you around"
                MC "Really? Thanks!"
                hanna "It's the least I can do for a cutie like you..."
                MC "Wait, what?"
                hanna "Let's go!"
                scene v4118
                with dissolve
                "You and Hanna leave the tavern and head outside"
                "You follow her to several places in the city"
                scene v4234
                with dissolve
                hanna "This is the dock"
                hanna "I'd imagine you'll need to charter a ship out of here to get back"
                hanna "However, it doesn't seem like any ships are in port right now."
                hanna "Next..."
                scene v4236
                with dissolve
                hanna "This is the City Church... It's been closed for some reason"
                hanna "Maybe someone was doing naughty things...{i} Giggle"
                hanna "But it's been closed for a while, so who knows"
                hanna "Let's move on"
                scene v4233
                with dissolve
                hanna "This is the most luxurious bath house in the City"
                hanna "There are a few, but I personally recommend this one"
                hanna "If you're looking to unwind after your ordeal, this the place"
                scene v4232
                with dissolve
                hanna "Finally, we have my house"
                hanna "Unfortunately this ends the tour as I have some work I must get back to"
                hanna "If you need a place to stay for a day or two, I'll put you up"
                scene v4235
                with dissolve
                hanna "Anyway, enjoy your stay in our City. Goodbye [MC]"
                "She heads inside leaving you alone on the street"
                jump v4slayerplaza_1
            else:




                scene v4145
                with dissolve
                keeper "Hello again"
                keeper "What can I get you? Mead for 1 coin?"
            menu:
                "I could use a drink" if Gold >=1:
                    scene v4146
                    with dissolve
                    keeper "There you go!"
                    play sound "sounds/coin.ogg"
                    $ Gold -= 1
                    "You lost 1 coin"
                    scene v4145
                    with dissolve
                    MC "Thanks"
                    "You have a nice cold drink"
                    jump v4tavernday

                "Nothing I'm leaving" if v4visiteon >= 1:
                    keeper "See you another time then"
                    jump v4slayerplaza_1
        "Talk with the bald man":


            scene v4142
            with dissolve
            "You approach the man"
            sman "Hey! You! You're new here!"
            sman "Want to gamble a bit?"
            MC "Gamble?"
            sman "Coin gamble, heads and tails if you prefer"
            sman "You bet coins, I bet coins... The winner gets all"
            menu:
                "Not interested in gambling":
                    scene v4143
                    with dissolve
                    sman "Well, if you change your mind I'm here"
                    jump v4tavernday
                "Sure let's gamble":
                    jump v4gambleevent


        "Leave" if v4visiteon >= 1:
            jump v4slayerplaza_1


label v4gambleevent:
    scene v4143
    with dissolve
    sman "Great!! How much do you want to gamble?"
    menu:
        "1 Coin" if Gold >=1:
            $ gamblegold = 1
            scene v4142
            with dissolve
            sman "1 coin... Ok then..."
            jump v4gambleevent2
        "5 Coins" if Gold >=5:
            $ gamblegold = 5
            scene v4142
            with dissolve
            sman "5 coins... That's good..."
            jump v4gambleevent2
        "10 Coins" if Gold >=10:
            $ gamblegold = 10
            scene v4142
            with dissolve
            sman "10 coins... Ahah great!"
            jump v4gambleevent2
        "25 Coins" if Gold >=25:
            $ gamblegold = 25
            scene v4142
            with dissolve
            sman "25 coins... Now we're talking"
            jump v4gambleevent2
        "Nevermind":
            jump v4tavernday

label v4gambleevent2:
    $ dice = renpy.random.randint(1, 2)
    scene v4142
    with dissolve
    sman "Heads you win, tails I win"
    show cointail
    with dissolve
    hide cointail
    show coinhead
    with dissolve
    hide coinhead
    show cointail
    with dissolve
    hide cointail
    show coinhead
    with dissolve
    hide coinhead
    show cointail
    with dissolve
    hide cointail
    show coinhead
    with dissolve
    hide coinhead

    if dice == 1:
        show cointail
        "Tails! You lost"
        scene v4143
        with dissolve
        sman "Ahaha I win, my coin please..."
        $ Gold -= gamblegold
        play sound "sounds/coin.ogg"
        "You lost [gamblegold] coins"
        sman "Want to go again?"
        menu:
            "Yes":
                jump v4gambleevent
            "No":
                jump v4tavernday
    else:
        show coinhead
        "Heads! You win"
        scene v4144
        with dissolve
        sman "Damn it... Here take your coin..."
        $ Gold += gamblegold
        play sound "sounds/coin.ogg"
        "You got [gamblegold] coins"
        sman "Want to go again?"
        menu:
            "Yes":
                jump v4gambleevent
            "No":
                jump v4tavernday

label v4slayercitymap:
    scene v4slayercity
    call screen v4slayercitymap

label v4citychurch:
    if churchreadyv42 == 0:
        "You can't go there yet"
        jump v4slayercitymap
    else:
        jump v42church


label v4hannahouse:
    if tavernhanna == 0:
        "You can't go there yet"
        jump v4slayercitymap
    else:
        "It looks like there is nobody home"
        jump v4slayercitymap

label v4slayershop:
    if v42magicshop == 0:
        "Looks like some sort of magic shop..."
        "But it's closed right now"
    else:
        jump v42magicshop
    jump v4slayercitymap

label v4slayerdocks:
    if v42check == 0:
        "I wonder if I can use a boat to get out of here"
        "But first I need to know why I'm here"
        jump v4slayercitymap
    else:
        jump v42slayerdocks


label v4afterbath:
    scene v41067n
    with dissolve
    "You are outside the baths and it's night"
    MC "How long did I stay inside...?"
    "You feel like you're being observed"
    scene v41068
    with dissolve
    MC "What the...? Is that a person?"
    scene v41069
    with dissolve
    "You see someone dressed in black moving on a rooftop"
    MC "Is that a woman? Is she looking at me?"
    scene v41070
    with dissolve
    MC "Hey! You there!"
    scene v41071
    with dissolve
    "Your shout makes her jump of the roof"
    scene v41072
    with dissolve
    "And you can't see her anymore"
    MC "What just happened? Oh.. Fuck it"
    scene v4124
    with dissolve
    "You decide to ignore it and walk around"
    MC "What should I do now?"
    if v4soldiergone == 1:
        MC "Oh look the guard is back..."

    jump v4itsnight

label v4itsnight:


    if v4soldiergone == 3:
        scene v4127
        with dissolve
    else:
        scene v4124
        with dissolve
    if v4calessabrothelfun > 1:
        stop music
        play music "<loop 0.0>sounds/beat.mp3"
        show shotr
        with hpunch
        MC "Ah.... What is this... Not you again..."
        MC "I think I'm about to faint... I..."
        MC "I need to find a room"
        jump v4tavernstone

    menu:
        "[abgreen]Go talk with the guard" if v4soldiergone != 3:
            scene v4122
            with dissolve
            sol "What do you want?"
            menu:
                "Nothing... I'm leaving":
                    jump v4itsnight
                "Use magic to mess with the guard[abgreen] [abgold15]":

                    scene v4123
                    with dissolve
                    sol "Oh!! FUCK!! God damn it!!"
                    scene v4125
                    with dissolve
                    sol "AH!!! My face!!!"
                    scene v4126
                    with dissolve
                    "He's gone..."
                    MC "Oh! What's that? He dropped some gold"
                    play sound "sounds/coin.ogg"
                    "You found 15 gold"
                    $ Gold += 15
                    $ v4soldiergone = 3
                    jump v4itsnight
        "Go to the tavern":

            scene v4130
            with dissolve
            MC "It's late but it should be open..."
            "You try the door and it's open"
            scene v4141n
            with dissolve
            MC "Good... Maybe I should ask if there is a place to spend the night"
            "You move to the counter"
            scene v4145n
            with dissolve
            keeper "Hi there need a drink?"
            MC "Actually I'm looking for a place to stay for the night"
            keeper "Sure..."
            scene v4146n
            with dissolve
            keeper "Here have a drink while I get you the key to a room"
            MC "Thank you"
            fvoice "That one is on me"
            scene v4162
            with dissolve
            MC "Hmm?"
            MC "Is that...?"
            if hanna3some == 1:
                MC "Well... Hello there Hanna..."

            elif calessapet >= 1:
                "That's the girl that gave you the tour and was spying on you earlier"
                "Hello again, Hanna"
            else:
                "I remember this face... It's the writer from earlier"
                "Hi.. Hanna..."

            hanna "And give me one too"
            keeper "Very well"
            scene v4163
            with dissolve
            "You and Hanna chat and drink for a while"
            "You tell her all about what you've been doing since she met you in the Village"
            hanna "And what are you doing here?"
            MC "Actually I was looking for a place to stay"
            hanna "Really? Did you not remember me offering my place? It's still available"
            menu:
                "Accept[ablovecolor] [ablove]":
                    MC "That would be great!"
                    hanna "Let's go then?"
                    scene v4162
                    with dissolve
                    hanna "There you go miss"
                    keeper "Thank you come again"
                    hanna "Let's go [MC]"
                    $ hannalove += 1
                    "Hanna Likes you more"
                    jump v4hannahousenight
                "Decline":

                    MC "I'm going to pass the offer, I'll stay here"
                    scene v4164
                    with dissolve
                    hanna "Oh... Ok... In that case..."
                    scene v4168
                    with dissolve
                    hanna "See you around.. Bye"
                    MC "Bye..."
                    "She left"
                    scene v4178
                    with dissolve
                    MC "About that room..."
                    $ v4spentthenight = "tavern"
                    "You find a room and fall asleep"
                    scene black
                    with dissolve
                    stop music
                    play music "<loop 0.0>sounds/beat.mp3"
                    Nonen "Do you feel this? Do you?"
                    jump v4lustmean
        "Go to the brothel":


            scene v4131
            with dissolve
            "You get close to the door and knock"
            fvoice "Password?"
            MC "If I remeber is..."
            menu:
                "Phoenix":
                    fvoice "Welcome"
                    jump v4brothelpart
                "Hummingbird":
                    "There is no answer after this, maybe it was another type of bird?"
                    jump v4itsnight
                "I don't know":
                    "It was a bird right?"
                    jump v4itsnight
                "Leave":
                    "You leave the place"
                    jump v4itsnight

label v4tavernstone:
    scene v4141n
    show shotr
    with hpunch
    "You stumble into the tavern, disoriented and in a daze."
    show shotr
    with vpunch
    scene v4145n
    show shotr
    "You wobble and teeter, somehow miraculously managing to make your way to the bar"
    with vpunch
    "Without falling on your face."
    MC "Room... please..."
    "Before the tavern keeper can respond, a familiar face enters your vision."
    scene v4162
    show shotr
    hanna "[MC]! Are you alright? You look hammered..."
    MC "No... I..."
    "Hanna stops you before you can attempt to explain further in your sorry state."
    scene v4164
    show shotr
    hanna "I'm not letting you stay in this hovel!"
    keeper "What?! Hey!"
    hanna "You're staying at my place tonight. Let's go."
    scene black
    with dissolve
    "You feel you are walking outside while holding on Hanna"
    hanna "Here we are... [MC]? are you ok? [MC]!"
    jump v4lustmean

label v4hannahousenight:
    "You reach Hanna's place"
    scene v4019
    with dissolve
    hanna "Make yourself comfortable"
    hanna "Grab a seat if you want to"
    scene v4020
    with dissolve
    "You get closer to her"

    if hanna3some == 1:
        hanna "We had fun earlier right? Do you..."
        scene v4021
        with dissolve
        hanna "Want to have a bit more?"
        menu:
            "Not really, I want to sleep":
                jump v4sleeptime
            "[abgreen]You bet I want to":

                scene v4025
                with dissolve
                hanna "Good to know..."
                scene v4028
                with dissolve
                "She's signaling you to kiss her and that's what you do"
                jump v4hannasex


    elif calessapet >= 1:
        hanna "You know... I was at the bath house earlier"
        scene v4021
        with dissolve
        MC "I know... I saw you... Spying on me"
        hanna "I... I..."
        scene v4022
        with dissolve
        MC "It's ok... I don't mind..."
        menu:
            "[abgreen]Try to seduce her":
                "Did you enjoyed what you saw?"
                jump v4seducehanna
            "Go to sleep":

                scene v4024
                with dissolve
                MC "Sorry I need to rest now, it's been a long day"
                jump v4sleeptime
    else:

        menu:
            "[abgreen]Try to seduce her":
                jump v4seducehanna
            "Go to sleep":

                scene v4024
                with dissolve
                MC "Sorry I need to rest now, it's been a long day"
                jump v4sleeptime

label v4seducehanna:
    scene v4023
    with dissolve
    MC "You know... We could try something..."
    scene v4024
    with dissolve
    hanna "Hmm... What do you mean?"
    MC "I mean... Look at you..."
    scene v4025
    with dissolve
    hanna "{i} Giggle"
    MC "You're stunning... That skin... Those lips"
    scene v4028
    with dissolve
    "She's signaling you to kiss her and that's what you do"
    jump v4hannasex

label v4hannasex:
    scene v4029
    with dissolve
    hanna "Do you want to see something?"
    MC "I'm pretty sure I do..."
    scene v4030
    with dissolve
    "She then gets naked in front of you, which is exactly what you hoped for"
    "This girl is amazingly beautiful"
    hanna "So.. What do you think?"
    MC "I've lost the ability to think..."
    hanna "Oh really?"
    scene v4031
    with dissolve
    hanna "What about now? Hmm?"
    MC "I..."
    hanna "No words for me?"
    hanna "Then I guess I don't need my mouth for talking..."
    MC "What do you....?"
    scene v4032
    with dissolve
    "Before you could finish the sentence she's on her knees"
    hanna "Take off your clothes"
    MC "Yes ma'am!"
    scene v4033
    with dissolve
    "You remove your clothes revealing your already erect cock"
    hanna "My oh my... Look at this..."
    scene v4034
    with dissolve
    "She grabs your member and starts stroking it"
    MC "Ah.... Yes..."
    hanna "I bet this tastes great"
    scene v4035
    with dissolve
    "You start to feel her tongue coating the tip of your dick with saliva"
    MC "Ah...Fuck...That's..."
    scene v4036
    with dissolve
    "She moves more vigorously introducing the head into her mouth"
    "You can feel her warm and sloppy lips around you"
    scene v4037
    with dissolve
    "Without either of you saying anything she goes deeper"
    "Which makes you instantly tremble with pleasure"
    hanna "{i}cough{/i} grrll"
    "You feel the tip of your dick touching her throat while she chokes on it"
    scene v4038
    with dissolve
    "She takes a little break for air"
    "She sure knows how to suck a dick"
    scene v4032
    with dissolve
    MC "If the writing thing doesn't pan out, I know a skill you're great at..."
    hanna "If you think that was something.."
    hanna "Maybe it's time to show you my other skills..."
    hanna " Don't you think?"
    MC "Don't let me stop you..."
    scene v4039
    with dissolve
    "She gets up and start to remove her boots"
    "As soon as they are off, you approach her"
    scene v4040
    with dissolve
    "You give her a little slap on the ass"
    "She grabs your hand a takes you to the sofa"
    scene v4041
    with dissolve
    MC "Hmmm... What a great view..."
    "She's waiting for your move..."
    hanna "What's the matter?"
    scene v4042
    with dissolve
    "You get closer to her aiming your cock into her entrance"
    "You begin rubbing it and lubricating it a bit before entering"
    scene v4043
    with dissolve
    "She throws herself in your direction"
    MC "Ah!! Fuck!!"
    hanna "Ah!! YES!!"
    "Now this is a sex crazy girl"
    hanna "Fuck me! Fuck me!!"
    scene v4044
    with dissolve
    "You don't even give her time to get used to it"
    "And give it all you got"
    scene v4045
    with dissolve
    "All the way in, hard and fast"
    hanna "AH!!! Fuck me more!!"
    scene v4046
    with dissolve
    MC "Oh... Shit...."
    hanna "Yes!! Yes!! More!! Give me more!"
    scene v4047
    with dissolve
    "You instinctively grab her face and shoulder and thrust hard"
    hanna "Ah!! Fuck me like a whore!! Fuck me!!"
    MC "Oh... Yes..."
    "You are forced to slow down a bit and she jumps off of your cock"
    scene v4048
    with dissolve
    "You grab her, preventing her escape"
    hanna "Hmmm... Yes... That's it"
    MC "Time for you to work, ride me!"
    scene v4049
    with dissolve
    "You lie down with you dick pointing up"
    "Hanna puts her pussy close to it"
    scene v4050
    with dissolve
    "She then forces you dick inside her"
    hanna "Ah.... So big... So good"
    scene v4051
    with dissolve
    "You give it to her deeper"
    MC "Damn!"
    hanna "Let me face you"
    scene v4052
    with dissolve
    "She keeps your dick inside her but manages to rotate around"
    hanna "Now give me all you got!!"
    scene v4053
    with dissolve
    "You comply... Giving her everthing you got"
    "Hard, fast, no mercy"
    scene v4054
    with dissolve
    hanna "YEEEESSS!!! I'm Coming!!! Ahh!!!"
    "Her orgasm makes her pussy squeeze you even more"
    "Bringing you close to orgasm too"
    menu:
        "Cum inside her":
            hanna "Are you about to cum? Do you want to see it filling me?"
            scene v4050
            with dissolve
            "She returns to her previous position with her ass turned to you"
            hanna "Yes! Come on fill me up!!"
            scene v4051
            with dissolve
            MC "Oh... SHIT! I'm..."
            show shot
            with hpunch
            scene v4051c
            with dissolve
            show shot
            with vpunch
            hide shot
            MC "Ahhhhh...."
            hanna "Yes.... Fill me..."
            "After all that you are both exausted and fall asleep right there"
            $ v4spentthenight = "hannain"
            scene black
            with dissolve
            stop music
            play music "<loop 0.0>sounds/beat.mp3"
            Nonen "Do you feel this? Do you?"
            jump v4lustmean
        "Try to hold a little longer":

            hanna "Are you trying to hold more? Let me take care of that!"
            scene v4055
            with dissolve
            "She jumps off of your cock and starts to lick it all"
            hanna "Hmmmm both our fluids together taste amazing"
            MC "Oh fuck..."
            "This woman is something else... And you love it"
            scene v4056
            with dissolve
            hanna "Hmmmfmmm"
            "The vibration of her throat is sending pleasure shocks through your spine"
            scene v4057
            with dissolve
            "And she get's deeper..."
            hanna "Gah.... Glrllr, uck my ace"
            "Did she say fuck my face? You grab hear head and make sure that's what she asked"
            scene v4058
            with dissolve
            hanna "Hmmm... As it..."
            "She forces your dick all the way down... You start to she her saliva dripping"
            hanna "Grlrlrl.... Hmmm"
            scene v4059
            with dissolve
            "She removes your dick from her mouth to be able to breathe"
            "You can she that her drool and tears are covering her face and your dick"
            scene v4060
            with dissolve
            MC "I'm about to cum...."
            "She gives you some final agressive strokes and that's all it takes"
            MC "Ahhhhhh!"
            show shot
            with hpunch
            scene v4061
            with dissolve
            show shot
            with hpunch
            hide shot
            scene v4062
            with dissolve
            "The previous mixture that was on her face now has an extra ingredient"
            "You released so much that you feel light headed"
            hanna "So much.... I can't believe it..."
            scene v4063
            with dissolve
            MC "Holy shit... This was.... I can't even move"
            hanna "This was so much fun..."
            hanna "I knew you could take good care of my needs"
            MC "Pffew...."
            scene v4064
            with dissolve
            hanna "Well you stay there and rest, I have a lot to write about"
            MC "You what?"
            hanna "Yes... This was exactly the inspiration I needed"
            $ hannalove += 1
            "Hanna likes you more"
            scene v4065
            with dissolve
            hanna "Bye... Have a nice sleep"
            MC "...."
            scene v4066
            with dissolve
            "She left"
            MC "I can't even think right now... I need to sleep"
            $ v4spentthenight = "hannaout"
            "Your eyes start to get heavy and you fall asleep"
            play music "<loop 0.0>sounds/beat.mp3"
            Nonen "Do you feel this? Do you?"
            jump v4lustmean


label v4katlab:
    scene v4229
    with dissolve
    "You and Mida enter the lab and you spot Katriona"
    if v4katlabvisit == 0:
        $ v4katlabvisit = 1
        katriona "Aww... this reminds me of when you two were teenagers"
        katriona "Roaming around looking for empty rooms to make out in"
        scene v4230
        with dissolve
        MC "We were not, Kat jeez"
        amida "Yes, we were actually about to head out to go the the City"
        katriona "Oh so is he taking you out on a date?"
        amida "Kinda, like an Adventure Date"
        katriona "Did I teach you nothing about women? Not a romantic bone in your body"
        MC "I can be plenty romantic, thank you."
        MC "How do you think I've kept someone as amazing as Mida?"
        scene v4238
        with dissolve
        "Katriona suggestively looks down"
        katriona "Oh I'm sure there's a reason"
        MC "Whatever, we need to get going, seeya later Kat"
        amida "Goodbye Mistress"
        scene v4237
        with dissolve
        katriona "Wait!! Before you go, do me a favor and drink this!"
        MC "Hell no. I am not falling for that again."
        MC "Last time I grew scales and the Archmage had to fix it"
        katriona "Oh yeah, that was hilarious."
        katriona "You kept complaining about how it itched everywhere."
        scene v4231
        with dissolve
        amida "Ahahaha"
        MC "Oh, not you too... I'm out of here, girls ganging up on me."
        scene v4230
        with dissolve
        katriona "You have fun Mida, enjoy your date"
        amida "We will"
        jump afterorcv39
    else:
        MC "I'll come back later"
        jump afterorcv39

label v4sleeptime:
    hanna "Oh... Ok... Have a nice sleep then"
    scene v4026
    with dissolve
    hanna "You can sleep there, make yourself confortable"
    scene v4027
    with dissolve
    hanna "I guess I'll go to sleep too... Bye..."
    scene v4066
    with dissolve
    "She left...."
    MC "Hmm... I guess she wasn't expecting this..."
    MC "Time to sleep I guess..."
    $ v4spentthenight = "hannanosex"
    scene black
    with dissolve
    play music "<loop 0.0>sounds/beat.mp3"
    Nonen "Do you feel this? Do you?"
    jump v4lustmean

label v4lustmean:
    Nonen "Power..."
    scene meanwhile
    with dissolve
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    scene v4239
    with dissolve
    tiberius "You were right once again... We found it"
    aelia "Yes my King, my love... All the power, will be yours"
    tiberius "We are still missing one of the stones, where can we find it?"
    scene v4240
    with dissolve
    aelia "Oh... I think this one will... {i} Find us instead..."

    jump v42all



label v4baths:
    if v42check == 1:
        scene v4067
        with dissolve
        "There is nobody here, you should leave"
        jump v4slayercitymap
    else:
        jump v4baths2

label v4baths2:
    "Still a feeling a bit grimy from earlier"
    "You decide to check out the bath house and relax a bit "
    scene v4067
    with dissolve
    "You enter to find the most prestigious-looking bathing area you've ever seen"
    MC "Fancy..."
    scene v4068
    with dissolve
    scl "Look what we have here..."
    "While trying to find a clerk of some sort to speak to"
    "A scantily clad woman walking towards you catches your attention"
    scene v4069
    with dissolve
    scl "Never seen you before. Thought you could sneak in here and peek at naked women?"
    scene v4133
    with dissolve
    MC "I wanted to try the baths...."
    MC "I'm guessing you're not the one to speak to if I want service?"
    scl "Hm... Tell ya what, I have my own private bath here"
    scene v4134
    with dissolve
    scl "I'll let you use it so I can make sure you don't go wandering off..."
    scl "... To peek at the defenseless naked women around this place"
    MC "...Excuse me?"
    "You totally would have"
    scene v4135
    with dissolve
    "You give her a sidelong glance, wondering what she's playing at"
    scl "I have to keep an eye on you so you don't do anything... dirty"
    MC "Hmm..."
    scl "Good. Now, follow me"
    scene v4133
    with dissolve
    "You follow the strange woman down a hallway towards your destination"
    scl "Calessa"
    MC "What?"
    scene v4134
    with dissolve
    cal "My name, it's Calessa"
    MC "..."
    cal "Aren't you going to tell me yours?"
    MC "Are you going to tell me what that charade was all about?"
    scene v4135
    with dissolve
    cal "My, whatever do you mean?"
    "You're unsure if you find her little games annoying or intriguing"
    "But, one thing's for sure: she's something else"
    "You respond to her little game by playing one of your own"
    MC "If I didn't know any better, I'd say you're just trying to get me all alone"
    cal "What?! Shhh..."
    scene v4134
    with dissolve
    MC "A woman of your caliber would never offer herself to a guy she just met"
    MC "So... What's the catch?"
    scene v4133
    with dissolve
    cal "Just follow me and get in here... whatever your name is"
    "She opens the door to the private bath, inviting you in"
    MC "[MC]"
    scene v4070
    with dissolve
    "You decide to play her game as you walk into the room"
    "Taking in her intoxicating scent as you walk past her"
    scene v4071
    with dissolve
    MC "So... Calessa, was it...?"
    MC "Interested in telling me now why you wanted so desperately to get me alone?"
    scene v4072
    with dissolve
    "She closes the door, a mischievous smile adorns her face as she turns to you"
    cal "So, what are you waiting for?"
    scene v4073
    with dissolve
    MC "What? Are you going to hang around and watch me bathe?"
    MC "Weren't you just teasing me about not doing that to the girls?"
    cal "Aww, you're not shy are you?"
    scene v4074
    with dissolve
    cal "Let's just say I offer a... special... service"
    "You simply watch her as she makes her way towards you"
    if my_path_is == "good":
        scene v41126g
        with dissolve
    elif my_path_is == "evil":
        scene v41126e
        with dissolve
    else:
        scene v4075
        with dissolve
    "She closes in and begins removing your clothes"
    "You're curious to see where this is going"

    if my_path_is == "good":
        scene v41127g
        with dissolve
    elif my_path_is == "evil":
        scene v41127e
        with dissolve
    else:
        scene v4075
        with dissolve
    "Simply standing there as she slips your clothes off and into a heap around your feet"
    "She looks you over from head to toe"
    scene v4072
    with dissolve
    "While seductively bringing a finger up to her mouth and biting her lip..."
    cal "Oh, I knew you were dirty, but I didn't expect you to be downright filthy"
    MC "You ever going to tell me what it is you're after..."
    MC "Or should I try to find a bathhouse where I can bathe in peace?"
    scene v4073
    with dissolve
    cal "Not to worry, we'll get you all cleaned up..."
    cal "Now about that special service I mentioned..."
    MC "Oh, really? What special service do you offer? Sponge baths?"
    scene v4074
    with dissolve
    cal "I could do that, for the right price..."
    MC "Price? Do you mean you're a...?"
    cal "Let's just say for 50 gold, I'll be whoever you want me to be.."
    cal "Plus some free bathing help added in..."
    cal "So what do you say handsome? Interested?"
    "This feeling again... The stone..."

    menu:
        "Refuse":
            scene v4073
            with dissolve
            MC "Sorry, I'm not interested"
            cal "Really...?"
            MC "Yeah, I'm sorry. I only came here to bathe"
            MC "I wasn't looking for a prostitute's services..."
            cal "Oh... okay"
            scene v4074
            with dissolve
            cal "If you change your mind, I run the Love Nest brothel"
            cal "The password to get in is 'Phoenix'. Come by and see me sometime"
            scene black
            with dissolve
            "You gather your clothes and leave"
            "Calessa locks up her private bath and exits the bathhouse"
            scene v4067
            with dissolve
            "You make your way back to the public bath to have a soak before leaving."
            jump v4afterbath


        "Pay 50 gold" if Gold >= 50:
            $ calessapet = 50
            $ Gold -=50
            play sound "sounds/coin.ogg"
            "You lost 50 gold"
            scene v4077
            with dissolve
            "Having already rid you of your clothing, she begins removing her suit made of pearls"
            scene v4078
            with dissolve
            cal "I knew it would be a good idea to wear this suit today"
            MC "Why not wear it every day?"
            "She gives you a cheeky grin as she turns"
            scene v4079
            with dissolve
            "She steps away and sets her delicate pearl suit down safely"
            "Giving you an exquisite view of her luscious cheeks"
            cal "Like what you see?"
            scene v4080
            with dissolve
            "You waltz over to her, giving her a firm smack on her big, juicy butt"
            scene v4081
            with dissolve
            "Before bringing your fingers to her crotch"
            cal "Ah! Oooh..."
            scene v4082
            with dissolve
            MC "Looks like I wasn't the only one enjoying a view..."
            "She twists her torso, reaching back"
            scene v4083
            with dissolve
            "And tightly gripping one of her cheeks with her hand"
            "And spreading it away from the other whilst looking at you with a teasing expression"
            cal "Are we just going to stand around teasing each other"
            cal "Or do you want to take what you paid for?"
            scene v4084
            with dissolve
            "You grasp her hips tightly, aligning your throbbing shaft with her slick entrance"
            cal "Mmmm! That's more like it. Now, treat me like whore I am and..."
            cal "Fuck. Me. Good."
            scene v4085
            with dissolve
            "She sets her hands on the edge of the bath and spreads her legs for you more"
            "Giving you uninhibited access to ravage her hole"
            "You begin thrusting your hips forward, spreading her lips and entering her pussy"
            "Surprised at just how wet she is"
            scene v4084
            with dissolve
            "You effortlessly glide along the slick coating of her vaginal walls"
            "Until you're in all the way to the hilt"
            "She gasps and her body shudders, feeling your length inching ever deeper as you enter"
            scene v4085
            with dissolve
            "Ending with a larger quake and a moan once you're fully inside"
            cal "Oh! Mmmm..."
            "You begin pumping in long, slow, but deep thrusts"
            "Slamming home once you've reached the base to drive it deeper into her pleasure spots"
            scene v4084
            with dissolve
            "She settles into the rhythm with you, pulling away as you pull out"
            "Pushing back against you as your shaft grinds against her insides upon re-entry"
            "Ending with a slap as you both slam into each other wildly"
            scene v4086
            with dissolve
            "You give her curvacious ass a heavy slap as you begin to pick up the pace"
            cal "Oh! Fuck!"
            "The suddenness of it all catches her by surprise"
            "She bucks her hips back against you harder as the pleasure becomes more intense"
            "She fully submits to you, reaching both arms straight back"
            jump v4question3some
        "Allow the stone to take over her mind[abred] [abnoalignment2] [abstoneuses]":

            $ stoneuses += 1
            $ calessapet = 1
            $ Points -= 2
            "You lost 2 points"
            "You have an idea to try using the power of the stone"
            "To temporarily bend Calessa to your will"
            "You can feel your influence on her mind, molding her into your obedient little sex pet"
            "In the midst of twisting her psyche"
            "You sense the ability to deepen your control over her"
            "To break her mind and bend her to your will completely"
            "It tempts you, eating away at your very soul"
            "To experience what it would be like to have someone"
            "Utterly devoted to you, to serve your every need"
            Nonen "Yes! Let's control her! Let's make her our slave!"
            "Do you give into this temptation?"
            menu:
                "Yes[abred] [abnoalignment5] [abstoneuses2]":
                    $ stoneuses += 2
                    "You seize upon the opportunity, making Calessa utterly devoted to you. Forever"
                    Nonen "Ahaha! Let's make this whore our slave! Forever!"
                    $ Points -=5
                    $ calessapet = 2
                    "You lost 5 points"
                    jump v4calessapet
                "No":

                    "You do not give into the temptation to make her yours forever."
                    jump v4calessapet

label v4calessapet:
    if my_path_is == "good":
        scene v41126g
        with dissolve
    elif my_path_is == "evil":
        scene v41126e
        with dissolve
    else:
        scene v4075
        with dissolve
    "Calessa, now under your control, peers up at you in elation as she walks over to you."
    scene v4077
    with dissolve
    cal "How do you want me, Master?"
    scene v4111
    with dissolve
    "You grasp her pearl suit and pull hard, sending the pearls flying everywhere"
    scene v4112
    with dissolve
    cal "Mmm, Master! So forceful..."
    scene v4082
    with dissolve
    "She melts like ice at your touch, already quivering and ready for you"
    "You reach between her legs as she overflows, coating your fingers in her juices"
    cal "Please, Master, take me."
    scene v4083
    with dissolve
    "You let her go."
    "She sets her hands on the edge of the bath and spreads her legs wide for you"
    "Giving you uninhibited access to ravage her hole"
    scene v4084
    with dissolve
    "You begin thrusting your hips forward, spreading her lips and entering her cavern"
    "Still surprised at just how wet she is"
    scene v4085
    with dissolve
    "You effortlessly glide along the slickness coating her vaginal walls"
    "Until you're in all the way to the hilt"
    "She gasps and her body shudders"
    "Feeling your length inching ever deeper as you enter her"
    "Ending with a larger quake and a moan once you're fully inside"
    scene v4086
    with dissolve
    cal "Oh, Master! Mmmm..."
    "You begin pumping in long, slow, but deep thrusts"
    "Slamming home once you've reached the base to drive it deeper into her pleasure spots"
    scene v4084
    with dissolve
    "She settles into the rhythm with you, pulling away as you pull out"
    "And pushing back against you as your shaft grinds against her insides upon re-entry"
    "Ending with a slap as you both slam into each other wildly"
    scene v4086
    with dissolve
    "You give her curvacious ass a heavy slap as you begin to pick up the pace"
    cal "Oh yes, Master!"
    "She bucks her hips back against you harder as the pleasure becomes more intense"
    "She fully submits to you, reaching both arms straight back"
    jump v4question3some

label v4question3some:
    scene v4084
    with dissolve
    "Each grasping one of her rounded lower cheeks and spreading"
    "She moans loudly with each rough penetration"
    "Reveling in the feeling of your coarse rod scraping along her embankment"
    "Until your spear tip collides with her cervix before pushing through into her womb"
    "You feel Calessa's pussy clench tightly and flood in the throes of an orgasm."
    cal "Fuck, I'm cumming!"
    fvoice "Yes!"
    scene v4087
    with dissolve
    "Calessa peeks over her shoulder at you with a look of surprise"
    "You both turn your eyes carefully to the mirror in the room"
    "Trying to get a glimpse of who's at the door"
    "Without alerting your little spy"
    "You're a bit shocked to see a familiar face at the door"
    "Watching the two of you intently and fingering herself"
    "Calessa looks back at you again, this time with a suggestive smile..."
    "Do you want to try to convince the girl at the door to join you for a threesome?"
    menu:
        "[abgreen]Yes!!!":
            jump v43somehanna
        "No":

            jump v4no3some

label v43somehanna:
    scene v4088
    with dissolve
    cal "Oh, Hanna, we can see you..."
    "Hanna is startled upon hearing her name"
    hanna "Shit!"
    cal "Don't even think about running, honey. You've already been caught"
    cal "Why don't you just come inside and close the door?"
    hanna "...Fine"
    scene v4089
    with dissolve
    "Hanna nervously steps into the room and closes the door behind her"
    MC "Well hello... Hanna"
    "Hanna gets a good look at you"
    scene v4090
    with dissolve
    hanna "Oh, I was just curious where you were going and..."
    hanna "...and now I... you're... naked..."
    "Hanna's face turns flush as she looks away, embarrassed"
    scene v4091
    with dissolve
    cal "Little writer girl, always so curious"
    cal "I hope you weren't planning on writting this story down."
    hanna "No, Calessa. I, um... I was following [MC] to see if he didn't..."
    hanna "Get lost again... and I saw you two... um..."
    cal "Haha! No need to be so shy now, Hanna. We know you enjoyed what you saw"
    cal "We saw you fingering yourself at the door"
    hanna "Oh, no..."
    "Calessa, still stark naked, steps closer to the nervous and embarrassed Hanna"
    cal "It's just a shame, really. I mean, why be over there by yourself watching"
    cal "When you could be in here having fun with us?"
    hanna "Oh, I couldn't possibly..."
    scene v4092
    with dissolve
    cal "And why not? Look at you, Hanna..."
    "Calessa runs her hand down Hanna's arm"
    cal "Your beautiful skin..."
    "Hanna shudders a bit at Calessa's touch"
    scene v4093
    with dissolve
    "Calessa moves up to Hanna's face, tracing along Hanna's jawline"
    "Till she reaches her chin with her fingertip"
    cal "Your sharp, exotic facial features, and most of all..."
    "Calessa grabs Hanna and pulls her in very close, face to face, and begins to speak..."
    cal "Your big, luscious lips Mmmm..."
    scene v4094
    with dissolve
    "It seems like Calessa is about to seal the kiss"
    "Until she pulls away and sends Hanna toward you with a firm slap on her butt."
    "You catch Hanna and hold her tight, making sure she doesn't fall"
    cal "However, I think story boy and writer girl should work on a new story together"
    cal "Wouldn't you agree?"
    "Even though Hanna is plenty stable enough to stand on her own"
    "You hold her tight and close while you speak to her"
    MC "You know, Calessa's right. You really are beautiful, Hanna"
    hanna "Oh, God..."
    MC "You're still all hot and bothered from watching us, I'm sure"
    MC "Don't you want to join us and get some release?"
    "The three of you move to the bathtub"
    scene v4095
    with dissolve
    hanna "Oh, it's been like torture since you caught me! Both of you standing here naked"
    hanna "Calessa holding me close, almost kissing me..."
    hanna "I can't take it anymore"
    scene v4096
    with dissolve
    "Hanna grabs your head, pulling you into a wild, passionate kiss"
    "You grab a generous handful of her butt, sinking your fingers into her tender flesh"
    "Pulling her in closer, returning the kiss with your own fiery passion"
    scene v4097
    with dissolve
    "You let your free hand wander over her silky smooth skin"
    "Roaming up her leg and stomach before stopping at her breast"
    "Groping her tempestuously and pinching her nipple"
    hanna "Mmmm!"
    scene v4098
    with dissolve
    "Calessa closes in on the two of you during your heavy makeout session"
    cal "I knew she would want to join us..."
    "Your handsy assault on Hanna's flesh makes her moan out in bliss"
    "You kiss her chin and make your way down to attack the nape of her neck"
    "Heightening her pleasure"
    scene v4099
    with dissolve
    "Calessa comes face to face with Hanna once again, speaking to her sensually"
    "Increasing the tension Hanna's feeling to the point that it's almost unbearable"
    scene v4098
    with dissolve
    cal "Admit it, Hanna. You wanted to get caught"
    hanna "Mmmm! I... Yes!"
    cal "You were hoping this would happen, weren't you?"
    hanna "Yes! I'm so hot right now. It's so good...!"
    scene v4099
    with dissolve
    "Hanna moans into Calessa's mouth as they lock lips and swap spit"
    "All the while you continue attacking Hanna's pleasure points"
    "Calessa places her hand between Hanna's legs"
    "Tracing her fingers along Hanna's slick, smooth lower lips"
    "Before spreading them and inserting her fingers"
    "Hanna presses her face harder into Calessa's and moans even louder into her mouth"
    "As the lip lock continues"
    scene v4100
    with dissolve
    "You release your grip on her luscious lower cheek, moving your cock between them"
    "Giving her back door a gentle massage with the tip"
    "Hanna's knees begin to buckle as she quakes from the overload of sexual stimulus"
    "Calessa breaks the kiss, looking into Hanna's lust-filled eyes as she pulls away"
    "Leaving Hanna tense and panting"
    cal "I think it's time we stop teasing the poor girl"
    cal "And give her what she oh so desperately wants..."
    scene v4101
    with dissolve
    "You lift Hanna up, unsure if she can stand on her shaky legs"
    "Hanna gasps, feeling your tip pushing against her entrance"
    "Hanna relaxes her body and wiggles her hips downward, taking your tip inside of her"
    scene v4102
    with dissolve
    cal "Looks like she wants it right here and now"
    hanna "Yes!"
    scene v4104
    with dissolve
    "You lower her down, burying yourself into her to the hilt"
    "Hanna claws at your back and rolls her eyes when your tip hits her cervix"
    scene v4105
    with dissolve
    "She relaxes her grip, holding you around the neck"
    "and leaning back so she can look you in the eyes"
    "You pump your hips into her, slamming hard into her depths"
    scene v4102
    with dissolve
    "Calessa sucks her fingers, clearly planning something"
    scene v4103
    with dissolve
    "She puts her fingers on Hanna's rear entrance"
    "Gently massaging and easing forward until her her fingertips are inside"
    hanna "Oooh...!"
    scene v4104
    with dissolve
    "Calessa inches deeper"
    "Making Hanna gasp and moan in joy at the fullness she feels inside her butt"
    hanna "Yes! Fuck me!"
    "You and Calessa pump into her unison"
    "Sending Hanna over the edge as her body begins to sieze"
    scene v4105
    with dissolve
    hanna "Cumming! Oh god..."
    "You feel her pussy clench hard, starting a torrent of juices to flow and coat your cock"
    "You don't stop, her hard climax exciting you more"
    "Causing you ream her deeper and slip into her womb"
    "Calessa digs deeper into Hanna's now gaping asshole"
    "Pulling Hanna into a deep kiss and groping her breast"
    "Hanna practically screams into Calessa's mouth from pleasure overload"
    "As her body yearns for more"
    "Hanna does all she can to shift her weight lower and lower"
    "To feel you as deep as she possibly can"
    "You shift up your thrusting, gliding the length of your shaft along Hanna's g-spot"
    "Hanna can't handle the pleasure, tensing up her body"
    "Throwing her head back and pressing her hips against you"
    scene v4106
    with dissolve
    "Calessa slips between your legs"
    "Licking your balls while still finger deep inside of Hanna and pumping"
    "With Hanna's insides gripping like a vice from her constant orgasm"
    "And Calessa working your balls"
    "You can feel your climax approaching"
    "You blast your seed into Hanna's womb, filling her rapidly"
    show shot
    with vpunch
    scene v4106c
    with dissolve
    show shot
    with vpunch
    hide shot
    "Her body shakes harder as she feels you filling her up, becoming even more tense"
    "The already vice-like grip of her pussy somehow grips you even tighter"
    "As if to milk you for everything you've got"
    hanna "There's so much. Mmmm..."

    $ hannacorr += 1
    "Hanna corruption increased"
    scene v4107
    with dissolve
    "Hanna basks in the warm, full feeling for a bit"
    "But soon the party's over and everyone gets dressed"
    scene v4108
    with dissolve
    "The three of you walk out of the private bath together and down the hall"
    "Striking up a conversation"
    hanna "That was {i}so{/i} good, I really needed that"
    cal "Haha! I'm sure you did, Hanna."
    hanna "How do you two know each other, anyway?"
    $ hanna3some = 1

    if calessapet == 1 or calessapet == 2:
        cal "He's my master."
        "You look over at Calessa as she sends you a flirty look."
        hanna "Oh, really?"
        "You laugh as though it's a joke"
        "Nervously trying to ward off suspicions of your foul deeds"
        MC "Playtime is over Calessa, you can stop calling me master now"
        cal "Yes, Maste... I mean, yes, [MC]..."
        "The three of you find yourself at the bathhouse entrance."
        hanna "It was fun. I'd really love to do it again right now"
        hanna "But I have other things I need to do, sadly"
        hanna "I'll see you two some other time"
        "Hanna walks out, leaving you alone with Calessa"
        scene v4109
        with dissolve
        "You turn to Calessa and compel her using the power of the stone"
        MC "Only call me master when we're alone or during our play time. Understood?"
        cal "Yes, Master. Will you come and see me again?"
        "She looks at your with sad, longing eyes"
        cal "I run the Love Nest brothel. The password to get in is 'Phoenix'"
        cal "I'll be there and waiting for you, Master."
        scene v4110
        with dissolve
        "She bows in servitude to you before she turns and walks away..."
        jump v4afterbath
    else:

        MC "Actually, we just met."
        "You look over at Calessa as she sends you a flirty look"
        hanna "Oh, really?"
        "The three of you find yourself at the bathhouse entrance"
        hanna "It was fun. I'd really love to do it again right now"
        hanna "But I have other things I need to do, sadly"
        hanna "I'll see you two some other time"
        scene v4109
        with dissolve
        "Hanna walks out, leaving you alone with Calessa"
        cal "I run the Love Nest brothel. The password to get in is 'Phoenix'"
        cal "Come by and see me sometime, big boy"
        scene v4110
        with dissolve
        "She gives you a light kiss and a playful wink before she walks away"
        jump v4afterbath

label v4no3some:
    "You feel too good inside Calessa to stop now"
    "Leaving the familiar face at the door to simply enjoy the view."
    "Calessa's warm, flooded depths too enticing"
    "You elect to use Calessa's body as a basin for your desire."
    scene v4085
    with dissolve
    "You push Calessa's head down low to wedge your pole inside her, deep into her core"
    "Overwhelming her with a brutal wrecking of her cervix."
    "The sound of skin slapping skin from your rapid hard thrusting"
    "Sends echoes throughout the bath."
    scene v4084
    with dissolve
    "Calessa loudly moans and screams out in ecstasy, unable to form a coherent thought"
    "From the rapid waves of pleasure."
    cal "Ooooooo-ho-ooooh! Fuck!"
    "Your length grinds and scrapes along her vaginal walls"
    "As they clench and pulse and undulate in continuous climax."
    "The unrelenting pillage of her crevasse too much to handle, her knees begin to slack."
    "Holding her up by her hips as you continue your ravaging of her pussy"
    scene v4086
    with dissolve
    "You feel her clamping down ever tighter on your rod"
    "And your own climax approaching."
    jump v4bathcum

label v4bathcum:
    menu:
        "Cum inside":
            scene v4085
            with dissolve
            "You don't stop hammering into her, bearing down on her womb's entrance"
            "And slipping inside."
            "Her womb's opening kisses your tip every time you ream into her down to the hilt"
            "Pushing you over the edge."
            show shot
            with hpunch
            scene v4085c
            with dissolve
            show shot
            with vpunch
            hide shot
            cal "Oh holy fuck!"
            "She shakes violently in bliss, feeling your seed pour into her innermost reaches."
            scene v4086c
            with dissolve
            "Your ravaging doesn't stop until you're certain there isn't a drop left in you."
            cal "Oh God, there's so much..."
            "Completely spent, you set her down gently before nearly collapsing yourself."
            if calessapet == 1 or calessapet == 2:
                scene v4205
                with dissolve
                "You make your new pet Calessa give you a sponge bath while you relax in the tub."
                "Once you're feeling refreshed again"
                scene v4116
                with dissolve
                "You order Calessa to stop bathing you and dry you off before dressing you."
                "The two of you make your way out of the private bath and toward the bathhouse exit."
                scene v4109
                with dissolve
                cal "Will you come and see me again, Master?"
                "She looks at your with sad, longing eyes."
                cal "I run the Love Nest brothel. The password to get in is 'Phoenix'."
                cal "I'll be there and waiting for you, Master."
                scene v4110
                with dissolve
                "She bows in servitude to you before she turns and walks away..."
                jump v4afterbath
            else:

                scene black
                with dissolve
                scene v4205
                "You both decide to clean up, relax, and chat in the bath"
                cal "You may have to carry me home, handsome"
                cal "I don't think I'll be able to walk for a while after that"
                "She shoots a flirty grin over to you."
                MC "50 gold for my princess carry service"
                "Calessa sputters before bursting out in laughter"
                cal "So, favors for favors?"
                MC "You could always try making it home on your own..."
                scene v4197
                with dissolve
                "The two of you chat up a storm while you finish bathing"
                "Before getting dressed and heading out"
                scene v4109
                with dissolve
                cal "It's too bad you didn't let Hanna in to play, we could've had a lot of fun with her"
                MC "Hanna? She's a writer, isn't she?"
                cal "Yes, actually. Do you know her?"
                MC "I met her briefly, but it sounds like you know her pretty well"
                cal "You could say that..."
                "Calessa bites her lip and gives you a sensual look."
                cal "I run the Love Nest brothel. The password to enter is 'Phoenix'"
                cal "Come by and see me sometime, big boy."
                scene v4110
                with dissolve
                "Calessa pulls you into a deep goodbye kiss"
                "Before making her way out of the bathhouse"
                jump v4afterbath
        "Pull out":


            if calessapet == 1 or calessapet == 2:
                "You pull out and let her down gently"
                scene v4113
                with dissolve
                "Still panting, moaning, and shaking, Calessa sits herself up on her knees"
                "Mouth wide open and pushing out her tits to use as a semen catch"
                show shot
                with vpunch
                scene v4113c
                with dissolve
                show shot
                with vpunch
                hide shot
                "A few strokes is all it takes to unleash your load all over her."
                scene v4114
                with dissolve
                "You cover her face and chest with your spunk"
                "While she swallows the portions that landed in her open mouth"
                scene v4115
                with dissolve
                cal "Thank you, Master! Mmm, so much!"
                "Calessa delights in your cum shower for a while"
                "Before you make her give you a sponge bath while you relax in the tub"
                scene v4205
                with dissolve
                "Once you're feeling refreshed again"
                "You order Calessa to stop bathing you and dry you off before dressing you"
                scene v4116
                with dissolve
                "The two of you make your way out of the private bath and toward the bathhouse exit"
                scene v4109
                with dissolve
                cal "Will you come and see me again, Master?"
                "She looks at your with sad, longing eyes."
                cal "I run the Love Nest brothel. The password to get in is 'Phoenix'."
                cal "I'll be there and waiting for you, Master"
                scene v4110
                with dissolve
                "She bows in servitude to you before she turns and walks away..."
                jump v4afterbath
            else:

                "You pull out and let her down gently."
                scene v4113
                with dissolve
                "Still panting, moaning, and shaking, Calessa sits herself up on her knees"
                "Mouth wide open and pushing out her tits to use as a semen catch"
                show shot
                with vpunch
                scene v4113c
                with dissolve
                show shot
                with vpunch
                hide shot
                "A few strokes is all it takes to unleash your load all over he."
                scene v4114
                with dissolve
                "You cover her face and chest with your spunk"
                "While she swallows the portions that landed in her open mouth"
                scene v4115
                with dissolve
                cal "Mmm, so much!"
                "Calessa delights in your cum shower for a while"
                "Before you both decide to clean up, relax, and chat in the bath"
                scene v4205
                with dissolve
                cal "You may have to carry me home, handsome"
                cal "I don't think I'll be able to walk for a while after that"
                "She shoots a flirty grin over to you"
                MC "50 gold for my princess carry service."
                "Calessa sputters before bursting out in laughter"
                cal "So, favors for favors?"
                MC "You could always try making it home on your own..."
                scene v4197
                with dissolve
                "The two of you chat up a storm while you finish bathing"
                "Before getting dressed and heading out"
                scene v4109
                with dissolve
                cal "It's too bad you didn't let Hanna in to play, we could've had a lot of fun with her"
                MC "Hanna? She's a writer, isn't she?"
                cal "Yes, actually. Do you know her?"
                MC "I met her briefly, but it sounds like you know her pretty well"
                cal "You could say that..."
                "Calessa bites her lip and gives you a sensual look"
                cal "I run the Love Nest brothel. The password to enter is 'Phoenix'."
                cal "Come by and see me sometime, big boy"
                scene v4110
                with dissolve
                "Calessa pulls you into a deep goodbye kiss"
                "Before making her way out of the bathhouse"
                jump v4afterbath




label v4brothelpart:
    scene v4180
    with dissolve
    if calessapet == 2:
        "As you make your way inside the brothel"
        "You scan the room and spot Calessa in the main hall"
        scene v4181
        with dissolve
        "She spies you as you make your way towards her"
        "Barely able to contain her excitement"
        "Her elation clearly visible in her bright eyes and smile"
        scene v4183
        with dissolve
        "She speaks in hushed tones so no one overhears"
        cal "I'm so happy you're here, Master. I couldn't wait to see you again..."
        "She bites her lip and looks away, shifting somewhat nervously"
        "Unsure of how you'll respond to what she has to say next"
        cal "Master, I'm already so hot."
        cal "Should we just get naked and fuck like beasts right here?"
        menu:
            "No, I have other things to do":
                MC "Not right now, Calessa, I have other things to do. Some other time"
                scene v4183
                with dissolve
                "Sadness becomes apparent on her face at your rejection."
                cal "I understand, Master. I'll be waiting for you to return"
                "You leave the brothel"
                $ v4calessabrothelfun = 1
                jump v4itsnight
            "Fucking you in front of everyone should be interesting":

                $ v4calessabrothelfun = 3
                jump v4fuckpethall
            "Here? Take me to a room!":

                scene v4201
                with dissolve
                "You both head up to a lavish private room of the brothel"
                $ v4calessabrothelfun = 4
                jump v4fuckpetroom
    else:
        "A particularly beautiful woman amongst the bunch catches your attention yet again."
        scene v4181
        with dissolve
        cal "Got your eye on me again, handsome?"
        MC "Long time no see, Calessa"
        scene v4182
        with dissolve
        cal "Haha! Missed me already?"
        MC "And what if I did?"
        "She poses alluringly, putting emphasis on her assets"
        "And gives them an enticing shake"
        cal "Then come and get me"
        menu:
            "No, I have other things to do":
                MC "Not right now, Calessa, I have other things to do. Some other time"
                cal "That's okay, babe. You know where to find me"
                scene v4181
                with dissolve
                "She gives you a flirty smile and a wink as you walk away..."
                $ v4calessabrothelfun = 1
                jump v4itsnight

            "Yes (Pay 50 gold)" if Gold >=50:
                $ Gold -= 50
                $ v4calessabrothelfun = 5
                scene v4185
                with dissolve
                play sound "sounds/coin.ogg"
                "You lost 50 gold"
                cal "Come with me, big boy"
                scene v4201
                with dissolve
                "You follow her upstairs"
                jump v4fuck50room
            "Use the stone to briefly control her mind[abred] [abnoalignment]":

                $ Points -=1
                $ v4calessabrothelfun = 2
                "You lost 1 point"
                scene v4183
                with dissolve
                cal "I... Want you now... Follow me"
                scene v4201
                with dissolve
                "You both head up to a lavish private room of the brothel"
                jump v4fuckpetroom


label v4fuckpethall:
    scene v4189
    with dissolve
    "You start stripping her naked there in front of everyone"
    "Once you rid yourself of your garments, you begin giving her commands"
    scene v4190
    with dissolve
    MC "Now, suck it."
    "Calessa, begins practically worshipping your cock"
    scene v4191
    with dissolve
    "Rubing it against her cheek and planting kisses down the length of your shaft"
    "Before greedily answering:"
    cal "Yes, Master!"
    scene v4192
    with dissolve
    "She takes the head of your member into her mouth"
    "Masterfully swirling her tongue around the tip"
    "Before taking in more of your turgid rod."
    scene v4193
    with dissolve
    "You feel the topmost part of your mast sink into her throat."
    "It feels fantastic, but you find yourself craving more..."
    "Fucking in front of everyone fills you with immense lust"
    "You find yourself with an unrelenting desire to seek deeper pleasure"
    "From your new pet"
    scene v4194
    with dissolve
    "You grasp her head and force your pole as deep into her face as you can"
    cal "Mmmm, ah ove ur ock, Masder..."
    "She murmurs and hums and moans as you repeatedly ram your meat stick"
    "Into her wide open gorge"
    scene v4193
    with dissolve
    "She fingers herself furiously while you bear down relentlessly on her esophagus"
    "The moist sounds echo about the room as the crowd watches the two of you intently"
    "Eventually you free your cudgel from the confines of her larynx"
    MC "It's about time I show everyone that your pussy is mine"
    cal "Tame me, Master"
    scene v4195
    with dissolve
    "You push her down on a table on her back, legs splayed for everyone to see"
    cal "Do you want to breed me, Master? My pussy is ready for you..."
    "She's not lying. She's so wet she's practically dripping"
    "A simple touch causes her to flood under the influence of the soul stone"
    "She spreads herself open for you with a wet squelch, inviting you in..."
    "Calessa gives you a seductive, pleading look before begging you:"
    cal "Come inside me, Master..."
    scene v4196
    with dissolve
    "You quickly impale her and begin gouging out her hole"
    cal "Oh yes! Fuck!"
    cal "Show everyone here that I'm just a sleeve for your beautiful cock, Master!"
    "You focus on a particular spot inside her, pounding it in a rhythm"
    "Making her buck her hips harder against you"
    "Seeking to drive you deeper into that spot which makes her cry out in bliss"
    scene v4198
    with dissolve
    "The mind-broken whore looks up into your eyes longingly"
    "Her mouth agape as she pants and moans, and mumbles mindless drivel"
    scene v4199
    with dissolve
    cal "You fuck me so good, Master..."
    "You begin to feel your orgasm upon you"
    show shot
    with hpunch
    scene v4199c
    with dissolve
    show shot
    with vpunch
    hide shot
    "You erupt inside of her, drowning the deepest parts of her in your viscid seed"
    cal "Mmmmm! Master is breeding me...!"
    "The torrent of semen seems as though it won't stop"
    "Flooding her pussy until she overflows"
    "As if trying to overpower any contraception at play"
    scene v4198c
    with dissolve
    "She holds herself open"
    "Staring at the unbelieveable amount of seed pouring from her insides"
    cal "Oh! So full."
    cal "I've never been so full before. I really hope our breeding is successful, Master"
    "She inhales deeply then bites her lip"
    scene v4200
    with dissolve
    "Rubbing herself down below to heighten last waves of pleasure"
    "As they begin to subside"
    "You begin to dress yourself while Calessa still lies naked on the table"
    "Basking in her bliss."
    "Your pet finally rouses from her trance, seeing you fully clothed and about to leave"
    scene v4202
    with dissolve
    "She rushes over to you and gives you a tight hug."
    cal "You'll come see me again soon right, Master? I'll be waiting for you..."
    "You say nothing, simply a nod of approval as you make your way out of the brothel"
    "As her master walks away, Calessa's face beams with joy"
    "Already dreaming of her next encounter with her master"
    jump v4itsnight

label v4fuckpetroom:
    scene v4203
    with dissolve
    "As soon as the door closes"
    scene v4204
    with dissolve
    "You grab her and strip her clothes off. She floods at your touch"
    cal "Oh, you make me so hot! I can't take it anymore, I need to feel you no."
    "Please, stop teasing me and let me have it, Master..."
    menu:
        "[abgreen]Tease her more":
            jump v4teasehermore
        "Give it to her already":
            jump v4dontteaseher

    label v4teasehermore:
        scene v4208
        with dissolve
        "You decide to tease her some more"
        "Bringing your hand to her well-moistened mound, giving her button a little rub"
        "She squeals in bliss at your touch and you feel the immense heat"
        "Radiating from her sex"
        "She tries hard to find deeper pleasure, but you refuse her"
        "You tease her until you're good and ready to take her"

    label v4dontteaseher:
        MC "Time for you to get your wish, whore"
        scene v4209
        with dissolve
        "She bends over, legs wide, and spreads her luscious cheeks giving you easy access"
        cal "Give it to me, Master I can't wait..."
        "You line up your head with her wet hole, grab her by the shoulders..."
        scene v4210
        with dissolve
        "And thrust in all the way to the hilt."
        "She convulses in pleasure as you plow your way through to her deepest parts"
        cal "Oh, fuck! You feel so good, Master. I'm so full..."
        scene v4211
        with dissolve
        "Without hesitation, you grab her hips tightly and begin to ravage her"
        "With long, deep, swift strokes"
        "Digging into her cervix and pushing through into her womb"
        cal "So thick! Oh! So deep! I love it so much, Master!"
        scene v4212
        with dissolve
        "You feel her cavern tighten and quiver around your stiffened rod"
        "As you continuously wedge yourself into her deep and hard"
        "The torrent of wetness is immense from her constant climax"
        "As you savagely throw yourself into her depths on repeat"
        scene v4211
        with dissolve
        "She bites her lip hard, trying to contain her voice, unsuccessfully."
        cal "Mmmm! Mmmm! Mmmm! Oh! Oh! OHHHHHH!!"
        "She screams in rapture as her cunt endures the full extent of your relentless assault"
        scene v4212
        with dissolve
        "Her pussy grips you tighter, as if trying to milk your seed"
        "And your body feels ready to oblige it"
        MC "I'm gonna cum."
        cal "Yes! Breed me, Master! Drown my womb in your seed!"
        show shot
        with hpunch
        scene v4212c
        with dissolve
        show shot
        with vpunch
        hide shot
        "The explosive release of cum paints her insides white"
        "She moans in glee as the feeling of fullness builds until she overflows."
        cal "You came so much, Master. I can feel it flowing out..."
        "She plays with herself for a few moments"
        "Trying to keep the precious seed from flowing out, but to no avail"
        cal "Mmm! So good..."
        scene v4206
        with dissolve
        "Calessa quivers, savoring the final embers of orgasmic bliss before they fade"
        "You get dressed to leave, but Calessa stops you"
        "Your pet looks wistfully into your eyes as she begins to plead to you"
        scene v4207
        with dissolve
        cal "You'll come to see me again, won't you, Master?"
        "Her sad eyes look longingly into yours"
        "As though she'd prefer to ask you to stay with her, but wouldn't dare"
        MC "I'll be sure to"
        "She smiles, relieved to hear your answer, as you make your way out of the brothel"
        jump v4itsnight


label v4fuck50room:
    scene v4203
    with dissolve
    "Calessa leads you up to a luxurious private room in the brothel"
    cal "So, what'll it be?"
    MC "Show me how skilled you are. I want you to ride me"
    cal "Mmm, intriguing..."
    scene v4214
    with dissolve
    "You disrobe and lie on the bed"
    "Looking up and taking in the sight of Calessa's beautiful form"
    "Calessa climbs on the bed on all fours"
    "Staring into your eyes as she slowly crawls toward you"
    scene v4215
    with dissolve
    "Seductively and ravenously licking her lips"
    "She positions herself between your legs, staring at your already rigid shaft"
    cal "Mmm, looks like you really enjoyed the view. You're {i}all{/i} ready for me"
    cal "Should I get it wet before we start, baby?"
    cal "I'm told I can do wonderous things with my mouth..."
    menu:
        "Yes":
            jump v4bjcal
        "Give me the pussy already":
            jump v4calmainevent

    label v4bjcal:
        scene v4216
        with dissolve
        "Calessa looks you right in the eyes"
        "Gripping each of your thighs in each of her hands"
        "And taking your rigid tip into her mouth"
        "She sucks hard, her tongue working the head of your cock with extreme precision"
        "The skill of a master at her craft"
        "She starts humming and moaning on your tip"
        "The vibrations giving you intense pleasure waves"
        scene v4228
        with dissolve
        "After a few more moments of working your crown"
        "She moves her head lower, taking more of you into her mouth"
        "All the while still sucking hard and never stops moving her tongue"
        "You can feel the apex of your shaft slip into her open throat"
        "As she continues her descent down your length until it's all inside"
        "Eye contact is never broken as Calessa begins to bob her head up and down"
        "Taking and releasing all of your length in rapid motion"
        "The suction is immense as she relentlessly works your pole"
        "Still moaning and humming all the while, her tongue never missing a pleasure spot"
        scene v4215
        with dissolve
        "While her blowjob is indeed as spectacular as she claims"
        "It isn't what you came here for"

    label v4calmainevent:
        "You let her know that you're ready to get to the main event."
        cal "Now, {i}this{/i} this is something I can work with..."
        "She admires your long, thick shaft for a moment"
        scene v4218
        with dissolve
        "She positions herself above you, aligning the tip of your spear with her dripping slit"
        scene v4219
        with dissolve
        "Calessa thrusts down, hard and fast"
        "Tossing her hair and arching her back with a moan"
        "As her lower lips swallow you whole in an instant with a satisfying squelch"
        cal "Ah, it's still a surprise to me how good you feel"
        cal "It's almost a shame making you pay for this..."
        "She lifts and drops in furious succession, coating your pole in juices that run down"
        "And pool on the bedsheets and onto your belly"
        scene v4221
        with dissolve
        "She leans forward, resting her weight on her hands"
        "Giving her leverage to bear down on you with more force"
        "Seeking deeper pleasure as she reaches the edge..."
        cal "You're gonna make me cum, stud. Ooooh!"
        "You feel her pussy clench like a vice grip"
        "Her hands grasping at the bedsheets"
        "Her legs and hips quake, rapid and fierce, in total satisfaction"
        "Her voice is a half moan half shriek of blissful rapture"
        scene v4227
        with dissolve
        cal "Oh, how rare it is that I find someone who is able to handle me"
        "She looks you straight in the eyes with a glint and a bright smile"
        "But you haven't yet been satisfied"
        MC "That's great, but you're not done yet"
        "You thrust hard upward into her depths, signalling her to finish her job"
        cal "Don't worry, stud."
        cal "I haven't forgotten what you came here and paid good money for"
        scene v4219
        with dissolve
        "After a moment to regain her senses"
        "She continues bearing down on you forcefully, but it's not enough..."
        "You grasp her exorbitant breasts and begin pumping your own hips"
        "Meeting her in the midst of her ferocious downward thrust"
        "Making her gasp and squeal in pleasure"
        "You utter to her whilst launching an assault of your own on her pleasure center:"
        scene v4227
        with dissolve
        MC "You're supposed to be pleasing me, not yourself, woman."
        cal "I can't help it, I... Oooh! Fuck!"
        "The persistent pummeling of her cervix renders her incapable of thought"
        "She cries out in screams of pure joy"
        "Incessantly bringing her hips to clash with yours, seeking more pleasure"
        scene v4221
        with dissolve
        "Calessa begins to sieze and quiver"
        "Panting and gasping as her inner walls tightly clasp your tumid mast once more"
        scene v4226
        with dissolve
        "You flip her on her back as she begins to tire"
        "Her sinful body now only serving as a receptacle for your rampant lust."
        "She lies there in submission"
        "Throwing her arms back above her head and spreading her legs"
        "Giving you unfettered access in order to appease your desires"
        "She arches her back and moans loudly in the grips of yet another wave of euphoria."
        "Your seemingly unending hunger finally sated..."
        "You decide on where to unleash the results of your climax..."
        menu:
            "Cum inside":
                "You decide to continue furiously pounding away at her hole"
                "Thrusting into her ever faster and harder whilst she's in the throes of ecstasy"
                show shot
                with hpunch
                scene v4226c
                with dissolve
                show shot
                with hpunch
                hide shot
                "She gasps sharply, eyes wide and mouth agape, gripping the bedsheets tightly"
                "As she feels your seed begin to flow into her deepest parts"
                "She rolls her eyes and throws her head back in rhapsody"
                "Arching her back and tightly grasping her breast in delight"
                "Soon as you've finished plastering her insides with white"
                "You release yourself from her confines"
                scene v4225c
                with dissolve
                jump v4end50fuck
            "Cum on her face":

                "You pull out of her warm hole and set your sights on her luscious lips"
                MC "You're gonna suck me off till I'm about to blow"
                scene v4222
                with dissolve
                "You point the crest of your rigid mast at her parted lips as she opens wide"
                "And begins to suck"
                "She takes you deeper into her open maw, but her suction is weak"
                "And you need more to finish"
                "You grab the top of her head and furiously buck your hips"
                "Slamming your rod deep into her face and down her throat"
                "Her eyes widen as she moans on your shaft"
                "Overwhelmed by the suddenness of your ravaging"
                "Gasping for breath as you punish her throat"
                "A few more thrusts is all you need to feel yourself on the verge"
                scene v4223
                with dissolve
                "You remove your pulsating phallus from her lips, ready to blow"
                "She opens wide"
                "Panting and gasping for breath as you unload onto her face and into her mouth"
                scene v4224
                with dissolve
                "She breathes heavily through her nose"
                "As she swallows the load that landed on her tongue"
                "She takes a moment to catch her breath"
                "Lapping up blobs of jizz on her face as she does so"
                cal "Mmm, fuck, what did you do to me...?"
                scene v4225fc
                with dissolve
                jump v4end50fuck

label v4end50fuck:
    "She lies on the bed, sprawled out and lightly shaking"
    "Totally spent and basking in the afterglow of her orgasms"
    "She stares up at the ceiling, still trying to catch her breath"
    cal "Ho...ly... fuck... Mmmm!"
    "She rubs her pussy for brief moment"
    "Closing her eyes and biting her lip while she smiles"
    "Still experiencing small orgasms from the overwhelming amounts of pleasure"
    scene v4207
    with dissolve
    "After another moment of relaxation, she's now facing you in bed"
    cal "That was amazing. I really feel like I should be paying you for that"
    scene v4208
    with dissolve
    "She walks over to you, speaking to you in a voice that sounds as though she's pleading"
    "With an equally similar look on her face"
    cal "I, um... would really like it if you came by to visit me again sometime"
    MC "Yeah, I'll do that"
    cal "Great! Well, I'll see you again some other time..."
    MC "Looking forward to it"
    scene black
    with dissolve
    "You leave the brothel"
    jump v4itsnight
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
