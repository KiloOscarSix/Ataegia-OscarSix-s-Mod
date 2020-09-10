label v25evil:
    scene black
    with dissolve
    Bredita "So, you know what to do"
    scene v25001
    show blink1
    show blink2
    show blink3

    Bredita "Look who's waking up"
    hide blink3
    with dissolve
    hide blink2
    with dissolve
    hide blink1
    with dissolve
    "You see a familiar face and a weird guy in front of you"
    MC "I...Where am I? Who are you?"
    scene v25002
    with dissolve
    Bredita "Well, I'm Bredita and you are in my home... Lair..Hmm.. Castle?"
    Bredita "Whatever, call it what you want, but it's my place"

    MC "Ok... And why am I here?"
    Bredita "You remember being attacked by a giant demon and being saved by me?"
    Bredita "You fainted and I brought you here"
    MC "Now I remember...Bredita... I read about you in some history book"
    Bredita "It's possible... There should be plenty of things about me"
    Bredita "Not that it matters now..."
    menu:
        "{color=#1BBB20}What about the Archmage? She was there also":
            Bredita "Yes she was, but I felt that you would be a lot better here with me"
            Bredita "So I brought you with me"
            MC "Is she ok?"
            Bredita "Yes she is, don't worry about her now"
            MC "Are you a Master in Magic as well?"
            Bredita "Seriously? Ahaha I'm the most powerful Mage you'll ever meet"
        "Ok thank you for saving me, but what now?":

            Bredita "Now? Hmm... I was thinking that I could show you around"
            Bredita "Maybe teach you a thing or two."
            Bredita "You don't have to make a decision now"
            MC "Are you a Master in magic?"
            Bredita "Seriously? Ahaha I'm the most powerful Mage you'll ever meet"

    Bredita "You can leave us alone now"
    scene v25003
    with dissolve
    "You see the weird guy leave"
    MC "I had a dream about you and the Archmage"
    scene v25004
    with dissolve
    "An expression of curiosity came over Bredita's face"
    Bredita "Really? Me and Ayna? What kind of dream?"
    MC "Well... You were kissing... And..."
    scene v25005
    with dissolve
    Bredita "Hmmm let me check..."
    "You feel her power around you and... Inside you?"
    scene v25006
    with dissolve
    Bredita "How about that... How could you dream of something like that?"
    MC "You saw my dream? How?"
    Bredita "What did I tell you about my power?"
    Bredita "Alright let's go... Follow me"
    scene v25007
    with dissolve
    "You follow the woman through some kind of catacombs"
    scene v25008
    with dissolve
    "You reach a big room with a throne and two skeletons kneeling"
    MC "What the hell is happening here?"
    Bredita "Don't worry they won't bite...Much..."
    "You keep following her"
    scene v25016
    with dissolve
    Bredita "This will be your room while you stay here with me"
    MC "Thank you... I guess..."
    Bredita "I'll leave you then, you need to rest"
    MC "Wait...I... Can you tell me more about you?"
    scene v25017
    with dissolve
    Bredita "Hmmm... What do you want to know?"
    $ collegev25 = 0
    jump questionbreditav25

label questionbreditav25:
    menu:
        "Who are you?":
            Bredita "My name is Bredita Darkheart and I'm a Mage"
            MC "I've heard your name before, you were..."
            Bredita "Attacking and killing everyone in the College?"
            MC "Yes..."
            Bredita "Don't believe everything that you read, still some parts are true"
            jump questionbreditav25
        "Why did I dream about you and the Archmage?":

            Bredita "Now that's a good question, you must have some kind of hidden power"
            Bredita "I bet it's not the first time you dreamt of something like that"
            MC "Indeed... I've had my share of strange dreams..."
            Bredita "I bet that the more you raise your power, the more the dreams will make sense"
            MC "I'm not sure that's good news..."
            jump questionbreditav25
        "What do you want with me?":

            Bredita "To show you that I'm the best way for you to achieve your potential"
            MC "I've heard that before, others told me all about my potential"
            MC "Why do you think you'd know so much better?"
            Bredita "Believe me, I know what I'm talking about, I could be wrong..."
            Bredita "But for me, Ayna and the Elite to be wrong... Well... "
            MC "What is my potential? Can I become one of the Elite?"
            Bredita "That's not an answer I can give you, only you can decide that"
            jump questionbreditav25
        "What really happened with you and the College?":

            $ collegev25 = 1
            Bredita "That's a long story and you need to rest"
            MC "Please at least tell me what power you and the Archmage felt that day"
            Bredita "Hmmmm.... Very well... So..."
            scene v25166
            with dissolve
            Bredita "We went to see Suntako, he was the Archmage at the time"
            yBredita "Did you feeel that Archmage?"
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
            scene v25017
            with dissolve
            Bredita "Ayna always had a special power to deal with people"
            Bredita "And with me, she was one of the few that understood me"
            scene v25171
            with dissolve
            yayna "I need to do this, I'll be back in no time"
            suntako "This will be discussed by the Elite"
            suntako "Such insubordination shall not be forgotten"
            yayna "Let me go alone please"
            yBredita "Hmmf...."
            scene v25172
            with dissolve
            Bredita "Then I left them there talking"
            scene v25173
            with dissolve
            Bredita "I knew what Suntako was planning, like always"
            Bredita "He was scared of Ayna, he knew that she would take his place someday"
            scene v25017
            with dissolve
            Bredita "It eventually happened, that's why she is the Archmage today"
            MC "That's.... But what happened next?"
            Bredita "A curious one aren't you?"
            Bredita "Well, I was not going to let Ayna go alone, I felt the danger..."
            scene v25047
            with dissolve
            Bredita "She was not even surprised, she knew I would go with her"
            Bredita "We reached a cave that seemed the source of the power"
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
            Bredita "We fought that enemy for hours"
            Bredita "His powers appeared to be infinite"
            scene v25053
            with dissolve
            Bredita "We used all our power, but he wouldn't even flinch"
            scene v25017
            with dissolve
            Bredita "We had never faced such an opponent, it was a Lich after all..."
            MC "What is a Lich?"
            Bredita "What does the College teach nowadays? A Lich is a powerful Mage"
            Bredita "Well... A dead Mage, one that traded his life for more power"
            MC "Wow... What happened next?"
            Bredita "I'll tell you... Some other time."
            MC "What? why?"
            Bredita "I can't reveal all my secrets on our first date, hahah"
            jump questionbreditav25


        "That's all I wanted to know" if collegev25 == 1:

            Bredita "Very well, see you tomorrow then?"
            Bredita "You need to rest and I have other things to attend"
            Bredita "See you tomorrow morning, meet me downstairs"
            Bredita "Oh... Feel free to read a book to help you sleep, Bye"
            MC "Bye..."
            scene v25018
            with dissolve
            "She left you on the room alone"
            menu:
                "Try to sleep":
                    scene black
                    with dissolve
                    "You lied on the bed closed your eyes and fell asleep"
                    jump v25bredmorning
                "{color=#1BBB20}Read a book":

                    scene v25018
                    with dissolve
                    MC "There are books about everything, what should I read?"
                    menu:
                        "Read about Battlemagic{color=#1BBB20} (+1 Destpoint) {image=001battle}":
                            "You grab a book about Battlemagic and lie on the bed"
                            $ Destpoints += 1
                            "Your Battlemagic skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning
                        "Read about Summoning{color=#1BBB20} (+1 Summpoint) {image=001summon}":

                            "You grab a book about Summoning and lie on the bed"
                            $ Summpoints += 1
                            "Your Summoning skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning
                        "Read about Alteration{color=#1BBB20} (+1 Altepoint) {image=001alteration}":

                            "You grab a book about Alteration and lie on the bed"
                            $ Altepoints += 1
                            "Your Alteration skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning
                        "Read about Ilusion{color=#1BBB20} (+1 Iluspoint) {image=001illusion}":

                            "You grab a book about Ilusion and lie on the bed"
                            $ Iluspoints += 1
                            "Your Ilusion skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning
                        "Read about Mysticism{color=#1BBB20} (+1 Mystpoint) {image=001myst}":

                            "You grab a book about Mysticism and lie on the bed"
                            $ Mystpoints += 1
                            "Your Mysticism skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning
                        "Read about Healing{color=#1BBB20} (+1 Healpoint) {image=001heal}":

                            "You grab a book about Healing and lie on the bed"
                            $ Healpoints += 1
                            "Your Healing skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning
                        "Read about Necromancy{color=#1BBB20} (+1 Necropoint) {image=001necro}":

                            "You grab a book about Necromancy and lie on the bed"
                            $ Necropoints += 1
                            "Your Necromancy skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25bredmorning

label v25bredmorning:
    scene black
    with dissolve
    MC "{i}Yawn{/i}!!"
    scene v25018
    with dissolve
    MC "Considering all that's happened, I slept quite well"
    MC "I should meet Bredita downstairs"
    "You dress, leave the room and go look for Bredita"
    scene v25054
    with dissolve
    Bredita "Hey! Look who's awake, so did you rest well?"
    MC "Yes... I had such a great night, so yes"
    scene v25055
    with dissolve
    Bredita "Great! Then you can come with me, you are right on time"
    MC "And where are we going?"
    "You get a bit closer to her"
    scene v25056
    with dissolve
    Bredita "[MC] will come with me, you can stay here"
    "You never heard that weird guy talk..."
    "Before you could say anything"
    scene v25057
    with dissolve
    "Bredita begins casting a spell, her power is overwhelming"
    scene v25110
    with dissolve
    "In the next moment you and Bredita are somewhere else"
    MC "Where are we? How did you...."
    Bredita "Shhh.... Follow me"
    scene v25111
    with dissolve
    "A bit confused you decide to do as she says, and then you hear"
    woman "Help me!!!"
    scene v25112
    with dissolve
    woman "Ahhhhh, please!!"
    "You see a woman running in you direction in panic"
    "She notices you and fall on her knees"
    scene v25113
    with dissolve
    woman "Please, let me go! Please!"
    MC "I...."
    Bredita "Calm down, we're not here to hurt you"
    scene v25114
    with dissolve
    "Her face changed"
    woman "You're not? Who are you?"
    sol "There she is!!"
    scene v25115
    with dissolve
    "You see some soldiers laughing"
    sol "Look! We have a bonus, another pretty chick"
    "They seem to ignore you completely"
    woman "Oh no.... Please help me!!"
    scene v25116
    with dissolve
    Bredita "Why are you harassing the girl, boys?"
    sol "Look at this one, ahahahha"
    sol "Now that you're here, we're gonna have even more fun"
    Bredita "Oh, is that so? Are we playing catch or something?"
    sol "Ahahaha, can you believe this one? Ahahaah"
    "They have no clue how much of a mess they're in..."
    Bredita "So what's all the fun about? I want to have fun too, you know!"
    sol "Oh you will!! Who do you want to fuck you first? Maybe all of us?"
    Bredita "Hmm, I think I'll take you all at the same time"
    sol "Ahahaha, wait what?"
    Bredita "Let me start then"
    scene v25117
    with dissolve
    sol "What?! Oh fuck... What is happening, put me down!!"
    sol "She's a Mage... Oh shit!!"
    Bredita "Bye...."
    scene v25118
    with dissolve
    "She launches the soldiers up into the sky"
    Bredita "Now we can have a decent conversation"
    woman "Oh my... You saved me..."
    Bredita "That's a way of seeing things yes..."
    scene v25119
    with dissolve
    Bredita "This one here is [MC]"
    woman "Hello [MC]"
    woman "Thank you, they attacked our village and took everyone as prisoners"
    woman "I was hidden during the attack, but then these guys appeared..."
    scene v25120
    with dissolve
    Bredita "That means you are the only one left?"
    woman "I...Believe so..."
    Bredita "Hey [MC] do you want to keep this one or should I keep her?"
    MC "What?"
    scene v25121
    with dissolve
    Bredita "Nevermind, I like her, I'll keep her, you get to choose the next one"
    "You feel Bredita casting something"
    scene v25122
    with dissolve
    Bredita "Let's go pretty thing"
    scene v25123
    with dissolve
    MC "They are gone... What just happened?"
    "You start to hear some familiar voices"
    MC "I know these voices, I need to check this out"
    scene v25124
    with dissolve
    "You notice Mida and Liliana walking on the beach close to you"
    scene v25125
    with dissolve
    amida "Is that??!! [MC]!!! You were right! He is here!!"
    scene v25126
    with dissolve
    amida "[MC]!! My love!!"
    MC "What are you doing here?!"
    scene v25127
    with dissolve
    amida "Liliana came to see me. She said that she knew where you were"
    amida "So we went into the College's portal room and here we are"
    MC "But how did you knew where I was Liliana?"
    scene v25128
    with dissolve
    lili "Let's just say we have a common friend"
    scene v25129
    with dissolve
    lili "And when I saw Mida here worried sick about you"
    lili "I knew she wouldn't hesitate to come with me"
    amida "I... I..."
    scene v25130
    with dissolve
    "She kissed you"
    Bredita "I leave for a few minutes and you're already kissing girls?"
    scene v25131
    with dissolve
    Bredita "Didn't I meant anything to you? You have another one already?!!"
    MC "I..."
    scene v25132
    with dissolve
    Bredita "Ahahaha, what cutie we have here, is she your girlfriend?"
    "You start to feel her power"
    scene v25133
    with dissolve
    Bredita "Now she can't hear you. I like her, I want to keep her"
    Bredita "But, I said you could choose the next one, so let's go home"
    scene v25134
    with dissolve
    scene v25135
    with dissolve
    "What is going to happen now?"
    scene v25137
    with dissolve
    Bredita "Here we are!! Back home, back in your room"
    Bredita "We have a fine girl here, look at her"
    "Mida seems paralyzed with an empty look on her face"
    scene v25138
    with dissolve
    Bredita "Look at this body, and her ass... Let's wake her up"
    scene v25139
    with dissolve
    Bredita "There we go!"
    amida "I... where are we? What is happening?"
    scene v25140
    with dissolve
    Bredita "Now [MC] do you want to keep her? Or do I keep her?"
    MC "What do you mean?"
    scene v25141
    with dissolve
    Bredita "Oh...Look at her... I would really enjoy keeping her.."
    Bredita "What I mean is that, if you keep her you do whatever you want with her"
    Bredita "If I keep her, I do whatever I want with her"
    "Should you keep Mida? You can try to keep her safe this way"
    "Who knows what Bredita will do to her if you let her go"
    "But letting Bredita keep Mida may improve her feelings toward you"
    "Or Bredita may respect you, for having a backbone by keeping Mida?"
    Bredita "What do you want to do [MC]?"
    $ midaowner = 0

    menu:
        "I'll keep her {color=#f00} (lead to vanilla and/or group-MFF) {/color}":
            $ midaowner = 1
            $ midalove += 1
            $ Points += 1
            "Mida's love increased, gained +1 Alignment"
            scene v25143
            with dissolve
            Bredita "Very well I will leave you two alone for a moment"
            Bredita "Meet me downstairs in five minutes [MC]"
            scene v25144
            with dissolve
            amida "Thank you I guess, what is happening?"
            MC "Don't worry everything will be fine"
            scene v25145
            with dissolve
            amida "Ok... Who is that woman?"
            menu:
                "She's my new master of magic":
                    amida "New master? Like a teacher?"
                    MC "Kind of, yes, she is very powerful, maybe the most powerful I've seen"
                    amida "What about the Archmage? She is stronger for sure"
                    MC "I wouldn't be so sure, still she's not teaching me, this one is"
                    amida "I guess you're right..."
                    scene v25146
                    with dissolve
                    amida "I'm glad we're here together, at least"
                    scene v25147
                    with dissolve
                    amida "You know what would be nice?"
                    scene v25148
                    with dissolve
                    "She kissed you"
                    scene v25147
                    with dissolve
                    amida "Having some fun... What do you say?"
                    MC "I... Would love to have some fun now, but you heard her..."
                    scene v25149
                    with dissolve
                    amida "Yeah... Five minutes... Go on then, I guess I'll wait here"
                    amida "I'll read a book or something"
                    jump v252ndmorn
                "{color=#1BBB20}She is helping me improve my power":

                    amida "Helping you improve? Like a teacher?"
                    MC "Kind of, she is very powerful, maybe the most I've seen"
                    amida "What about the Archmage? She is stronger for sure"
                    MC "I wouldn't be so sure, still she's not teaching me, this one is"
                    amida "I guess you're right..."
                    scene v25146
                    with dissolve
                    amida "I'm glad we're here together at least"
                    scene v25147
                    with dissolve
                    amida "You know what would be nice?"
                    scene v25148
                    with dissolve
                    "She kissed you"
                    scene v25147
                    with dissolve
                    amida "Having some fun...What do you say?"
                    MC "I... Would love to have some fun now, but you heard her..."
                    scene v25149
                    with dissolve
                    amida "Yeah... Five minutes... Go on then, I guess I'll wait here"
                    amida "I'll read a book or something"
                    jump v252ndmorn
        "You can keep her {color=#f00} (lead to Fem-dom and/or NTR and/or group-ALL) {/color}":

            $ midaowner = 2
            $ midacorr += 1
            $ Points -= 1
            "Mida's corruption increased, Alignment -1"
            scene v25142
            with dissolve
            amida "What?...I..."
            Bredita "Oh really.... That's very good news..."
            scene v25140
            with dissolve
            Bredita "I have some plans for a cutie like you my dear..."
            scene v25143
            with dissolve
            Bredita "Follow me girl, [MC] meet me downstairs in five minutes"
            MC "Very well"
            scene v25145
            with dissolve
            amida "..."
            scene v25018
            with dissolve
            "They left you alone"
            MC "I let Bredita keep Mida to herself, I hope it was a good choice"
            MC "I think five minutes have passed, let's go downstairs"
            jump v252ndmorn

label v252ndmorn:
    scene v25009
    with dissolve
    "You're downstairs and see Bredita sitting at her throne"
    "You get closer"
    scene v25010
    with dissolve
    MC "You said you wanted to see me in five minutes"
    Bredita "Yes, I want to start your training"
    scene v25011
    with dissolve
    Bredita "Are you ready? I won't go easy on you"
    MC "Training? Great, I can't wait to get stronger"
    scene v25012
    with dissolve
    Bredita "Oh... I like your confidence and motivation"
    MC "Yeah! Can't wait!"
    scene v25013
    with dissolve
    Bredita "You surely don't know what you're about to suffer ahaha"
    "Is she kidding? Is she being serious? Anyway you're here so..."
    Bredita "Ready? Or do you want to know something before we start?"
label trainingbred01:
    scene v25013
    with dissolve
    menu:
        "What are you going to teach me?":
            Bredita "What will I teach you... Everything?"
            Bredita "Do you want to summon a Dragon? Cast a Meteor rain?"
            Bredita "Teleport? Control weaker minds? Raise the dead?"
            scene v25014
            with dissolve
            Bredita "Have the power to crush your enemies?"
            jump trainingbred01

        "{color=#1BBB20}Where is Mida" if midaowner == 2:
            scene v25012
            with dissolve
            Bredita "Well, she's mine now, so that's my business"
            scene v25013
            with dissolve
            Bredita "Don't tell me you are having second thoughs..."

            menu:
                "No, you can keep her {color=#f00} (lead to Fem-dom and/or NTR and/or group-ALL) {/color}":
                    MC "I have no problem with that, she is yours you can do what you please"
                    scene v25012
                    with dissolve
                    Bredita "Oh... really? The great [MC] allows me to keep my new toy?"
                    Bredita "Thank you your lordship"
                    scene v25014
                    with dissolve
                    Bredita "Remember where you are and who I am! Just because I like you"
                    Bredita "It doesn't mean you can do whatever you want..."
                    MC "I'm sorry, it won't happen again..."
                    scene v25013
                    with dissolve
                    Bredita "Good, any more questions?"
                    $ midaowner = 4
                    jump trainingbred01
                "Yes, I changed my mind {color=#f00} (lead to vanilla and/or group-MFF) {/color}":

                    MC "I realised I made a mistake..."
                    scene v25012
                    with dissolve
                    Bredita "Oh... really? So you want her back? Is that so?"
                    MC "Yes... I apologize, but I like her"
                    scene v25014
                    with dissolve
                    Bredita "Remember where you are and who I am! Just because I like you"
                    Bredita "It doesn't mean you can do whatever you want..."
                    MC "I'm really sorry..."
                    Bredita "I will send her to your room, and you keep her"
                    Bredita "This was the first and the last time I allowed you a request"
                    MC "Thank you very much"
                    scene v25013
                    with dissolve
                    Bredita "Good, any more questions?"
                    $ midaowner = 3
                    jump trainingbred01

        "Is Mida staying in my room with me?" if midaowner == 1:
            scene v25012
            with dissolve
            Bredita "Well, she's yours and the room is yours, so you do what you please"
            scene v25013
            with dissolve
            Bredita "Don't tell me you are having second thoughs... You don't want her after all?"

            menu:
                "Yes, you can keep her {color=#f00} (lead to Fem-dom and/or NTR and/or group-ALL) {/color}":
                    MC "She is yours you can do what you please"
                    scene v25012
                    with dissolve
                    Bredita "Oh... really? I guess the girl will be a bit sad?"
                    Bredita "But I'll find a way to keep her entertained"
                    scene v25013
                    with dissolve
                    Bredita "I will get her later on then, she's mine now"
                    Bredita "Any more questions?"
                    $ midaowner = 6
                    jump trainingbred01
                "No, I'll keep her {color=#f00} (lead to vanilla and/or group-MFF) {/color}":


                    scene v25012
                    with dissolve
                    Bredita "Oh... really? You don't seem so sure"
                    MC "I am, She will stay with me in my room"
                    scene v25013
                    with dissolve
                    Bredita "Ok then, remember, the room and the girl are yours"
                    Bredita "But everything else is mine, don't you ever forget that"
                    MC "I won't, thank you"
                    Bredita "Good, any more questions?"
                    $ midaowner = 5
                    jump trainingbred01
        "Can we start the training now?":

            scene v25013
            with dissolve
            Bredita "Now that's what I like to hear"
            scene v25014
            with dissolve
            "Her face changes"
            Bredita "Get ready weakling, you are about to experience real pain"
            scene v25015
            with dissolve
            MC "What I..."
            scene black
            with dissolve
            Bredita "Come on, open your eyes... It's not that hard"
            scene v25232
            with dissolve
            "As you open your eyes you see Bredita and a skeleton in front of you"
            Bredita "First thing, you are facing this skeleton so I can see your power"
            "A skeleton? Really? You have faced worse things before"
            scene v25233
            with dissolve
            Bredita "Never underestimate your opponents, never..."
            MC "This is just a skeleton..."
            scene v25234
            with dissolve
            MC "Ahhhh... Shit"
            scene v25233
            with dissolve
            Bredita "A Mage skeleton..."
            "Now she tells you..."
            $ enemy = "e1"
            $ enemychoice = 0
            jump combat_tutorial
