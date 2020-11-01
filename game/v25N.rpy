label v25neutral:
    scene black
    with dissolve
    isabella "Why would you say that Irgodon?"
    irgodon "If the demons are after him it's very dangerous to keep him here"
    scene v25019
    show blink1
    show blink2
    show blink3

    isabella "Isn't that what we are supposed to do? Protect people from the demons?"
    hide blink3
    with dissolve
    hide blink2
    with dissolve
    hide blink1
    with dissolve
    "You see a familiar face and a big guy in front of you"
    scene v25020
    with dissolve
    irgodon "It's true, but we have to play it safe, I don't want our camp overrun by demons"
    MC "Mmm... hello?"
    scene v25021
    with dissolve
    isabella "Oh, hello [MC] I'm glad you're ok"
    MC "What am I doing here? What happened to the giant demon?"
    scene v25022
    with dissolve
    irgodon "Remember what we talked about..."
    isabella "I told you what I think, I'm not changing my mind"
    irgodon "Hmmf..."
    "You see the tall man leave the room without even looking at you"
    scene v25023
    with dissolve
    isabella "Don't mind him, he's just playing it safe"
    MC "Can I ask what's happening? Why am I here?"
    scene v25024
    with dissolve
    isabella "I had been looking for a demon, but I found you unconscious instead"
    MC "What do you mean?"
    isabella "I've been feeling some demon magic on Allesterra, that's why you found me there"
    isabella "Yesterday I felt the most powerful demon magic I've ever felt"
    isabella "But before I could find a boat to check it out, it disappeared"
    isabella "I still went to investigate and I found you unconscious on some wooden planks"
    isabella "Come, let's head outside, I want you to meet our leader."
    "You follow her outside"
    scene v25025
    with dissolve
    "You see an older man speaking with the guy from before"
    irgodon "But Rolf, it's dangerous!"
    rolf "I understand your concerns, but let me take care of this"
    scene v25026
    with dissolve
    rolf "Hello young man, Isabella told me your are a Mage?"
    MC "Yes... I am..."
    rolf "Very well, do you have any idea why a powerful demon like Adamastor"
    rolf "Would be exactly where you were found?"
    MC "I have no idea, but the demon said something about knowing me"
    rolf "Really?! You know why?"
    MC "I have no clue..."
    irgodon "Nonsense!! You must have done something!!"
    rolf "Enough Irgodon! Go check if there is news about Leefside"
    irgodon "Hmf.. Very well"
    scene v25027
    with dissolve
    rolf "Don't mind him, he's just overprotective of our Isabella here"
    isabella "But he should understand that I can take care of myself"
    rolf "That's not important now, we need to find out why the demons are after you"
    scene v25028
    with dissolve
    rolf "You say you have no idea, try to remember something that could help us"
    menu:
        "There are some people who believe that I have some hidden power":
            rolf "But why would the demons want you?"
            rolf "Are they afraid of your untaped power? Was it just a coincidence?"
        "I fought an Imp before":

            rolf "I don't see a demon like Adamastor hunting you because of that"
            rolf "An Imp is of little importance to them"
        "[abgreen]I have no idea why":

            rolf "We should investigate then"
            rolf "There are some strange things happening"

    isabella "What was that about Leefside?"
    rolf "We seem to have lost contact with the town"
    isabella "Wasn't my mother travelling there?"
    rolf "Indeed, we should have had news from her by now"
    "You can tell by her face and voice that Isabella is worried"
    isabella "I must go there then!"
    rolf "Calm down please, Irgodon is already taking care of it"
    rolf "You and your friend here should rest now"
    rolf "I'm sure tomorrow we will have news"
    isabella "But..."
    rolf "When was the last time you slept?"
    rolf "Besides, do you feel any demonic presence that has you worried?"
    isabella "You're right, I don't feel any demon activity nearby"
    rolf "Go rest then. Tomorrow, if there is no news, you can check for yourself"
    isabella "Very well, thank you"
    rolf "You must make all the time you can rest count"
    rolf "You never know when you'll have the chance again in our work"
    isabella "[MC] let's go, let me show you where you'll stay"
    MC "Sure, lead the way"
    "You follow her"
    scene v25029
    with dissolve
    isabella "This is where you'll stay for tonight"
    isabella "Feel free to read the books we have here to help you sleep"
    isabella "I need to go now, see you tomorrow"
    scene v25030
    with dissolve
    MC "Wait, let me ask you something"
    isabella "Very well, what do you want to ask?"
    scene v25029
    with dissolve
    MC "Well I..."
    $ v25iastalk = 0

label isabtalkv25:

    menu:
        "I wanted to thank you for saving me":

            isabella "Oh.. Ok, I wasn't exactly there to save you though..."
            MC "I would have probably drowned if you hadn't found me"
            isabella "Hmm, you're right, I saved you, guess you owe me one now"
            MC "That's not what I meant..."
            isabella "Ahaha too late, I'll remember"
            jump isabtalkv25
        "Where are we?":

            isabella "We are at a temporary Demon Hunter outpost"
            isabella "At the very left tip of Highgard since it's close to Allesterra"
            MC "Is that Leefside town close?"
            isabella "Yes, it's just a few hours away by horse"
            jump isabtalkv25
        "What was that about your mother?":

            $ v25iastalk = 1
            isabella "She was at Leefside looking for signs of a demonic presence"
            isabella "But we should have heard news from her by now"
            MC "But you feel no demonic presence there?"
            isabella "No... But demons are not the only danger in the world"
            isabella "And my mother... She's my only remaining family"
            isabella "I lost my father and brother when I was younger"
            isabella "I can't lose her too"
            MC "I'm sure she is fine, I lost my family too when I was younger"
            MC "But I can't remember them, I lost my memory..."
            isabella "That's terrible, I feel for you..."
            jump isabtalkv25

        "That's all, Good night" if v25iastalk == 1:
            scene v25030
            with dissolve
            isabella "Very well, see you tommorow, good night"
            scene v25031
            with dissolve
            "She leaves"
            MC "I'm all alone here, what should I do?"
            menu:
                "Try to sleep":
                    scene black
                    with dissolve
                    "You lie on the bed, close your eyes and fall asleep"
                    jump v25neutral01
                "[abgreen]Read a book":

                    scene v25031
                    with dissolve
                    MC "There are books about everything, what should I read?"
                    menu:
                        "Read about Battlemagic[abgreen] [abdestpoint] {image=001battle}":
                            "You grab a book about Battlemagic and lie on the bed"
                            $ Destpoints += 1
                            "Your Battlemagic skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25neutral01
                        "Read about Summoning[abgreen] [absummpoint] {image=001summon}":

                            "You grab a book about Summoning and lie on the bed"
                            $ Summpoints += 1
                            "Your Summoning skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25neutral01
                        "Read about Alteration[abgreen] [abaltepoint] {image=001alteration}":

                            "You grab a book about Alteration and lie on the bed"
                            $ Altepoints += 1
                            "Your Alteration skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25neutral01
                        "Read about Illusion[abgreen] [abiluspoint] {image=001illusion}":

                            "You grab a book about Illusion and lie on the bed"
                            $ Iluspoints += 1
                            "Your Illusion skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25neutral01
                        "Read about Mysticism[abgreen] [abmystpoint] {image=001myst}":

                            "You grab a book about Mysticism and lie on the bed"
                            $ Mystpoints += 1
                            "Your Mysticism skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25neutral01
                        "Read about Healing[abgreen] [abhealpoint] {image=001heal}":

                            "You grab a book about Healing and lie on the bed"
                            $ Healpoints += 1
                            "Your Healing skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve

                            jump v25neutral01
                        "Read about Necromancy[abgreen] [abnecropoint] {image=001necro}":

                            "You grab a book about Necromancy and lie on the bed"
                            $ Necropoints += 1
                            "Your Necromancy skill improved"
                            "After a while you start to feel your eyes trying to close"
                            "You can't read anything else and fall asleep"
                            scene black
                            with dissolve
                            jump v25neutral01

label v25neutral01:
    scene black
    MC "{i}Yawn!!{/i}"
    scene v25031
    with dissolve
    MC "I slept surprisingly well, I should go outside and look for Isabella"
    scene v25058
    with dissolve
    "Once you're outside you see Isabella and Rolf talking about something"
    isabella "Nothing yet??! What about Irgodon?"
    MC "Good morning, is everything alright?"
    scene v25059
    with dissolve
    isabella "No! No news from my mother or Leefside..."
    rolf "And now Irgodon... He should have sent some word by now"
    scene v25058
    with dissolve
    isabella "That's it, I'm going there!"
    rolf "I can't let you go alone, I will call someone to help you"
    isabella "That will take at least another day, I can't wait that long"
    scene v25059
    with dissolve
    isabella "[MC], will you come with me?"
    rolf "But... He is not a Demon Hunter"
    scene v25058
    with dissolve
    isabella "You said it yourself, do you feel any demonic presence?"
    rolf "No... I don't..."
    scene v25059
    with dissolve
    isabella "So... It doesn't matter, also [MC] is a capable Mage"
    isabella "So will you do it, [MC]?"
    MC "Yeah sure, it's the least I can do"
    scene v25058
    with dissolve
    isabella "See? We are going at once"
    rolf "Very well, good luck to you and be careful"
    isabella "We will, bye Rolf see you soon"
    scene v25059
    with dissolve
    isabella "Let's go, follow me [MC]"
    scene v25060
    with dissolve
    "You follow Isabella"
    isabella "I'll get my horse so we can get there in a few hours"
    scene v25062
    with dissolve
    isabella "Hey Noisy, how are you?"
    "She seems very fond of that horse"
    scene v25063
    with dissolve
    isabella "Are you coming or what [MC]? Climb up, Noisy can take us both"

    scene v25064
    with dissolve
    $ mountable = 0
    menu:
        "Sure I'll ride with you":
            isabella "Hurry up then!"
            scene v25070a
            with dissolve
            "You climb to the horse's back, you can feel Isabella's body pressed against yours"
            isabella "Are you ready? Hold on to me, Noisy is fast"
            "You ride for a couple of hours"
            scene v25071
            with dissolve
            "Until you reach a wooded area"
            "And Isabella stops"
            scene v25070
            with dissolve
            isabella "We need to go by foot now... I feel a demon nearby"
            MC "Very well..."
            jump demonnerbyv25
        "[abgreen]I can summon my own mount":

            isabella "Really? that's awesome, show me"
            if Summpoints >= 5:
                $ mountable = 1
                scene v25064a
                with dissolve
                "You pour energy into your summoning"
                scene v25065
                with dissolve
                isabella "Wow!! That's amazing!!"
                MC "I told you I could do it"
                isabella "Right... The things you do just not to ride close to me..."
                "Did she just say that?"
                isabella "Can we go now? We need to be fast"
                MC "Sure..."
                scene v25067
                with dissolve
                "You get on your summoned creature back and follow Isabella"
                scene v25068
                with dissolve
                "You keet travelling for a couple of hours until you reach a wooded area"
                isabella "Wait...."
                scene v25069
                with dissolve
                "She dismounted"
                isabella "We need to go by foot now... I feel a demon nearby"
                MC "Very well..."
                jump demonnerbyv25
            else:
                scene v25064b
                with dissolve
                "You try to summon something... But you fail..."
                scene v25064
                with dissolve
                MC "Shit..."
                scene v25066
                with dissolve
                isabella "Hehe did you fail your summon on purpose just to ride close to me?"
                MC "I... No... I mean.. Yes..."
                isabella "Heheh, come on, we need to go"
                scene v25070a
                with dissolve
                "You climb to the horse's back, you can feel Isabella's body pressed agaisnt yours"
                isabella "Are you ready? Hold on to me, Noisy is fast"
                "You ride for a couple of hours"
                scene v25071
                with dissolve
                "Until you reach a wooded area"
                "And Isabella stops"
                scene v25070
                with dissolve
                isabella "We need to go by foot now... I feel a demon nearby"
                MC "Very well..."
                jump demonnerbyv25

label demonnerbyv25:
    scene v25072
    with dissolve
    isabella "We need to be very quiet now"
    scene v25073
    with dissolve
    isabella "Leefside is very close, I can feel a demonic presence, but it's a lesser demon"
    isabella "No way it could have harmed my mother or Irgodon..."
    "You move a bit further"
    scene v25074
    with dissolve
    isabella "There's the town wall, does it..."
    MC "Smell like smoke? Quite a bit in fact"
    isabella "Let's go!"
    "You reach the entrance to the town and you can't believe what you see"
    scene v25075
    with dissolve
    isabella "Look at this... It's terrible... Who would do this?"
    MC "Demons?"
    isabella "It had to be a very powerful demon or many, but I felt nothing this bad"
    isabella "I can feel the lesser demon inside, let's check it out"
    scene v25076
    with dissolve
    MC "Wait.... Oh what the hell... Let's go"
    "There is so much smoke, it's hard to breath and you can barely see Isabella"
    scene v25077
    with dissolve
    isabella "There he is!!"
    "You see a dark winged creature in the smoke"
    MC "Oh shit..."
    "The creature notices you"
    scene v25078
    with dissolve
    demon "Hmmm there are still survivors after all, time to finish what I started"
    "You falter as how to deal with it, but Isabella doesn't seem impressed by it"
    scene v25079
    with dissolve
    demon "Such a pretty one we have here... Let's make a deal girl"
    demon "You satisfy my special needs and I let you and your friend live"
    isabella "I don't make deals with demons... Tell me what happened here?"
    demon "What? You want to die? I will kill you, just like I did with everyone here"
    isabella "Really? You did this? Where are the bodies then?"
    demon "I... I... Ate them! Yeah, very tasty peasants..."
    isabella "You're not that kind of demon, come on answer my question"
    "You don't know what to think... And you notice confusion on the demon's face"
    scene v25078
    with dissolve
    demon "What?!! How dare you!!?? I'll kill you now!!"
    "Before the demon could spit another word"
    scene v25080
    with dissolve
    "You see Isabella taking two blades out of nowhere and her cape falling to the ground"
    scene v25081
    with dissolve
    "The demon barely dodges the blade in the face"
    "But Isabella rotates and kicks him in the stomach"
    demon "Ahhhh!! You bitch!!!"
    scene v25082
    with dissolve
    demon "How dare you!! No deal for you!! You die now!!"
    "You feel the demon begin casting something"
    MC "Look out!!"
    scene v25083
    with dissolve
    "The demon cast some kind of red beam in Isabellas direction"
    "But it seems to have no effect..."
    MC "What the...."
    scene v25084
    with dissolve
    "You see a shocked look on the demons face"
    demon "What?! How?! Who are you?"
    isabella "I'm a demon hunter, immune to your tricks, now answer my question"
    scene v25082
    with dissolve
    demon "A demon hunter??!! Please forgive me... Please..."
    demon "I had nothing to do with what happened here, I swear!!"
    isabella "I know... That's why I'm asking..."
    demon "Humans... Humans did this, an army of them"
    isabella "Describe them to me, in detail..."
    demon "I only saw them from a distance, they had red flags and red square shields..."
    demon "They didn't kill anyone, just took everyone as prisoners"
    demon "That's all I know... Please... Don't kill me..."
    scene v25084
    with dissolve
    isabella "Red flags and shields...Slayers. At least they didn't come to kill"
    scene v25085
    with dissolve
    isabella "What do you think [MC]?"
    "You see the demon getting away"
    MC "He's getting away!!"
    $ demonescape = 0
    menu:
        "Let him go[abred] [abnoalignment]":
            $ Points -= 1
            "Gain alignment towards evil"
            scene v25087
            with dissolve
            isabella "Bastard... He got away..."
            scene v25092
            with dissolve
            isabella "He got away... Who knows what he's going to do now..."
            MC "I bet he is too scared of you to try something soon"
            scene v25093
            with dissolve
            isabella "Heheh, maybe... Let's move on then"

            jump afterdemonv25
        "Use Telekinesis to stop him {image=001myst}":

            if Mystpoints >= 3:
                $ demonescape = 1
                scene v25086
                with dissolve
                MC "Stop!! Now!!"
                "You are able to stop him mid air, in a split second Isabella jumps on him"
                scene v25088
                with dissolve
                isabella "Who said you could leave demon?"
                demon "Please let me go... Please..."
                "You feel comfortable to get closer"
                scene v25089
                with dissolve
                isabella "Tell me demon why should I let you go? Convince me you're a good boy"
                isabella "Convince me from now on, the demon is going to be a {i}very{/i} good boy"
                "You can't hold it and just laugh at that"
                scene v25090
                with dissolve
                MC "Pfff ahahahah"
                demon "I'm really sorry... You are both very powerful demon hunters"
                MC "Actually I'm not..."
                scene v25091
                with hpunch
                demon "A demon hunter?!"
                isabella "Look out!!"
                scene black
                with dissolve
                isabella "Are you okay?"
                scene v25094
                with dissolve
                isabella "[MC]?? Are you ok?"
                MC "I guess..."
                scene v25095
                with dissolve
                isabella "Great, are you able to walk?"
                MC "I'm good, let's find out where the soldiers went from here"
                jump afterdemonv25
            else:


                "You failed to cast the spell"
                scene v25087
                with dissolve
                isabella "Bastard... He got away..."
                scene v25092
                with dissolve
                isabella "He got away... Who knows what he's going to do now..."
                MC "I bet he is too scared of you to try something soon"
                scene v25093
                with dissolve
                isabella "Heheh, maybe... Let's move on then"

                jump afterdemonv25


label afterdemonv25:
    scene black
    with dissolve
    "You and Isabella follow the trail left by the soldiers"
    "Several hours later, you reach an Inn"
    scene v25096
    with dissolve
    isabella "Well let's ask around here and maybe have a couple of drinks"
    MC "Seems fine to me"
    "You order drinks for both of you and talk a bit with the Tavern Keeper"
    scene v25097
    with dissolve
    keeper "Yes, some soldiers passed here about half day ago"
    keeper "I believe they were using the docks to travel somewhere"
    isabella "It's almost night, do you have rooms for us?"
    keeper "Only one, but it has two beds, I can join them if you want"
    isabella "No, don't worry, it's fine like that"
    scene v25098
    with dissolve
    "You spend some time drinking with Isabella"
    "She seems to have become a bit more calm"
    "She tells you that her mother would never let herself get caught by the Slayers"
    "But that she was probably following them"
    scene v25099
    with dissolve
    "Some hours passed"
    isabella "I think I'm a bit drunk, let's go to the room..."
    scene v25100
    with dissolve
    "You look at the tavern keeper and he hands you a key"
    keeper "That's the key for the room, behave you two"
    isabella "Eheheh, sure sure we will"
    scene v25101
    with dissolve
    "You reached the room, it was clean and looked pretty good"
    MC "Not bad... I've seen a lot worse"
    scene v25102
    with dissolve
    isabella "Yeah me too, I'm tired now... How about a goodnight kiss?"
    MC "I..."
    scene v25103
    with dissolve
    isabella "Come on... don't be shy, you look cute {i}giggle{/i}"
    "She is definitely drunk should you kiss her?"
    $ isakiss = 0
    menu:
        "[abgreen]Yes kiss her":
            $ isakiss = 1
            scene v25104
            with dissolve
            "She kisses you"
        "No, she is drunk":

            MC "You are drunk, we shouldn't do this"
            isabella "Oh... ok.."

    scene v25105
    with dissolve
    isabella "I'm feeling so hot right now..."
    "She removed her cape, you could see her trained body in detail"
    "Then she removed her boots and armor, such a sight..."
    scene v25106
    with dissolve
    isabella "Ah... I feel much better now... Let's see if the bed if comfortable"
    scene v25107
    with dissolve
    isabella "How about that... It's really good, check if yours is good too"
    "You lie on the other bed"
    scene v25108
    with dissolve
    isabella "So? How is it?"
    MC "It's pretty good..."
    isabella "Great... time to sleep then..."

    scene v25109
    with dissolve
    "She blows out the candles and the room becomes dark"
    MC "Isabella?... Isabella?.. She's sleeping already? That was fast..."
    MC "Guess I need to do the same..."
    scene black
    with dissolve
    "You wake up hearing some strange noises outside your room"
    "You decide to take a look outside"
    scene v25213
    with dissolve
    "You see a black hooded figure"
    scene v25214
    with dissolve
    Nonen "You! I feel magic in you"
    MC "Who the hell are you?"
    scene v25214
    with dissolve
    Nonen "You'll be very useful to me, ahahaah"
    $ enemy = "n1"
    $ enemychoice = 0
    jump combat_tutorial
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
