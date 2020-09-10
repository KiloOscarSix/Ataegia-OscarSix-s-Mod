init:

    $ sexwithmidav26 = 0

label v031good:
    scene black
    with dissolve
    ayna "[MC], I need to speak with you, come meet me at once"
    MC "Hmm? Archmage?"
    if sexwithmidav26 == 1:
        scene v3g093
        with dissolve
        "You wake up and Mida is still lying next to you"
        MC "I need to get up..."
        MC "Should I wake her to tell her I'm leaving? Or just leave her sleeping?"
        menu:
            "{color=#1BBB20}Wake her up":
                MC "Hey Mida... Mida?"
                amida "Hmmm mnmnmm"
                MC "It's morning already, sorry but I need to go"
                amida "Hmm wha..."
                scene v3g092
                with dissolve
                amida "{i}Yawn{/i}... Oh.. Hello love"
                MC "The Archmage is calling me, I need to go"
                amida "Oh.. Of course... I'll leave too then"
                "You both dress and leave the room going separate ways"
            "Let her sleep":

                MC "She looks so peaceful"
                MC "I'll just leave her sleeping"
                MC "I must dress and meet the Archmage now"
                "You dress and leave the room"
    else:

        scene v3g082
        with dissolve
        MC "{i}Yawn{/i}... I'm being summoned again... Let's see what's happening"
        "You dress yourself and leave the room"

    scene v32g001
    with dissolve
    "You arrive at the throne room and see the Ayna, Enainia and Silvana talking"
    ayna "You know that we don't interfere with outside politics and events"
    silvana "I understand that, but they are my people, they asked for help"
    enainia "My realm is also under attack by those bastards..."
    ayna "I know... That's why I'm..."
    MC "Good morning..."
    scene v32g002
    with dissolve
    ayna "Oh.. Hello [MC]"
    silvana "Hi [MC]"
    enainia "Good morning young mage"
    MC "So.. You called me here Archmage?"
    ayna "Indeed, you are right on time"
    MC "What do you need me to do?"
    scene v32g003
    with dissolve
    ayna "I'm glad you asked, you see..."
    ayna "We have decided to help some of the nations that are under siege by the Slayers"
    ayna "I know.. We don't usually participate in outside events"
    ayna "But this has gone on far too long"
    ayna "And who says that they will not come here after they finish with all the others?"
    MC "I understand..."
    scene v32g004
    with dissolve
    silvana "Darkaria... My homeland is being slaughtered, thousands die each day..."
    silvana "Like many other nations, we need to act now"
    scene v32g005
    with dissolve
    enainia "It's really concerning, they are killing and raping all the elves"
    enainia "There are reports that they have mages on their side too"
    MC "Mages? Regular mages? Necromancers?"
    enainia "My mother told me that some villages just disappear, nobody to be found"
    enainia "No dead bodies... Nothing..."
    enainia "Some rumors also say that before some of the attacks there is a strange fog"
    enainia "Then fire from the sky... So you can imagine what we are dealing with"
    scene v32g006
    with dissolve
    ayna "And that's why we are helping them!"
    MC "I'll help in anyway I can"
    ayna "Good... Your help is most welcome"
    ayna "So this is what we will do"
    scene v32g004
    with dissolve
    ayna "You will travel with Mistress Silvana to Darkaria"
    ayna "Mistress Katriona and Master Katarro will meet you there later"
    ayna "Mistress Qa'arra and Master Bojay will travel with Princess Enainia here"
    ayna "They will help the elves defend Elvaria"
    scene v32g006
    with dissolve
    ayna "I will meet an old... {w} friend and see if she'll agree to help us"
    MC "An old friend?"
    ayna "Yes... No time to lose, let's start moving"
    "Archmage Ayna leaves"
    scene v32g007
    with dissolve
    silvana "We should do the same and leave"
    MC "Of course!"
    enainia "Good luck to you both"
    MC "Good luck to you too"
    scene v32g008
    with dissolve
    enainia "Let us all hope this is not the last time we see each other"
    enainia "Man galu na cin neth curunir!"
    scene v32g009
    with dissolve
    "Enainia left the room"
    MC "Was that elvish?"
    MC "What did she say?"
    scene v32g010
    with dissolve
    silvana "Yes, that was elvish."
    silvana "She said 'Good fortune to you, young wizard'"
    MC "Should we go?"
    silvana "Yes... But before we go let me tell you something"
    scene v32g012
    with dissolve
    silvana "I know you are a very capable mage..."
    silvana "But please don't try to face impossible odds"
    silvana "To win, we must work together, all of us"
    MC "I understand..."
    scene v32g011
    with dissolve
    silvana "Great! Let's get to the portal room at once"
    MC "So what can I expect to see in Darkaria?"
    silvana "Well, I haven't been there for a long time"
    silvana "But..."
    scene meanwhile
    with dissolve
    scene v25035
    with dissolve
    ayna "Will you help us?"
    Bredita "Hmmm... My lovely Ayna... What do I get in return?"
    ayna "I'm sure we can come to some sort of agreement"
    Bredita "Really? What could you give me that I don't have?"
    Bredita "Tell me though, why are you messing with problems outside the College?"
    ayna "This time it is a matter of great importance, it concerns all of Ataegina"
    ayna "Don't you think it's strange how the Slayers have become so powerful so fast?"
    Bredita "Hmmm... What do you mean?"
    ayna "I think there is demonic intervention involved..."
    Bredita "Ahaha you are very clever my dear..."
    ayna "You already knew?"
    Bredita "Well..."
    scene v32g013
    with dissolve
    silvana "Here we are... The front gates of Cysanore, the capital of Darkaria"
    MC "Wow.. those are some big walls!"
    silvana "Indeed..."
    scene v32g014
    with dissolve
    silvana "Cysanore is one of the most fortified cities in all of Ataegina"
    silvana "The dark elves are master builders, you know'"
    scene v32g015
    with dissolve
    MC "I can see that... I suppose this is where we will make our stand?"
    silvana "Yes..."
    "Such massive towers and walls will make it difficult for the Slayers to get in"
    onzanu "Welcome home, Mistress Silvana"
    scene v32g016
    with dissolve
    MC "I remember that guy... Onzanu"
    scene v32g017
    with dissolve
    onzanu "I'm glad to see you Mistress Silvana"
    silvana "It's good to be here, I wish it were for better reasons though.."
    onzanu "True... I'm glad you're here also [MC]"
    MC "Hello again, Onzanu"
    onzanu "Shall we get inside? The Queen will like to see you"
    silvana "Lead the way please"
    scene v32g018
    with dissolve
    "You see them start to go inside the walls and follow"
    "There are many fortifications but only a few soldiers inside"
    "Maybe they are hiding somewhere?"
    "You go inside one of the buildings"
    scene v32g019
    with dissolve
    silvana "Looks just like I remember..."
    silvana "It was so long ago..."
    onzanu "You know, our Queen doesn't care much about changing this place"
    scene v32g020
    with dissolve
    onzanu "Our Queen is upstairs"
    silvana "How long has it been since I saw her last...?"
    MC "I have no clue who they are talking about"
    "You reach the peak of the stairs"
    scene v32g021
    with dissolve
    "You see a dark elf woman sitting in a throne"
    onzanu "Great Queen Zordruza, here we are"
    zordruza "Thank you Onzanu"
    zordruza "So you finally decided to help your homeland... Sister..."
    scene v32g022
    with dissolve
    silvana "Hello little sister"
    silvana "Now you know that I'm not that makes those decisions for the Mages"
    "Little sister? Now that's something"
    zordruza "Little sister?... ahahah you haven't seen me in ages..."
    zordruza "Still you call me little sister, I'm a queen you know?"
    silvana "To me, you'll always be my little sister"
    "You feel some tension between them"
    scene v32g023
    with dissolve
    zordruza "And who is this? Introduce yourself young man"
    MC "I'm [MC] milady"
    zordruza "What is that power I feel around you?"
    zordruza "I... {w} come closer please"
    scene v32g024
    with dissolve
    "You get closer to her, you can feel her examining you"
    zordruza "Are you the shy type? Come closer"
    zordruza "I won't bite... Much.. Ahaha"
    MC "Ok...."
    scene v32g025
    with dissolve
    "You got really close to her"
    zordruza "That's better... Tell me something"
    zordruza "How long have you had this kind of power?"
    MC "What do you mean?"
    zordruza "You look young, yet your power feels like it was shaped for centuries..."
    zordruza "Care to explain to me why that is?"
    MC "I can't really tell you, I guess that's just how I am"
    scene v32g026
    with dissolve
    "You notice by her face that she is intriged"
    "You also notice that she has a big scar on her face, a strange symbol on her forehead"
    "And some unique purple colored eyes"
    "You wonder why Silvana's eyes are different from every dark elf"
    "She's the only one with fully white eyes..."
    zordruza "Is my face funny to you or something?"
    MC "Hmm... what?"
    zordruza "You've been staring into my eyes for a while now..."
    menu:
        "{color=#1BBB20}I find your eyes to be beautiful":
            scene v32g025
            with dissolve
            zordruza "Ahahaha, what a charmer we have here..."
            zordruza "I like it, ahaha"
        "I've never seen purple eyes before":

            scene v32g025
            with dissolve
            zordruza "They are quite rare, even among the dark elf people"
            zordruza "In fact, only my family has purple eyes that I know of"
        "I apologize, I didn't mean to stare":

            scene v32g025
            with dissolve
            zordruza "Ahaha what a shy boy... Don't worry"
            zordruza "I know, I have eyes of a pretty rare color"
            MC "Yes..."

    scene v32g027
    with dissolve
    "You start to feel something around you"
    zordruza "I wonder who you are... {w} What kind of power are you hiding from me?"
    MC "I'm... not hiding anything your highness"
    zordruza "Oh you are... You may not be aware of it, but you are"
    "You feel her power around you fade out..."
    scene v32g026
    with dissolve
    zordruza "You're..."
    zordruza "I'm intriged by you..."
    scene v32g028
    with dissolve
    zordruza "Onzanu take my sister and show her our plans to defend the city"
    scene v32g022
    with dissolve
    onzanu "I will my Queen!"
    silvana "Well, let's go [MC]"
    zordruza "No, let him stay, I want to talk to him in private"
    scene v32g023
    with dissolve
    zordruza "You don't mind, right [MC]?"
    MC "Of course not"
    silvana "Very well, lead the way Onzanu"
    scene v32g024
    with dissolve
    "They left"
    zordruza "Now that we are alone, can you tell me who you really are?"
    scene v32g025
    with dissolve
    MC "I was being honest... I don't know what you mean..."
    zordruza "Hmmm... Very well, follow me"
    scene v32g029
    with dissolve
    zordruza "Come on... Follow me"
    MC "Sure..."
    "What does she know about you?"
    scene v32g030
    with dissolve
    MC "I guess I need to follow her to find out more"
    "You follow her through a big corridor until you reach a room"
    scene v32g031
    with dissolve
    "You reach some sort of bedroom, there is a bed at least"
    zordruza "Please step into that magic circle"
    MC "But... why?"
    zordruza "If you are being honest and you really don't know who you are"
    zordruza "Then this spell may help"
    zordruza "You're also interested to find out, right?"
    MC "Yes..."
    zordruza "So... go on"
    scene v32g032
    with dissolve
    "As you get closer to the magic circle you start to feel weird"
    zordruza "Come on, don't be scared, get in"
    "You get inside the circle"
    zordruza "Good..."
    scene v32g033
    with dissolve
    "You feel her casting something"
    MC "So much power..."
    "You are impressed with what you are feeling"
    "There are some skilled mages outside the college"
    scene v32g034
    with dissolve
    zordruza "Abdulon Passadum"
    MC "What... Is .... this..."
    MC "I feel... weird..."
    zordruza "Revelium!!"
    scene black
    with dissolve
    scene v3g047
    with dissolve
    MC "Where the hell...?"
    Nonen "You again... This time I'll take what is rightfully mine"
    scene v3g048
    with dissolve
    Nonen "Let's see if you are a match for me, ahahaha"
    MC "You again? Who are you?"
    Nonen "You'll find out soon enough!"
    scene v3g049
    with dissolve
    $ enemy = "necromage"
    $ companion = 0
    jump combat

label v32glich:
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    scene v3g048
    with dissolve
    Nonen "Ahahahaaha, you are even stronger than I imagined, ahahahah"
    Nonen "Ahaahah, that's even better, ahahaha"
    Nonen "My return will be sooner than I expected, ahahaha"
    Nonen "I'll give you a gift... Here..."
    scene v3g049
    with dissolve
    "You feel some power around you"
    MC "What is happening?"
    $ powercount = Destpoints + Iluspoints + Healpoints + Mystpoints + Summpoints + Altepoints + Necropoints + 5

    $ Destpoints = 0
    $ Iluspoints = 0
    $ Healpoints = 0
    $ Mystpoints = 0
    $ Summpoints = 0
    $ Altepoints = 0
    $ Necropoints = 0

    scene v3g048
    with dissolve
    Nonen "Where are your powers now?"
    MC "What have you done?!"
    Nonen "I took all your powers, how will you face me now?"
    MC "But..."
    Nonen "Ahahaha, don't worry, I want you as powerful as possible"
    Nonen "That's why I'm reseting your skills and giving you an extra 5 points to add"
    MC "What?"
    Nonen "Choose wisely, after all... I need you..."
    scene black
    with dissolve

    stop music
    play music "<loop 0.0>ingame.mp3"
    scene black
    nvl clear
    n "You will now redistribute all your skills"
    n "With a bonus of 5 extra points"


label checkskills:
    if powercount >= 1:
        jump keepchoosingv32g
    else:
        jump nextfasezordruzav32g


label keepchoosingv32g:
    "You have [powercount] skill points to assign"
    menu:
        "Raise Battlemagic {image=001battle}":
            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))

            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Destpoints = skillcheck + Destpoints
                "Your Battlemagic skill improved"
                $ powercount = powercount - skillcheck
        "Raise Summoning {image=001summon}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))

            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Summpoints = skillcheck + Summpoints
                "Your Summoning skill improved"
                $ powercount = powercount - skillcheck
        "Raise Alteration {image=001alteration}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Altepoints = skillcheck + Altepoints
                "Your Alteration skill improved"
                $ powercount = powercount - skillcheck
        "Raise Ilusion {image=001illusion}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Iluspoints = skillcheck + Iluspoints
                "Your Ilusion skill improved"
                $ powercount = powercount - skillcheck
        "Raise Mysticism {image=001myst}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Mystpoints = skillcheck + Mystpoints
                "Your Mysticism skill improved"
                $ powercount = powercount - skillcheck
        "Raise Healing{image=001heal}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Healpoints = skillcheck + Healpoints
                "Your Healing skill improved"
                $ powercount = powercount - skillcheck
        "Raise Necromancy{image=001necro}":

            $ skillcheck = int(renpy.input(prompt="How many points?", default="0", allow="0123456789", length=2))
            if skillcheck >= powercount +1:
                "You don't have that many available points, you have [powercount] left"
                jump keepchoosingv32g
            else:
                $ Necropoints = skillcheck + Necropoints
                "Your Necromancy skill improved"
                $ powercount = powercount - skillcheck

    jump checkskills

label nextfasezordruzav32g:
    scene v32g035
    with dissolve
    zordruza "Revelium!!"
    zordruza "Altradis Revelium!!"
    zordruza "Fin Revelium!!"
    scene v32g036
    with dissolve
    zordruza "Oh my God!! Your are even stronger now"
    MC "What the hell just happened?"
    MC "What have you done? I feel like..."
    zordruza "You have such an incredible untapped power..."
    zordruza "How is that even possible?"
    scene v32g037
    with dissolve
    zordruza "For a moment I felt all your powers disappear"
    zordruza "But then they came back, stronger than before"
    zordruza "I can't understand what happened"
    MC "That makes two of us..."
    zordruza "You may have a lot of power..."
    zordruza "But since every Mage has a limit, you should carry a real weapon"
    scene v32g038
    with dissolve
    "You see her moving a sword that was on the wall"
    zordruza "This is what you need"
    scene v32g039
    with dissolve
    zordruza "Take it"
    MC "Thank you, but I think that's a little too big to carry in my robe..."
    zordruza "This is a magical Dark Elf sword, it will only exist when summon it"
    MC "What do you mean?"
    zordruza "I mean that it will exist elsewhere, but materialize when called"
    MC "Like a sword summon?"
    zordruza "Yes, but with no magic consumption"
    MC "Awesome! Thank you so much"
    scene v32g040
    with dissolve
    zordruza "Take good care of it"
    MC "I will!!"
    $ weapon = 1
    "You can now use {color=#f00}{b}Melee{/b}{/color} during combat"
    zordruza "Are you feeling ok?"
    MC "I...."
    scene v32g041
    with dissolve
    scene v32g041
    with dissolve
    scene v32g040
    with dissolve
    MC "What is..."
    zordruza "[MC]? [MC]! Do you hear me?"
    scene v32g041
    with dissolve
    scene v32g041
    with dissolve
    scene v32g040
    with dissolve
    MC "I feel... Weird..."
    scene v32g041
    with dissolve
    scene black
    with dissolve
    scene v32g041
    with dissolve
    label galleryScene3:
    zordruza "You want to have some fun with me?"
    MC "But..."
    scene v32g041
    with dissolve
    scene v32g041
    with dissolve
    scene v32g042
    with dissolve
    zordruza "Don't you think I'm pretty? Have you ever kissed a Dark Elf?"
    scene v32g040
    with dissolve
    scene v32g040
    with dissolve
    scene v32g042
    with dissolve
    MC "No... I never did..."
    zordruza "Don't you want to?"
    MC "I..."
    menu:
        "{color=#1BBB20}Yes I want to":
            scene v32g044
            with dissolve
            zordruza "Hmmm... Then let's give you something to remember"
            zordruza "Lie on the bed!!"
            MC "Now that's agressive"
            zordruza "Move!"
            scene v32g045
            with dissolve
            "You lie on the bed and stare at her"
            zordruza "What a good boy you are"
            zordruza "Are you ready for my kiss?"
            MC "Yes..."
            scene v32g046
            with dissolve
            zordruza "Let me just put this here, we don't want anybody to hurt themselves"
            zordruza "Not much I mean, ahahah"
            scene black
            with dissolve
            scene v32g047
            with dissolve
            zordruza "You like what you see?"
            MC "Yes... You have an amazing body"
            scene v32g048
            with dissolve
            zordruza "Kiss me!"
            "You kiss her for a brief moment"
            scene v32g049
            with dissolve
            zordruza "Is it just my body you like?"
            zordruza "Nothing else?"
            MC "That's not what I meant"
            scene v32g050
            with dissolve
            MC "Your face is exotic, your eyes are..."
            MC "Unique... Even this scar..."
            scene v32g051
            with dissolve
            "She kisses you again"
            scene v32g050
            with dissolve
            MC "Can you tell me the story behind this scar?"
            zordruza "I'd prefer not to..."
            zordruza "Instead, why don't you play with my boobs?"
            MC "What? I mean... If you insist"
            scene v32g052
            with dissolve
            MC "Like this?"
            zordruza "Hmmm yes... you can squeeze a bit harder you know?"
            "She grabs your arm"
            scene v32g053
            with dissolve
            zordruza "Come on, feel it the right way"
            "Her boobs feel great, soft but firm, you give them a tigher squeeze"
            zordruza "Ah... Yes... That's better, keep going"
            zordruza "Hmmm... Yes..."
            scene v32g054
            with dissolve
            zordruza "Do you like them?"
            MC "Yes I do..."
            zordruza "Do like to squeeze them like that?"
            MC "Yes..."
            scene v32g055
            with dissolve
            "She kisses you again"
            zordruza "Hmmm... This feels great"
            zordruza "Take those clothes off now"
            "You do what you're told"
            scene v32g056
            with dissolve
            "She grabs your already erect dick"
            zordruza "You have a big one here... I bet you can satisfy a girl"
            MC "I haven't had any complaints yet..."
            scene v32g057
            with dissolve
            zordruza "Hmmmm... Good..."
            "She starts to stroke you"
            MC "Hmmmm"
            zordruza "How does that feels? Good?"
            MC "Yes... Very good"
            scene v32g058
            with dissolve
            zordruza "Let's see if it tastes as good as it looks"
            "You start to feel her tongue moving around you dick head"
            zordruza "Hmmm it's a bit salty but I like it"
            scene v32g059
            with dissolve
            "She then started to put it inside her mouth"
            "It feels wonderful... She knows exactly what she is doing"
            MC "Ah....."
            "You don't know if you can hold much longer if she keeps like this"
            scene v32g060
            with dissolve
            zordruza "Hmmm I hope you are enjoying yourself"
            MC "I most certainly am"
            scene v32g061
            with dissolve
            "She's really good, her mouth, her tongue, even her touch..."
            "You never felt something like this before"
            zordruza "Now, it's time for you make me feel good as well"
            scene v32g062
            with dissolve
            "She lies on her back and starts to rub her pussy"
            zordruza "Show me what you got, young man"
            MC "I will"
            scene v32g063
            with dissolve
            "You dive down with your mouth, right on to her pussy"
            zordruza "Oh my... Such vigor... Hmmm"
            zordruza "Yes... keep going!!"
            MC "Hmhmhmhm"
            zordruza "Yes! Put your tongue deeper!!"
            zordruza "Move it faster!!"
            scene v32g064
            with dissolve
            zordruza "AH!!! YES!! Don't stop! lick it all!"
            zordruza "More more!"
            "You feel her hand pulling your head to her pussy with increasing strength"
            zordruza "Don't you dare to stop!!"
            scene v32g063
            with dissolve
            zordruza "Hmmmm... Oh my... That's great..."
            zordruza "Hmm...."
            scene v32g065
            with dissolve
            "She pushes you to the bed"
            zordruza "That was intense... I've never come from a tongue before..."
            MC "Glad I could help with that..."
            scene v32g066
            with dissolve
            zordruza "Oh you did more than help..."
            zordruza "Have you ever felt the inside of a Queen?"
            MC "Can't say I have..."
            scene v32g067
            with dissolve
            zordruza "Hmmm I can't wait any longer for this big cock"
            zordruza "I bet it feels great..."
            zordruza "Put it in..."
            scene v32g068
            with dissolve
            "With no more delay you start to slide inside of her"
            zordruza "Mhhff yes.... That's it..."
            zordruza "Ah... Yes...."
            scene v32g069
            with dissolve
            "You are almost all the way inside"
            "She then grabs your arm and says"
            zordruza "I'm gonna drain you completely!!"
            "With those words you push your dick deeper"
            scene v32g070
            with dissolve
            zordruza "Ah.... Yeah...."
            MC "Ah.... This is great..."
            zordruza "You are so deep... keep going..."
            MC "Turn around, I want to try something else"
            zordruza "Very well"
            scene v32g071
            with dissolve
            "She turns around, you are now facing her lovely butt"
            zordruza "Is this what you wanted?"
            "Before she could hear your answer..."
            scene v32g072
            with dissolve
            "You slide your dick all the way inside her pussy and start pounding"
            zordruza "Ahhhh!!! YES!!!!YES!!! I'm cumming!"
            MC "Ah..... I'm about to..."
            scene v32g073
            with dissolve
            zordruza "Hold on... I didn't say you could cum yet!"
            MC "But..."
            scene v32g074
            with dissolve
            "She returns to stroke your cock"
            zordruza "You want to cum?? Do you??"
            zordruza "But you can only cum when I tell you, alright?"
            scene v32g075
            with dissolve
            "Her pace gets faster and faster"
            MC "Ah! I can't hold it anymore... I'm..."
            zordruza "Yeah cum for me!"
            MC "Ahhhhhh"

            scene v32g076
            show shot
            with hpunch
            hide shot
            show shot
            with hpunch
            hide shot
            MC "Ahhh shit..... Ah..."
            show shot
            with hpunch
            hide shot
            scene v32g077
            show shot
            with hpunch
            hide shot
            MC "Ah.... pfew..."
            zordruza "So much cum you got... Look at this..."
            MC "I...."
            scene black
            with dissolve
            scene v32g077
            with dissolve
            zordruza "I wonder if it tastes good"
            scene black
            with dissolve
            scene v32g078
            with dissolve
            zordruza "Hmmm.... delicious..."
            MC "I feel..."
            scene black
            with dissolve
            scene v32g078
            with dissolve
            zordruza "Hmmm..."
            scene v32g079
            with dissolve
            zordruza "Are you ok? [MC]?"
            scene black
            with dissolve
            zordruza "[MC]?"
            darkelf "Oh hello Zordruza"
            scene v32g080
            with dissolve
            yzordruza "You wanted to see me father?"
            darkelf "I did... We need to celebrate"
            scene v32g081
            with dissolve
            yzordruza "Celebrate? Why?"
            darkelf "Your sister is going to Mage College"
            yzordruza "That's great news"
            darkelf "Here, have a drink!"
            yzordruza "But I..."
            darkelf "Come on! It's just for today!"
            scene v32g082
            with dissolve
            yzordruza "Ok... I guess it won't hurt..."
            darkelf "That's my girl! Here take it"
            scene v32g083
            with dissolve
            yzordruza "Yes... Father..."
            darkelf "You know, there is something else to celebrate"
            yzordruza "Really? What is it?"
            scene v32g084
            with dissolve
            darkelf "You..."
            yzordruza "Father... What are you doing?..."
            darkelf "You are so pretty, my dear Zordruza..."
            yzordruza "Father what...?"
            darkelf "I bet you look even better without..."
            scene v32g085
            with dissolve
            darkelf "This!!!"
            yzordruza "What are you doing??!!"
            darkelf "Ahahahaa, turn around!"
            scene v32g086
            with dissolve
            yzordruza "Stop it!"
            darkelf "Look at this... No wonder why everbody wants to marry you..."
            yzordruza "Stop this father! Please!"
            darkelf "But I get to test it first..."
            scene v32g087
            with dissolve
            yzordruza "What are you talking about? Why are you doing this?"
            darkelf "Don't you want to please your father? Your King?"
            darkelf "You need to do what you're told!"
            scene v32g088
            with dissolve
            darkelf "Now turn around and spread those legs!!"
            yzordruza "No!!! Stop it!!! STOP!!"
            scene v32g089
            with dissolve
            darkelf "Before anyone takes you as his wife, I want to try everything"
            yzordruza "STOP!!! SOMEBODY HELP!!"
            darkelf "Shut it bitch!! You think anyone would lift a finger against me?"
            yzordruza "HELP!!"
            darkelf "This is going to be great!"
            fvoice "What is happening here?"
            scene v32g090
            with dissolve
            darkelf "Silvana? What are you doing here?"
            yzordruza "Help me sister, please!"
            ysilvana "What are you doing to her?"
            scene v32g091
            with dissolve
            darkelf "I'm the King!! I do what I want!!"
            ysilvana "You were trying to rape her!!"
            ysilvana "Wait until everyone knows about this"
            ysilvana "Then we will see what they think about their... King"
            darkelf "How dare you threaten me?!"
            scene v32g092
            with dissolve
            darkelf "You bitch!!"
            ysilvana "Ah... Let me go"
            yzordruza "Stop it! Leave her alone!!"
            scene v32g093
            with hpunch

            "Slap"
            darkelf "Shut it you whore!!"
            yzordruza "Ah!!"
            scene v32g094
            with dissolve
            darkelf "Look what you made me do..."
            darkelf "Now your face is ruined!! You whore!!"
            ysilvana "HOW DARE YOU?!!"
            darkelf "Hmm?"
            scene v32g095
            with dissolve
            ysilvana "HOW DARE YOU?!!"
            darkelf "What?"
            ysilvana "YOU HURT MY SISTER!!! YOU'LL PAY!!"
            scene v32g096
            with dissolve
            darkelf "What do you think you're doing?"
            darkelf "I'm gonna crush your little..."
            scene v32g097
            with dissolve
            darkelf "Aharhahrhag"
            ysilvana "AHHHH!!"
            scene black
            with dissolve
            scene v32g098
            with dissolve
            yzordruza "Sister? are you ok?"
            yzordruza "Sister?"
            ysilvana "I.... Can't see..."
            ysilvana "My eyes... I..."
            scene v32g099
            with dissolve
            yzordruza "Silvana??"
            ysilvana "I can't see... I'm blind..."
            scene v32g100
            with dissolve
            yzordruza "Thank you! Thank you big sister..."
            yzordruza "He was going to rape me... I..."
            ysilvana "There... It's ok now..."
            scene black
            with dissolve
            zordruza "Are you ok? [MC]?"
            scene v32g103
            with dissolve
            MC "Hmm?"
            zordruza "You blacked out for a moment"
            MC "I'm ok... I guess..."
            scene v32g104
            with dissolve
            zordruza "Can't handle a real woman? Ahaha"
            zordruza "I told you I would drain you...."
            MC "You sure did... I need to sleep now..."
            scene black
            with dissolve
            zordruza "Sweet dreams..."
            jump v32gmorning
        "I don't think it's a good idea":


            scene v32g043
            with dissolve
            zordruza "Really?"
            scene black
            with dissolve
            scene v32g040
            with dissolve
            zordruza "Are you ok?"
            MC "I'm not sure..."
            zordruza "[MC]? [MC]?"
            scene black
            with dissolve
            darkelf "Oh hello Zordruza"
            scene v32g080
            with dissolve
            yzordruza "You wanted to see me father?"
            darkelf "I did... We need to celebrate"
            scene v32g081
            with dissolve
            yzordruza "Celebrate? Why?"
            darkelf "Your sister is going to to Mage College"
            yzordruza "That's great news"
            darkelf "Here, have a drink!"
            yzordruza "But I..."
            darkelf "Come on! It's just for today!"
            scene v32g082
            with dissolve
            yzordruza "Ok... I guess it won't hurt..."
            darkelf "That's my girl! Here take it"
            scene v32g083
            with dissolve
            yzordruza "Yes... Father..."
            darkelf "You know, there is something else to celebrate"
            yzordruza "Really? What is it?"
            scene v32g084
            with dissolve
            darkelf "You..."
            yzordruza "Father... What are you doing?..."
            darkelf "You are so pretty, my dear Zordruza..."
            yzordruza "Father what...?"
            darkelf "I bet you look even better without..."
            scene v32g085
            with dissolve
            darkelf "This!!!"
            yzordruza "What are you doing??!!"
            darkelf "Ahahahaa, turn around!"
            scene v32g086
            with dissolve
            yzordruza "Stop it!"
            darkelf "Look at this... No wonder why everbody wants to marry you..."
            yzordruza "Stop this father! Please!"
            darkelf "But I get to test it first..."
            scene v32g087
            with dissolve
            yzordruza "What are you talking about? Why are you doing this?"
            darkelf "Don't you want to please your father? Your King?"
            darkelf "You need to do what you're told!"
            scene v32g088
            with dissolve
            darkelf "Now turn around and spread those legs!!"
            yzordruza "No!!! Stop it!!! STOP!!"
            scene v32g089
            with dissolve
            darkelf "Before anyone takes you as his wife, I want to try everything"
            yzordruza "STOP!!! SOMEBODY HELP!!"
            darkelf "Shut it bitch!! You think anyone would lift a finger against me?"
            yzordruza "HELP!!"
            darkelf "This is going to be great!"
            fvoice "What is happening here?"
            scene v32g090
            with dissolve
            darkelf "Silvana? What are you doing here?"
            yzordruza "Help me sister, please!"
            ysilvana "What are you doing to her?"
            scene v32g091
            with dissolve
            darkelf "I'm the King!! I do what I want!!"
            ysilvana "You were trying to rape her!!"
            ysilvana "Wait until everyone knows what you are doing"
            ysilvana "Then we see what they think about their... King"
            darkelf "How dare you threatening me?!"
            scene v32g092
            with dissolve
            darkelf "You bitch!!"
            ysilvana "Ah... Let me go"
            yzordruza "Stop it! Leave her alone!!"
            scene v32g093
            with dissolve
            "Slap"
            darkelf "Shut it you whore!!"
            ysilvana "Ah!!"
            scene v32g094
            with dissolve
            darkelf "Look what you made me do..."
            darkelf "Now your face is ruined!! You whore!!"
            ysilvana "HOW DARE YOU?!!"
            darkelf "Hmm?"
            scene v32g095
            with dissolve
            ysilvana "HOW DARE YOU?!!"
            darkelf "What?"
            ysilvana "YOU HURT MY SISTER!!! YOU'LL PAY!!"
            scene v32g096
            with dissolve
            darkelf "What do you think you're doing?"
            darkelf "I'm gonna crush your little..."
            scene v32g097
            with dissolve
            darkelf "Aharhahrhag"
            ysilvana "AHHHH!!"
            scene black
            with dissolve
            scene v32g098
            with dissolve
            yzordruza "Sister? are you ok?"
            yzordruza "Sister?"
            ysilvana "I.... Can't see..."
            ysilvana "My eyes... I..."
            scene v32g099
            with dissolve
            yzordruza "Silvana??"
            ysilvana "I can't see... I'm blind..."
            scene v32g100
            with dissolve
            yzordruza "Thank you! Thank you big sister..."
            yzordruza "He was going to rape me... I..."
            ysilvana "There... It's ok now..."
            scene black
            with dissolve
            zordruza "Are you ok? [MC]?"
            scene v32g101
            with dissolve
            MC "Hmm?"
            zordruza "You blacked out a moment ago"
            MC "Oh... Ok..."
            scene v32g102
            with dissolve
            zordruza "I think you need to sleep a bit"
            zordruza "Feel free to do so"
            MC "Thank you... i do feel tired.."
            scene black
            with dissolve
            zordruza "Sweet dreams..."
            jump v32gmorning

label v32gmorning:
    $ renpy.end_replay()
    fvoice "Hello [MC]"
    scene v32g106
    with dissolve
    fvoice "I'm so proud of you for resisting evil"
    fvoice "But I feel a taint in you now"
    scene v32g107
    with dissolve
    fvoice "A taint that makes you stronger..."
    fvoice "Don't let that taint control you"
    scene v32g108
    with dissolve
    fvoice "You are stronger than that!"
    scene v32g109
    with dissolve
    fvoice "You are stronger than anything"
    scene v32g110
    with dissolve
    fvoice "Good luck... You're going to need it..."
    scene black
    with dissolve
    scene black
    with dissolve



    play sound "sounds/bell.mp3"
    "Bells tolling"
    MC "Hmm what..."
    scene v32g105
    with dissolve
    MC "Where am I? Oh right... Was all that a dream?"

    MC "What is happening?"
    ppl "Move move!! They are coming!!"
    mvoice "Run! Hurry!"
    MC "What the hell?"
    "You move to one of the doors that leads outside"
    scene battle01v32g
    with dissolve
    "You can't believe your eyes..."
    MC "Holy shit!! Look at that..."
    "You try to look further away"
    scene battle02v32g
    with dissolve
    "And it's even more impressive..."
    MC "I can't see the end of that army..."
    MC "Is the battle about to start??"

    jump v31orctalk

label goodis1year:
    scene 1y001
    with dissolve
    MC "They are starting to move, the catapults are beginning to fire"

    scene 1y002
    with hpunch
    scene 1y002
    with vpunch
    MC "Oh shit!! I need to get inside.. Fast!"
    scene 1y003
    with dissolve
    MC "Are they inside already? But how?"
    scene 1y004
    with dissolve
    sol "Look what we've got here!! "
    sol2 "Ahahah more entertainment!"
    MC "Bastards! You want entertainment?!"
    scene 1y005
    with dissolve
    MC "Come and get it!!"
    "You don't care anymore, you just unleash your power on them"
    scene 1y006
    with dissolve
    sol "Arghhh!!"
    sol2 "What the fuck!!"
    sol "Stop this!!"
    scene 1y007
    with dissolve
    "In the next moment they are all down"
    fvoice "Well well well... What do we have here?"
    scene 1y008
    with dissolve
    fvoice "Another Mage? Let's bring him in!"
    MC "Who the hell are you?"
    scene 1y009
    with dissolve
    fvoice "Stop!"
    "You can't seem to move at all. Is this her doing?"
    scene 1y010
    with dissolve
    fvoice "Sweet dreams..."
    MC "..."
    scene black
    with dissolve
    jump lichthehellout
