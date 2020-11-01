


screen choicegood:
    imagemap:
        ground "heavenchoice.jpg"
        hover "heavenchoice01.jpg"

        hotspot (0, 0, 1017, 1080) clicked Jump ("katrionachoice01")
        hotspot (1018, 0, 1920, 1080) clicked Jump ("aynachoice01")


screen choiceroom01:
    imagemap:
        ground "katroombg.jpg"
        hover "katroombgout.jpg"

        hotspot (676, 0, 450, 440) clicked Jump ("windowchoice01")
        hotspot (699, 535, 220, 50) clicked Jump ("bookchoice01")
        hotspot (1116, 490, 35, 95) clicked Jump ("statuechoice01")
        hotspot (66, 331, 333, 70) clicked Jump ("globechoice01")
        hotspot (1806, 235, 190, 525) clicked Jump ("doorchoice01")




label sweetdream:
    scene heaven
    with dissolve
    fvoice "Yes, follow those stairs"
    scene heaven001
    with dissolve
    fvoice "On the top you will have"
    fvoice "A gift to choose"
    fvoice "See you upstairs...."
    MC "Wait I.."
    scene heaven001
    with dissolve
    scene heaven002
    with dissolve
    scene heaven003
    with dissolve
    scene heaven
    with dissolve
    MC "She's gone..."
    MC "Well... let's see what we’ve got up there"
    scene heaven004
    with dissolve
    scene heaven005
    with dissolve
    scene heaven006
    with dissolve
    fvoice "I'm glad you came"
    fvoice "Now you can choose one of the girls"
    fvoice "To show you a good time"
    call screen choicegood

label katrionachoice01:
    scene heaven01
    with dissolve
    scene heaven007
    with dissolve
    katriona "So..."
    katriona "You choose me"
    scene heaven008
    with dissolve
    katriona "I'm flattered"
    katriona "But what do you want with me?"
    katriona "Don't tell me..."
    scene heaven009
    with dissolve
    katriona "Is this what you want?"
    katriona "Your face says it all"
    scene heaven010
    with dissolve
    katriona "Is it getting better?"
    katriona "Do you want to see more?"
    katriona "Or maybe you want a kiss?"
    scene heaven011
    with dissolve
    katriona "Do you want to kiss me?"
    katriona "While I play with my nipple?"
    MC "Yes..."
    katriona "Too bad..."
    katriona "You're just a kid..."
    MC "What?"
    scene heaven012
    with dissolve
    katriona "So..."
    katriona "I must go now"
    katriona "It's time to wake up"
    scene heaven01
    with dissolve
    scene black
    with dissolve
    jump wakepart01




label aynachoice01:
    scene heaven01
    with dissolve
    scene heaven013
    with dissolve
    ayna "Hi"
    ayna "You choose me?"
    ayna "Is it because I'm pretty?"
    scene heaven014
    with dissolve
    ayna "I also think you're cute"
    ayna "But let me guess"
    scene heaven015
    with dissolve
    ayna "You want to see these?"
    ayna "Of course you do."
    scene heaven016
    with dissolve
    ayna "Do you like them?"
    ayna "Want to see more?"
    scene heaven017
    with dissolve
    ayna "Want me to play with them?"
    ayna "Like this?"
    ayna "You want something more?"
    ayna "Too bad you're a kid..."
    MC "What?"
    scene heaven018
    with dissolve
    ayna "It's time to wake up"
    ayna "... bye.."
    MC "Wait I..."
    scene heaven01
    with dissolve
    scene black
    with dissolve
    jump wakepart01



label nightmare:
    scene a026
    with dissolve
    mom "Nooo, let me go!!"
    cpt "Ahahaha"
    cpt "Show me that pretty face"
    scene mare001
    with dissolve
    mom "Why are you doing this?"
    cpt "You look too good not to do this"
    cpt "Now let's remove those clothes"
    mom "What the?..."
    scene mare002
    with dissolve
    cpt "Now that's better"
    cpt "Ahahaha"
    mom "How did this happen?"
    cpt "You look amazing let me tell you"
    mom "Stop this!!"
    cpt "Time to get on your knees"
    mom "Never!!"
    scene mare003
    with dissolve
    mom "How are you doing this??"
    cpt "Ahahaha"
    cpt "Imagine what you will do next!"
    cpt "Ahahaha"
    sis "Why are you allowing this?"
    MC "What?"
    scene mare004
    with dissolve
    sis "Yes!!"
    sis "Why are you allowing this!!??"
    scene mare005
    with dissolve
    sis "You like to see mom suffering??"
    sis "After all that happened??"
    sis "You're lucky I'm just in your dream!"
    scene black
    with dissolve
    nvl clear
    n "That last sentence"
    n "You get awoken out of the dream"
    nvl clear

label wakepart01:
    $ renpy.end_replay()
    play music "<loop 0.0>ingame.mp3"
    scene wake001
    with dissolve
    scene wake002
    with dissolve
    scene wake003
    with dissolve
    scene wake004
    with dissolve

    MC "What the hell just happened?"
    scene katroombg
    with dissolve
    scene meanwhile
    with dissolve
    scene meanwhile
    with dissolve
    scene meet001
    with dissolve
    suntako "So you are saying that boy has the potential"
    suntako "To be as powerful as one of us?"
    scene meet002
    with dissolve
    ayna "Yes"
    ayna "With the correct help he can become a very skillful mage"

    scene meet003
    with dissolve
    silvana "Are you sure?"
    silvana "It's been a while since Mistress Katriona joined us"

    katriona "Well that depends...60 years is nothing for an Elf"

    silvana "That's correct... But still..."
    scene meet002
    with dissolve
    ayna "As if 60 years is anything to any of us"
    scene meet001
    with dissolve
    bojay "So you're saying that the boy could reach our level if we train him the right way?"

    scene meet002
    with dissolve
    ayna "That's exactly what I'm saying"
    scene meet003
    with dissolve
    silvana "We have to be careful though... Remember Bredita?"

    scene meet001
    with dissolve
    nvl clear
    "Everyone got serious after hearing that name"

    suntako "Yes... That's what I'm worried about…"
    scene meet002
    with dissolve
    ayna "Well, we all have the responsibility for that"
    katriona "Well I don't... Hehehe"

    scene meet003
    with dissolve
    Qa "Lucky you... We've heard nothing in regards to her for a while"

    katriona "Well I hope we don't. I was almost killed last time"

    scene meet002

    with dissolve

    katarro "{i}*telepathy-( Don't you want to tell them the truth? ){/i}"
    ayna "{i}*telepathy-( You know some of them will not accept it ){/i}"
    katarro "{i}*telepathy-( I trust your judgement ){/i}"
    ayna "{i}*telepathy-( Thank you ){/i}"

    scene meet001
    with dissolve
    suntako "Tell me something... Where did you find the boy?"

    suntako "Whats more, how did he appear here?"
    scene meet002
    with dissolve
    ayna "Well, a village in Arfam was attacked by the Slayers, he was the sole survivor"

    katriona "Those damned Slayers... They're always looking to conquer everyone"

    scene meet003
    with dissolve
    Qa "Yes... they're like the damned orcs... But smarter..."

    scene meet001
    with dissolve
    suntako "Well, if there is nothing else to talk about"
    bojay "Yeah.. I want to go too"
    scene meet003
    with dissolve
    silvana "You guys always have lots of things to do..."
    Qa "No matter the age... Boys will be boys..."

    scene meet002
    with dissolve
    ayna "Before you go... I want to ask something"
    ayna "What do you all think of sending the boy to the College, with the other kids?"

    katriona "I think it's a good idea!"
    scene meet001
    with dissolve
    suntako "Of course you think it's a good idea, you always agree with the Archmage"

    scene meet003
    with dissolve
    katriona "Well... You always disagree... so..."
    silvana "I also agree"
    Qa "Me too, as long as I don't have to babysit him"
    scene meet002
    with dissolve
    katarro "I think it's a good idea"
    scene meet001
    with dissolve
    bojay "I'm with Qa'arra, as long as I don't have to worry about him"

    suntako "Very well, do what you want.."
    scene meet002
    with dissolve
    ayna "So it's settled! He will be joining classes as soon as possible"

    ayna "You are all dismissed"
    scene katroombg
    with dissolve
    show screen points_all
    MC "What kind of place is this? My head... Hurts..."

    MC "That dream felt so real... But who am I?"

    MC "Why don't I remember anything?"
    MC "Well.. staying in bed will not change anything... I should get up"

label katroomdream:

    scene katroombg


    with dissolve
    MC "What to do.... What to do?"
    call screen choiceroom01


label bookchoice01:
    MC "It's a book about the schools of magic..."
    MC "Should I read it?"
    menu:
        "[abgreen]Yes":
            MC "Let's read a bit about that"
            MC "I want to check..."
            menu:
                "Battlemagic":
                    "Battle magic focuses on combat spells, it uses elements like fire or lightning"
                    "Fireball, Thunder or Ice spike are typical spells of this school"
                    "Masters of this school are feared because of their raw destructive power"
                    jump katroomdream
                "Healing":
                    "Healing Magic focuses on the restoration of your own health, as well as others"
                    "Healing can also be used in combat versus some kinds of undead opponents"
                    "Masters of this school are highly loved and regarded for saving so many lives"
                    jump katroomdream
                "Summoning":
                    "Summoning focuses on magically creating creatures or objects to aid you"
                    "Lizards, Wolfs, Cats, Swords, you name it..."
                    "Masters of this school can summon giant creatures and create massive objects"
                    jump katroomdream
                "Illusion":
                    "Illusion Magic focuses on tricking the mind, feelings and senses of others"
                    "Fear, invisibility, mind control fall on this school specialities"
                    "Masters of this school can trick and control weaker opponents"
                    jump katroomdream
                "Alteration":
                    "Alteration Magic focuses on converting raw magical energy into useable forms"
                    "Using energy to create floating light sources and powerful magical barriers"
                    "Masters of this school can infuse energy into anything and change their nature"
                    jump katroomdream
                "Mysticism":
                    "Mysticism focuses on spells that defy the laws of physics"
                    "Telekinesis, teleporting and time manipulation are just some examples"
                    "Masters of this school can create walls of pure force and manipulate gravity"
                    jump katroomdream
        "No":


            MC "I'm not going to read it..."
            jump katroomdream


label windowchoice01:
    MC "I can't see what's outside"
    MC "There's too much fog..."
    jump katroomdream

label statuechoice01:
    MC "It's a statue of some kind of divinity"
    MC "A woman with a child in her arms..."
    MC "It looks familiar for some reason..."
    jump katroomdream

label globechoice01:

    MC "Wow, those look kinda tasty..."
    MC "..err on second thought, who knows what that lady has in here..."

    jump katroomdream

label doorchoice01:
    MC "Is the door open?"
    MC "Let's check"
    jump leftkatroom

label leftkatroom:


    scene hall
    with dissolve
    MC "Wow..."
    MC "What is this place?"
    nvl clear
    MC "Maybe I'll find someone if I look around..."
    "You start to hear a woman's voice"
    "Like some kind of singing"

    MC "I should see where this singing is coming from"
    scene aynabath001
    with dissolve
    MC "Is this some kind of bath house?"
    ayna "{i}*Singing- Mmmhhmm{/i}"
    ayna "{i}*Singing- La la la{/i}"
    MC "There's someone there"
    scene aynabath002
    with dissolve
    MC "It's a woman..."
    scene aynabath003
    with dissolve
    MC "Oh man..."
    MC "Look at that..."
    scene aynabath004
    with dissolve
    MC "Wow.."
    MC "That's the pretty lady that was talking to me earlier"
    MC "She's naked..."
    scene aynabath005
    with dissolve
    ayna "Phew"
    ayna "I really needed this.."
    ayna "That Suntako always gets on my nerves.."

    scene aynabath006
    with dissolve
    katriona "I knew I would find you here"
    MC "There's the other one too, she looks amazing..."
    MC "Should I stay? What if someone see me?"
    menu:
        "[abgreen]Leave":
            MC "Let's get out of here"
            jump endbath
        "Stay":
            MC "I want to see what's going on"
            jump keepbath

label keepbath:
    ayna "What are you doing here?"
    katriona "What do you think?"
    scene aynabath007
    with dissolve
    katriona "I came to lift your spirits"
    ayna "You know I'm always up for that"
    ayna "But you also know that nobody can find out about it.."
    katriona "Yeah yeah... I know...."
    scene aynabath008
    with dissolve
    katriona "Come here, let me kiss you"
    scene aynabath009
    with dissolve
    ayna "Mhhmm"
    katriona "Mmm"
    MC "Wow, they're kissing?"
    MC "But they're both girls"
    scene aynabath010
    with dissolve
    ayna "Snnc yum err"
    katriona "What? ahahah"
    scene aynabath011
    with dissolve
    ayna "Since you're so eager.."
    ayna "Why don't we get to more serious stuff??"
    katriona "So direct... I like it"
    scene aynabath012
    with dissolve
    ayna "Really?"
    ayna "Come here then"
    MC "Wow..."
    scene aynabath013
    with dissolve
    katriona "Oh... I will"
    ayna "What are you doing?"
    scene aynabath014
    with dissolve
    ayna "You naughty girl..."
    katriona "Don't you like it?"
    katriona "Let me show you more"
    scene aynabath015
    with dissolve
    ayna "Uhh"
    ayna "Yes..."

    ayna "Ah.... Wait..."
    scene aynabath016
    with dissolve
    ayna "Let's go to my room"
    MC "..."
    MC "Oh no..."
    scene aynabath017
    with dissolve
    katriona "Hey... What's wrong?"
    ayna "Come on.."
    scene aynabath017
    with dissolve
    MC "Is she looking at me?"
    MC "Crap...It can't be..."
    scene aynabath019
    with dissolve
    MC "I need to hide"
    katriona "Your room?"
    scene aynabath018
    with dissolve
    ayna "Yeah..."
    MC "Are they leaving?"
    scene aynabath020
    with dissolve
    MC "Did she see me?"
    MC "Probably not"
    MC "Or did she?"
    MC "I better leave anyway"
    $ renpy.end_replay()
label endbath:
    scene hall
    with dissolve
    MC "I'm back here"
    katarro "So... You're awake..."
    MC "What the..??"
    show k001
    with hpunch
    katarro "Sorry"
    katarro "I didn't mean to scare you"
    menu:
        "[abgreen]You didn't, don't worry":
            katarro "A tough one aren't you?"
            jump lessons
        "I... just wasn't expecting that":
            katarro "Ahaha, You'll get used to it"
            jump lessons
