
init:
    $ v44check = 0
    $ orcpath = 0
    $ v44youtulsex = 0
    $ v44katlab = 0
    $ v44rejectkat = 0
    $ v44citytravel = 0
    $ v44visitbrothel = 0
    $ v44visitshop = 0


label v44script:
    stop music
    play music "<loop 0.0>ingame.mp3"
    $ v44check = 1
    scene black
    with dissolve
    yotul "[MC]? [MC] you here?"
    MC ".... Uhmmm"
    yotul "Yotul is going inside"
    MC "Hmm?"
    scene v39117
    with dissolve
    "You open your eyes and see Yotul inside your room"
    "You fell asleep"
    MC "Oh... Hi Yotul"
    yotul "Yotul called [MC] but no answer"
    yotul "Yotul enter room anyway"
    MC "Sure... No problem..."
    scene v39118
    with dissolve
    "Did she learn that she has to knock before entering rooms?"
    MC "What brings you here?"
    yotul "Me here? You... You bring Yotul here to castle"
    MC "Yeah... I mean... Do you want to speak with me?"
    MC "Or is there another reason you came to my room?"
    yotul "Yotul needs help to leave"
    MC "Leave? The College?"
    yotul "Yotul needs to find tribe..."
    MC "I see... I guess we should go talk with the Archmage"
    scene v39058
    with dissolve
    "You and Yotul move to the Throne room where Ayna and Kat are"
    "Yotul explains them she wants to look for her tribe"
    scene v39059
    with dissolve
    ayna "What do you say [MC]? Do you want to go with Yotul?"
    ayna "And help her find her tribe?"
    menu:
        "Of course I will[ablovecolor] [abloveboth]":
            scene v39058
            with dissolve
            MC "Of course I will"
            yotul "Yes... [MC] help Yotul"
            $ katrionalove +=1
            $ aynalove +=1
            "Katriona and Ayna like you more"
            scene v39059
            with dissolve
            ayna "Great to know, I'll get the portal ready for you"
            ayna "Just go there and use it"
            MC "Thanks"
            katriona "Good luck.... {i} Orc boy..."
            MC "You..."
            yotul "Yes, we go"
            scene v44160
            with dissolve
            "You and Yotul move to the portal room"
            MC "Are you ok Yotul?"
            yotul "Yotul is happy [MC] helps"
            MC "My pleasure, ready?"
            scene v44161
            with dissolve
            yotul "Yotul ready but... Why we here?"
            yotul "We need to go out"
            MC "We are about to go out don't worry"
            MC "You trust me?"
            scene v44162
            with dissolve
            yotul "Yotul trusts [MC]"
            MC "Let's go then!!"
            scene v44163
            with dissolve
            yotul "Yes..."
            play sound "sounds/portaltravel.wav"
            $ renpy.movie_cutscene("opti/portal.webm")
            scene v44003
            with dissolve
            "You and Yotul are now in another place"
            "Lots of trees, a small river and plants, not what you were expecting"
            MC "Is this the place?"
            yotul "Yes, this is Orc lands"
            MC "Not exactly what I was expecting to be honest..."
            yotul "Yotul doesn't understand"
            MC "Oh don't worry, I mean... It's very pretty here"
            scene v44004
            with dissolve
            yotul "[MC] think Yotul pretty?"
            MC "What? What I meant was..."
            scene v44005
            with dissolve
            "Yotul removes her top"
            "Is she being serious? Aren't you here to look for her tribe?"
            yotul "[MC] wants to have fun with Yotul here?"
            MC "..."
            menu:
                "[abgreen]Hell yes!":
                    jump v44sexyotul
                "No, we have matters to take care of":
                    scene v44004
                    with dissolve
                    "Yotul dresses her top back"
                    yotul "Yes... Yotul wants it too"
                    jump v44rejsexyotul
        "No, I have other things to do now \n{color=#f00}{b}Locks all future Yotul and orc paths{/b}{/color}":

            $ orcpath = "no"
            scene v39060
            with dissolve
            ayna "I guess I'll go with you then Yotul, I'll help you find your tribe"
            yotul "Yotul thanks pretty lady"
            scene v39061
            with dissolve
            ayna "Come on let's go then"
            katriona "Really?...."
            scene throne
            with dissolve
            "They all left leaving you alone in the throne room"
            $ katrionalove -=1
            $ aynalove -=1
            "Ayna and Katriona now like you less"
            "{color=#f00}{b}Yotul and orc side story locked{/b}{/color}"
            MC "Time to do something else"
            jump v44postyotul

label v44sexyotul:
    scene v44006
    with dissolve
    "Yotul removes her clothing and is standing naked in front of you"
    yotul "What should Yotul do now?"
    MC "Well... I..."
    scene v44007
    with dissolve
    "She gets closer to you"
    yotul "Maybe Yotul can try to act like human ladies?"
    "What does she mean with that?"
    scene v44008
    with dissolve
    "She is now sitting naked in a big rock"
    yotul "Want to come closer?"
    MC "I see... You..."
    scene v44009
    with dissolve
    yotul "You like Yotul body?"
    MC "I certainly do"
    scene v44010
    with dissolve
    MC "Not only your body, also your pretty face"
    MC "I haven't ever seen another female orc"
    MC "But I'm pretty sure none of them are..."
    scene v44011
    with dissolve
    MC "... This cute..."
    yotul "..."
    "She doesn't have an answer...."
    "You know that's the first time she's heard something like that"
    "She starts to remove your clothes exposing your naked body"
    scene v44012
    with dissolve
    "And your erect penis..."
    yotul "Yotul wants sex with [MC]"
    MC "Like I could stop now..."
    scene v44013
    with dissolve
    "You gently push her trained body on her back"
    "You then line your dick with her pussy"
    scene v44014
    with dissolve
    "And you start to slide it in..."
    yotul "Hmmm... Yes..."
    "You can feel her tight pussy gripping around your dick"
    MC "Ah... Fuck... Your pussy is amazing"
    yotul "Yes... Give more to Yotul"
    "You keep pounding her harder and faster"
    scene v44015
    with dissolve
    "You and her keep going at it, changing positions"
    "Ignoring everything else, just focusing on each other"
    MC "Ah.... Fuck..."
    scene v44016
    with dissolve
    yotul "Ah...Good yes!! [MC] strong!"
    MC "I wouldn't say that's the best of my assets"
    yotul "Yotul wants harder"
    MC "You don't have to ask again"
    scene v44017
    with dissolve
    "You force her on all fours, her hands keeping her from falling"
    "You then start to slide you dick back in"
    MC "Hmmm..."
    scene v44018
    with dissolve
    yotul "Ah....Yes..."
    "You are now giving her everything you have"
    "You fuck her as fast and hard as you can"
    scene v44019
    with dissolve
    MC "Ah.... You feel amazing Yotul"
    "As you look closer to the place where the two of you connect"
    "You wonder if she ever had anal"
    scene v44020
    with dissolve
    "You start using you finger to test the waters"
    "First you just rub her asshole for a few moments"
    scene v44021
    with dissolve
    "Then you start to slide your finger inside"
    "Yotul has a mix of surprise and pleasure on her face"
    "Probably because you keep pounding her hard"
    MC "Have you ever used your ass for sex Yotul?"
    yotul "Yotul ass...? No... But Yotul can try to please [MC]"
    MC "Really?"
    scene v44022
    with dissolve
    "You lose no time, and start pointing your dick to her other entrance"
    "You wonder, once again, if all orc ladies are like this"
    "If they are, orcs are some lucky motherfuckers"
    MC "Ok, I'll do it slowly... Tell me if you want me to stop"
    scene v44023
    with dissolve
    "Yotul nods and you slowly start to push your dick inside her"
    MC "So tight... I'm not sure I can put it in..."
    "After some effort you start to move in and out"
    scene v44024
    with dissolve
    yotul "Ah...."
    MC "Are you ok? Am I hurting you?"
    yotul "Yotul is fine... It's good"
    "You gradually start to speed up"
    scene v44025
    with dissolve
    yotul "Yes... More... More"
    yotul "Give Yotul more"
    "She is loving it and you do what she says"
    "You start to feel you're getting close"
    scene v44026
    with dissolve
    yotul "AHHHHHHHH!!!!!"
    "And looks like she is too"
    yotul "[MC]!!!! YES!!"
    "You can't hold it anymore either"
    MC "Shit... I'm about to cum..."
    show shot
    with vpunch
    hide shot
    MC "AHH!"
    yotul "YES!!"
    show shot
    with vpunch
    scene v44027
    with dissolve
    "You filled her ass completely with your cum"
    MC "{i} Pant pant pant...."
    MC "That was..."
    scene v44028
    with dissolve
    yotul "Yotul like ass sex... We do again"
    MC "Oh we will..."
    yotul "Yotul pleased, Yotul wants to look for tribe now"
    MC "Let's go then"
    $ v44youtulsex = 1
    jump v44rejsexyotul

label v44rejsexyotul:
    scene v44029
    with dissolve
    yotul "Hear that?"
    MC "What?"
    scene v44030
    with dissolve
    yotul "Follow Yotul..."
    MC "...Sure..."
    scene v44031
    with dissolve
    "You and her climb some rocks"
    "She is sure she heard something... You follow her"
    scene v44032
    with dissolve
    yotul "Look [MC]"
    "You notice two orcs and some other creature nearby"
    "She was right after all"
    scene v44033
    with dissolve
    "Yotul keeps hiding and silent"
    "Why isn't she going to them? Aren't they from her tribe?"
    "You notice that the weird creature starts to move and sniff around"
    scene v44034
    with dissolve
    "And it starts to get closer..."
    MC "Oh shit..."
    orc "What are you doing, stupid Magrash?!"
    "Magrash? is that the name of that thing?"
    orc2 "What's that?!"
    scene v44035
    with dissolve
    orc "Get them!!"
    yotul "They saw us"
    MC "Yeah... Looks like it"
    scene v44036
    with dissolve
    "The magrash creature is roaring in your direction"
    orc "Kill them!!"
    "You decide to use your illusion magic on the creature"
    scene v44037
    with dissolve
    "To make it like you"
    MC "Who's a good boy?? Who's a good boy?"
    MC "A very ugly.... Good boy..."
    "Neither Yotul nor the random orcs can hide their surprise"
    yotul "What?!"
    MC "Now... Do you want to bite those bad orcs?"
    MC "Do you? Go... Go get them!! Go!"
    scene v44038
    with dissolve
    "The creature understands what you want and turns to the orcs"
    orc "How...? "
    orc2 "This human is wizard... Please...No "
    MC "Easy boy... Calm down..."
    scene v44039
    with dissolve
    "The creature feels the calm tone of your voice and stops"
    yotul "This human is strong, don't try to attack him"
    orc "Who are you?"
    yotul "Yotul, sister of chief Vakgu, he [MC], a mage"
    orc2 "Lies!"
    scene v44040
    with dissolve
    "The magrash doesn't like the orc tone and threatens him"
    orc2 "Wait... Sorry... No..."
    orc "Vakgu is dead, red humans kill Vakgu"
    MC "Have you seen it with your eyes?"
    orc "No..."
    MC "He could still be alive then"
    orc "Yotul can join the trials to be new chief"
    yotul "Yes, go. Tell all tribes I will"
    orc "Yes... And will tell about wizard friend"
    scene v44041
    with dissolve
    "They left and you are now alone with Yotul"
    yotul "[MC] was amazing... "
    MC "Hehehe... Magic..."
    scene v44042
    with dissolve
    yotul "..."
    MC "Something on your mind?"
    yotul "Humans want to steal my land"
    MC "I won't let that happen..."
    scene v44041
    with dissolve
    yotul "Yotul happy"
    MC "So... Should we return to the college for now?"
    yotul "Yes"
    stop music
    play music "<loop 0.0>dark.mp3"
    scene meanwhile
    with dissolve
    scene v44001
    with dissolve
    Bredita "Come on... I don't have all day"
    Bredita "Rise and shine big boy"
    brutus "Hmmmmm... Yes.... Mistress..."
    scene v44002
    with dissolve
    Bredita "Are you ready to be helpful to me?"
    brutus "Yes.... Mistress... Anything you ask"
    Bredita "Good... Let's get you some fitting garments"
    Bredita "Then we start to put my plan in motion"
    brutus "Your wish is my command mistress"
    Bredita "Indeed..."
    stop music
    play music "<loop 0.0>ingame.mp3"
    scene v44161
    with dissolve
    "You and Yotul are back to the college"
    yotul "Yotul thanks [MC] for help"
    menu:
        "You are now even more in my debt[abred] [abnoalignment]":
            $ Points -= 1
            "You lost 1 point"
            scene v44160
            with dissolve
            yotul "Yes... Yotul will pay"
            yotul "Yotul needs to rest now"
            scene v44163
            with dissolve
            MC "Very well"
            jump v44postyotul
        "You don't have to, I'm glad to help[abgreen] [abalignment]":

            $ Points += 1
            "You gain 1 point"
            scene v44162
            with dissolve
            yotul "[MC] is too good for Yotul"
            yotul "Yotul needs to rest now"
            scene v44163
            with dissolve
            MC "See you later then"
            jump v44postyotul


label v44postyotul:
    scene hall
    with dissolve
    "As you are walking around the college you hear something..."
    "It looks like it's coming from the training grounds"
    scene v44147
    with dissolve
    "As you reach the training room you see Ryo and a giant Lizard"
    MC "This looks like interesting stuff..."
    MC "Wait... Where is Professor Rerlvam?"
    scene v44148
    with dissolve
    MC "There she goes... She's fast"
    "As Ryo and the lizard are about to clash, the princess jumps"
    scene v44149
    with dissolve
    "And with some acrobatic move she stabs the lizard..."
    "Right on the top of its skull"
    "Blood starts to splurt everywhere"
    scene v44150
    with dissolve
    ryo "Hello [MC], You know... In my culture"
    ryo "Hiding and watching other people is a bit rude"
    MC "I... Sorry it's not what it looks like"
    scene v44151
    with dissolve
    ryo "I'm kidding... I know that if you wanted to hide you would"
    ryo "With some spell or something like that"
    MC "Yeah, but around here I still get c... I mean I'd still get caught by the Archmage"
    MC "Or Kat, or apparently Mida and Konkeo too..."
    scene v44152
    with dissolve
    ryo "So... You were looking for me? Or did you come to train?"
    MC "Actually I was passing by and saw you training..."
    MC "Speaking about that... How's your magic training?"
    ryo "I spoke with Professor Rerlvam about it"
    ryo "But I have something for you"
    MC "For me? What is it?"
    ryo "It's a surprise, will you come with me? It's in my room"
    MC "In your room... Hmmm.. Ok"
    ryo "Good... Let's go"
    "You follow her to her room"
    scene v44153
    with dissolve
    "Not only her room is next to yours, it's almost identical"
    ryo "Hold on a second please"
    "You wonder what's the surprise... A naked surprise would be nice"
    scene v44154
    with dissolve
    ryo "It's here, let me get it"
    MC "Oh..."
    "Doesn't look like it's a naked surprise..."
    scene v44155
    with dissolve
    ryo "Here it is!"
    MC "A book?"
    ryo "Not a regular book, a magic book..."
    ryo "Here, I give it to you"
    scene v44156
    with dissolve
    MC "Thank you, what is it about?"
    ryo "I don't know... Like I told you before I never managed to learn magic"
    ryo "I can't even read it... Yeah... I'm that bad..."
    MC "I... Can't read it either... Is it in your language?"
    scene v44157
    with dissolve
    ryo "You can't?"
    MC "Nope... Never seen this language before..."
    if v43bookpay == 1:
        "Actually this looks like those demons books"
        MC "Wait... This actually looks like..."
        ryo "What?"
        MC "Uhmm... Like something Yisnna would know"
    MC "I should take this to Yisnna"
    scene v44156
    with dissolve
    ryo "Sure... Tell me if you find what it is about?"
    MC "Deal! Also, I'll teach you a new spell as soon as possible"
    scene v44159
    with dissolve
    ryo "I would like that very much"
    ryo "Me learning magic... Feels like I'm a kid again"
    MC "I'm sure you'll be a talented student"
    scene v44158
    with dissolve
    ryo "Ahaha sure... See you later then?"
    MC "Yes, goodbye Ryo"
    ryo "Jaa nei"
    $ v42spellbookcount += 1
    scene hall
    with dissolve
    "You leave her room"
    MC "I should take this to Yisnna right now"
    MC "She will surely know what this is about"
    "You go to the library and meet Yisnna"
    scene v43082
    with dissolve
    MC "Hello Yisnna"
    yisnna "Hi [MC] how are you?"
    MC "I'm good, I have something for you though"
    if v43bookpay == 1:
        yisnna "Don't tell me you have another book..."
        MC "Yes..."
        scene v43083
        with dissolve
        MC "Look...."
    scene v43083
    with dissolve
    MC "Here...."
    scene v43085a
    with dissolve
    if v43bookpay == 1:
        yisnna "Another book in the demon language..."
        yisnna "Amazing..."
        scene v43084
        with dissolve
        yisnna "At this rate I'll have no more gold for you"
        yisnna "Ahaha"
        $ Gold += 50
        play sound "sounds/coin.ogg"
        "You got 50 gold"
        yisnna "Visit me later, I need time to translate this"
        MC "Sure... Bye Yisnna"
        jump v44postbook
    else:

        $ v43bookpay = 1
        yisnna "No way... you're kidding"
        yisnna "Oh my... This is... Do you even know what this is?"
        yisnna "This is demonic language... Incredible..."
        MC "Is there a problem with it?"
        yisnna "How did you get your hands on this? No way"
        yisnna "I... This is a spell book..."
        MC "..."
        scene v43084
        with dissolve
        yisnna "Right... Sorry, I'm just... Surprised"
        yisnna "And no, there's no problem with it"
        yisnna "Knowledge is never an issue..."
        yisnna "The way you use it, is"
        yisnna "I'll need some time to translate this.."
        yisnna "I still can't believe this..."
        MC "..."
        yisnna "Right... Your reward... Here"
        $ Gold += 50
        play sound "sounds/coin.ogg"
        "You got 50 gold"
        scene v43082
        with dissolve
        yisnna "Good reward right? Bring me more..."
        yisnna "And I'll reward you more"
        MC "Thanks Yisnna, see you later"
        jump v44postbook

label v44postbook:
    jump afterorcv39

label v44labkat:
    if v44katlab == 0:
        $ v44katlab = 1
        scene v44044
        with dissolve
        "You enter the lab to find Kat making a list and packing a satchel full of items"
        MC "Hey Kat, what are you up to?"
        scene v44045
        with dissolve
        katriona "Wow, great timing actually"
        katriona "I'm gonna be leaving the College for a bit to search for ingredients for Potions"
        MC "Oh god... what horrible plan do you have now?"
        scene v44043
        with dissolve
        katriona "Hush, it's not always about humiliating you..."
        MC "What percentage?"
        katriona "Say 40 percent of the time it's about you"
        MC "That's still pretty high"
        katriona "{i} giggle"
        scene v44046
        with dissolve
        "She put her satchel strap on her shoulder"
        katriona "So anyway, would like to come along and help out?"
        katriona "Keep a girl company out in the big bad world?"
        MC "First, I highly doubt as an Elite you are actually scared of anything on Allesterra"
        MC "Second, yeah sure, I'd love to spend some time with you"
        scene v44047
        with dissolve
        katriona "Great, let me get finished up here then I'll meet you in the courtyard"
        MC "Sure"
        jump afterorcv39
    else:
        scene v44045
        with dissolve
        katriona "I'm almost done, wait for me in the courtyard"
        MC "Come on, hurry up..."
        scene v44044
        with dissolve
        katriona "Now where is that thing..."
        MC "..."
        jump afterorcv39

label v44katcourt:
    scene courtyard
    with dissolve
    MC "Why is she taking so long..."
    katriona "Hey!!"
    scene v44192
    with dissolve
    katriona "I don't have all day you know? Let's go!"
    MC "You little..."
    katriona "Great, so I have to hit a few places on this trip for sure"
    scene v44193
    with dissolve
    katriona "The Crater, Mt. Frost and I need to see a shop owner in the village"
    MC "So lets head north first and work our way down"
    scene v44194
    with dissolve
    katriona "Oh... so you want to go down huh?"
    MC "Ugh... let's just go...."
    scene v44192
    with dissolve
    katriona "Screw you, I'm funny"
    "You travel with Katriona for a while, her cracking jokes, you feigning annoyance"
    "It was your thing"
    "How you two always interacted and showed you cared about each other"
    scene v44064
    with dissolve
    "Soon you find your way to Mt. Frost"
    MC "Here we are"
    katriona "Yeah... Brrrr"
    scene v44065
    with dissolve
    MC "Feeling cold?"
    MC "Who would have thought a bikini and a robe was the wrong attire for snow"
    katriona "Haha... Funny..."
    scene v44066
    with dissolve
    katriona "Ok, so we're looking for a pretty large cave"
    MC "I think I know which one you mean"
    MC "I had to take shelter there once during a snow storm"
    katriona "Great, lead the way [MC]"
    scene v44067
    with dissolve
    "You soon come upon the cave you ducked in before"
    MC "So you know, there were a lot of Ice Spiders in here the last time I was here"
    scene v44068
    with dissolve
    katriona "Oh really? And let me guess you got scared and ran away..."
    "You suddenly remember that you actually did"
    MC "Ahem, so what are we looking for?"
    katriona "Heh, right, well we're looking for Frost Moss"
    katriona "It's a magic type of moss that is infused with ice magic..."
    katriona "So it looks like growths of ice crystals on the undersides of rocks"
    scene v44068s
    with dissolve
    "It's getting colder and foggy... Looks like a storm is coming"
    katriona "We should get inside"
    scene v44069
    with dissolve
    katriona "Ok here we are"
    MC "It's as dark and cozy as I remember"
    katriona "Let me take care of the dark part"
    scene v44070
    with dissolve
    "You can see Katriona casting magelight"
    scene v44071
    with dissolve
    katriona "Ok, now I can see your scared face clearly"
    MC "Oh ha ha..."
    katriona "So, know what to look for right?"
    MC "Yeah some magical moss that looks like crystals"
    katriona "Ehh... Yes..."
    MC "Alright, sounds simple enough, I'll check over here"
    katriona "Ok, then I'll start on this side"
    scene v44072
    with dissolve
    "You search for about 5 minutes until you see some glowing crystals"
    MC "That must be it"
    scene v44073
    with dissolve
    MC "This doesn't look like moss at all..."
    MC "Why don't they just call it ice crystals?"
    "You reach the crystals and grab some"
    scene v44074
    with dissolve
    "They glow even more when in contact with your hands"
    MC "Shiny..."
    "After you collect some crystals you return to where you where"
    scene v44075
    with dissolve
    "You see Katriona with some crystals in her hand"
    katriona "See?! Easy"
    MC "Yeah, I'm actually having fun"
    scene v44076
    with dissolve
    "Suddenly the two of you hear something from above"
    katriona "What the...?"
    scene v44077
    with dissolve
    "You look up just in time to see a group of full grown Ice Spiders coming straight at you"
    "Instinctively you pull Kat out of the way and end up holding her close"
    scene v44078
    with dissolve
    "She looks up at you slightly confused by also trying to hide a smile"
    MC "See, told you there were Ice Spiders"
    scene v44079
    with dissolve
    katriona "Ummm... yeah. Right! Let's show them who they're dealing with"
    $ companion = 1
    $ companion_name = "Katriona"
    $ enemy = "v44spiders"
    jump combat

label v44deadspiders:
    stop music
    play music "<loop 0.0>ingame.mp3"
    hide screen companions
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    scene v44080
    with dissolve
    katriona "Remind me to come back here and find their nest"
    katriona "I can use the spider eggs for various things"
    MC "I don't want to know... So, crater next?"
    katriona "Actually let's go to the forest first"
    katriona "It will get dark in a few hours and it's already this cold"
    MC "Ok..."
    scene v44071
    with dissolve
    katriona "Normally I'd go there alone because it's a really delicate place"
    katriona "But since it's you I'll take you with me"
    katriona "There's a field you can find if you know the way."
    katriona "It's filled with a lot of very rare flora and fauna"
    MC "Sounds amazing"
    katriona "It is, but it's also dangerous"
    katriona "Smell the wrong flower and I'll be waking you up in 3 weeks after your coma"
    MC "Yeesh, ok then, I'll be careful"
    scene v44100
    with dissolve
    "After a while of travel from the mountain you make it to the forest"
    MC "Here we are"
    katriona "Let's move before it gets dark"
    "You walk through several winding paths.."
    scene v44101
    with dissolve
    "...You even catch sight of a bear at one point.."
    "...Who takes one look at you and runs the other way"
    scene v44102
    with dissolve
    "You think to yourself... Yeah you better run"
    katriona "Hmm... Weird..."
    scene v44103
    with dissolve
    katriona "We're almost there... it's right past that cliff"
    scene v44104
    with dissolve
    "After some time you come to a rather hidden field in the middle of the woods"
    "Untouched by the snow of the rest of the wooded area"
    "Here it seemed like spring and everything was in bloom"
    "You could feel the magic coming from this place."
    MC "How is this place possible..."
    katriona "It was created while I was in school"
    katriona "By a Mage who wanted to help me in my studies"
    MC "Who was it?"
    scene v44105
    with dissolve
    katriona "My sister..."
    MC "You don't talk about her much, where is she?"
    katriona "Gone. It was long before you came to the College"
    katriona "Suntako sent her on an errand, there was an accident. No one's fault. But she died"
    scene v44108
    with dissolve
    "You walk up and hug Katriona."
    "She melts into the hug for a minute before drawing away."
    scene v44106
    with dissolve
    katriona "Thanks, I'm glad I was able to bring you here"
    katriona "It feels like my family's all in one place for once"
    MC "I would have liked to have met her"
    scene v44107
    with dissolve
    katriona "No you wouldn't. You think I give you crap, I'm tame compared to her"
    MC "Oh God, I take it back, I couldn't take two of you"
    katriona "Good thing I'm not as well versed in Illusion Magic then"
    scene v44109
    with dissolve
    katriona "Ok then, I'm looking for two things..."
    katriona "A blue flower with red thorns"
    katriona "And a sporecap mushroom with a redish-orange cap"
    MC "Ok, where should I look?"
    katriona "The garden changes all the time..."
    scene v44106
    with dissolve
    katriona "She said, 'Well Kat this way is more fun for you'"
    katriona "'This way it will always be an adventure for you to find what you're looking for'"
    katriona "That bitch..."
    MC "HAHAHA Ok, I'll start over here then"
    scene v44110
    with dissolve
    "After about 40 minutes of searching you find a Mushroom with a redish-blue cap"
    MC "Wait.. did she say the flower had blue or the mushroom?"
    scene v44111
    with dissolve
    MC "Oh well I can just take it to her and ask"
    scene v44112
    with dissolve
    "You pick the mushroom"
    MC "Let see if I got it right"
    scene v44113
    with dissolve
    "You walk over to her... careful to avoid any possibly dangerous plants"
    "She is checking some plants"
    scene v44114
    with dissolve
    MC "Hey Kat, I think I have what you asked me"
    katriona "You have?"
    scene v44115
    with dissolve
    MC "Is this what you were talking about?"
    katriona "What? Wait.. I said redish orange cap... that... Oh crap"
    katriona "Why did you have to pick that out of everything?"
    MC "Why? What's wrong with it?"
    katriona "Throw it away quick, before it's spores are released"
    scene v44116
    with dissolve
    "But it was too late, the small mushroom puffed out a cloud of spores between you"
    "Inhaling without meaning to, suddenly you became overwhelmed with lust"
    scene v44117
    with dissolve
    "You looked at Katriona... She was looking weird"
    scene v44118
    with dissolve
    "After a few seconds it was clear the same thing was happening to her"
    "You were desperate to rip her clothes off and take her right here"
    katriona "You idiot... sexy sweet idiot... NO!"
    katriona "No...We.... we need to resist it"
    katriona "Hold on, I have a spell that will help lessen the effects"
    katriona "I just need to concentrate..."
    scene v44119
    with dissolve
    MC "Just hurry Kat.... I'm having trouble not just jumping you..."
    katriona "I have that problem every time I see you lately....."
    katriona "No! Stop! Katriona get a hold of yourself"
    katriona "[MC] walk over there, right now...."
    MC "Right... distance, good idea.... I hate it..."
    "You start to move.. But both of you are distracted by a weird noise"
    scene v44120
    with dissolve
    katriona "A SLIME! The spores must have attracted it. We have to kill it and save the garden!"
    MC "Right...I'm coming...."
    katriona "Oh god did you have to phrase it that way right now..."
    scene v44121
    with dissolve
    MC "Let's just get it and you can do your spell very quickly after..."
    $ companion = 1
    $ companion_name = "Katriona"
    $ enemy = "v44slime"
    jump combat

label v44deadslime:
    stop music
    play music "<loop 0.0>ingame.mp3"
    hide screen companions
    hide screen MC_bars
    hide screen hpbar
    $ companion = 0
    scene v44122
    with dissolve
    "After being defeated, the green slime explodes"
    "The viscous material covered both of you..."
    scene v44123
    with dissolve
    "...And had a startling side effect as the clothes covering both you and Katriona..."
    "Began getting eaten away, leaving your naked bodies untouched"
    scene v44124
    with dissolve
    "Still under the effects of the spores and now presented with her perfect nude skin"
    katriona "No... This... Eww..."
    scene v44125
    with dissolve
    katriona "I... Can't...."
    "You could no longer resist and pulled Katriona into your arms kissing her"
    scene v44126
    with dissolve
    katriona "Hmm.... [MC]... I..."
    scene v44127
    with dissolve
    "You kiss her again..."
    "Your hands reached down her back and grabbed her round ass"
    scene v44126
    with dissolve
    katriona "No... no we shouldn't, it's the spores...."
    MC "No it's not, I want you... I have for a while now..."
    katriona "You have? Oh God.... I can tell.. it's pressing into me..."
    MC "I can't help it, look how sexy you are"
    scene v44128
    with dissolve
    "Kat reaches down and grabs your dick"
    katriona "I was so jealous that Mida got you... I wanted this all to myself..."
    MC "It's yours now, what are you going to do with it?"
    "Katriona began rubbing your cock with her hand, stroking along it gently at first"
    scene v44129
    with dissolve
    "She got down on her knees and began working it in earnest"
    katriona "Do you like this?"
    MC "You have no idea..."
    katriona "Oh so you're happy with this? Because I was going to suck it..."
    MC "Oh God Kat, for once just shut up and suck my dick..."
    katriona "Gladly!"
    scene v44130
    with dissolve
    "She took you into her mouth and begain to suck while moving her head back and forth"
    "Licking the underside of your shaft with her tongue."
    "The feeling was better than any you had felt before"
    "You didn't know if it was because of the spores, or because she was just that good"
    scene v44131
    with dissolve
    "It didn't take long until your lust was overpowering"
    scene v44132
    with dissolve
    "You pulled Kat away from your cock and pushed her down onto the grass"
    scene v44133
    with dissolve
    "Spreading her legs you began by putting your finger in her pussy"
    katriona "Ah.... You... Hmm..."
    scene v44134
    with dissolve
    "Her pussy looked to good, so you decide to taste it"
    "It was so sweet..."
    katriona "Yes...please... don't stop..."
    "You flipped her over and pulled her back on top of you"
    scene v44135
    with dissolve
    "You ate her pussy while she went back to sucking your dick"
    MC "Hmm... Fuck..."
    katriona "Slurp... Slurp..."
    "It didn't take long until you were both on the edge"
    scene v44136
    with dissolve
    "Sensing your were about to come, Katriona started sucking harder"
    "Giving you the go ahead to just let loose in her mouth."
    "At the same time, you could feel her tensing up"
    katriona "YES! I'm... I'm cumming!!!"
    MC "Me too.. It's coming now!"
    show shot
    with vpunch
    scene v44137
    with dissolve
    show shot
    with hpunch
    hide shot
    "Kat quickly put your cock back in her mouth"
    "Just as your balls unloaded lots of cum straight down her throat"
    "But as your orgasm subsided you realized the spores effects were still going strong"
    scene v44138
    with dissolve
    "You pulled Kat off you and mounted her on the ground"
    "Lining your dick up with her pussy...."
    katriona "No.. no! Wait, [MC], not like this..."
    katriona "Not under the effect of some mushroom... please..."
    MC "Yeah... you're right... I'm sorry...."
    scene v44139
    with dissolve
    "You quickly back away from her. She manages to compose herself long enough"
    scene v44139s
    with dissolve
    "Magical energy swirls around you and her"
    "Suddenly you start to feel the lust subside"
    scene v44125
    with dissolve
    "Suddenly embarrassed by everything that happened"
    "Katriona blushes and turns away from you"
    katriona "I'm sorry. I shouldn't have let it get to that point..."
    MC "Kat, it's my fault for picking the wrong thing, I got the colors confused"
    katriona "Yeah, that's right, it is your fault...."
    MC "Were you really jealous of Mida?"
    katriona "Yes... Do you think this was a mistake?"

label v44menuask:
    menu:
        "Yes, the spores did it[abred] [abnoloveidiot3]":
            $ katrionalove -= 3
            $ v44rejectkat = 1
            "Katriona loves you less"
            MC "No... I don't think I want this. You've always been like a sister to me"
            MC "Sure I've had some thoughts about you in passing"
            MC "But I love you too much to think about you that way"
            katriona "Hey, it's fine. I totally understand."
            katriona "I feel the same way. You'll always be my little flower boy"
            katriona "We'll put this behind us and move on"
            MC "Speaking of behinds, ours are totally naked... how are we getting back to the College?"
            jump v44bugr
        "No, I wanted it as much as you[ablovecolor] [ablove]":

            $ katrionalove += 1
            "Katriona loves you more"
            scene v44126
            with dissolve
            MC "No, not at all."
            MC "I used to fantasize about something like this with you all the time"
            MC "Back when I was a teenager"
            katriona "Really now?"
            MC "Well, sometimes it was you and Mida at the same time, or others..."
            katriona "Oh God, Mida...."
            katriona "I'm sorry, she'll be furious with us if she ever learns about this..."
            MC "Do you plan on telling her?"
            scene v44125
            with dissolve
            katriona "NO! But.... now that our feelings are out there..."
            katriona "I don't want to just go back to how we were either..."
            katriona "Don't get me wrong, I still love you like I always have, just now more too"
            MC "I feel the same..."
            katriona "But Mida..."
            MC "And aren't you with the Archmage?"
            katriona "Oh... that... that's more like... for fun?"
            MC "You know, Mida has this giant crush on Ayna..."
            katriona "Yeah?"
            MC "You and I could work together to try to get them hooked up..."
            MC "Then the two of us could just join them"
            MC "Then no one gets hurt and everyone gets what they want..."
            katriona "You make a very interesting point."
            katriona "Yeah, I definitely raised you right, you inherited my deviousness"
            MC "Thank you. Now.. about our clothes?"
            jump v44bugr



label v44bugr:
    katriona "Yeah I need to summon some clothing"
    scene v44139
    with dissolve
    "She starts to cast something"
    scene v44140
    with dissolve
    "In the next moment she has her clothes back"
    katriona "Ok... I'm ready to go..."
    scene v44141
    with dissolve
    katriona "I'm waiting... Are you going to dress or what?"
    MC "Eh... I..."
    scene v44142
    with dissolve
    MC "I don't know any spell to summon clothes..."
    katriona "You... Don't..."
    scene v44143
    with dissolve
    katriona "Ahahaha.... Ahahaha!!"
    MC "..."
    katriona "Ahahaha"
    MC "Yeah yeah... laugh..."
    katriona "Look at me... The mighty mage... I can't cast clothes"
    katriona "Ahahaha!"
    MC "..."
    scene v44144
    with dissolve
    katriona "Ok... Let me help you then"
    MC "..."
    scene v44144s
    with dissolve
    "You feel her magic around you"
    MC "What are you..."
    scene v44144
    with dissolve
    katriona "There you go"
    MC "Really....?"
    scene v44143
    with dissolve
    katriona "Ahahah! You look amazing in that"
    MC "... bitch..."
    scene v44145
    with dissolve
    katriona "Oh come on... "
    MC "I really need to learn that, I lose my clothes entirely too often"
    katriona "Maybe you should have stayed in that ugly ass brown student robe"
    scene v44146
    with dissolve
    MC "Hell no, I'd rather go around naked"
    katriona "Kinky. The Legend of the Naked Mage and his massive staff"
    MC "Ha ha"
    katriona "See? I'm funny, now let's keep going"
    "After a while Katriona and you managed to find the real ingredients"
    "Then moved to the village"
    scene v44081
    with dissolve
    "You both reach a part of the village you haven't visited before"
    "The Sun is pretty much gone and darkness is taking place"
    katriona "We lost way too much time in the woods..."
    katriona "Hope the store is still open"
    scene v44082
    with dissolve
    katriona "I used to come here when I was a student"
    katriona "They had a bakery back then that was amazing"
    katriona "All sorts of tarts, pastries and fresh breads"
    MC "That sounds delicious. What happened to it?"
    scene v44083
    with dissolve
    katriona "Well that's a thing you'll have to get used to. Magic gives us a lot"
    katriona "We gain powers, can do extraordinary things"
    katriona "And we live much longer than normal members of our races would"
    katriona "But you end up seeing a lot of people die because you outlive them"
    MC "Wow, I guess I've always sort of hazed over that part of it"
    katriona "Now you know why a lot of us just stay in the College"
    katriona "Better to be around people you know you're going to keep seeing"
    MC "Yeah..."
    scene v44082
    with dissolve
    katriona "Ok, enough sad stuff. Shop's this way"
    MC "Kat..."
    scene v44081
    with dissolve
    "But she already had turned and walked away toward the shop"
    scene v44088
    with dissolve
    "As you both enter, you're greeted by a young girl behind the counter"
    daug "Wow... Um, I mean, welcome to our shop... Um, are you two Mages?"
    katriona "Yes we are, how did you know?"
    daug "Your clothes are so different from what people in this town wear, and they match"
    daug "I figured you must be from the College"
    scene v44089
    with dissolve
    MC "Yeah... They match... The blue robes..."
    daug "Excuse me?"
    MC "Oh.. Nothing, nothing go on"
    scene v44088
    with dissolve
    katriona "You're a smart one for sure. So this is your shop?"
    daug "It's my family's. It belonged to my Grandma"
    daug "Now I'm running it since my mother and father already had other work"
    scene v44089
    with dissolve
    MC "You seem so young to be running a store. It's quite impressive"
    daug "Thank you, but I look younger than I am. I'm actually 16, so I'm almost an adult"
    scene v44088
    with dissolve
    katriona "Well I knew your grandmother, she always kept certain supplies on hand for me"
    scene v44094
    with dissolve
    katriona "Could you check if you have what's on this list?"
    daug "Oh... Sure"
    scene v44095
    with dissolve
    daug "Let me see. Ok, I think we have all of this."
    scene v44096
    with dissolve
    daug "Let me go look in our store room"
    scene v44090
    with dissolve
    "As the girl leaves Kat turns to you"
    katriona "She's a cute girl. Seems sweet too"
    MC "Yeah, she's a nice girl"
    katriona "Yup, that's why I'll have to come back later and warn her..."
    MC "About what?"
    katriona "About what a letcherous pervert you are, so she doesn't fall for your act"
    MC "If anyone is a pervert around here, it's you"
    scene v44091
    with dissolve
    katriona "True, but I'm a pretty girl and you're you. Who's she going to believe?"
    MC "{i}sigh{/i} Come on, don't be making trouble for me, I may need to come here occasionally"
    katriona "I was just kidding. Make friends with her"
    katriona "That's how it was for me and her Grandma"
    katriona "She was still a young woman when I was a kid"
    MC "Kat, you know you can talk to me about stuff like that, right?"
    MC "I'm not the same little kid I used to be, I can take care of you too"
    katriona "I know... much as I hate to admit that you grew up, I see it"
    scene v44092
    with dissolve
    "The girl comes back with a bag full of things"
    daug "Ok here you are, and with the bag to carry them in that comes to 50 Gold"
    scene v44093
    with dissolve
    katriona "Let me see..."
    menu:
        "Pay for Katriona[ablovecolor] [ablove]" if Gold >= 50:
            scene v44098
            with dissolve
            MC "Here"
            katriona "What are you..?"
            MC "Shush... Let me.."
            scene v44099
            with dissolve
            $ Gold -= 50
            play sound "sounds/coin.ogg"
            "You lost 50 gold"
            $ katrionalove += 1
            "Katriona loves you more"

        "Pay, but tell her she owes you now[abcorruptioncolor] [abcorruption]" if Gold >= 50:
            scene v44098
            with dissolve
            MC "Here"
            katriona "What are you...?"
            scene v44099
            with dissolve
            MC "You owe me now..."
            katriona "{i} giggle"
            $ Gold -= 50
            play sound "sounds/coin.ogg"
            "You lost 50 gold"
            $ katrionacorr += 1
            "Katriona corruption increased"
        "Let her pay":

            scene v44097
            with dissolve
            play sound "sounds/coin.ogg"
            katriona "There you go"

    scene v44088
    with dissolve
    katriona "Thank you miss"
    daug "Thank you!"

    scene v44099
    with dissolve
    katriona "There is still one last place I want to go [MC]"
    MC "The crater right?"
    katriona "Yes... Let's move"
    scene v44048
    with dissolve
    "After a while you and Kat reach the crater site"
    katriona "Finally... We're almost done for the day"
    scene v44049
    with dissolve
    katriona "So what we're looking for is a type of flower"
    katriona "That grows exclusively at the impact point..."
    katriona "Listen...."
    MC "Yeah?"
    katriona "I know I usually give you crap about that day and call you Flower Boy..."
    katriona "And we're looking for a flower now..."
    MC "I knew it, here it comes....."
    scene v44050
    with dissolve
    katriona "No wait, just listen to me. I'm gonna go get this one alone...."
    katriona "I don't want to have a relapse of what happened to you back then"
    MC "Katriona, I'm fine. Look at me, I fainted actually right around here"
    MC "So if I'm fine here, I'll be fine there"
    scene v44051
    with dissolve
    katriona "Please, just for me, stay here"
    MC "Fine, if it'll keep you from worrying"
    katriona "Thank you"
    scene v44052
    with dissolve
    "Katriona heads down into the crater slowly"
    scene v44053
    with dissolve
    "The smooth surface still almost pristine from the day the Allestrium fell"
    scene v44054
    with dissolve
    "She's gone for 10 minutes now, you think about everything that happened"
    "Since that day you fainted right here in this place"
    MC "So much has happened..."
    scene v44055
    with dissolve
    katriona "Got it!!"
    scene v44056
    with dissolve
    MC "Is that it? I was expecting something more... shiny?"
    katriona "They do shine... On full moon"
    scene v44057
    with dissolve
    katriona "Give these to a girl during a full moon and she'll be yours forever"
    MC "Huh, something to consider..."
    scene v44058
    with dissolve
    katriona "You don't need them, you have Mida...."
    katriona "Unless you're thinking about a different future..."
    MC "Well say I was, would that interest you?"
    katriona "Maybe... Not like I'd go rat you out or anything... and then watch the fun..."
    scene v44059
    with dissolve
    MC "Ah, you had me wondering there for a second. Thought you meant something else"
    katriona "Like what?"
    if v44rejectkat == 1:
        scene v44061
        with dissolve
        MC "Nothing..."
        katriona "Oh... Sure..."
    else:
        scene v44060
        with dissolve
        "You kiss her soft lips"
        scene v44061
        with dissolve
        MC "Like you silly"
        katriona "I... I..."
        MC "Ah! first time I see you speechless!!"
        scene v44062
        with dissolve
        katriona "I always have a comeback... Unlike you flower boy"
        MC "..."
        katriona "Ahahah"

    scene v44063
    with dissolve
    katriona "Let's go home, flower boy?"
    MC "{i} Grumble"
    MC "Yeah yeah... Let's go"
    "While you travel back to the college you talk about what you saw"
    "About the Slayer city you visited"
    "The luxriousness of the baths, the types of buildings you saw"
    "And what happened in the Cathedral"
    "Of course you take note to edit out anything that she doesn't need to know about"
    "Or that the Archmage may not have shared with her"
    scene v44201
    with dissolve
    "You arrive at the college courtyard and the night has reached it's peak"
    katriona "And we're back, hope you had fun adventuring with me"
    MC "Yes, we had some fun"
    if v44rejectkat == 1:
        scene v44203
        with dissolve
        katriona "Yes... I'm sorry about what happened"
        MC "No need to, let's just forget it"
        katriona "Yes, see you later then"
    else:
        scene v44202
        with dissolve
        katriona "Yes... we did {i} giggle"
        MC "And we made a cunning plan right?"
        katriona "Ahaha, yes... We'll see about that"
        katriona "I need some rest now..."
        MC "Yeah me too"
        katriona "I'm sure you do, see you later then"

    scene v44204
    with dissolve
    "She's gone, and you are all alone in the courtyard"
    MC "Time to go to my room and sleep"
    scene v44205
    with dissolve
    MC "Yawn.... I'm going to lie down a bit..."
    scene black
    with dissolve

    scene black
    with dissolve
    scene v44206
    with dissolve
    MC "Yawn.... Oh.. It's morning already..."
    MC "I need to find some clothing..."
    MC "I can't walk around the college dressing like Kat"
    MC "Hmm... let's look around"
    "You can only find your old student robe..."
    MC "Damn you Kat..."
    "You dress in it and go out"
    $ v44citytravel = 1
    jump afterorcv39


label v44citytravel1:
    scene v4136
    with dissolve
    "You're in the throne room and Ayna is there"
    ayna "Good morning [MC]"
    MC "Hello Archmage"
    scene v4137
    with dissolve
    ayna "Is everything ok with you?"
    MC "Yeah, I'm great"
    scene v44195
    with dissolve
    ayna "Why are you wearing that?"
    MC "Kat stole my clothes..."
    ayna "Here... let me fix it... That girl..."
    scene v44196
    with dissolve
    "You feel some magic around you"
    scene v44197
    with dissolve
    ayna "So what do you think?"
    MC "It's nice.... but it's still brown..."
    ayna "Yes, but you don't look like a sack of potatoes anymore"
    MC "Aha! When we were kids..."
    MC "We always thought you just picked our stuff up at a farmer's market or something"
    scene v44198
    with dissolve
    ayna "I admit nothing..."
    MC "By the way, is there a book in the library about summoning clothes?"
    ayna "You don't know how?"
    MC "No...."
    ayna "I'm going to have to talk with Professor Rerlvam about his curriculum"
    scene v4139
    with dissolve
    ayna "Also... I need something..."
    ayna "I was wondering if you're free to help me maybe?"
    MC "Hmm... Sure... I guess, what do you need?"
    scene v4137
    with dissolve
    ayna "I need something from the shop in the city"
    MC "Really?"
    ayna "Yes..."
    MC "And..."
    ayna "And if you can, can you look around for suspicious things?"
    MC "What do you mean?"
    scene v41049
    with dissolve
    ayna "The Slayers are collapsing, the demons are showing their colors"
    ayna "I just want to make sure the city is doing fine"
    MC "I think I know what you mean..."
    scene v41050
    with dissolve
    ayna "Great... I knew you would"
    ayna "You've always been a smart one {i} giggle"
    MC "Now you sound like Kat..."
    scene v4138
    with dissolve
    ayna "I told you before... What if she is the one who sounds like me"
    MC "..."
    ayna "Thanks... I left the portal ready for you, see you later"
    MC "Later.."
    scene portalroom
    with dissolve
    MC "Guess I should go now"
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    scene v2169
    with dissolve
    "You are now in Alesterra city"
    MC "Guess I'll go check the store, maybe I could check other places too..."
    MC "After all Ayna asked me to look around"
    jump v44citytravel

label v44citytravel:
    if v44visitshop == 0:
        call screen allesterracitymapnoshipv44
    else:
        "Should I return to the college?"
        menu:
            "[abgreen]Return to the college":
                jump v44backtothecollegeayna
            "Keep looking around the city":
                call screen allesterracitymapnoshipv44




label docksallesterrav44:
    scene v021046
    with dissolve
    MC "Everything looks fine around here..."
    MC "I should look somewhere else"
    jump v44citytravel

label cityguildv44:
    scene v021005
    with dissolve
    guildm "Hello there. can I help y..."
    guildm "Oh I remember you... Where have you been?"
    MC "You know... Mage stuff..."
    MC "So how's everything around here?"
    guildm "Going great actually... No more incidents since that day"
    MC "Great... See you around"
    jump v44citytravel

label tavernv44:
    "You try to enter the tavern but the door is locked"
    MC "Strange... Maybe if I come back later..."
    jump v44citytravel

label shopv44:
    if v44visitshop == 0:
        $ v44visitshop = 1
        scene v021007
        with dissolve
        shop "Good morning, nice to see you again, what can I help you with?"
        MC "Hi, the Archmage told me to pick something up for her"
        shop "That can't be right..."
        MC "Why not?"
        shop "She came by a few minutes ago and took it herself"
        MC "What?!"
        scene v021009
        with dissolve
        shop "Yeah... Maybe she forgot to tell you?"
        MC "Forgeting things that doesn't sound like her at all"
        scene v021008
        with dissolve
        shop "Sorry that you lost your time, but I gave her the box already"
        MC "So it's a box..."
        scene v021007
        with dissolve
        MC "I'll see you some other time then, bye"
        shop "Thank you, come again"
        "Why would she tell you to come here if she came herself..."
        jump v44citytravel
    else:
        scene v021007
        with dissolve
        shop "Good morning, have you met with the Archmage?"
        MC "Hi, no... Not yet, bye"
        jump v44citytravel

label graveyardv44:
    scene v021047
    with dissolve
    "Graveyard is pretty silent..."
    MC "As it should..."
    jump v44citytravel

label runarmanorv44:
    "Locked"
    jump v44citytravel

label arnoldushousev44:
    "Locked"
    jump v44citytravel

label brothelv44:
    scene v021018
    with dissolve
    madam "Good morning young man..."
    if v44visitbrothel == 0:
        $ v44visitbrothel = 1
        madam "I'm glad you're visiting us this early, but the girls haven't arrived yet"
        MC "Actually I..."
        scene v021019
        with dissolve
        madam "Oh... Looks like you're lucky..."
        scene v021020
        with dissolve
        madam "You met Emilia before right?"

    MC "Hi..."
    madam "So what do you say?"
    madam "Emilia can satisfy all your desires for just 25 gold"
    menu:
        "[abgreen]A little fun wouldn't hurt":
            madam "That's great, you have to pay up front though"
            MC "Ok..."
            if Gold >= 25:
                $ Gold -= 25
                play sound "sounds/coin.ogg"
                MC "Here you go"
                "You lost 25 gold"
                madam "Ok Emilia take good care of this young man"
                emilia "I will!"
                jump v44emiliasexpart
            else:

                MC "I don't have the gold right now..."
                madam "Well, no gold no fun..."
                scene v021020
                with dissolve
                emilia "Bye, hope to see you again"
                "You left the brothel"
                jump v44citytravel
        "That's not what I'm here for":

            MC "I'm looking for information, nothing more"
            madam "Well... Everything is fine here..."
            madam "I hope to see you around sometime"
            "You left the brothel"
            jump v44citytravel

label v44emiliasexpart:
    scene v44164
    with dissolve
    emilia "So what should I do for you today?"
    MC "Hm..."
    scene v44165
    with dissolve
    emilia "Do you want me lying in bed?"
    MC "Go on..."
    scene v44166
    with dissolve
    emilia "Maybe you want me naked..."
    MC "It does help..."
    scene v44167
    with dissolve
    "She get's closer to you signaling you to come closer"
    "You remove your clothes and get closer"
    scene v44168
    with dissolve
    emilia "Oh... You're already this hard for me?"
    emilia "I like it..."
    MC "If you like it, suck it"
    scene v44169
    with dissolve
    "And she does..."
    "Like the professional she is, makes you feel great"
    emilia "Hmmmm... Big...."
    scene v44170
    with dissolve
    "She is now going full speed on your dick"
    MC "Ah shit.... That's great..."
    scene v44171
    with dissolve
    "She sucks and strokes faster and harder"
    "You feel you're about to cum..."
    MC "Ah... I can't"
    menu:
        "Cum":
            MC "I can't take it anymore!!"
            show shot
            with vpunch
            scene v44172
            with dissolve
            show shot
            with hpunch
            hide shot
            MC "AHHHH!!!"
            emilia "Hmmmm"
            scene v44173
            with dissolve
            emilia "So much cum... You really saved it for me..."
            MC "Shit..."
            scene v44174
            with dissolve
            emilia "And it's tasty..."
            MC "Glad you like it..."
            jump v44endemilia
        "[abgreen]Resist":

            MC "Lie on the bed, I'm going to fuck you hard"
            scene v44175
            with dissolve
            "She complies"
            emilia "Hmm... Promises..."
            "You grab her legs, spread them..."
            scene v44176
            with dissolve
            "And you shove your dick all the way in"
            emilia "AHHH!!! FUCK!!"
            "You waste no time and start pumping as hard as you can"
            scene v44177
            with dissolve
            MC "Take it all!!"
            emilia "Ah.... YES!! More!"
            "You feel you're close to orgasm"
            menu:
                "Cum inside":
                    MC "I can't hold it anymore... Ahhhh"
                    show shot
                    with vpunch
                    scene v44177c
                    with dissolve
                    show shot
                    with hpunch
                    hide shot
                    MC "FUUUCK!!! Yeah..."
                    jump v44endemilia
                "Pull out":

                    MC "I can't hold it anymore... Ahhhh"
                    show shot
                    with vpunch
                    scene v44178
                    with dissolve
                    show shot
                    with hpunch
                    hide shot
                    MC "FUUUCK!!! Yeah..."
                    scene v44179
                    with dissolve
                    emilia "So much cum... You really saved it for me..."
                    MC "Shit..."
                    emilia "And it's tasty..."
                    MC "Glad you like it..."
                    jump v44endemilia
                "[abgreen]Resist":

                    MC "Turn around I'm fucking you from behind"
                    scene v44180
                    with dissolve
                    "She does what you ask"
                    emilia "Like this...?"
                    scene v44181
                    with dissolve
                    "Instead of answering you get closer to her"
                    menu:
                        "Put it in her ass":
                            scene v44182
                            with dissolve
                            MC "I'm going to use this hole now..."
                            emilia "Hmmm... Yes... Use it"
                            MC "You little slut..."
                            emilia "You're already fucking me, no need for more flatery"
                            scene v44183
                            with dissolve
                            "You shove your dick all the way in"
                            emilia "AHHHH!! Fuck!!"
                            MC "Take it!!"
                            emilia "Ah...."
                            "This is too intense... You can't hold it anymore"
                            MC "I can't take it anymore.... Fuck!!"
                            show shot
                            with vpunch
                            scene v44183c
                            with dissolve
                            show shot
                            with hpunch
                            hide shot
                            MC "Hell yeah.... {i} pant pant..."
                            scene v44184
                            with dissolve
                            emilia "You filled my ass completely..."
                            MC "Yes I did..."
                            jump v44endemilia
                        "Put it in her pussy":

                            scene v44185
                            with dissolve
                            MC "I'm going to go full speed now"
                            emilia "Hmmm... Yes... do it"
                            MC "You little slut..."
                            emilia "You're already fucking me, no need for more flatery"
                            scene v44186
                            with dissolve
                            "You shove your dick all the way in"
                            emilia "AHHHH!! Fuck!!"
                            MC "Take it!!"
                            emilia "Ah...."
                            scene v44185
                            with dissolve
                            "This is too intense... You can't hold it anymore"
                            MC "I can't take it anymore.... Fuck!!"
                            show shot
                            with vpunch
                            scene v44185c
                            with dissolve
                            show shot
                            with hpunch
                            hide shot
                            MC "Hell yeah.... {i} pant pant..."
                            emilia "You filled me up completely..."
                            MC "Yes I did..."
                            jump v44endemilia


label v44endemilia:
    if v44visitbrothel <= 1:
        scene v44187
        with dissolve
        $ v44visitbrothel = 2
        emilia "This was really good... I hope you come back again"
        MC "I'll be tempted to..."
        scene v44188
        with dissolve
        "As you are leaving the brothel you see another girl talking with madam Claude"
        madam "Yes Tenizha, that patron is very important..."
        madam "Take good care of him..."
        scene v44189
        with dissolve
        madam "Oh you're back... Hope you had fun"
        MC "I did...."
        madam "You can go now Tenizha"
        scene v44190
        with dissolve
        MC "Who is that?"
        madam "Hot isn't she?"
        madam "Maybe you can come later and have fun with her..."
        scene v44191
        with dissolve
        MC "I'll definitely think about it..."
        if v44visitshop == 1:
            "You should return to the college now..."
        jump v44citytravel
    else:
        scene v44187
        with dissolve
        emilia "This was really good... I hope you come back again"
        MC "I'll be tempted to..."
        jump v44citytravel


label v44backtothecollegeayna:
    "You use the stone to teleport you back to the college"
    play sound "sounds/portaltravel.wav"
    $ renpy.movie_cutscene("opti/portal.webm")
    scene portalroom
    with dissolve
    MC "And we're back here... now let's try to find what's going on"



    jump v45start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
