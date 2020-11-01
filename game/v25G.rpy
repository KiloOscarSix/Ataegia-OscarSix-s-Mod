label v25good:
    scene black
    with dissolve
    ayna "Time to wake up, sleepy head"
    scene v25032
    show blink1
    show blink2
    show blink3

    ayna "How's your head?"
    hide blink3
    with dissolve
    hide blink2
    with dissolve
    hide blink1
    with dissolve
    "You see the Archmage front of you"
    MC "I...What happened? where are we?"
    scene v25033
    with dissolve
    ayna "We are back in the College and you are in my room"
    ayna "I needed to be sure you were going to be alright"
    MC "Do you have any idea of what happened?"
    scene v25034
    with dissolve
    ayna "I know that you were attacked by a giant creature"
    ayna "And you were looking for something on that ship"
    MC "Then you showed up and that other woman..."
    ayna "Follow me"
    scene v25035
    with dissolve
    "You follow the Archmage to another room"
    scene v25036
    with dissolve
    "You both enter your room"
    MC "Why are we here?"
    ayna "I wanted to tell you something..."
    MC "Yes..."
    ayna "You are going to receive magic lessons directly from me"
    MC "Really? That's great, why me though?"
    ayna "Are you questioning my decisions?"
    MC "I...Didn't mean..."
    ayna "Hehehe, I'm kidding"
    scene v25037
    with dissolve
    ayna "I've added some advanced magic books to your collection"
    MC "Advanced magic books?"
    ayna "Yes, feel free to use them"
    ayna "I need to go for now, take your time to rest"
    scene v25178
    with dissolve
    "You see her leaving"
    MC "Wait, let me ask you something"
    scene v25176
    with dissolve
    ayna "Sure what's on your mind?"
    MC "I had a dream about you and that woman that saved me"
    scene v25177
    with dissolve
    ayna "You did? what kind of dream?"
    "You think back to the details of the dream and pause"
    MC "Hmmm I don't know exactly how to say it..."
    scene v25176
    with dissolve
    ayna "Oh come on, it can't be that bad"
    MC "Well, you called her Bredita, that's a name I've heard before"
    MC "You were lovers? And you felt something dangerous"
    MC "The dream ended when you said that you needed to talk with the Archmage"
    MC "But Bredita didn't seem to trust the Archmage"
    scene v25177
    with dissolve
    ayna "How could you... Is this the first time you have had such dreams?"
    MC "I've had some strange dreams before"
    ayna "I see that you're telling the truth..."
    scene v25176
    with dissolve
    ayna "So yes... That dream is from my past, you must have some hidden power"
    ayna "Your dreams will probably make more sense as you grow stronger"
    ayna "I need to leave now, do you have more questions?"
    MC "I want to know..."
    $ v25aynaresp = 0

label v25aynares:
    menu:
        "Who is Bredita?":
            ayna "Bredita has been an enemy of the College for some time"
            MC "Why did she help you against that monster then?"
            ayna "There are times when enemies must work together"
            ayna "This was such a time, however, you must remember this:"
            ayna "She is probably the smartest and most powerful person you'll ever meet"
            MC "More powerful than you?!"
            ayna "Maybe, I'm not really sure, but it's possible. But smarter? Definitely"
            jump v25aynares
        "Why was that creature after me?":

            ayna "It seems that the demons want you for some reason"
            ayna "Or just want you dead, we can't really know which"
            MC "Do you have an idea why?"
            ayna "They must know about your potential, like I do"
            ayna "Maybe they are afraid? Maybe they want to use you? I don't know"
            jump v25aynares
        "Can you tell me why Bredita is not part of the College anymore?":

            $ v25aynaresp = 1
            ayna "That is a very long story, maybe I'll tell you another time"
            MC "At least tell me what happened that day, what was that power you felt?"
            ayna "Ok, I guess I can spare a little more time"
            scene v25166
            with dissolve
            ayna "We went to see Suntako, as you know he was the Archmage"
            yBredita "Did you feel that Archmage?"
            suntako "Yes... I thought I would never see him again..."
            suntako "I was sure he was dead, how could this be?"
            yBredita "You know the one responsible for this power?"
            yayna "I feel not only a massive power but also a great evil"
            scene v25167
            with dissolve
            suntako "And that's why I want you to go and investigate"
            yayna "Very well, we will check what is happening"
            yBredita "Yes, this needs to be taken care of"
            scene v25168
            with dissolve
            suntako "You are not going Bredita, I want Ayna to take care of this"
            yBredita "What?! Are you kidding?"
            scene v25167
            with dissolve
            yayna "Isn't she coming with me?"
            yBredita "Is this because she is threatening your position as Archmage?"
            yBredita "You want to dispose of her??!!"
            scene v25169
            with dissolve
            yBredita "I will not allow this!! You think I don't see what you're planning?"
            suntako "You stop this right now!! I will not tolerate this!!"
            yBredita "I.... Will..."
            yayna "Please calm down Bredita"
            scene v25170
            with dissolve
            yBredita "You know what he is trying to do!"
            yayna "Please calm down, that will not help"
            scene v25176
            with dissolve
            ayna "Bredita never trusted Suntako, she always believed he feared me"
            ayna "I was able to calm her down, I understood her though"
            scene v25171
            with dissolve
            yayna "I need to do this, I'll be back in no time"
            suntako "This will be discussed by the Elite"
            suntako "Such insubordination shall not be forgotten"
            yayna "Let me go alone, please"
            yBredita "Hmmf...."
            scene v25172
            with dissolve
            ayna "Bredita left me and Suntako alone"
            scene v25173
            with dissolve
            suntako "I will do everything in my power to expel her from here"
            suntako "She doesn't have the authority to question me!!"
            yayna "Don't you think we have more serious matters at hand right now?"
            scene v25176
            with dissolve
            ayna "Then I went to the place I felt the power source"
            MC "That's.... But what happened next?"
            ayna "I knew that Bredita wouldn't let me go alone"
            ayna "It only took her a few minutes to find me"
            scene v25047
            with dissolve

            ayna "We reached a cave that seemed to be the source of the power"
            scene v25048
            with dissolve
            yayna "This looks like a Necromancer hideout"
            yBredita "Hey! I'm the specialist on Necromancy you know?"
            yayna "Heheh sure my dear, I know"
            scene v25049
            with dissolve
            yayna "What is that?! Do you feel it?"
            yBredita "It's amazing!!"
            scene v25050
            with dissolve
            Nonen "Hmm tasty... Two new toys for me, powerful ones..."
            Nonen "It's a shame I'll have to ruin those pretty faces"
            yBredita "Is that a Lich?! Shit... You need to come with us"
            Nonen "No man alive or dead commands me, my power is absolute"
            yayna "Look out! He is casting something"
            scene v25051
            with dissolve
            yBredita "Bring it on... Lich!!"
            scene v25052
            with dissolve
            ayna "We fought the Lich for hours"
            ayna "But he was too strong, something I couldn't believe"
            scene v25053
            with dissolve
            ayna "We used all we knew but it had no effect..."
            scene v25176
            with dissolve
            ayna "We had never faced such an opponent, it was a Lich after all..."
            MC "What is a Lich?"
            ayna "A Lich is a powerful Mage who has traded his humanity for power"
            MC "Wow... What happened next?"
            ayna "I'll tell you... Some other time."
            MC "What? why?"
            ayna "It's long story, if I tell you everything today what will we talk about tomorrow?"
            jump v25aynares



        "See you tomorrow then" if v25aynaresp == 1:
            ayna "Sure, rest now, feel free to read a book if you're in the mood"
            "She turns around and while leaving says"
            scene v25178
            with dissolve
            ayna "Try not to dream about naked girls again, okay?"
            "How could she know?"
            scene v25038
            with dissolve
            "She leaves you alone"
            menu:
                "Try to sleep":
                    scene black
                    with dissolve
                    "You lied on the bed closed your eyes and fell asleep"
                    jump v25goodmorning
                "[abgreen]Read a book":

                    scene v25038
                    with dissolve
                    MC "There are books about everything, even Necromancy?"
                    menu:
                        "Read about Battlemagic[abgreen] [abdestpoint] {image=001battle}":
                            "You grab a book about Battlemagic and lie on the bed"
                            $ Destpoints += 1
                            "Your Battlemagic skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25goodmorning
                        "Read about Summoning[abgreen] [absummpoint] {image=001summon}":

                            "You grab a book about Summoning and lie on the bed"
                            $ Summpoints += 1
                            "Your Summoning skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25goodmorning
                        "Read about Alteration[abgreen] [abaltepoint] {image=001alteration}":

                            "You grab a book about Alteration and lie on the bed"
                            $ Altepoints += 1
                            "Your Alteration skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25goodmorning
                        "Read about Illusion[abgreen] [abiluspoint] {image=001illusion}":

                            "You grab a book about Illusion and lie on the bed"
                            $ Iluspoints += 1
                            "Your Illusion skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25goodmorning
                        "Read about Mysticism[abgreen] [abmystpoint] {image=001myst}":

                            "You grab a book about Mysticism and lie on the bed"
                            $ Mystpoints += 1
                            "Your Mysticism skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25goodmorning
                        "Read about Healing[abgreen] [abhealpoint] {image=001heal}":

                            "You grab a book about Healing and lie on the bed"
                            $ Healpoints += 1
                            "Your Healing skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25goodmorning
                        "Read about Necromancy[abgreen] [abnecropoint] {image=001necro}":

                            "You grab a book about Necromancy and lie on the bed"
                            $ Necropoints += 1
                            "Your Necromancy skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve
                            jump v25goodmorning

label v25goodmorning:
    scene black
    with dissolve
    MC "{i}Yawn!!{/i}"
    scene v25038
    with dissolve
    MC "I slept quite well and no dreams this time..."
    MC "I guess it's time to dress and look for the Archmage"
    "You hear a voice outside the door, but you can't figure who it is"
    "You see the door opening and realize you're still naked"

    scene v25039
    with dissolve
    amida "So you are here!! I'm so glad you are ok!"
    menu:
        "Hello my love[ablovecolor] [ablove]":
            $ midalove += 1
            "Mida love increased"
            amida "[MC] my love!!"
        "Oh... It's you Mida":

            amida "Hello..."

    scene v25040
    with dissolve
    amida "Oh... [MC] I was so worried about you, I missed you!"
    MC "I missed you too, my dear"
    amida "Is that why you are naked, waiting for me?"
    MC "Well I just..."
    scene v25041
    with dissolve
    amida "Maybe I need to get naked too?"
    MC "I guess it couldn't hurt to try that..."
    "Knock Knock"
    scene v25042
    with dissolve
    ayna "[MC]? Are you awake?"
    amida "Shit... It's the Archmage!!"
    MC "Quick dress yourself!"
    "You and Mida dressed as fast as a lightning"
    MC "Come on in Archmage"
    scene v25043
    with dissolve
    ayna "Oh... Hello Mida...Did you spend the night here with [MC]?"
    scene v25044
    with dissolve
    amida "Oh I... No... I just got here... I..."
    amida "I wanted to see if [MC] was ok, I was very worried"
    scene v25045
    with dissolve
    ayna "You can calm down, it's not a problem for me if you visit [MC]"
    ayna "Come with me now, though"
    scene v25046
    with dissolve
    amida "Sure Archmage..."
    ayna "[MC] meet me at the training room"
    scene v25038
    with dissolve
    "They left"
    scene black
    with dissolve
    "You went to the training room to meet the Archmage"
    scene v25179
    with dissolve
    ayna "So [MC], are you ready for some real training?"
    ayna "It will be really hard, believe me... Ready?"
    MC "You bet I am!!"
    scene v25180
    with dissolve
    ayna "Great! That's the spirit"
    ayna "Let me get the room ready then"
    scene v25181
    with dissolve
    "She begins to cast some powerful spells, you've never felt anything like it"
    MC "Wow... "
    scene v25182
    with dissolve
    ayna "Ok, so now the room is protected against damage, are you ready?"
    MC "Yes I am, what do you want me to do?"
    ayna "Attack me with all your might!"
    MC "What? Attack you?"
    ayna "Yes... use a Battlemagic spell on me"
    MC "But... I..."
    ayna "I {i}can{/i} handle it, you know?"
    MC "If you insist!"
    scene v25183
    with dissolve
    "You start to cast Frost"
    scene v25184
    with dissolve
    scene v25185
    with dissolve
    scene v25186
    with dissolve
    "She looks angry..."
    ayna "What was that? Can you try for real this time?"
    MC "I..."
    scene v25187
    with dissolve
    ayna "Oh I know... You don't want to hurt me right? Very well"
    scene v25188
    with dissolve
    "What is she doing? Is she casting something?"
    scene v25189
    with dissolve
    scene v25190
    with dissolve
    scene v25191
    with dissolve
    scene v25192
    with dissolve
    scene v25193
    with dissolve
    scene v25194
    with dissolve
    scene v25195
    with dissolve
    "You see a massive creature between you and the Archmage"
    ayna "What about him? Are you afraid of hurting him too?"
    "You feel chills run up your spine when you hear the Archmage say"
    ayna "Kill that boy, be quick about it!"
    MC "Oh...Shit..."
    "You see her go to the end of the room"
    scene v25196
    with dissolve
    "The creature starts to move in your direction"
    $ enemy = "g1"
    $ enemychoice = 0
    jump combat_tutorial
