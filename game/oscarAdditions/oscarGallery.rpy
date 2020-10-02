init python:
    galleryCharacter = "All"
    galleryPageNumber = 1

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1
        return

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1
        return

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["All", ""],
    ],
    "All": {
    1: [
    ["keepbath", {}, "/images/bath001/aynabath013.jpg"], # Katriona + Ayna
    ["galleryScene1", {}, "/images/Bredita/bredita018.jpg"], # Bredita
    ["sweetdream", {}, "/images/Dreams/heaven017.jpg"], # Ayna + Katriona
    ["sunbanglili001", {}, "/images/suntakolili/sunlili020.jpg"], # lili
    ["fuckgisellev2", {"helparnoldus":0}, "/images/v0.2/2stage/v2137.jpg"], # giselle
    ["emiliasexpart", {}, "/images/v0.2.1/v021033.jpg"], # emilia
    ["v25", {}, "/images/v0.2.5/v25154.jpg"], # Bredita + Ayna
    ["v026", {}, "/images/v0.2.6A/v26a009.jpg"], # Yumiko
    ],
    2: [
    ["galleryScene2", {}, "/images/v0.2.6np/v26n102.jpg"], # Master Vampire
    ["v026neutralpart2", {"isabellalove":99, "Points":99}, "/images/v0.2.6np/v26n137.jpg"], # Isabella
    ["yourroomv3e", {"afteralinepart":1, "midaown":0, "midalove":99}, "/images/v0.3/evil/v3e088.jpg"], # Amida
    ["afterfannayv3g", {}, "/images/v0.3/good/v3g088.jpg"], # Amida
    ["v3sheknowsisa", {"isabellalove":99}, "/images/v0.3.1n/v31n091.jpg"], # Isabella
    ["galleryScene3", {}, "/images/v0.3.2g/v32g060.jpg"], # Zordruza
    ["v33salazar", {"Points":99}, "/images/v0.3.3e/v33066.jpg"], # Lili
    ["v36fannay", {}, "/images/v0.3.6/v36045.jpg"], # Fannay + Amida
    ],
    3: [
    ["end_1_nothing_else_matters", {}, "/images/v0.3.6/v36112.jpg"], # Aelia + Amida + Ayna + Isabella + Lili
    ["galleryScene4", {}, "/images/v0.3.7/v37072.jpg"], # Enainia
    ["tisbetterthan2", {"my_path_is":"good", "midacorr":99}, "/images/v0.3.8/v38043.jpg"], # amida + fannay
    ["soloingisgood2", {}, "/images/v0.3.8/v38081.jpg"], # Amida
    ["evilpartroomv38", {}, "/images/v0.3.8/v38135.jpg"], # Fannay
    ["orcbedv39", {}, "/images/v0.3.9/v39136.jpg"], # Yotul
    ["v4hannasex", {}, "/images/v0.4/v4046.jpg"], # Hanna
    ["v43somehanna", {"hannacorr":99, "calessapet":2}, "/images/v0.4/v4105.jpg"], # Calessa + Hanna
    ],
    4: [
    ["v4fuckpethall", {}, "/images/v0.4/v4198.jpg"], # Calessa
    ["v4fuck50room", {}, "/images/v0.4/v4215.jpg"], # Calessa
    ["v4runartalk", {}, "/images/v0.4.1/v41114.jpg"], # Mida
    ["galleryScene6", {}, "/images/v0.4.2/v42048.jpg"], # Carilielle
    ["v43isasex", {"isabellalove":99}, "/images/v0.4.3/v43109.jpg"], # Isabella
    ["v43lilisex", {"lilicorr":99}, "/images/v0.4.3/v43135.jpg"], # Lili
    ["v43zorsex", {}, "/images/v0.4.3/v43166.jpg"], # Zor
    ["galleryScene7", {}, "/images/v0.15/missions/v15mission073.jpg"], # Amida
    ],
    5: [
    ["galleryScene8", {}, "/images/v0.18/breditalili/v18044.jpg"], # Bredita, Lili
    ["postlibrarystory", {}, "/images/v0.18/devil sibs/v18101.jpg"],
    ["v18midasex2", {"midacorr":99, "midalove":99, "firstgoingv18":0}, "/images/v0.18/mcroom/v18137.jpg"],
    ["beforeGalleryScene9", {}, "/images/y1/1y065.jpg"],
    ["v44sexyotul", {}, "/images/v0.4.4/v44012.jpg"],
    ["v44deadslime", {"katrionalove":99}, "/images/v0.4.4/v44129.jpg"],
    ["v44emiliasexpart", {}, "/images/v0.4.4/v44181.jpg"],
    ],
    },
    }

label galleryNameChange:
    default persistent.player_name = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("What's your name?", default='Hjard')
    return

# screen sceneGalleryMenu():
#     tag menu
#     modal True
#     add "#23272a"
#
#     text "Oscar's Scene Gallery":
#         style "galleryHeader"
#         xcenter 0.5
#         ycenter 165
#
#     vbox:
#         spacing 20
#         pos (1868, 50)
#
#         fixed:
#             xmaximum 186
#             ymaximum 76
#             xanchor 1.0
#
#             imagebutton:
#                 action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
#                 idle "/oscarAdditions/images/button.png"
#                 hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
#             text "Back":
#                 style "galleryBody"
#                 xcenter 0.5
#                 ycenter 0.5
#
#         imagebutton:
#             action OpenURL("https://www.patreon.com/oscarsix/overview")
#             idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
#             hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
#             xanchor 1.0
#
#     vpgrid:
#         cols 4
#         xspacing 50
#         yspacing 37
#         pos (117, 360)
#
#         for i in sceneGalleryMenuDict["galleryMenu"]:
#             vbox:
#                 imagebutton:
#                     action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
#                     idle Transform(i[1], zoom=0.2)
#                     hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
#                 text i[0]:
#                     style "galleryBody"
#                     xcenter 0.5

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "galleryBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"player_name":persistent.player_name}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)


label beforeGalleryScene9:
    menu:
        "OscarSix" "Path?"
        "Good":
            $ wheretoafterslayerbath = "good"
        "Neutral":
            $ wheretoafterslayerbath = "neutral"
        "Evil":
            $ wheretoafterslayerbath = "Evil"
    jump galleryScene9
