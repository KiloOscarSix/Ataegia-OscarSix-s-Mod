label v026:
    scene meanwhile
    with dissolve
    scene meanwhile
    with dissolve
    scene v26a001
    with dissolve
    chang "Now my dear Yumiko, how does it feel to be a married woman?"
    yumiko "Oh my love, it's a dream come true. I'm so happy"
    scene v26a002
    with dissolve
    chang "You're so pretty, like a porcelain doll"
    yumiko "Does a porcelain doll look like this?"
    scene v26a003
    with dissolve
    chang "Oh... My mistake... You have just surpassed any possible comparison"
    yumiko "That's better, what do you plan to do about this?"
    yumiko "Do you plan to undress or what? Let me help you"
    scene v26a004
    with dissolve
    chang "I like where this is going, but isn't your father going to be mad?"
    yumiko "Eheheh... You're so funny, for the first time we don't have to worry about him"
    yumiko "Unlike the other times, we are allowed to do this. Still he's not the boss of me"
    chang "Ahaha, well then!"
    scene v26a005
    with dissolve
    chang "What do you plan to do?"
    yumiko "I have a few ideas..."
    scene v26a006
    with dissolve
    yumiko "How is my cute friend here? Is he ready for a good night?"
    chang "Just by looking at you my dear"
    yumiko "Lie down!"
    scene v26a007
    with dissolve
    yumiko "That's better, you know what's next?"
    chang "I can think of some..."
    scene v26a008
    with dissolve
    chang "Hmmmm..... Ah...."
    yumiko "Lick...Suck..."
    scene v26a007
    with dissolve
    yumiko "Was this what you were thinking? Eheheh"
    chang "Hum hum... Turn around I want to give you something"
    yumiko "Really? What?"
    scene v26a009
    with dissolve
    yumiko "Ahhh... That's great..."
    scene v26a010


    show v26achang idle

    yumiko "Ahhh yes... Keep going..."
    chang "Ah... this is great my dear"
    chang "I could do this everyday you know?"
    yumiko "Ah... Ah...Yes... Give me more"
    scene v26a011
    with dissolve
    chang "Ah... I'm...About to..."
    yumiko "Wait not yet... I need..."


    scene v26a012
    show shot
    with hpunch
    scene v26a012
    with dissolve
    chang "Ahhhhhh!! Fuck yeah...."
    chang "That was great"
    yumiko "Yeah... It was... Guess I'll try to sleep now"
    $ renpy.end_replay()
    scene v26a013
    with dissolve
    chang "Do you have news for me?"
    suntako "Yes, I'm ready when you are"
    scene v26a014
    with dissolve
    chang "That's great news. Soon I'll be a King and so will you my friend"
    suntako "What about the woman?"
    chang "Don't worry about her, she is completely in love with me"
    suntako "Does she know about your plans?"
    chang "Of course not, but when I become King she becomes irrelevant"
    chang "Do you want to keep her when I'm done with her? ahahah"
    scene v26a013
    with dissolve
    suntako "Let's just stick to the plan, I'll start tomorow"
    scene v26a015
    with dissolve
    chang "Very well..."
    if enemy == "n1":
        jump v026neutral
    elif enemy == "e1":
        jump v026evil
    else:
        jump v026good

    label slayerbathv26:
        scene meanwhile
        with dissolve
        scene meanwhile
        with dissolve
        scene v26a016
        with dissolve
        tiberius "My dear Aelia, as soon as I become the Emperor of all Ataegina"
        tiberius "That won't be a problem anymore"
        aelia "How long do you think it will take, to take care of the Orcs and the Nords?"
        scene v26a017
        with dissolve
        tiberius "Maybe a couple of months if it all goes to plan"
        tiberius "But the Orcs are not like any other race, they will never become slaves to anyone"
        aelia "Don't Orcs use slaves? I mean like war prisoners?"
        tiberius "Yes... If the Orc leader can prove he is stronger in combat than anyone else"
        aelia "So they act like animals? The strongest is the leader? Primitive creatures..."
        tiberius "That's good though"
        tiberius "They don't know that real power is intelligence and wisdom"
        tiberius "True power is to know when you can't win, and when to retreat."
        tiberius "True power is to know your enemy's weakness, and strike there"
        tiberius "True power is..."
        pacu "Excuse me my lord..."
        scene v26a018
        with dissolve
        tiberius "Yes Pacuvianus? I hope you have a motive for bothering me"
        pacu "Yes my lord..."
        pacu "I have news about our expeditions to Highgard, Tanzani and the Orc lands"
        tiberius "Very well, tell me about them"
        pacu "We started to bring slaves from the north and from Tanzani"
        pacu "Our forces are clearly more powerful, and they know it..."
        tiberius "Very well and the Orcs?"
        pacu "Well... They... "
        tiberius "Speak!"
        pacu "They won't allow themselves to be captured... They fight to their last breath..."
        tiberius "As expected... Aelia my dear, we need to finish our bath..."
        aelia "I understand my lord"
        scene v26a019
        with dissolve
        tiberius "Pacuvianus we will use that Orc pride against them"
        tiberius "Reunite my generals, I'll speak with them tonight"
        scene v26a020
        with dissolve
        pacu "Very well my lord, I shall assemble them at once"
        tiberius "Brutus!!"
        scene v26a021
        with dissolve
        brutus "Yes, my lord?"
        tiberius "How do you feel about brawling an Orc?"
        brutus "Happy... No man is a challenge to me... Maybe an Orc will be"
        tiberius "I knew you would like the idea..."
        scene v26a022
        with dissolve
        tiberius "We will leave tomorrow morning to the Orc lands"
        tiberius "Be ready to go..."
        brutus "Yes my lord!"
        scene v26a023
        with dissolve
        aelia "Psst... Hey Brutus before you leave in the morning"
        aelia "Meet me in my room tonight..."
        aelia "Tiberius will spend the whole night with his generals"
        aelia "And I need a real man in my bed..."
        brutus "Hmm yes, my lady..."
        scene black
        with dissolve

        if wheretoafterslayerbath == "neutral":

            jump v026neutralpart2

        elif wheretoafterslayerbath == "Evil":
            jump v026evilpart2
        else:

            jump v026goodpart2

label devilsv3all:
    scene meanwhile
    with dissolve
    scene v3all001
    with dissolve
    pride "So why have you called us here Lust?"
    lust "There are important matters to discuss"
    scene v3all002
    with dissolve
    greed "What could be so important that I care?"
    lust "Can any of you sense Wrath anywhere?"
    scene v3all001
    with dissolve
    pride "I can't say I do..."
    greed "..."
    lust "He is gone, Andrath has no ruler right now..."
    scene v3all002
    with dissolve
    greed "Hmm... Interesting... Care to explain what it has to do with me?"
    greed "Wrath and his 4th hell can fuck themselves for all I care"
    scene v3all003
    with dissolve
    greed "I'm out of here, you idiots!"
    scene v3all004
    with dissolve
    pride "What is the real reason for calling us Lust?"
    lust "I said it already... Wrath is gone. Nobody is ruling the 4th hell"
    pride "And...?"
    lust "Aren't you curious to know what happened to him?"
    lust "He is not the strongest of us, but he's not the weakest either"
    lust "If something or someone killed him, we might be the next target"
    pride "I would like to see them try!"
    lust "What if the Devil Siblings had something to do with it?"
    pride "You mean Goggos and Zegladar?"
    scene v3all005
    with dissolve
    lust "Yes..."
    pride "Why would they do it?"
    lust "Why would any of us do it? For power of course"
    scene v3all006
    with dissolve
    lust "We all want to see each other dead"
    pride "Then why are you telling me this?"
    lust "Because I know you are different, you are Pride!"
    lust "You are the only devil or demon that wouldn't break a promise"
    lust "You wouldn't attack an opponent from behind..."
    lust "And of course, you are more powerful than any of the others"
    pride "Then why did you call Greed here?"
    lust "Because he is Greed... I know he will try to get the 4th hell all to himself"
    lust "Then what do you think the others will assume?"
    pride "That he is behind Wrath's disappearance..."
    lust "Yes... Giving us time to look for the real culprits"
    scene v3all005
    with dissolve
    pride "Hmm... Why should I trust you?"
    lust "My lovely Pride... You shouldn't, but you must..."
    lust "You know I like you, don't you?"
    lust "You know that if we have to face Goggos and Zegladar"
    lust "The only chance we have is if we stay together"
    scene v3all006
    with dissolve
    lust "And I know you like me, don't you?"
    pride "You make valid points... So what's the plan?"
    scene v3all007
    with dissolve
    lust "I knew you wouldn't let me down"
    lust "We wait for Greed to make his move, then we'll begin our plan"

    if wheretoafterslayerbath == "neutral":

        jump v031neutral

    elif wheretoafterslayerbath == "Evil":
        jump v031evil
    else:

        jump v031good
