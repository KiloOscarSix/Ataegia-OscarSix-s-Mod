label caveinteriorv2:
    scene v2065
    with dissolve
    "You managed to get inside the cave"
    MC "It's much better in here, but it's so dark"
    MC "I need to do something so I can see"
    menu:
        "{color=#1BBB20}Use Magelight{image=001alteration}":
            scene v2065
            with dissolve
            MC "I think that Magelight will allow me to see where I am"
            scene v2066
            with dissolve
            scene v2067
            with dissolve
            scene v2068
            with dissolve
            MC "Nice I can see this place now"
            "You start to hear something above you"
            MC "What the...?"
            scene v2071
            with dissolve
            MC "Oh Shit!! A giant spider!!"
            scene v2072
            with dissolve
            MC "And it's coming for me..."
            MC "I have to do something"
            scene v2074
            with dissolve
            MC "Now!!"
            jump fightspiderv2
        "Don't use anything and rest{color=#FF0000} (Game over)":


            scene v2065
            with dissolve
            MC "I'll just rest a bit here"
            "As you are falling asleep you start to hear something"
            MC "Am I hearing things? What's going on?"
            scene v2069
            with dissolve
            MC "What the..? Is that a..."
            scene v2070
            with dissolve
            MC "Argh!!"
            show youaredead
            "You were killed by a giant frost spider"
            "Better luck next time"
            return


label fightspiderv2:
    scene v2074
    with dissolve
    menu:
        AB "Use only what you have >= 4 or {color=#FF0000}game over{/color}"
        "Use Fireball{image=001battle}":
            scene v2075
            with dissolve
            if Destpoints  >= 4:
                scene v2076dest
                with dissolve
                "You cast a Fireball that hit the spider"
                scene v2077
                with dissolve
                MC "Is it dead? It looks dead"
                jump spidersareuglyv2
            else:
                "You failed to cast Fireball"
                jump deadbyspiderv2
        "Use Telekinesis{image=001myst}":

            scene v2075
            with dissolve
            if Mystpoints  >= 4:
                scene v2076myst
                with dissolve
                "You use Telekinesis to throw the spider against the cave wall"
                scene v2077
                with dissolve
                MC "Is it dead? It looks dead"
                jump spidersareuglyv2
            else:
                "You failed to use Telekinesis"
                jump deadbyspiderv2
        "Use Summon Lizard{image=001summon}":

            scene v2078
            with dissolve
            if Summpoints  >= 4:
                scene v2079
                with dissolve
                "You summon a Lizard to fight the spider"
                scene v2080
                with dissolve
                MC "That's it!! Take it down!!"
                scene v2081
                with dissolve
                "Your Lizard looks back at you showing you the results"
                MC "Is it dead? Well done!"
                jump spidersareuglyv2
            else:
                "You failed to summon a creature"
                jump deadbyspiderv2
        "Use Turn to stone{image=001alteration}":

            scene v2078
            with dissolve
            if Altepoints  >= 4:
                scene v2083
                with dissolve
                "You turned the spider into stone"
                MC "Ahahaha!! You won't be attacking me again"
                jump spidersareuglyv2
            else:
                "You failed to cast your spell"
                jump deadbyspiderv2
        "Use Fear{image=001illusion}":

            scene v2078
            with dissolve
            if Iluspoints  >= 4:
                scene v2082
                with dissolve
                "You cast fear and the spider ran away"
                MC "Yeah keep running!!"
                scene v2068
                with dissolve
                MC "That was easier than I expected"
                jump spidersareuglyv2
            else:
                "You failed to cast Fear"
                jump deadbyspiderv2

label spidersareuglyv2:
    scene v2068
    with dissolve
    MC "What should I do now?"
    MC "Wait... What is..."
    scene v2084
    with dissolve
    MC "That?! Oh shit!! I need to do something"
    scene v2085
    with dissolve
    MC "There are too many of them, I need to run"
    "You run around the cave trying to escape"
    "Until you find a large hole in the ground"
    scene v2086
    with dissolve
    MC "I... Fuck it! I need to jump"
    scene v2087
    with hpunch
    scene v2087
    with vpunch
    scene v2087
    with hpunch
    scene v2087
    with vpunch
    scene black
    "You hit your head against someting and are knocked out"
    scene meanwhile
    with dissolve
    scene v2088
    with dissolve
    Bredita "My lovely Ayna, you're even more beautiful than I remember"
    ayna "Bredita..."
    Bredita "It would be polite for you to compliment me back you know?"
    scene v2089
    with dissolve
    Bredita "We are in such a beautiful place"
    scene v2090
    with dissolve
    Bredita "It really brings out the blue in your eyes"
    scene v2091
    with dissolve
    ayna "Will you cut the crap?!"
    ayna "Do you have anything important to say?"
    ayna "Or are you just stalling for time?"
    ayna "Trying to get me to lower my guard?"
    Bredita "Oh..My dear Ayna, straight to the point"
    Bredita "Very well, let's talk about the devil siblings"
    ayna "Goggos and Zegladar... those two..."
    Bredita "Yes!! Those two... Do you remember?"
    Bredita "Goggos almost raped you, do you remember who saved you?"
    scene v2090
    with dissolve
    ayna "You..."
    Bredita "Yes... And how did you thank me?"
    Bredita "By expelling me from the College..."
    scene v2091
    with dissolve
    ayna "You were playing with the dead!!"
    ayna "You used your fellow colleagues bodies, with no care in the world"
    ayna "And for what?! Just to learn Necromancy?!"
    Bredita "Don't play saint with me, you're also trained in Necromancy"
    scene v2090
    with dissolve
    Bredita "You were quite skilled if I remember correctly"
    scene v2091
    with dissolve
    ayna "I never used my colleagues dead bodies for fun!"
    ayna "And I certainly didn't turn living people into undead"
    Bredita "I see that we still don't see eye to eye... That's a shame..."
    ayna "Will you tell me now why you wanted to talk with me?"
    ayna "Tell me about the devils"
    Bredita "Well, they came to me asking for help"
    Bredita "To attack your beloved College"
    ayna "Why?"
    Bredita "They must think that I hate you as much as they do"
    ayna "No... I mean, why do they want to attack the College?"
    scene v2090
    with dissolve
    ayna "They want to destroy us and the Allesterium"
    ayna "But why now? And why try to make a deal with you?"
    ayna "It sounds like they are afraid of something..."
    Bredita "Maybe your boy?"
    scene v2091
    with dissolve
    ayna "What? My boy?"
    Bredita "Yes... Don't play dumb with me, Ayna"
    Bredita "Your boy, you call him [MC] if I'm not mistaken"
    ayna "How can you... nevermind... What about him?"
    Bredita "You think I don't feel his power?"
    Bredita "It was only a matter of time before the devils felt it too"
    ayna "I need to go... And prepare..."
    Bredita "Very well my dear, If you need my help and are ready to pay..."
    Bredita "Just tell me..."
    scene black
    MC "Ah...My head... It's so dark here"
    "You feel some sort of wooden door in front of you"
    MC "Is this a door? Let's open it, better than facing more spiders"
    scene v015069
    with dissolve
    MC "What the hell? Am I at the College?"
    "You discovered a secret passage"
    MC "Where is everybody? My head still hurts"
    MC "I think I need to go lie down for a bit"
    "You go to your room"
    scene v015009
    with dissolve
    MC "I'm need to lay down..."
    fannay "Hey [MC]!!"
    scene v015001
    with dissolve
    MC "Oh... What now?"
    scene v2092
    with dissolve
    fannay "I knew I saw you arriving"
    fannay "What's the matter?"
    scene v2093
    with dissolve
    fannay "You look a little distant"
    MC "I bumped my head, but I'm fine now"
    fannay "Do you want a kiss to make you feel better?"
    menu:
        "{color=#1BBB20}Yes, that would help for sure":
            scene v2094
            with dissolve
            fannay "Hmmm here you go then"
            fannay "Muahw!"
            jump midav2st2
        "No, I have a girlfriend you know?":
            scene v2095
            with dissolve
            fannay "Meh... I don't see the problem..."
            jump midav2st2

label midav2st2:
    amida "Hey [MC]!!"
    scene v2096
    with dissolve
    fannay "Right on time..."
    amida "Hey [MC] are you there?"
    scene v2097
    with dissolve
    fannay "Your pretty girl must have sensed you in danger or something.. Heheh"
    fannay "Let me open the door for her"
    scene v2098
    with dissolve
    fannay "Hello, my dear"
    scene v2099
    with dissolve
    amida "Fannay? What are you doing here?"
    fannay "Oh, I came to ask if [MC] and you wanted to come to the party later"
    scene v2100
    with dissolve
    amida "Party? What party?"
    fannay "Our graduation party? For passing the final exam"
    MC "Yeah... I was going to ask you next"
    amida "Sure... I think that'll be ok"
    amida "I came here to tell you [MC], the Archmage wants to see you"
    amida "She's waiting for you outside"
    MC "(Damn... I really need a nap)"
    MC "Ok I'll meet her in a minute"
    fannay "I need to go..."
    amida "I'll go too"
    scene v2101
    with dissolve
    fannay "Bye"
    amida "Bye my love"
    MC "Bye ladies..."
    "You leave your room to look for the Archmage"
    scene v15mission048
    with dissolve
    ayna "Hey [MC]!"
    MC "Hello Archmage"
    scene v15mission050
    with dissolve
    ayna "Is everything ok with you?"
    MC "Yes, everything's fine, just a little tired"
    MC "I was looking for you earlier"
    MC "But nobody knew where you were"
    scene v15mission049
    with dissolve
    ayna "I...Was... Meditating. Sometimes, even I need to leave the College"
    MC "I can understand that"
    scene v15mission050
    with dissolve
    ayna "Well, I have a new mission for you"
    if savedgirl == True:
        ayna "You completed the previous mission and saved the girl"
        ayna "So you deserve a new mission to show your skills"
        jump missionv2st2
    else:
        ayna "You didn't find the missing girl previously"
        ayna "Luckily Master Katarro found her"
        ayna "But I think you deserve a second chance"
        jump missionv2st2

label missionv2st2:
    MC "Thank you Archmage, what do you need me to do?"
    scene v15mission049
    with dissolve
    ayna "It's a complicated matter, it has to do with the Slayers"
    MC "The Slayers?!"
    ayna "Yes... I need you to go to the city, here on Allesterra"
    ayna "You need to go to a tavern called Sunstone Mask"
    ayna "There you will meet a Dark Elf named Onzanu"
    ayna "I can't send another mage because it will draw too much attention"
    ayna "And I don't believe any other student is ready for this"
    MC "I'll do it, it's not a problem"
    scene v15mission050
    with dissolve
    ayna "Great!! Bring him here as soon as you can, and please be careful"
    MC "I will, don't worry"
    scene v15mission048
    with dissolve
    ayna "Here you'll need this"
    $ Gold += 10
    "You got 10 gold and a passage to the city"
    scene v15mission050
    with dissolve
    ayna "You'll need this pass to enter the city"
    ayna "Please leave immediately [MC], and thank you again"
    MC "Of course Archmage, thank you for the pass"


label v2st2v2st2:
    scene allesterra
    call screen allesterramapv2st2

label nottherev2:
    MC "I'll visit that place some other time"
    MC "I need to go to the city as fast as possible"
    jump v2st2v2st2


label cityallesterrav2st2:
    scene v2051n
    with dissolve
    MC "It's so dark already, there's the guard"
    MC "If he doesn't allow me to enter I'll..."
    scene v2052n
    with dissolve
    sol "What do you want at this hour?"
    MC "I want to go inside, I have a pass"
    sol "Let me see... Hmmm"
    sol "Yes... Everything is fine"
    sol "You can go inside, but don't disturb anyone or anything"
    scene v2170
    with dissolve
    "You walk around the city looking for the tavern"
    scene v2171
    with dissolve
    MC "Sunstone Mask, is that it? Let's get inside"
    scene v2102
    with dissolve
    "You enter the tavern, it's almost empty"
    MC "This must be the place, now where is that Dark Elf?"
    MC "Let's ask the tavern keeper"
    scene v2103
    with dissolve
    keeper "Hey, what can I get you?"
    MC "Hi, I'm looking for someone"
    keeper "This is not that kind of place, I can only get you a drink"
    keeper "If you want girls, there are other places in the city"
    MC "No, actually I'm looking for a Dark Elf. I was told I should meet him here"
    keeper "So no girls, you are looking for a guy, a Dark Elf"
    MC "No... I... Nevermind..."
    scene v2104
    with dissolve
    keeper "I'm just kidding, there is a Dark Elf upstairs"
    keeper "It's probably who you are looking for"
    MC "Upstairs? thanks!!"
    arnoldus "Hey young man!!"
    "You turn around and see"
    scene v2105
    with dissolve
    "A couple having drinks"
    arnoldus "Join me and my wife here!!"
    arnoldus "We are celebrating, drink all you want it's on me"
    scene v2106
    with dissolve
    giselle "Please have a seat here"
    arnoldus "Come on, sit down"
    scene v2107
    with dissolve
    "You decide to sit down for a while"
    arnoldus "I'm Duke Arnoldus and this is my beloved wife Giselle"
    MC "I'm [MC], nice to meet you"
    giselle "Nice to meet you [MC]"
    arnoldus "Hey!! Bring this young man some ale"
    "You stay with them for a while"
    scene v2108
    with dissolve
    "After a lot of drinking and partying"
    "You look at Arnoldus and he is completely drunk"
    giselle "Again...? You just can't handle your drink..."
    MC "Excuse me, I'm very sorry but I need to go, I have to meet someone"
    giselle "Oh.. Ok, sure. Nice meeting you"
    scene v2109
    with dissolve
    MC "(I need to check if Onzanu is upstairs)"
    "You move upstairs"
    scene v2110
    with dissolve
    "You see a Dark Elf all alone, he looks worried"
    "This must be the guy I'm looking for"
    scene v2111
    with dissolve
    MC "Hello, are you Onzanu?"
    scene v2112
    with dissolve
    onzanu "What the hell!?"
    onzanu "Don't disturb me!! Get the hell out!!"
    MC "Ok... I'm sorry?? I'll leave"
    scene v2113
    with dissolve
    onzanu "Pssst, keep quiet, they have been following me"
    onzanu "Meet me tomorrow morning near the docks"
    onzanu "I have to get rid of the people following me..."
    MC "Ok... We shall meet tomorrow then..."
    onzanu "Tomorrow as soon as the sun rises, meet me at the docks"
    onzanu "Make sure you are not followed, now go outside"
    onzanu "While they are looking at you I'll leave"
    MC "They?... Hmm.. Ok...Sure... See you tomorrow..."
    scene v2171
    with dissolve
    "You decide to go outside and wait for a while"
    MC "I think he had enough time to leave... It's late..."
    MC "Now... where will I sleep? I'll ask the tavern keeper"
    arnoldus "Ahahaha, then I... hick.. told them.."
    scene v2114
    with dissolve
    arnoldus "Suck my cock you bastards!!"
    giselle "Meh... I always have to carry you..."
    arnoldus "I need to..."
    scene v2115
    with dissolve
    arnoldus "Blahhh"
    $ helparnoldus = 0
    menu:
        "{color=#1BBB20}Help them":
            MC "Maybe I should help them? They did buy me drinks after all"
            scene v2116
            with dissolve
            giselle "Hi [MC], it's always the same thing..."
            giselle "Arnoldus drinks too much and I have to take care of him..."
            MC "I can help don't worry"
            $ helparnoldus = 1
            jump helpingarnold
        "Ignore them and go inside":

            MC "That's not my problem, let's get inside"
            jump nothelparnold

label helpingarnold:
    scene v2119
    with dissolve
    menu:
        AB "If heal>= 4 the first option will work"
        "Use your healing on Arnoldus":
            scene v2120
            with dissolve
            MC "Let me try something Giselle"
            scene v2121
            with dissolve
            giselle "Wow, you're a Mage?"

            if Healpoints >= 4:
                $ helparnoldus = 3
                scene v2122
                with dissolve
                arnoldus "I'm.... Feeling... Better..."
                scene v2123
                with dissolve
                arnoldus "That... Was... Amazing!!"
                arnoldus "I feel great, I can get drunk again, ahahah"
                giselle "No more drinks..."
                arnoldus "Fine... Hey [MC] do you have a place to stay tonight?"
                MC "Actually I don't..."
                scene v2124
                with dissolve
                arnoldus "Then you will stay with us, let's go to our place"
                giselle "Yes, it's the least we can do"
                menu:
                    "{color=#1BBB20}Go with them":
                        scene v2123
                        with dissolve
                        MC "That would be great, I didn't know where I was going to stay"
                        scene v2124
                        with dissolve
                        arnoldus "Great! My house is close, let's go"
                        scene v2125
                        with dissolve
                        arnoldus "We're almost there, it's right there"
                        scene v2126
                        with dissolve
                        giselle "We have arrived, let's get inside"
                        jump gisellehomev2
                    "Refuse":

                        scene v2123
                        with dissolve
                        MC "What am I thinking, I forgot I paid for a room already"
                        arnoldus "I'll pay you back another time then, don't worry"
                        MC "Maybe another time, thank you"
                        MC "See you around"
                        "You went inside the tavern"
                        jump nothelparnold
            else:
                scene v2120
                with dissolve
                MC "It didn't work... But I can help you carry him home"
                scene v2119
                with dissolve
                giselle "That would be great... let's go"
                jump carryarnoldv2
        "Help Giselle carrying Arnoldus home":




            scene v2119
            with dissolve
            MC "I can help you carry him home"
            giselle "That would be great... let's go"
            jump carryarnoldv2

label carryarnoldv2:
    scene v2117
    with dissolve
    giselle "Yes, hold him on that side, let's go"
    giselle "It's not to far from here"
    scene v2118
    with dissolve
    giselle "See, it's right there"
    MC "So... Does he do this on a daily basis?"
    scene v2117
    with dissolve
    giselle "Unfortunatly yes... He loves ale, but he always drinks too much"
    "You arrive at their place and put Arnoldus on a bench"
    scene v2127
    with dissolve
    giselle "Look at him... Completely wasted..."
    MC "Someone will have a massive headache tomorrow, that's for sure"
    scene v2128
    with dissolve
    giselle "I think that he isn't affected by that anymore, heheheh"
    giselle "Let me show you our guest room, you can stay there tonight"
    MC "I... Don't think I should..."
    giselle "Nonsense, come on! I won't take a no for an answer"
    "You follow her to a room"
    scene v2131
    with dissolve
    giselle "Here we are, what do you think?"
    MC "It's nice, really nice, thank you"
    scene v2132
    with dissolve
    giselle "That's good, if you need anything just ask"
    scene v2133
    with dissolve
    giselle "'Anything at all'"
    menu:
        "{color=#1BBB20}Anything hmm?":
            scene v2132
            with dissolve
            giselle "Yes... If you understand what I mean..."
            giselle "Kiss me..."
            "She kisses you"
            MC "I..."
            giselle "You want more?"
            menu:
                "I think we had enough":
                    scene v2132
                    with dissolve
                    MC "I think I'll sleep now... I'm very tired"
                    scene v2134
                    with dissolve
                    giselle "Oh... Ok... Then I guess I'll see you tomorrow..."
                    scene v2135
                    with dissolve
                    giselle "Goodbye..."
                    "She leaves the room"
                    scene v2161
                    with dissolve
                    "You lie on the bed and quickly fall asleep"
                    show blink1
                    with dissolve
                    show blink2
                    with dissolve
                    show blink3
                    with dissolve
                    scene black
                    with dissolve
                    jump newdayv2
                "{color=#1BBB20}You bet your ass I want more":

                    scene v2132
                    with dissolve
                    giselle "That's good, let me show you something then"
                    jump fuckgisellev2
        "I want to sleep":

            scene v2134
            with dissolve
            giselle "Oh... Ok... Then I guess I'll see you tomorrow..."
            scene v2135
            with dissolve
            giselle "Goodbye..."
            "She leaves the room"
            scene v2161
            with dissolve
            "You lie on the bed and quickly fall asleep"
            show blink1
            with dissolve
            show blink2
            with dissolve
            show blink3
            with dissolve
            scene black
            with dissolve
            jump newdayv2


label gisellehomev2:
    scene v2129
    with dissolve
    "You get inside the house and Arnoldus sit's on a bench"
    arnoldus "Giselle my dear, show our guest here a place to sleep"
    giselle "Sure dear"
    scene v2130
    with dissolve
    giselle "[MC] follow me please. let me show you the guest room"
    MC "Thank you"
    scene v2131
    with dissolve
    giselle "Here we are, what do you think?"
    MC "It's really nice, I like it"
    scene v2132
    with dissolve
    giselle "That's good, if you need anything just ask"
    scene v2133
    with dissolve
    giselle "'Anything at all'"
    menu:
        "{color=#1BBB20}Anything hmm?":
            scene v2132
            with dissolve
            giselle "Yes... If you understand what I mean..."
            giselle "Kiss me..."
            "She kisses you"
            MC "I..."
            giselle "You want more?"
            menu:
                "I think we had enough":
                    scene v2132
                    with dissolve
                    MC "I think I'll sleep now... I'm very tired"
                    scene v2134
                    with dissolve
                    giselle "Oh... Ok... Then I guess I'll see you tomorrow..."
                    scene v2135
                    with dissolve
                    giselle "Goodbye..."
                    "She leaves the room"
                    scene v2161
                    with dissolve
                    "You lie on the bed and quickly fall asleep"
                    show blink1
                    with dissolve
                    show blink2
                    with dissolve
                    show blink3
                    with dissolve
                    scene black
                    with dissolve
                    jump newdayv2
                "{color=#1BBB20}You bet your ass I want more":

                    scene v2132
                    with dissolve
                    giselle "That's good, let me show you something then"
                    jump fuckgisellev2
        "I want to sleep":

            scene v2134
            with dissolve
            giselle "Oh... Ok... Then I guess I'll see you tomorrow..."
            scene v2135
            with dissolve
            giselle "Goodbye..."
            "She leaves the room"
            scene v2161
            with dissolve
            "You lie on the bed and quickly fall asleep"
            show blink1
            with dissolve
            show blink2
            with dissolve
            show blink3
            with dissolve
            scene black
            with dissolve
            jump newdayv2


label fuckgisellev2:
    scene v2132
    with dissolve
    giselle "Lie on the bed please"
    "You do what you're told"
    scene v2136
    with dissolve
    giselle "So what do you think? Do you like them?"
    MC "Yes I do, they are amazing"
    giselle "I see that you are growing downstairs..."
    MC "I...Can't help it..."
    "Without saying a word, she pulls your dick out"
    scene v2138
    with dissolve
    giselle "Wow, What a big thing we have here"
    giselle "I wish Arnoldus had such a big one"
    scene v2137
    with dissolve
    giselle "Now, let's see how well you can use your 'thing' hehehe"
    "She starts to stroke your cock"
    scene v2139
    with dissolve
    MC "Humm...That's good..."
    giselle "It looks tasty, let's try it out"
    scene v2140
    with dissolve
    giselle "Hummm"
    "You feel her tongue all over the place"
    MC "(Wow, she has some skills, is she going to...?)"
    scene v2141
    with dissolve
    MC "Oh...Yeah..."
    giselle "Mhmmhf hmmm"
    scene v2140
    with dissolve
    MC "(Oh shit, she is too good, I'm about to...)"
    MC "Ahhhh I'm cumming..."
    giselle "Mhmmmf"
    scene v2142
    with dissolve
    "She looks at you with a mouth full of cum"
    MC "Wow... You..."
    scene v2143
    with dissolve
    giselle "Gulp Gulp"
    scene v2144
    with dissolve
    giselle "Hmm tasty... Young cum is great"
    MC "Oh my..."
    giselle "There is still a bit here"
    scene v2145
    with dissolve
    giselle "Hmmm yes..."
    MC "Shit... You're great..."
    scene v2139
    with dissolve
    giselle "It's all clean now, but it's still hard..."
    giselle "I think you need something more..."
    "She gets up, looking at you"
    if helparnoldus == 3:
        scene v2146
        with dissolve
        giselle "So...Are you ready for the next stage?"
        MC "(What the fuck? Is that Arnoldus? Was he watching us?)"
        MC "I...Don't know..."
        "She removes her top"
        scene v2147
        with dissolve
        giselle "Does this help you decide?"
        menu:
            "Refuse, it's too weird":
                MC "I need to sleep now..."
                MC "I think you should leave"
                giselle "Oh...Ok..."
                scene v2148
                with dissolve
                giselle "Goodbye then..."
                "She leaves the room"
                scene v2161
                with dissolve
                "You lie on the bed"
                MC "That was weird... Was he enjoying his wife and me?"
                "You think about what happened for some time, then you fall asleep"
                show blink1
                with dissolve
                show blink2
                with dissolve
                show blink3
                with dissolve
                scene black
                with dissolve
                jump newdayv2
            "{color=#1BBB20}Fuck it, let's do it":

                $ helparnoldus = 4
                scene v2147
                with dissolve
                MC "Oh yes it does... I love it"
                MC "(Does she know that her husband is watching?)"
                scene v2149
                with dissolve
                giselle "Lie on the bed please, I'll show you something good"
                MC "Yes ma'am..."
                MC "(Is Arnoldus enjoying this?)"
                scene v2150
                with dissolve
                giselle "Let me take off the rest of my clothes"
                MC "You won't hear me complain"
                scene v2151
                with dissolve
                giselle "Your little guy doesn't seem to mind either"
                MC "Little guy?"
                scene v2152
                with dissolve
                giselle "Here, do you like what you see?"
                MC "Yes I do!"
                giselle "Are you ready to put it in?"
                "Before you could answer, she moved you inside her"
                scene v2153
                with dissolve
                MC "Oh...Hmmm"
                giselle "Hmmm... So big... I love it"
                giselle "I'm going to start moving now"
                scene v2154
                with dissolve
                "You can see your cock getting swallowed by her pussy"
                giselle "Wow... So good...Hmmm"
                MC "Shit... That's great..."
                scene v2155
                with dissolve
                scene v2156
                with dissolve
                scene v2155
                with dissolve
                scene v2156
                with dissolve
                giselle "Yes... More...I want more!!"
                giselle "Let me turn around"
                scene v2157
                with dissolve
                giselle "Look at my pussy, it's all stretched, put it in again"
                scene v2158
                with dissolve
                MC "Hmmm... Ahhh..."
                giselle "YES!! Cum... Make me cum!!"
                MC "Ahhhh!"
                giselle "Yes!!! Ahhhh!"
                scene v2159
                with dissolve
                giselle "That was great... I hope you can sleep better now"
                MC "Oh... I will..."
                scene v2160
                with dissolve
                giselle "Bye stallion... See you tomorrow..."
                MC "Bye..."
                scene v2161
                with dissolve
                MC "That was weird... Was he enjoying his wife and me?"
                "You think about what happened for some time, then you fall asleep"
                show blink1
                with dissolve
                show blink2
                with dissolve
                show blink3
                with dissolve
                scene black
                with dissolve
                jump newdayv2
    else:





        scene v2146a
        with dissolve
        giselle "So...Are you ready for the next stage?"
        MC "I...Don't know..."
        "She removes her top"
        scene v2147a
        with dissolve
        giselle "Does this help you decide?"
        menu:
            "Refuse, before Arnoldus shows up":
                MC "I need to sleep now..."
                MC "I think you should leave"
                giselle "Oh...Ok..."
                scene v2148
                with dissolve
                giselle "Goodbye then..."
                "She leaves the room"
                scene v2161
                with dissolve
                "You lie on the bed"
                "You think about what happened for some time, then you fall asleep"
                show blink1
                with dissolve
                show blink2
                with dissolve
                show blink3
                with dissolve
                scene black
                with dissolve
                jump newdayv2
            "{color=#1BBB20}Fuck it, let's do it":

                $ helparnoldus = 5
                scene v2147a
                with dissolve
                MC "Oh yes it does... I love it"
                MC "(I'm about to fuck someone's wife)"
                scene v2149a
                with dissolve
                giselle "Lie on the bed please, I'll show you something good"
                MC "Yes ma'am..."
                MC "(Let's hope Arnoldus doesn't show up)"
                scene v2150
                with dissolve
                giselle "Let me take the rest of my clothes off"
                MC "You won't hear me complain"
                scene v2151a
                with dissolve
                giselle "Your little guy doesn't seem to mind either"
                MC "Little guy?"
                scene v2152
                with dissolve
                giselle "Here, do you like what you see?"
                MC "Yes I do!"
                giselle "Are you ready to put it in?"
                "Before you could answer, she moved you inside her"
                scene v2153a
                with dissolve
                MC "Oh...Hmmm"
                giselle "Hmmm... So big... I love it"
                giselle "I'm going to start moving now"
                scene v2154
                with dissolve
                "You see your cock getting swallowed by her pussy"
                giselle "Wow... So good...Hmmm"
                MC "Shit... That's great..."
                scene v2155
                with dissolve
                scene v2156
                with dissolve
                scene v2155
                with dissolve
                scene v2156
                with dissolve
                giselle "Yes... More...I want more!!"
                giselle "Let me turn around"
                scene v2157a
                with dissolve
                giselle "Look at my pussy, it's all stretched, put it in again"
                scene v2158
                with dissolve
                MC "Hmmm... Ahhh..."
                giselle "YES!! Cum... Make me cum!!"
                MC "Ahhhh!"
                giselle "Yes!!! Ahhhh!"
                scene v2159
                with dissolve
                giselle "That was great... I hope you can sleep better now"
                MC "Oh... I will..."
                scene v2160a
                with dissolve
                giselle "Bye stallion... See you tomorrow..."
                MC "Bye..."
                scene v2161
                with dissolve
                MC "That was great, that woman is like fire..."
                MC "Hot and dangerous..."
                "You think about what happened for some time, then you fall asleep"
                $ renpy.end_replay()
                show blink1
                with dissolve
                show blink2
                with dissolve
                show blink3
                with dissolve
                scene black
                with dissolve
                jump newdayv2




label nothelparnold:
    scene v2102
    with dissolve
    "You are inside the tavern again"
    MC "Let's talk with the tavern keeper"
    scene v2103
    with dissolve
    keeper "You again, what do you need?"
    MC "Do you happen to have a free room for tonight?"
    keeper "If you mean available, yes... Free? No way.."
    scene v2104
    with dissolve
    keeper "I have a room, it will cost you 5 gold coins"
    MC "5 Gold coins?"
    keeper "Or you can sleep on the streets if you want..."
    menu:
        "You bet I will!":
            scene v2103
            with dissolve
            MC "I'll find some place else"
            scene v2170
            with dissolve
            MC "Shit...That was dumb. Now what?"
            MC "I guess I'll have to sleep here..."
            scene v2171
            with dissolve
            "You lie down, and it doesn't take long for you to fall asleep"
            scene black
            with dissolve
            scene v2169
            show blink3
            with dissolve
            hide blink3
            show blink2
            with dissolve
            hide blink2
            show blink1
            with dissolve
            MC "Yawn...Ahh..My back...That's what you get for sleeping on the streets..."
            MC "Let's look for Onzanu now"
            jump newdayv2pt2
        "Nah, here, take the gold{color=#FF0000} (-5 Gold)":

            scene v2103
            with dissolve
            $ Gold -= 5
            "You lost 5 Gold coins"
            keeper "Great! Follow me"
            scene v2164
            with dissolve
            keeper "Come on... Let's go"
            scene v2165
            with dissolve
            keeper "It's right here, let yourself"
            MC "Thanks, can you wake me up at sun rise?"
            keeper "What? Am I your servant or something?"
            keeper "Go on inside, there's some food there also"
            scene v2166
            with dissolve
            "You are in the room"
            MC "Well, it's better than I expected..."
            "You eat something and then lie on the bench"
            "It doesn't take long until you fall asleep"
            scene black
            with dissolve
            scene black
            with dissolve
            scene v2175
            with dissolve
            MC "Where the hell am I? Am I dreaming?"
            enainia "Oh... Hello [MC]"
            MC "(That voice)"
            scene v2168
            with dissolve
            enainia "Cat got your tongue?"
            MC "Princess Enainia, what are you doing here?"
            enainia "I should ask you that, you are in my Kingdom"
            MC "Really?"
            scene v2167
            with dissolve
            enainia "Yes... What do you think? It's great, isn't it?"
            MC "It is... I wasn't expecting this"
            scene v2168
            with dissolve
            enainia "Hey, come with me, I want to show you something"
            MC "Of course, Princess"
            scene v2176
            with dissolve
            enainia "This is my favorite place, I like to come here to relax"
            enainia "Take long baths, think about everything..."
            MC "Take long Baths?"
            enainia "Yes... Should we take a bath together?"
            scene v2177
            with dissolve
            MC "Wow... I.... Sure..."
            enainia "What's the matter?"
            enainia "Are you shy or something?"
            enainia "Don't you take baths?"
            MC "Of course I do, let's bathe together then"
            enainia "Great, let's do it!"
            scene v2177
            with dissolve
            enainia "Hey wake up! Wake up!!"
            MC "What??"
            scene v2179
            with hpunch
            scene v2179
            with vpunch
            keeper "Wake up kid!"
            MC "What the fuck!!"
            scene v2180
            with dissolve
            keeper "Hey! You told me to wake you up, don't get all agressive with me"
            MC "Right... Sorry... I need to go"
            keeper "Stupid kids these days..."
            scene v2169
            with dissolve
            MC "Alright, let's look for Onzanu"
            jump newdayv2pt2


label newdayv2:
    scene v2162
    with dissolve
    MC "Yawn.... Oh shit the sun is already up!"
    MC "I need to go!"
    "You dress yourself and leave the room"
    scene v2163
    with dissolve
    MC "This place is huge... where is the exit?"
    "You eventualy find out the exit"
    scene v2169
    with dissolve
    MC "Guess I should look for Onzanu again"
    jump newdayv2pt2

label newdayv2pt2:
    scene v2169
    with dissolve
    MC "He said to look for him in the docks"
    "You walk for a while until you find the docks"
    scene v2172
    with dissolve
    MC "I guess this is the place, now where is that guy?"
    "You wait for a while"
    onzanu "Where the hell have you been?"
    scene v2173
    with dissolve
    MC "I got... Delayed..."
    onzanu "Bullshit, you were sleeping... Anyway, ready to go?"
    MC "Yes, and your 'followers'?"
    scene v2174
    with dissolve
    onzanu "I tricked them last night, they are probably looking for me outside the city"
    onzanu "Damn Slayers... There are so many of them..."
    scene v2173
    with dissolve
    MC "Shall we go the College now?"
    onzanu "Yes let's go!"
    "You both leave the city"
    scene v2185
    with dissolve
    MC "So tell me, what is happening with the Slayers"
    onzanu "It's a long story... I'm sure you heard it"
    scene v2187
    with dissolve
    onzanu "Slayers are killing us all... They hate everyone who's different from them"
    if Racist == True:
        MC "(I can understand why they do it)"
        MC "(Our world is filled with these guys...)"
        MC "Yeah yeah, that's terrible"
    else:
        MC "Those bastards... Why are they like that?"
        onzanu "I don't know, but we have to stop them"
    scene v2186
    with dissolve
    onzanu "What about you? Have you met any Slayers?"
    MC "Not that I remember, but my village, family and friends are lost because of them"
    onzanu "That's terrible... What happened?"
    MC "Well, it happened when I was a kid, they invaded..."
    scene v2188
    with dissolve
    onzanu "Hey look! What's happening?"
    scene v2189
    with dissolve
    "You see a girl and two guys on the road"
    thug "Come on, we won't bite...Much..."
    thug2 "Don't play hard to get with us Isabella"
    isabella "I said no, did you not hear me?"
    scene v2190
    with dissolve
    thug2 "I'll buy you a drink first, what do you say?"
    isabella "Do I have to repeat myself? I said no!"
    scene v2191
    with dissolve
    thug "Little bitch, we won't take a no for an answer!!"
    isabella "Well if you insist..."
    scene v2192
    with dissolve
    isabella "Yahh! Take that!"
    thug "Arghh!"
    thug2 "Ah! My face!"
    scene v2193
    with dissolve
    isabella "I warned you... You didn't listen..."
    MC "Wow! That was great!"
    scene v2194
    with dissolve
    isabella "Hello, and you are?"
    MC "I'm [MC], that was awesome!"
    scene v2195
    with dissolve
    isabella "{i}giggle{/i}... I guess..."
    isabella "My name is Isabella and I'm a Demon Hunter"
    MC "A Demon Hunter? Wow..."
    isabella "Yes, Demons, Devils, Imps... You name it"
    MC "It's nice to meet you. I'm a Mage, maybe I could help you hunting someday"
    isabella "A Mage? Yes... I could use all the help that I can get"
    MC "I really need to go to the College now, but I'll see you again soon, I hope"
    isabella "Sure, I'm staying in Allesterra City for a while"
    MC "Great! I'll be sure to meet you there sometime"
    scene v2196
    with dissolve
    isabella "Sure, goodbye"
    scene v2186
    with dissolve
    onzanu "Now, that was impressive... Should we go?"
    MC "Yes, let's go!"
    scene meanwhile
    with dissolve
    scene v2181
    with dissolve
    suntako "I already told your emissaries general, I don't need gold"
    chang "What about power? Don't you want power?"
    suntako "What do you mean power?"
    chang "Hmmm, so you are interested, let's say that soon I'll be King"
    chang "And I will rule Irokumata"
    suntako "How do you plan to do that?"
    chang "I will marry the princess of Nagatashi, making me part of the royal family"
    scene v2182
    with dissolve
    chang "Then I will tell my King that they are planning to send an assassin"
    chang "To kill him, then... I'll kill him myself..."
    chang "And when my plan is successful, I'll be the King"
    suntako "And why are you telling me this?"
    chang "Do you want to be the ruler of Nagatashi? Help me, and you will be!"
    chang "Do we have a deal?"
    scene v2183
    with dissolve
    suntako "Very well, let me get ready"
    chang "That's great Master Suntako!"
    scene v2184
    with dissolve
    chang "Meet me at Nagatashi's dock in five days"
    scene black
    with dissolve
    scene v2197
    with dissolve
    ayna "[MC], welcome back! I was worried something may have happned"
    ayna "And you brought Onzanu, great work"
    scene v2198
    with dissolve
    onzanu "Archmage Ayna, it's a great pleasure to meet you"
    onzanu "There are so many stories about your deeds"
    onzanu "We didn't make it earlier because I was being followed"
    scene v2199
    with dissolve
    MC "But here we are, safe and sound"
    ayna "That's great, I knew I could count on you [MC]"
    ayna "Here, take this as a reward"
    $ Gold += 20
    "You got 20 gold"
    MC "Thanks Archmage!"
    ayna "You are dismissed now, you can go study or practice"
    MC "Hmm... Ok... Thank you"
    scene v2198
    with dissolve
    ayna "Onzanu come with me, we have so much to talk about"
    "Archmage Ayna and Onzanu left"
    scene hall
    with dissolve
    MC "What now?"

    fannay "Hey [MC]!"
    scene v2200
    with dissolve
    fannay "Why didn't you show up last night?"
    fannay "We had a great party..."
    scene v2201
    with dissolve
    fannay "Let me guess... You stayed with your pretty girl fucking all night"
    MC "Well, not exactly...I was doing something for the Archmage"
    fannay "Hahaha, you wish... She is too much for you..."
    fannay "And there is a rumor that she likes girls, hehehe"
    MC "That's not what I meant..."
    scene v2202
    with dissolve
    fannay "Yeah yeah sure... see you around"
    scene hall
    with dissolve
    MC "The Archmage prefers girls? From what I remember, it's not just a rumor..."
    scene v2203
    with dissolve
    katarro "What's not just a rumor?"
    MC "Damn!! What the hell!?"
    scene v2207
    with dissolve
    katarro "Sorry if I scared you"
    MC "Geez... You have to teach me how you do that..."
    katarro "Sure, some other time. Listen I need you to do something for me"
    scene v2203
    with dissolve
    MC "You need something from me?"
    katarro "Yes, I need you to go to the city and bring me something"
    MC "Ok..."
    katarro "I would do it myself but I have a meeting with the Elite"
    katarro "So I need someone else to do it, I've seen that you are a capable one"
    scene v2207
    with dissolve
    katarro "That's why I'm asking you, In return I'll train you in Mysticism"
    MC "Private lessons by one of the Elite?"
    katarro "Not lessons, 'Lesson'. After that we will see"
    MC "Sure, what do you need then?"
    katarro "Follow me"
    scene v2204
    with dissolve
    "You follow Master Katarro to the portal room"
    scene v2205
    with dissolve
    katarro "Are you ready to go?"
    MC "But I don't even know what I'm supposed to do in the city..."
    katarro "Right... I bought an amulet that is arriving today"
    katarro "When the ship arrives talk with the captain and tell him I sent you"
    katarro "He will know what to do... So are you ready?"
    MC "I guess so..."
    scene v2206
    with dissolve
    katarro "Very well, I've opened the portal straight to the city dock"
    scene v2208
    with dissolve
    katarro "There it is, ready for you"
    MC "That was fast..."
    scene v2209
    with dissolve
    katarro "Yeah sure... Go on now..."
    scene v2210
    with dissolve
    "You look at the portal and start to get closer to it"
    scene v15mission010
    with dissolve
    "It starts to pull you in"
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    scene v2172
    with dissolve
    MC "Wow... That was amazing...Wish I could do that"
    MC "Katarro is a strange guy... I guess geniuses are often mistaken by fools..."
    MC "He is surely an example of that... Creepy little fellow..."
    MC "I don't see any ship, let's get closer to the dock"
    scene v2211
    with dissolve
    MC "There are no ships around here... What now?"
    thug "It's you! The Mage!"
    scene v2212
    with dissolve
    MC "Yes... It's me indeed"
    thug "What are you doing here? Waiting for the ship?"
    MC "..."
    thug "Haven't you heard? Some pirates attacked the ship!"
    MC "Pirates? Shit..."
    MC "(What now? Should I tell Master Katarro?)"
    thug "Lord Runar is pissed! It's his ship after all"
    MC "Lord Runar? Your boss right?"
    thug "Yes he's my boss"
    scene v2213
    with dissolve
    if helpjackv2 == 1:
        MC "I want to talk to him"
        thug "What? Why?"
        menu:
            "I want to talk about the Lumberjack's debt":
                thug "You want to pay his debt? Hahah"
                thug "Very well, follow me!"
                jump lordrunarv2
            "There is something I need on that ship":
                thug "And? What does Lord Runar have to do with it?"
                MC "Well idiot, it's his ship, I need something that's on the ship"
                MC "We can help each other with this matter..."
                thug "Humm... Makes sense... Follow me then"
                jump lordrunarv2
            "You said that I could make money" if helpthugv2 == 1:
                thug "Yes I'm sure Lord Runar will have work for you"
                thug "Very well, follow me!"
                jump lordrunarv2
    else:
        if helpthugv2 == 1:
            MC "I want to talk to him"
            thug "What? Why?"
            menu:
                "You said that I could make money":
                    thug "Yes I'm sure Lord Runar will have work for you"
                    thug "Very well, follow me!"
                    jump lordrunarv2
                "There is something I need on that ship":
                    thug "And? What does Lord Runar have to do with it?"
                    MC "Well idiot, it's his ship, I need something that's on the ship"
                    MC "We can help each other with this matter..."
                    thug "Humm... Makes sense... Follow me then"
                    jump lordrunarv2
        else:
            menu:
                "There is something I need on that ship":
                    thug "And? What does Lord Runar have to do with it?"
                    MC "Well idiot, it's his ship, I need something that's on the ship"
                    MC "We can help each other with this matter..."
                    thug "Humm... Makes sense... Follow me then"
                    jump lordrunarv2

label lordrunarv2:
    "You follow the thug to a large manor"
    scene black
    with dissolve
    scene v2214
    with dissolve
    "Inside you see an old, fat man on a chair and a towering Tanzani man"
    scene v2215
    with dissolve
    thug "My Lord, here is the Mage I told you about earlier"
    thug "He wants to speak with you"
    runar "Very well, you are dismissed"
    thug "Very well my Lord"
    "The thug left you and the two men"
    scene v2216
    with dissolve
    runar "So you are a Mage? What do you want with me?"
    menu:
        "I want to talk about the Lumberjack's debt" if helpjackv2 == 1:
            scene v2217
            with dissolve
            runar "Really? That's an interesting subject"
            scene v021001
            with dissolve
            runar "Can you leave us? I'm sure he'll be more comfortable if you leave"
            scene v021002
            with dissolve
            "With a angry look on his face, the big man leaves"
            scene v021003
            with dissolve
            runar "Well, right now I only care about my ship"
            runar "If you find it we'll talk about that Lumberjack fellow"

            jump v021

        "I heard that you might have a job for me?" if helpthugv2 == 1:
            scene v2217
            with dissolve
            runar "Hmmm... If you are a real Mage I might have some jobs for you"
            scene v021001
            with dissolve
            runar "Can you leave us? I'm sure he'll be more comfortable if you leave"
            scene v021002
            with dissolve
            "With a angry look on his face, the big man leaves"
            scene v021003
            with dissolve
            runar "Well, right now I only care about my ship"
            runar "If you find it we'll talk about other possible assignments"
            jump v021
        "I want to talk about your missing ship":

            scene v2216
            with dissolve
            runar "What do you know about my ship?!"
            MC "Nothing, but there is something onboard that belongs to me"
            MC "So I can help you find the ship"
            scene v2217
            with dissolve
            runar "Really? Hmm... That's interesting..."
            scene v021001
            with dissolve
            runar "Can you leave us? I'm sure he'll be more comfortable if you leave"
            scene v021002
            with dissolve
            "With a angry look on his face, the big man leaves"
            scene v021003
            with dissolve
            runar "Well, right now I only care about my ship"
            runar "If you find it I'll pay you and maybe give you some more work"
            jump v021


label deadbyspiderv2:
    scene v2075
    with dissolve
    MC "Oh shit!"
    scene v2073
    with dissolve
    "The spider is too fast and reaches you"
    show youaredead
    with dissolve
    "You got killed by a Giant Frost Spider"
    "Better luck next time"
    return
