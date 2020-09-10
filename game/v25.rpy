
init:
    $ lili_affection = 0


label v25:




    hide screen points_all

    scene black
    with dissolve
    play music "<loop 0.0>ingame.mp3"
    yayna "{i}Giggle{/i}... What are you doing"
    scene v25151
    with dissolve
    yBredita "What? Aren't you enjoying it?"
    yayna "You know me... of course I do"
    scene v25152
    with dissolve
    yBredita "What about this?"
    yayna "I know what you're planning"
    yBredita "Yeah? Then you'll love this spell of mine..."
    scene v25153
    with dissolve
    yayna "You dirty girl... Making my robes disappear like that"
    yBredita "What are you gonna do about it?"
    scene v25154
    with dissolve
    yayna "This!"
    yBredita "Hmm... Interesting... And what else?"
    scene v25155
    with dissolve
    yayna "What else do you want?"
    yBredita "I can think of some things"
    scene v25156
    with dissolve
    yayna "Mhmmm"
    yBredita "Mhmhmm"
    scene v25157
    with dissolve
    yBredita "Come with me...."
    yayna "{i}Giggle{/i}"
    scene v25158
    with dissolve
    yBredita "You know what I want you to do?"
    yayna "Hmmm let me guess... Want me to find something in there?"
    yBredita "Ahaha sure... sure, come take a look"
    scene v25159
    with dissolve
    yBredita "So did you find anything?"
    yayna "Maybe I should do something else besides looking?"
    scene v25160
    with dissolve
    yBredita "Ahhh... Yes!! That's it!!"
    yayna "Mhhmm"
    scene v25161
    with dissolve
    yBredita "Yes my love keep going"
    yayna "Slurp...Slurp...Lick... Lick"
    yayna "Turn around for me, please"
    scene v25162
    with dissolve
    yBredita "Ahhhh.... Oh... Yes.."
    yBredita "Give me a kiss"
    scene v25163
    with dissolve
    yayna "Mhhhmm"
    yBredita "Mmmmm, Your turn to lie down"
    yayna "Hmm, I like where this is going"
    scene v25164
    with dissolve
    yBredita "You are so pretty...."
    yayna "Just pretty? Aren't you... Wha..."
    yayna "Did you feel that?!!"
    scene v25165
    with dissolve
    yBredita "Yes... It's... Amazing... So much power..."
    yayna "We need to talk with Archmage Suntako"
    yBredita "Yeah... Him... I don't like him..."
    yBredita "He is afraid of losing his position to you"
    $ renpy.end_replay()
    scene black
    with dissolve

    $ yisnalove = 0
    $ yisnacorr = 0

    $ lililove = 0
    $ lilicorr = 0

    $ fannaylove = 0
    $ fannaycorr = 0

    $ karelialove = 0
    $ kareliacorr = 0

    if impressed == "lili":
        $ lililove += 1
    if liliseen == True:
        $ lililove +=1
    if lili_affection == 1:
        $ lililove +=1

    if savedgirl == True:
        $ karelialove += 3
    if farmgirlv2 == 2:
        $ karelialove += 1

    if midacorr >= 2:
        $ fannaylove += 1

    if yisnnaafect >= 1:
        $ yisnalove += 1


    $ companion = 0



    if Points >=2:
        $ aynalove = 1
    else:
        $ aynalove = 0

    $ aynacorr = 0

    if Points <=-2:
        $ breditalove = 1
    else:
        $ breditalove = 0

    $ breditacorr = 0

    $ katrionalove = 0
    $ katrionacorr = 0

    $ enainialove = 0
    $ enainiacorr = 0

    $ isabellalove = 0
    $ isabellacorr = 0

    $ silvanalove = 0
    $ silvanacorr = 0

    $ zegladarlove = 0
    $ zegladarcorr = 0

    $ gisellelove = 0
    $ gisellecorr = 0

    $ hannalove = 0
    $ hannacorr = 0

    $ jessicalove = 0
    $ jessicacorr = 0

    $ enemytypeis = 0
    $ enemyname = 0
    $ enemy = 0

    show skillbarmap

    "Time to talk about new stuff. As you can see, on the top right there is a heart"
    "If you click it, it will show you ' The girls stats Love/Corruption '"
    "Just click 'Close Stats' anytime you want to return back to where you were"
    hide skillbarmap

    show screen points_allhh
    "You can try it now, go ahead click it"

    "Since the game is in development, you now have the chance to change your alignment"

    "That, will allow you to experiment the other paths on the game without a start over"
    "I warn you though, changing now may cause some plotholes"
    "You can just keep it like it is for the first time, then try different choices"
    "So what do you want to do?"

    menu:
        "Change to Evil (Points = -5)":
            $ Points = -5
            jump v25a
        "Change to Neutral (Points = 0)":
            $ Points = 0
            jump v25a
        "Change to Good (Points = 5)":
            $ Points = 5
            jump v25a
        "Keep my alignment the same":
            jump v25a

label v25a:

    if Points >= 4:
        scene black
        with dissolve
        jump v25good
    elif Points <= -4:
        scene black
        with dissolve
        jump v25evil
    else:
        scene black
        with dissolve
        jump v25neutral



label aynaroomv001:
    MC "It's locked"
    call screen collegeblue

label v2exitroom001:
    MC "that's where I am..."
    call screen collegeblue

label courtyardv001:
    MC "I have nothing to do there"
    call screen collegeblue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
