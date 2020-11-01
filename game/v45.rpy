
init:
    $ v45check = 0
    $ manasteal = 0
    $ manaburnlvl1 = 0
    $ spellblizzard = 0
    $ mordarth = 0
    $ shadowwall = 0
    $ forcechoke = 0
    $ smite = 0
    $ multipath = 0


label v45start:
    $ v45check = 1
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    scene meanwhile
    with dissolve
    scene v45001
    with dissolve
    cal "I wonder what happened to you?"
    cal "You were one of the Slayers high ranked officers..."
    cal "The Queen's right hand... It doesn't makes sense"
    scene v45002
    with dissolve
    hanna "Calessa, I did it! I found him"
    cal "What did he say?"
    hanna "He said he would be here soon"
    scene v45003
    with dissolve
    mvoice "And here am I"
    cal "Oh..."
    hanna "Thank you so much for coming"
    scene v45004
    with dissolve
    bairn "So it's her..."
    cal "We found her near the burning church, right after what happened"
    hanna "We need to be fast..."
    hanna "I don't know if we are safe from the battle here"
    bairn "We're not... Let's see what I can do for her"
    scene v45005
    with dissolve
    bairn "Hmmm... I see..."
    cal "Can you help her?"
    bairn "Maybe... But do I want to?"
    hanna "What do you mean?"
    play sound "sounds/screamwoman.wav"
    cal "Ahhhh... They're here!"
    scene v45006
    with dissolve
    demon "Hmmm.... Food..."
    hanna "Oh fuck!"
    cal "We don't stand a chance, Run!!"
    scene v45007
    with dissolve
    incubus "Oh... Look at this... two hotties and an old man..."
    incubus "Should we kill him and have some fun?"
    incubus2 "No...  Lust will be angry if we don't just grab her little pet and get back"
    incubus2 "Let the Glutton eat the others..."
    bairn "It would be in your best interest if you 3 were to leave this room immediately"
    bairn "I won't let you touch these good people.... or her"
    incubus "And exactly who are you to stop us old man?"
    scene v45008
    with dissolve
    play sound "sounds/summon.ogg"
    incubus "Ahhhh"
    incubus2 "What the hell?!"
    demon "Uhhh"
    scene v45009
    with dissolve
    cerea "I am Cerea of Pride..."
    incubus2 "The heretic, pah, Lust will reward us even more if we bring her back!"
    incubus2 "Grab her! I'll go for Carilielle!"
    scene v45010
    with dissolve
    cerea "Stop right there you two!"
    scene v45010s
    with dissolve
    incubus "MY HEAD!!! AHHH"
    demon "AHHHRGG!"
    incubus2 "I've got you bitch!"
    scene v45011
    with dissolve
    cari "Who's got whom?"
    cari "And... What is going on here?"
    incubus2 "Ahhh... {i} Cough Cough"
    cari "I'm in need of energy... Let's see how tasty you are..."
    scene v45012
    with dissolve
    incubus2 "{i} Screams of extreme pain"
    cari "Yes... Now who's next?"
    scene v45013
    with dissolve
    cari "What is going on here? Cerea? You..."
    cari "I will..."
    scene v45014
    with dissolve
    cal "Thank you for saving us..."
    hanna "But... Who are you?"
    cari "What humans... who are they?"
    cerea "They are the people who rescued you from the church"
    cerea "You should thank them by not being a bitch"
    cari "I... I..."
    scene v45015
    with dissolve
    cal "Did she..."
    cerea "Faint, yes"
    cerea "I'm sorry you had to see this..."
    cerea "I had no intention of ever revealing my self to you or your friend Calessa"
    cal "What are you?"
    cerea "A demon. So is the girl in the bed, so were the things we just killed"
    cerea "But you have nothing to fear from me, I'm no friend of their kind anymore"
    scene v45016
    with dissolve
    cal "Are we supposed to trust you?"
    cerea "As much as you can anyone."
    cerea "But we've had a rather cordial relationship while I was hiding as Bairn"
    cerea "So I choose to continue that"
    hanna "What exactly is going on?"
    hanna "The city is a warzone"
    hanna "The soldiers are in a panic, demons and mages are fighting soldiers in the street"
    cal "Also there are rumors that the Emperor is dead, killed by the Empress herself"
    cal "That she tore him apart, and killed Captain Brutus as well"
    cerea "Right, then there's no point in hiding the truth."
    cerea "The Empress is actually a Devil Bitch named Lust"
    cerea "Devils are more powerful than demons, they control us more or less"
    cerea "This mark on my face says I've been ostracized, I'm a traitor in their eyes"
    scene v45015
    with dissolve
    cerea "Carielle over there has been under Lust's control for a long time."
    cerea "She seems to be free of it now"
    cerea "The black mages and the demons were using the Slayers for their own ends..."
    cerea "Seems Lust no longer has need of them so she's cleaning house"
    scene v45016
    with dissolve
    hanna "So what now?  What do we do?"
    cal "How will we get out of the city?"
    cerea "I can create a portal to get you out of the city, the two of you will be safe there"
    cal "But I can't just abandon my people. They need to escape as well."
    cerea "Fine, I'll get you and your people out as well..."
    cerea "But after that I have my own matters to attend to, you'll be on your own"
    scene v45015
    with dissolve
    hanna "What about her?"
    cerea "You saw, she's a demon as well...."
    cerea "She may not be a slave anymore but I can't say that she'll be friendly either"
    cerea "If I were you, I'd leave her here and flee"
    scene v45016
    with dissolve
    cal "I can't do that, she needs our help.  And she did help to save us.."
    cerea "She helped herself, helping you was just a side effect"
    cal "All the same, I will not leave her."
    cal "I've rescued plenty of girls off the street, she's no different"
    cerea "It's your choice, I can't stop you.  Gather your people so we can get going"
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene portalroom
    with dissolve
    MC "I need to find the Archmage and tell her what happened"
    MC "I should look around in the throne room"
    scene v45045
    with dissolve
    "You reach the throne room and it's completely empty"
    MC "She's not here..."
    MC "I should look for her around the college"
    jump afterorcv39

label v45library:
    scene v45033
    with dissolve
    "You enter the library and you see Yisnna sitting surrounded by books"
    MC "Is she working on the books I gave her?"
    "You get closer to her"
    scene v45034
    with dissolve
    yisnna "Hello [MC] good to see you!"
    yisnna "I have great news for you"
    MC "You do?"
    scene v45035
    with dissolve
    yisnna "Yes! Take a seat"
    MC "Thanks"
    scene v45036
    with dissolve
    MC "So... How's that translation going?"
    yisnna "Already complete"
    MC "Really?"
    yisnna "Yes, see that book there to your right?"
    scene v45037
    with dissolve
    MC "This one?"
    yisnna "I've compiled the translations there"
    MC "Great! I should go and study them as soon as possible"
    yisnna "Hold on... I have something else for you"
    scene v45038
    with dissolve
    "You see her moving towards the shelves"
    yisnna "Now... Where is...."
    yisnna "Ah.. Here"
    scene v45039
    with dissolve
    yisnna "This is also for you..."
    yisnna "A 'required reading'"
    scene v45040
    with dissolve
    MC "What's this? Beginner's magic?"
    "Portals and you, a beginner's guide"
    "How to summon clothes and other everyday essentials"
    "Spells useful to get out of trouble without fighting"
    MC "..."
    scene v45041
    with dissolve
    yisnna "The Archmage wanted me to give you the first part"
    yisnna "So you can learn how to tune the portal here at the College"
    MC "Hmmm..."
    yisnna "Katriona recommended the second one, she said you'd know why"
    MC "That little..."
    scene v45042
    with dissolve
    yisnna "The third one is something I thought you might be interested in"
    yisnna "Since you seem to get into trouble a lot"
    MC "Thanks a lot Yisnna! I'll go to my room to study them now"
    scene v45043
    with dissolve
    yisnna "You're welcome, I'm always glad to help with books"
    yisnna "Have fun with that, I know I had"
    yisnna "I'll rest a bit, it's late, Bye"
    scene v45044
    with dissolve
    MC "Bye Yisnna"
    "It's very late and you go to your room... With your new books"
    scene v45000
    with dissolve
    MC "Ok... Time to get out of these clothes and lie for a bit"
    MC "I need to see what new spells we have here"
    scene v45095
    with dissolve
    "You lie on the bed with the translated spellbook"
    MC "So what's this first one...."
    MC "Mana steal... Hmm... Interesting"
    scene v45096
    with dissolve
    "Mana steal, level 5 Alteration magic"
    "Costs 5 MP, steals 20 percent of you max MP from enemy"
    $ manasteal = 1
    "{color=#f00}{b}You learn Mana Steal{/b}{/color}"
    MC "What else do we have here?"
    if lvl1v42altspell >= 1:
        scene v45095
        with dissolve
        MC "Mana burn... This is a level 1 alteration spell"
        scene v45096
        with dissolve
        "Sacrifice a fourth of your current MP total and deal 2 damage for each point spent"
        "Your alteration points increase the total damage done"
        $ manaburnlvl1 = 1
        "{color=#f00}{b}You learn Mana Burn{/b}{/color}"
        MC "What else do we have here?"
    if lvl5v42desspell >= 1:
        scene v45098
        with dissolve
        MC "Blizzard... This is a level 5 Battlemagic spell"
        scene v45096
        with dissolve
        "Causes a snow and ice blizzard that blinds your opponent and causes damage"
        "Blizzard may freeze your opponent"
        $ spellblizzard = 1
        "{color=#f00}{b}You learn Blizzard{/b}{/color}"
        MC "What else do we have here?"
    if lvl5v42sumspell >= 1:
        scene v45098
        with dissolve
        MC "Mordarth... This is a level 5 Summoning spell"
        MC "Yisnna put a note here... apparently his name literally translates to 'bite you' huh..."
        scene v45097
        with dissolve
        "Summons a Draconic Hound that acts like a companion for sometime"
        $ mordarth = 1
        "{color=#f00}{b}You learn Draconic Hound{/b}{/color}"
        MC "What else do we have here?"
    if lvl5v42illspell >= 1:
        scene v45095
        with dissolve
        MC "Shadow Wall... This is a level 5 Illusion spell"
        scene v45096
        with dissolve
        "Casting Shadow Wall may cause fear on your opponent preventing it's attacks"
        $ shadowwall = 1
        "{color=#f00}{b}You learn Shadow Wall{/b}{/color}"
        MC "What else do we have here?"
    if lvl5v42mysspell >= 1:
        scene v45095
        with dissolve
        MC "Force Choke... This is a level 5 Mysticism spell"
        scene v45097
        with dissolve
        "Casting Force Choke prevents your opponent attacks and causes damage"
        "Force Choke may stun your opponent"
        $ forcechoke = 1
        "{color=#f00}{b}You learn Force Choke{/b}{/color}"
        MC "What else do we have here?"
    if lvl5v42heaspell >= 1:
        scene v45095
        with dissolve
        MC "Smite... This is a level 5 healing spell"
        scene v45097
        with dissolve
        "Smite causes direct damage to your opponent"
        "Smite causes extra damage to undead, vampires, demons etc..."
        $ smite = 1
        "{color=#f00}{b}You learn Smite{/b}{/color}"
        MC "What else do we have here?"
    MC "The beginnner's stuff, where should I start?"
    MC "What's this spell? The Eye of the Beholder?"
    MC "The Eye of the Beholder allows you to see something you must see or want to see"
    scene v45098a
    with dissolve
    "You start to feel a bit dizzy..."
    scene v45098ak1
    with dissolve
    scene v45098ak2
    with dissolve
    scene v45098ak3
    with dissolve
    karelia "Help me [MC], please help me!"
    MC "Karelia? I'll..."
    play sound "sounds/knock.mp3"
    ryo "[MC]?"
    scene v45098a
    with dissolve
    MC "Hmmm...?"
    play sound "sounds/knock.mp3"
    ryo "[MC]? I'm going in"
    scene v39085
    with dissolve
    MC "Ryo?"
    ryo "Are you ok? I was calling you but you just keep talking alone"
    MC "I'm ok... I think I need to go..."
    scene v39086
    with dissolve
    ryo "Go where?"
    MC "I... a girl I know...Karelia... "
    MC "I think she needs help, I have to go check"
    ryo "What? Nevermind, I'll go with you"
    ryo "I don't know if you are hallucinating or if that's true"
    ryo "Either way I will go with you"
    MC "Right... Let me get dressed and we'll go"
    scene v38164
    with dissolve
    "You and Ryo are in the College courtyard"
    ryo "So... What's this about this Karelia?"
    MC "I can't explain... I was learning a spell and..."
    scene v38165
    with dissolve
    ryo "And you felt she needs help?"
    MC "Yes... And I'm pretty sure it's urgent..."
    ryo "What are we waiting for then? Let's go!"
    MC "Right, it's still a bit far and night is here"
    scene v38166
    with dissolve
    ryo "And... you think I'm afraid of the dark?"
    ryo "At age 10 I was training night stealth on moonless nights"
    ryo "Unless you are the one afraid?"
    MC "What? Don't be foolish. Let's get going!"
    ryo "I'll follow you"
    scene v45085
    with dissolve
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    "You and Ryo travel to the farm where you met Karelia the last time"
    ryo "Is this the place?"
    MC "Yes... It is..."
    MC "But I see nothing wrong..."
    scene v45086
    with dissolve
    ryo "Don't move... I can feel we're being watched..."
    ryo "You there! I can see you, come out now"
    scene v45087
    with dissolve
    karelia "Please don't hurt me... I have nothing of value here..."
    karelia "I... [MC]??!!"
    scene v45088
    with dissolve
    karelia "Is that you?"
    MC "Hi Karelia"
    scene v45089
    with dissolve
    "The girl runs towards you crying"
    karelia "They killed him.... They killed him!!!"
    karelia "I was so scared...."
    MC "Please calm down..."
    MC "What happened?"
    scene v45090
    with dissolve
    karelia "There was this mage... He killed my father..."
    karelia "He killed my father right here... I saw him..."
    scene v45091
    with dissolve
    karelia "And I was too scared to do anything... I kept hidding.."
    karelia "I should have helped him... I..."
    scene v45092
    with dissolve
    ryo "And what would that do?"
    ryo "You would probably be killed too"
    karelia "He even took my fathers dead body..."
    scene v45093
    with dissolve
    MC "He did?! And did you see where he went?"
    karelia "I saw him going in the village graveyard's direction"
    MC "A fucking Necromancer..."
    scene v45092
    with dissolve
    ryo "You stay here inside the house, we'll be back in no time"
    karelia "But..."
    ryo "We can't let other people have the same fate your father had right?"
    karelia "Yes..."
    ryo "We'll be back in no time"
    scene v45093
    with dissolve
    MC "We will, don't worry"
    MC "But if we do not return until morning run to the college"
    karelia "But..."
    scene v45092
    with dissolve
    ryo "But we will, don't worry"
    scene v45093
    with dissolve
    ryo "Let's go [MC]"
    MC "Yes"
    scene v45066
    with dissolve
    "You and Ryo reach the graveyard and there's something going on"
    ryo "Look at that... Undead... I hate undead"
    MC "There are at least 2 zombies and 3 skeletons"
    scene v45067
    with dissolve
    ryo "And a mage..."
    MC "Indeed... and he's casting something... Powerful"
    MC "Wait... is that zombie..."
    scene v45068
    with dissolve
    MC ".... Looking at us..."
    ryo "Shit... Now we have to be fast"
    scene v45069
    with dissolve
    ryo "Let's help them reach their final rest"
    MC "I'm right here"
    scene v45070
    with dissolve

    $ companion = 1
    $ companion_name = "Ryo"
    $ enemy = "v45undead"
    jump combat

label v45killedunded:
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    hide screen companions
    hide screen MC_bars
    hide screen hpbar
    scene v45071
    with dissolve
    MC "They are... Well... dead... again..."
    ryo "No time to celebrate, look!"
    necromancer "How dare you!!??"
    ryo "You'll pay for your actions... Using dead people to fight for you..."
    ryo "You make me sick... I hate Necromancers"
    necromancer "Ahahah.... You are too late to stop me"
    scene v45072
    with dissolve
    necromancer "Ahahah..."
    necromancer "See my true power!"
    MC "Look out!! I sense a lot of magic power coming from him"
    scene v45073
    with dissolve
    necromancer "Now my child... Kill them... For now..."
    ryo "Did he just merge all the dead together?"
    MC "Looks like it... That thing is huge..."
    scene v45074
    with dissolve
    MC "And it's coming for us..."
    $ companion = 1
    $ companion_name = "Ryo"
    $ enemy = "v45giantundead"
    jump combat

label v45killedundedgiant:
    $ companion = 0
    stop music
    play music "<loop 0.0>huntercamp.mp3"
    hide screen companions
    hide screen MC_bars
    hide screen hpbar
    scene v45075
    with dissolve
    necromancer "NOOOO!!! What??? HOW!!!!??"
    ryo "And you are next!"
    scene v45076
    with dissolve
    necromancer "Who are you? Why did you come here?"
    MC "You should know that someone would come for you eventually"
    ryo "Have you no honor? Using the dead... Using defenseless... I..."
    scene v45077
    with dissolve
    necromancer "Fuck I'm out of here"
    MC "..."
    scene v45078
    with dissolve
    "Before you could do anything you see Ryo move like a flash"
    ryo "Oh no you don't..."
    necromancer "What the..."
    scene v45079
    with dissolve
    necromancer "AHHHHHH!!!"
    MC "Wow..."
    ryo "..."
    scene v45080
    with dissolve
    ryo "You won't be messing with any more dead bodies"
    "You are both impressed and scared about what you just witnessed"
    MC "That was... Impressive..."
    scene v45081
    with dissolve
    ryo "We need to burn the corpses... All of them"
    MC "What?"
    ryo "So they are not revived and used again"
    scene v45082
    with dissolve
    ryo "There are two things I don't understand about your culture"
    ryo "Why do you bury the bodies, and why some mages play with the dead?"
    ryo "I mean, number two would be a lot harder if number one wasn't true"
    scene v45081
    with dissolve
    MC "You don't bury the dead?"
    ryo "No, we cremate them. A body without it's soul is nothing but a vessel"
    ryo "An empty vessel... Waiting to be filled"
    MC "Yeah... I get what you mean"
    scene v45082
    with dissolve
    ryo "So should I look for firewood? Or do you have a spell for it"
    MC "Yeah I can do it"
    scene v45083
    with dissolve
    "You and Ryo grab the dead bodies and set them to flames"
    ryo "It is one of the greatest dishonors to be used like this..."
    MC "You mean your body being used after death?"
    scene v45084
    with dissolve
    ryo "Yes... Nobody deserves that... Should we go?"
    MC "Sure"
    ryo "Your friend Karelia will be happy to see you"
    MC "Yes... I mean... Poor girl"
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v45085
    with dissolve
    "You and Ryo return to Karelia's farm"
    scene v45086
    with dissolve
    ryo "You can come out, we're back"
    scene v45087
    with dissolve
    karelia "I'm so glad to see you're ok"
    karelia "I was so worried..."
    scene v45088
    with dissolve
    karelia "Did you find the mage? The one... that... killed my father?"
    ryo "Yes we did"
    scene v45090
    with dissolve
    ryo "He will no longer cause problems to anyone again"
    karelia "Did you kill him?"
    ryo "We did, you are safe now"
    scene v45091
    with dissolve
    karelia "Thank you [MC] thank you pretty lady"
    karelia "I... Don't know what I'll do now..."
    scene v45092
    with dissolve
    ryo "You have to be strong..."
    ryo "Thinking about it... You could come with us"
    scene v45093
    with dissolve
    ryo "Right [MC]?"
    karelia "What do you mean?"
    MC "I guess she could... The Archmage would understand"
    scene v45092
    with dissolve
    ryo "Even if she doesn't let you stay in the college"
    ryo "I'll take you with me back home"
    scene v45099
    with dissolve
    "Karelia hugs Ryo thight"
    ryo "..."
    karelia "Thank you! Thank you so much..."
    karelia "You are too kind... {i} Sob"
    karelia "{i} Cry"
    scene v45094
    with dissolve
    ryo "There... There... Calm down"
    ryo "I'll take care of you"
    karelia "{i} sob, sniff {/i} Thank you"
    ryo "Time to go [MC]"
    MC "Follow me ladies"
    scene v38164
    with dissolve
    "You, Ryo and Karelia are back on the college courtyard"
    ryo "I'm glad I went with you tonight"
    MC "I'm glad to have you on board too"
    scene v38165
    with dissolve
    ryo "Ok I'll take Karelia to my room now"
    ryo "We'll talk about it tomorrow"
    MC "Yes... Agreed"
    scene v38166
    with dissolve
    ryo "Oh... We make a good team"
    MC "You think?"
    ryo "See you tomorrow"
    scene v45000
    with dissolve
    "You return to your room"
    "I should lie down and look a bit more into those books before I go to sleep"
    scene v45095
    with dissolve
    "You remove you robe, lie on the bed and grab the book you were reading before"
    MC "Eye of the Beholder... That's what I was reading before"
    MC "Let's focus and try to see... The baths..."
    scene v45098a
    with dissolve
    MC "Oh... That feeling of dizziness again..."
    scene v45098aa1
    with dissolve
    MC "I'm starting to... see something..."
    scene v45098aa2
    with dissolve
    scene v45098aa3
    with dissolve
    label galleryScene10:
    scene v45100
    with dissolve
    MC "Is that the Archmage?"
    MC "Is she in the baths? Is this happening right now?"
    scene v45101
    with dissolve
    MC "Wow... That's... hot"
    "You focus and try to get closer to her"
    scene v45102
    with dissolve
    MC "This spell is amazing... I wonder how many people can do this.."
    MC "And.. If this is a common spell... Is it detectable?"
    MC "She's the Archmage... She would know.. She..."
    scene v45103
    with dissolve
    MC "I don't even care... Look at that..."
    MC "She's enjoying herself"
    scene v45104
    with dissolve
    MC "What I wouldn't give to be there... Helping her to bathe..."
    MC "Hmm..."
    scene v45105
    with dissolve
    ayna "{i} unintelligible"
    MC "Is she saying something? I'll try to focus more..."
    scene v45106
    with dissolve
    ayna "What a day... I need to think about my next move"
    MC "What is she talking about? Her next move?"
    scene v45107
    with dissolve
    ayna "{i} unintelligible"
    MC "Hmm... The spell is getting harder to control..."
    MC "Focus [MC]... Focus"
    scene v45108
    with dissolve
    MC "Look at that... You can do it... Come on..."
    MC "Get closer..."
    scene v45109
    with dissolve
    MC "Yes... That's it... Look at that"
    MC "She's amazing"
    ayna "Yeah... Time to relax a bit..."
    scene v45110
    with dissolve
    ayna "Me, myself and I..."
    MC "Is she...? She is...."
    MC "Holy shit..."
    scene v45111
    with dissolve
    MC "Now I really wish I was there"
    ayna "Hmmm....Yes... Ah..."
    MC "..."
    scene v45112
    with dissolve
    ayna "Oh yes.... Hmmm... So good..."
    ayna "And people say you can't have fun alone"
    MC "What do they know right?"
    scene v45113
    with dissolve
    ayna "AHHH...Uhmmm"
    MC "She going at it faster now... Shit..."
    MC "I'm getting hard myself..."
    scene v45114
    with dissolve
    ayna "Hmmm... ah..."
    "You can't believe what you are seeing"
    scene v45115
    with dissolve
    "The Archmage, the strongest mage in the world, having some solo fun"
    "And you get to watch..."
    ayna "Oh.... I'm close..."
    scene v45116
    with dissolve
    "As you get used to the spying spell"
    "You understand it works like you had several eyes on her"
    scene v45117
    with dissolve
    "You just have to focus on the one you want..."
    MC "This is going into my favorite pile of spells"
    ayna "AHHH!"
    scene v45118
    with dissolve
    ayna "Yes yes.... Ah...."
    MC "...."
    scene v45119
    with dissolve
    ayna "AHHHHHH!!! Fuck!"
    MC "Is she squirting? Holy shit!"
    scene v45120
    with dissolve
    "You use your new ability to watch every detail of what is happening"
    MC "This is amazing..."
    scene v45121
    with dissolve
    MC "Look at that... I wish I could help her now..."
    MC "I... my head... I feel..."
    scene v45122
    with dissolve
    ayna "That was great... I can rest now"
    "You start to feel sick..."
    MC "What's... Happening..."
    ayna "{i} unintelligible"
    "You start to lose control of the spell..."
    MC "Shit... My magic... I'm depleted... How?... Fuck..."
    scene v45098ab1
    with dissolve
    "You don't have enough energy to hold the spell"
    MC "I'm so... Tired..."
    $ renpy.end_replay()
    scene v45098ab2
    with dissolve
    scene v45098ab3
    with dissolve
    scene v45098a
    with dissolve
    "You can read one last line of the book"
    "This spell should only be used for short periods of time"
    "Even masters can easily lose control of it because of it's high magic consumption"
    MC "Shit..."
    "You feel yourself dozing off..."
    scene black
    with dissolve
    fvoice "[MC]?"
    fvoice "[MC]? Are you awake?"
    MC "Hmmm..."
    fvoice "Come on... Open your eyes"


    if my_path_is == "neutral":
        jump v45neutraldream


    elif my_path_is == "evil":
        jump v45evildream


    else:
        jump v45gooddream

label v45gooddream:

    scene v45017
    with dissolve
    MC "Wha....? You?"
    god "Surprised?"
    MC "Wait... is this a dream?"
    scene v45018
    with dissolve
    god "Maybe... Maybe it's an hallucination... Who knows?"
    god "Spending all your magic to spy naked girls... I think it's deserved no?"
    MC "It wasn't on purpose... Well... Not completely..."
    god "Right..."

    if Points < -2:
        $ multipath = "good_to_evil"
        god "I've seen your actions, and you have fallen to the dark side..."
        god "Why? I need you to be on my side, do you understand?"
        god "I'll show you why you should return to the path of light"

    if Points >= -2 and Points <=2:
        $ multipath = "good_to_neutral"
        god "I've seen your actions, you are not evil at heart"
        god "But sometimes you give up to temptation..."
        god "I'll show you why you should focus on the path of light"

    if Points >= 3:
        $ multipath = "pure_good"
        god "I've seen your actions, and you are still a good boy"
        god "That's exactly what this world needs"
        god "I'll show you why you should stay on the path of light"

    scene v45019
    with dissolve
    "You can't move... Your dick seems to work though..."
    god "Have you ever wished to have me? My body?"
    MC "What?"
    god "Your man parts got the question... Don't pretend you didn't"
    scene v45020
    with dissolve
    god "My body, you have wished for it haven't you?"
    MC "I... "
    god "If you didn't, why would I be here?"
    scene v45021
    with dissolve
    god "Look at this... You can't fool me you know?"
    god "Don't tell me you don't want to feel my lips around it..."
    MC "...."
    god "That's what I thought..."
    scene v45022
    with dissolve
    god "Hmmm..."
    "You feel her divine touch on the tip of your dick"
    MC "Ahh..."
    scene v45023
    with dissolve
    god "Do you like it?"
    MC "Yes... Ahh..."
    god "Time to show you what a Goddess can do"
    scene v45024
    with dissolve
    "She starts to put all your penis inside her mouth"
    MC "AH!! Fuck..."
    scene v45025
    with dissolve
    "She's going faster and harder on it"
    god "Hmmmm Hmmm"
    MC "Ah....Ah..."
    scene v45026
    with dissolve
    "She is perfect, it's like..."
    "She's able to press all the right spots, with the correct pressure..."
    "She's a Goddess after all..."
    scene v45027
    with dissolve
    god "I think we need to try something else don't you say?"
    MC "Yes?"
    "She starts pushing your dick against her pussy"
    MC "Hmmm..."
    scene v45028
    with dissolve
    god "Yes [MC]... do you feel it all the way in?"
    MC "Ah... Yes... This feels great..."
    god "Ok you can move faster now"
    scene v45029
    with dissolve
    "You start to move faster and faster"
    god "Yes... I know you can go even faster.. Do it"
    MC "Ok then!"
    scene v45030
    with dissolve
    "You give all you have, hard and fast"
    god "Ah... yes... that's it"
    god "Harder!"
    scene v45028
    with dissolve
    MC "Ah!! I can't.... Hold anymore..."
    god "Yes!!! Fill me!"
    show shot
    with vpunch
    scene v45028c
    with dissolve
    show shot
    with hpunch
    hide shot
    MC "Ahhhh!! YES!!"
    scene v45031
    with dissolve
    god "That was great... You know what's next?"
    MC "What?"
    god "You wake up"
    jump v45wokeup

label v45evildream:
    scene v45123
    with dissolve
    MC "Wha....? You?"
    lust "Surprised?"
    MC "Wait... is this a dream?"
    scene v45124
    with dissolve
    lust "Maybe... Maybe it's an hallucination... Who knows?"
    lust "Spending all your magic to quench your lust...I think you deserve to see me"
    MC "It wasn't on purpose... Well... Not completely..."
    lust "Ahahah sure..."
    if Points < -2:

        $ multipath = "pure_evil"
        lust "Anyway... I've seen what you've been doing all your life..."
        lust "You mostly choose what is the best for you... without caring for others"
        lust "I love it...Ahaha"

    if Points >= -2 and Points <=2:
        $ multipath = "evil_to_neutral"
        lust "Anyway... I've seen what you've been doing all your life..."
        lust "I still have hope that you keep pursuing your desires... Your lust..."
        lust "What others may want or need doesn't matter, only if it's good for you"

    if Points >= 3:
        $ multipath = "evil_to_good"
        lust "Anyway... I've seen what you've been doing lately..."
        lust "You started perfectly... But now? Helping people in need? Saving them?"
        lust "I think you'll be back to your true nature soon"

    scene v45126
    with dissolve
    "You can't move... Your dick seems to work though..."
    lust "Have you ever wished to have me? My body?"
    MC "What?"
    lust "Your lewd parts got the question... Don't your brain didn't"
    scene v45127
    with dissolve
    lust "My body, you have lusted for it haven't you? You dirty boy?"
    MC "I... "
    lust "If you didn't, why would I be here?"
    scene v45128
    with dissolve
    lust "Look at this... Your hard cock... Pulsating in my hand..."
    lust "It gets harder with each stroke..."
    lust "I think I should taste it... Don't you think?"
    MC "...."
    lust "That's what I thought..."
    scene v45129
    with dissolve
    lust "Hmmm... {i} Slurp, lick"
    MC "Ah... "
    lust "How does it feel to have Lust herself sucking you?"
    MC "AHHH!!!"
    scene v45130
    with dissolve
    lust "I'll make you cum you filthy, dirty pervert"
    MC "AHHH... SHIT!! I'm...."
    scene v45129
    with dissolve
    lust "Yes! Give me all your cum! Let me taste it"
    MC "Ahhhhh!!"
    show shot
    with vpunch
    scene v45129c
    with dissolve
    show shot
    with hpunch
    hide shot
    lust "Hmmmm.... Swho mwuchh"
    MC "Ah..."
    lust "Let me clean it all... Hmm.."
    scene v45130
    with dissolve
    "She sucks all your semen with a vicious hunger"
    lust "Hmmm tasty to the last drop..."
    MC "Ah... Fuck..."
    lust "What a great idea.."
    MC "Wha...?"
    scene v45131
    with dissolve
    "She moves on top of you, sliding your still erect cock inside her"
    MC "AH!!"
    lust "Hmm... You're great... Yes.. I am too I know..."
    lust "I think we need to speed things up..."
    scene v45132
    with dissolve
    "She's riding you like nobody ever did..."
    MC "AHH!! Shit..."
    lust "Yes... Fuck me harder, faster, don't you stop!"
    scene v45133
    with dissolve
    "You feel you're about to cum again..."
    MC "AH... I'm..."
    lust "Yes!! Fill me up!! Fill that pussy!"
    show shot
    with vpunch
    scene v45133c
    with dissolve
    show shot
    with hpunch
    hide shot
    MC "AH!!!!"
    lust "So much... But... We're not done yet.."
    MC "What?"
    scene v45134
    with dissolve
    "You see all your cum being pulled inside her pussy"
    "Like it was her mouth before"
    lust "Did I said stop?! Move!!"
    scene v45133
    with dissolve
    "She is riding you full speed again..."
    MC "FUCK!!! I can't take this any longer..."
    scene v45135
    with dissolve
    "She turns around so you can see her ass"
    lust "Of course you can... NOW FUCK ME!"
    MC "Ahh...."
    lust "I'll let you cum one last time... Fill me up!"
    show shot
    with vpunch
    scene v45135c
    with dissolve
    show shot
    with hpunch
    hide shot
    lust "Hmm... Great... You had so much in you... I love it"
    MC "I..."
    scene v45136
    with dissolve
    "She starts to slide out of you dick..."
    lust "Sweet dreams... Bye"
    scene black
    with dissolve
    MC "..."
    jump v45wokeup

label v45neutraldream:
    scene v45137
    with dissolve
    MC "Wha....? M...Katla?"
    katla "Surprised?"
    MC "Wait... is this a dream?"
    scene v45138
    with dissolve
    katla "Maybe... Maybe not... Who knows?"
    katla "Does it matter? I've seen how you look at me..."
    MC "I... What? I don't..."
    katla "Ahahah sure... Why am I in your dream then?"

    if Points < -2:
        $ multipath = "neutral_to_evil"
        katla "Anyway... I've seen what you've been doing lately"
        katla "And if you keep on this path you'll hurt people"
        katla "Think about it, I don't want Isa hurt"

    if Points >= -2 and Points <=2:
        $ multipath = "pure_neutral"
        katla "Anyway... I've seen what you've been doing lately"
        katla "I see that you care about people, but you are not stupid"
        katla "I need someone to take good care of Isa"

    if Points >= 3:
        $ multipath = "neutral_to_good"
        katla "Anyway... I've seen what you've been doing lately"
        katla "I see that you care about people, I like it"
        katla "But make sure you don't sacrifice yourself for who don't deserve"

    scene v45139
    with dissolve
    "You can't move... Your dick seems to work though..."
    katla "Look at this... And you were pretending you don't look at me..."
    MC "I..."
    katla "Why is it rising then? Getting harder?"
    katla "I think I know what you need to see..."
    scene v45140
    with dissolve
    katla "My body, what do you think about it?"
    MC "I... It looks great"
    katla "I know, if not, why would I be here?"
    scene v45141
    with dissolve
    katla "So... Where should we start? Do you think I should grab it?"
    katla "Of course you do..."
    scene v45142
    with dissolve
    katla "Hmmm... Look at this... So hard... So big"
    katla "I think I'm a bit jealous of Isabella..."
    MC "Hmmm... Ah..."
    katla "I love it"
    scene v45143
    with dissolve
    katla "I see that 'he' likes me too"
    MC "How could he not..."
    katla "Hmmm... I want it in my mouth"
    scene v45144
    with dissolve
    "She puts your dick inside her mouth"
    katla "Hmmm.... Shwo Bwig"
    MC "Ah...That's great"
    scene v45145
    with dissolve
    "She is now stroking faster and harder"
    MC "Oh fuck.... Hum..."
    katla "You like this? Then you're going to love what's next"
    scene v45146
    with dissolve
    katla "Look at that... All ready to use"
    katla "Are you ready?"
    MC "Gods yes..."
    katla "Good..."
    scene v45147
    with dissolve
    katla "Ah..... It's going in... Hmm..."
    MC "Ah... yes..."
    katla "Now... Let's start moving"
    scene v45148
    with dissolve
    "Katla starts to move faster, and your dick is getting deeper"
    katla "AH YES! that's it! More!"
    MC "Ah... Oh... Damn..."
    scene v45149
    with dissolve
    katla "Don't stop! Keep going! Keep going!!"
    MC "Ah... I'm..."
    katla "Yes... Me too! Don't stop!!"
    scene v45150
    with dissolve
    katla "Harder!! YEEESS!"
    MC "Ahhhh"
    show shot
    with vpunch
    scene v45150c
    with dissolve
    show shot
    with hpunch
    hide shot
    katla "That was great..."
    MC "Oh... I'm wasted..."
    scene black
    with dissolve
    MC "..."

label v45wokeup:
    $ renpy.end_replay()
    scene v45032
    with dissolve
    MC "That was... Intense..."
    MC "Is it morning already? No way... I don't remember falling asleep naked..."
    MC "Maybe when I was watching Ayna... I don't remeber everything I did last night"
    MC "Anyway I should get dressed and go look for the Archmage"
    MC "She should be in the throne room..."
    "You get dressed and leave your room"
    $ v45check = 2
    jump afterorcv39

label v45aynatalk:
    scene v45046
    with dissolve
    "You're at the throne room and you can see the Archmage there"
    ayna "Hi [MC] how are you?"
    MC "I'm fine... do you remember what you asked me to do?"
    scene v45050
    with dissolve
    MC "I failed..."
    ayna "I know..."
    MC "You do? But..."
    scene v45047
    with dissolve
    ayna "I'm sorry... I used you..."
    MC "You used me? What do you mean?"
    scene v45048
    with dissolve
    ayna "I sent you to get something, knowing that someone would get there first"
    MC "I don't understand... What are you talking about?"
    ayna "I'll explain it...Wait..."
    scene v45049
    with dissolve
    ayna "It's happening..."
    MC "What's happening? What going on?"
    scene v45051
    with dissolve
    ayna "I'm sorry I need to go..."
    MC "Wait! Are you serious? Now I want to know what's going on"
    scene v45049
    with dissolve
    ayna "Hmmm... Fine... Follow me in my room"
    MC "Ok..."
    scene v45052
    with dissolve
    MC "But can you tell me what's going on?"
    ayna "You'll understand in a moment"
    scene v45053
    with dissolve
    "You follow Ayna to her room"
    ayna "You'll understand what I mean now..."
    "You start to feel power emanating from her"
    scene v45054
    with dissolve
    "She's casting some spell that you're not quite sure of what it does"
    "Yet... The spell feels familiar..."
    MC "That feels like some sort of the spell I used.. The Eye of the Beholder"
    scene v45055
    with dissolve
    ayna "Now I need you to focus on that sphere... Look closely"
    ayna "You'll understand everything"
    scene v45056
    with dissolve
    "You focus on the spell... Ignoring everything else"
    "Some sort of image starts to fill your mind"
    scene v45056a
    with dissolve
    ayna "Can you see it?"
    MC "I... Can see something... But..."
    ayna "Concentrate!"
    scene v45057
    with dissolve
    "You focus on the spell and now, looks like you're there yourself"
    MC "Wait... Is that?"
    Bredita "What are you doing here... Katarro?"
    Bredita "You risk too much coming here like this"
    scene v45058
    with dissolve
    katarro "I had to... Time is running out"
    Bredita "What does that mean? Are the devils planning their final move?"
    katarro "I think so... That's why I brought you this"
    scene v45061
    with dissolve
    Bredita "Are these the secret sealing scrolls?"
    katarro "Yes, got it just before [MC] could get them for Ayna"
    Bredita "I see..."
    katarro "I was also able to grab something else..."
    Bredita "Don't make me wait longer"
    scene v45059
    with dissolve
    Bredita "Hum... A soulstone... is this the one that..."
    if v42grabstone == 1:
        katarro "[MC] brought from Lust, yes"
    else:
        katarro "I found near the church destroyed by the devils"
    Bredita "Interesting... Without it, the devils will have a hard time"
    katarro "That's why I brought it here, couldn't think of a safer place"
    Bredita "You did good Katarro, now go... Before someone finds out"
    scene v45060
    with dissolve
    katarro "Very well mistress..."
    scene black
    with dissolve
    scene v45062
    with dissolve
    ayna "Did you see it?"
    MC "I... I can't believe my eyes..."
    ayna "Now you understand right?"
    MC "Yes... But.. Why?"
    ayna "It doesn't matter... I want to do something for you though"
    scene v45063
    with dissolve
    ayna "You've seen too much, and know too much"
    MC "Wait what are you doing?!!"
    scene v45063a
    with dissolve
    "You feel something around you... But it feels... Good"
    ayna "Relax..."
    scene v45064
    with dissolve
    ayna "Are you ok? Feeling good?"
    MC "Actually... I feel great, what did you do?"
    ayna "Great! I unlocked some of your power"
    ayna "Both your health and magic should be higher now"
    $ bonushp = 25
    $ bonusmp = 25
    "{color=#f00}{b}Your HP and MP increased by 25{/b}{/color}"
    MC "That is awesome, thanks!"
    scene v45065
    with dissolve
    ayna "Glad I could help, see you later"
    ayna "I have some things to do"
    MC "Right... Thanks... Bye"
    jump yann11
