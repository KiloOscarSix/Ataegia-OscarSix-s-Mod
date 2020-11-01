define AB = Character("AB", who_color="380B61")

init python:
    abendings = ("[New Ending]") # [abgreen] [abendings]
    abrandompoint = ("[Random point]") # [abgreen] [abrandompoint]
    abstoneuses = ("[+1 Stoneuses]") # [abkarmacolor] [abstoneuses]
    abstoneuses2 = ("[+2 Stoneuses]") # [abkarmacolor] [abstoneuses2]
    abpregnantwtf = ("[+1 Pregnant]") # [abcorruptioncolor] [abpregnantwtf]
    abalignment = ("[+1 Alignment]") # [abgreen] [abalignment]
    abalignment2 = ("[+2 Alignment]") # [abgreen] [abalignment2]
    abalignmentlove = ("[+1 Alignment/Love]") # [abgreen] [abalignmentlove]
    abnoalignment = ("[-1 Alignment]") # [abred] [abnoalignment]
    abnoalignmentgold15 = ("[-1 Alignment/+15 Gold]") # [abred] [abnoalignmentgold15]
    abnoalignment2 = ("[-2 Alignment]") # [abred] [abnoalignment2]
    abnoalignment5 = ("[-5 Alignment]") # [abred] [abnoalignment5]
    abnoalignmentcorruption = ("[-1 Alignment/+1 Corruption]") # [abred] [abnoalignmentcorruption]
    abalignmenthealiluspoints = ("[+1 Alignment/Heal/Iluspoints]") # [abgreen] [abalignmenthealiluspoints]
    abaltepoint = ("[+1 Altepoint]") # [abgreen] [abaltepoint]
    abaltepoints2 = ("[+2 Altepoints]") # [abgreen] [abaltepoints2]
    abaltepoints3 = ("[+3 Altepoints]") # [abgreen] [abaltepoints3]
    abaltedestpoints = ("[+1 Alte/Destpoints]") # [abgreen] [abaltedestpoints]
    abdestpoint = ("[+1 Destpoint]") # [abgreen] [abdestpoint]
    abdestpoints2 = ("[+2 Destpoints]") # [abgreen] [abdestpoints2]
    abdestpoints3 = ("[+3 Destpoints]") # [abgreen] [abdestpoints3]
    abhealpoint = ("[+1 Healpoint]") # [abgreen] [abhealpoint]
    abhealpoints2 = ("[+2 Healpoints]") # [abgreen] [abhealpoints2]
    abhealpoints3 = ("[+3 Healpoints]") # [abgreen] [abhealpoints3]
    abiluspoint = ("[+1 Iluspoint]") # [abgreen] [abiluspoint]
    abiluspoints2 = ("[+2 Iluspoints]") # [abgreen] [abiluspoints2]
    abiluspoints3 = ("[+3 Iluspoints]") # [abgreen] [abiluspoints3]
    abmystpoint = ("[+1 Mystpoint]") # [abgreen] [abmystpoint]
    abmystpoints2 = ("[+2 Mystpoints]") # [abgreen] [abmystpoints2]
    abmystpoints3 = ("[+3 Mystpoints]") # [abgreen] [abmystpoints3]
    abnecropoint = ("[+1 Necropoint]") # [abgreen] [abnecropoint]
    abnecropoints2 = ("[+2 Necropoints]") # [abgreen] [abnecropoints2]
    abnecropoints3 = ("[+3 Necropoints]") # [abgreen] [abnecropoints3]
    abnecrosummpoints = ("[+1 Necro/Summpoints]") # [abgreen] [abnecrosummpoints]
    absummpoint = ("[+1 Summpoint]") # [abgreen] [absummpoint]
    absummpoints2 = ("[+2 Summpoints]") # [abgreen] [absummpoints2]
    absummpoints3 = ("[+3 Summpoints]") # [abgreen] [absummpoints3]
    abgold2 = ("[+2 Gold]") # [abgreen] [abgold2]
    abgold10 = ("[+10 Gold]") # [abgreen] [abgold10]
    abgold15 = ("[+15 Gold]") # [abgreen] [abgold15]
    abgold17 = ("[+17 Gold]") # [abgreen] [abgold17]
    abgold17 = ("[+50 Gold]") # [abgreen] [abgold50]
    abnogold = ("[-1 Gold]") # [abred] [abnogold]
    abnogold5 = ("[-5 Gold]") # [abred] [abnogold5]
    abaffection = ("[+1 Affection]") # [ablovecolor] [abaffection]
    abcorruption = ("[+1 Corruption]") # [abcorruptioncolor] [abcorruption]
    abmidabreditalovecorruption = ("[+1 Mida's Corruption/Bredita's Love]") # [abcorruptioncolor] [abmidabreditalovecorruption]
    abcorrulove = ("[Corruption/Love Points]") # [abgreen] [abcorrulove]
    abcorruptionlove = ("[+1 Corruption/Love]") # [abcorruptioncolor] [abcorruptionlove]
    abnocorruptionlove = ("[-1 Corruption/Love]") # [abred] [abnocorruptionlove]
    ablove = ("[+1 Love]") # [ablovecolor] [ablove]
    abloveboth = ("[+1 Love for both]") # [ablovecolor] [abloveboth]
    abaynalove = ("[+1 Ayna's Love]") # [ablovecolor] [abaynalove]
    abreditalove = ("[+1 Bredita's Love]") # [ablovecolor] [abreditalove]
    abmidalove = ("[+1 Mida's Love]") # [ablovecolor] [abmidalove]
    abnoloveidiot = ("[-1 Love]") # [abred] [abnoloveidiot]
    abnoloveidiot2 = ("[-2 Love]") # [abred] [abnoloveidiot2]
    abnoloveidiot3 = ("[-3 Love]") # [abred] [abnoloveidiot3]
    abgreen = "{color=#0f0}" # [abgreen]
    abkarmacolor = "{color=#FF8C00}" # [abkarmacolor]
    abred = "{color=#f00}" # [abred]
    ablovecolor = "{color=#FF69B4}" # [ablovecolor]
    abhatecolor = "{color=#DC143C}" # [abhatecolor]
    abcorruptioncolor = "{color=#f47fff}" # [abcorruptioncolor]
    abobeycolor = "{color=#FFA500}" # [abobeycolor]

    gr = "{color=#0f0}"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    python:
        persistent.y = renpy.input("Answer with your name.", default="Kyle")
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    python:
        y = renpy.input("Answer with your name.", default="Kyle")
    mod "Names successful changed"
    return
