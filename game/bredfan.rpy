#File 5
label bredfan:
    stop music
    play music "<loop 0.0>dark.mp3"
    scene v15mission039
    with dissolve
    Bredita "Are you ready?"
    lili "Yes!!"
    Bredita "Very well"
    scene v15mission040
    with dissolve
    lili "OH!!"
    Bredita "Come on my pretty girl!!"
    Bredita "Concentrate!!"
    lili "I...can't.... hold..."
    scene v15mission041
    with dissolve
    lili "Ahhhh"
    scene v15mission042
    with dissolve
    Bredita "Come on... get up"
    lili "Yes.. Mistress.."
    scene v15mission043
    with dissolve
    lili "I'm very sorry..."
    lili "I failed..."
    Bredita "No... You didn't, my pretty girl"
    Bredita "I'm quite satisfied with your progress"
    lili "But I..."
    scene v15mission044
    with dissolve
    Bredita "You are formidable"
    Bredita "But I have many years of training more than you"
    Bredita "You can't expect to beat me like this"
    Bredita "And... you have other qualities"
    lili "I... Understand"
    Bredita "You are beautiful my dear and you are the youngest college professor"
    Bredita "You also managed to get Suntako expelled from the College"
    Bredita "One of the most difficult foes I've ever faced"
    Bredita "And you didn’t even have to use magic"
    Bredita "Well... Not normal magic. Your own special magic."
    scene v15mission043
    with dissolve
    Bredita "So, you have to value yourself" #WhiskeyEdit
    lili "Yes..."
    scene v15mission044
    with dissolve
    Bredita "Confidence also gives you power"
    Bredita "The power to crush weaklings!!"
    Bredita "I'm very confident of my power"
    lili "But your are the most powerful mage there is..."
    Bredita "That might be true, still It wasn't always like that"
    Bredita "It was my power of will that allowed me to grow"
    Bredita "And fueled my search for real power"
    Bredita "Not the shit they teach you at the College..."
    scene v15mission045
    with dissolve
    Bredita "I'm gonna show you a spell"
    Bredita "When you master it"
    Bredita "The Elite will beg you to be one of them"
    lili "What do you mean?!"
    Bredita "That's my plan, you see. To get you on the Elite."
    lili "But they are so much more powerful than me..."
    Bredita "I'll show you real power..."
    scene v15mission046
    with dissolve
    Bredita "Just watch..."
    stop music fadeout 2.0

    if savedgirl == True:
        jump katsavinggirl
    else:
        jump katarrosavinggirl


label katsavinggirl:
    play music "<loop 0.0>epic.mp3" fadein 2.0
    scene v15mission032
    with dissolve
    MC "Here....We... are..."
    "You're exhausted after rushing all the way here"
    MC "I need to take her to Katriona"
    scene v15mission033a
    with dissolve
    "You enter her room as she is doing something..."
    scene v15mission033
    with dissolve
    katriona "What the hell happened?"
    "Panting, you answered-"
    MC "No... time...to explain..."
    MC "I need your... help"
    katriona "Sure"
    scene v15mission034
    with dissolve
    "Katriona started to cast a healing spell"
    play sound "sounds/spell01.mp3"
    scene v15mission035
    with dissolve
    scene v15mission036
    with dissolve
    scene v15mission037
    with dissolve
    katriona "..."
    katriona "Let me pick her up"
    scene v15mission038
    with dissolve
    katriona "I've done everything possible to save her"
    katriona "Now we need to wait"
    katriona "The rest of the battle will be within her own body..."
    katriona "You should speak with the Archmage"
    MC "And the girl?"
    katriona "Don't worry about her"
    katriona "I'll take it from here"
    MC "Thank you, Mistress Katriona"
    scene hall
    with dissolve
    MC "Let's look for the Archmage now"
    play music "<loop 0.0>ingame.mp3" fadein 4.0

    jump afterlogcabin

label katarrosavinggirl:
    play music "<loop 0.0>epic.mp3" fadein 2.0
    scene v15mission047
    with dissolve
    MC "There's a cabin..."
    MC "I should get in until the blizzard stops"
    "You enter the cabin"
    scene v15mission051
    with dissolve
    "As you get inside, you notice that it's not great"
    "But it better than outside..."
    "You also notice a strange book and a skull"
    MC "That seems out of place..."
    MC "What is this?"
    scene v15mission052
    with dissolve
    "You get closer...."
    MC "Sorcery of a Witch?"
    MC "Strange..."
    MC "Who left this here?"
    MC "I should read it while I wait for the blizzard to pass"
    scene v15mission053
    with dissolve
    MC "It's... like... it's calling me..."
    scene v15mission054
    with dissolve
    "You open the book and start reading"
    MC "This is a necromancy book"
    MC "It's filled with forbidden magic..."
    "You learn that Necromancy is a complementary magic"
    "It always needs to be combined with others"
    "Example: To summon a skeleton"
    "You'll need both summoning and necromancy"
    "To cast terror"
    "You need both Illusion and necromancy"
    "And so on..."
    "You read the whole book and eventually fall asleep"
    "You gained 1 necromancy points"
    $ Necropoints += 1
    scene black
    with dissolve
    nar "Good...."
    scene v15mission020
    with dissolve
    "You wake up and it's morning..."
    MC "Shit... I'm freezing..."
    "But you are in the middle of the forest"
    MC "Where the hell? Where is the cabin?"
    MC "Did I passed out?"
    MC "I need to return to the college before I freeze here"
    scene black
    with dissolve
    "You ran all you could until you reached the college walls"
    scene hall
    with dissolve
    MC "I'm... here... phew..."
    ayna "I'm glad you arrived"
    play music "<loop 0.0>ingame.mp3" fadein 4.0

    jump afterlogcabin

label afterlogcabin:

    scene v15mission048
    with dissolve
    ayna "I was worried about you"
    ayna "Maybe it was a mistake to send you on a mission so soon"
    MC "No! I'm fine..."
    MC "I'm ready for more"
    if savedgirl == True:
        ayna "I see that you managed to bring the girl"
        MC "Yes, Mistress Katriona is taking care of her"
        scene v15mission049
        with dissolve
        ayna "Poor girl..."
        ayna "I can't imagine what she has been through..."
        MC "I wonder what happened..."
        MC "She was all alone, did she run away from home?"
        ayna "Or maybe she was taken and escaped her captors..."
        scene v15mission050
        with dissolve
        ayna "Anyway, she is safe now"
        ayna "And it's thanks to you"
    else:
        MC "Yes... But I couldn't find the girl"
        ayna "I know, but Master Katarro found her"
        scene v15mission049
        with dissolve
        MC "What?"
        ayna "Poor girl..."
        ayna "He found her in the middle of the forest"
        ayna "Passed out and all alone"
        MC "I wonder what happened..."
        ayna "I have no idea..."
        scene v15mission050
        with dissolve
        ayna "Anyway, she is safe now"
        ayna "Luckily we have Katarro"
        ayna "One of the best sensitive mages there is"

    ayna "You should tell the farmer that his daughter is with us"
    amida "There you are!"
    scene v15mission056
    with dissolve
    amida "Where have you been?"
    amida "Oh... Please forgive me for interrupting you Archmage"
    ayna "No problem"
    ayna "I'll leave you two alone"
    ayna "[MC], don't forget to do what I asked"
    scene v15mission055
    with dissolve
    amida "She sent you on a mission?"
    MC "Yes... Let's talk about it in my room"
    amida "Okay let's go"
    label galleryScene7:
    scene v15mission057
    with dissolve
    amida "So tell me everything"
    MC "Well, she sent me to save a girl"
    MC "First I had to go through a portal she created..."
    "You explained the mission without going into much detail"
    MC "And then... Where is your robe?"
    amida "Back in storage.. Thank God"
    amida "So many years wearing that fucking robe..."
    amida "You like my dress? Now we can wear whatever we want! hehehe"
    scene v15mission058
    with dissolve
    MC "..."
    MC "Yes... you look great"
    scene v15mission059
    with dissolve
    amida "Muwah"
    scene v15mission057
    with dissolve
    amida "Thank you"
    MC "I bet you look even better without the dress..."
    scene v15mission060
    with dissolve
    amida "You're stupid..."
    amida "You want to find out don't you?"
    MC "Of course I want to, hehehe"
    scene v15mission061
    with dissolve
    amida "Really?"
    amida "So you want me to take off this dress?"
    MC "Yes...yes...yes..."
    scene v15mission062
    with dissolve
    amida "Like this?"
    MC "Oh yes...."
    amida "What are you waiting for?"
    scene v15mission063
    with dissolve
    amida "Come here"
    MC "You don't have to ask me twice"
    scene v15mission064
    with dissolve
    amida "So... do I look better without the dress?"
    MC "Are you kidding?"
    MC "So much better...."
    amida "Can you prove it to me?"
    MC "I prefer actions over words"
    scene v15mission065
    with dissolve
    MC "Kissing you should do the trick"
    MC "Such a pretty face"
    amida "And my kiss?"
    scene v15mission066
    with dissolve
    amida "Muwah"
    scene v15mission064
    with dissolve
    amida "What else do you want to try?"
    MC "How about these?"
    scene v15mission067
    with dissolve
    amida "Hmmm"
    MC "So soft... Yet so firm..."
    MC "Look at what you caused..."
    scene v15mission068
    with dissolve
    amida "It doesn't seem to take much from me..."
    MC "But it's still your fault..."
    MC "You should be the one to take care of it.."
    amida "Ahahh"
    scene v15mission069
    with dissolve
    "Mida took hold of your cock"
    "And began to stroke it"
    amida "Do you like how this feels?"
    "Before you could answer"
    scene v15mission070
    with dissolve
    MC "Oh..."
    amida "Hmmmm"
    scene v15mission071
    with dissolve
    "From her new position you could see the amazing curve of her butt"
    MC "Don't stop now baby"
    scene v15mission072
    with dissolve
    "She gave a kiss on the tip of your cock..."
    MC "Oh....yes..."
    scene v15mission068
    with dissolve
    amida "Lie on the bed, please"
    MC "Sure baby"
    scene v15mission073
    with dissolve
    amida "I'm going to make you cum"
    amida "Do you want to cum?"
    MC "I..."
    scene v15mission074
    with dissolve
    "She kept stroking so fast and hard"
    "You do your best to hold on..."
    scene v15mission073
    with dissolve
    MC "I... can't... hold..."
    amida "Cum for me baby!!"
    "Those words were the last straw"
    show shot
    with hpunch
    scene v15mission075
    with dissolve
    MC "AHH!!"
    MC "Damn...ahh"
    scene v15mission076
    with dissolve
    "Her face is completely covered with your cum"
    amida "Ah... Look at this mess..."
    MC "I..."
    $ renpy.end_replay()
    scene black
    with dissolve
    scene a013
    with dissolve
    ayna "How is she?"
    katriona "I think she's going to be fine"
    katriona "We should let her rest"
    ayna "Yes... I've sent [MC] to inform her father"
    ayna "I bet he will be happy to know she's fine"
    scene meanwhile
    with dissolve
    scene v3g092
    with dissolve
    amida "Aren't you forgetting something?"
    MC "What?"
    amida "What the Archmage asked you to do?"
    MC "Crap, you're right..."
    MC "I should go... It shouldn't take too long, baby"
    scene v3g093
    with dissolve
    amida "Go then... We'll talk later"
    scene snowplain
    with dissolve
    "It took you a couple of hours"
    "But you reached the farm"
    scene farmmission1
    with dissolve
    MC "Here we are again..."
    MC "Now where is the old man?"
    oldman "You're back!!"
    scene v15mission019
    with dissolve
    oldman "You found her?"
    oldman "Where is she?"
    MC "Don't worry"
    MC "She's with us at the College"
    scene v15mission017
    with dissolve
    "The man expression changed"
    oldman "What??"
    oldman "You took her to the College?"
    oldman "What did she tell you?!"
    oldman "What??!"
    MC "Hey calm down!"
    MC "She is resting, we haven't spoken with her yet"
    oldman "You lie!!"
    scene v15mission077
    with dissolve
    "The old man gets on his knees"
    oldman "You lie!!"
    oldman "You're a liar!!"
    MC "What the fuck??"
    oldman "Ahhh!"
    scene v15mission078
    with dissolve
    scene v15mission079
    with dissolve
    scene v15mission080
    with dissolve
    oldman "You will pay for lying"
    MC "What the...?"
    oldman "If I can't have her"
    oldman "Then I'll take you!!"
    scene v15mission081
    with dissolve
    oldman "I will use my magic"
    MC "Bring it!"
    scene v15mission082
    with dissolve
    MC "I'll kick your ass!"
    scene v15mission083
    with dissolve
    oldman "Wait wait... I'm kidding..."
    oldman "You are a Mage... A powerful one..."
    "His eyes dart over your shoulder"
    oldman "Hey guys! Grab him!"
    "As you are turning around to see who he was talking to"
    scene v15mission084
    with dissolve
    "He starts to run away..."
    oldman "Shit!"
    oldman "...."
    scene farmmission1
    with dissolve
    MC "What the hell just happened?"
    MC "What was that?"


    jump v018
