init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

define galleryMenu = [
["Mida", ""],
["Lili", ""],
["Ayna", ""],
["Isabella", ""],
["Katriona", ""],
["Bredita", ""],
["Fannay", ""], # 3
["Other", ""],
]

define all = GalleryItem("All", 1, "keepbath", "bath001/aynabath013.jpg") # Katriona + Ayna
define all = GalleryItem("All", 1, "galleryScene1", "Bredita/bredita018.jpg") # Bredita
define all = GalleryItem("All", 1, "sweetdream", "Dreams/heaven017.jpg") # Ayna + Katriona
define all = GalleryItem("All", 1, "sunbanglili001", "suntakolili/sunlili020.jpg") # Lili
define all = GalleryItem("All", 1, "fuckgisellev2", "v0.2/2stage/v2137.jpg", {"helparnoldus":0}) # Giselle
define all = GalleryItem("All", 1, "emiliasexpart", "v0.2.1/v021033.jpg") # Emilia
define all = GalleryItem("All", 1, "v25", "v0.2.5/v25154.jpg") # Bredita + Ayna
define all = GalleryItem("All", 1, "v026", "v0.2.6A/v26a009.jpg") # Yumiko

define all = GalleryItem("All", 2, "galleryScene2", "v0.2.6np/v26n102.jpg") # Master Vampire
define all = GalleryItem("All", 2, "v026neutralpart2", "v0.2.6np/v26n137.jpg", {"isabellalove":99, "Points":99}) # Isabella
define all = GalleryItem("All", 2, "yourroomv3e", "v0.3/evil/v3e095.jpg", {"afteralinepart":1, "midaown":0, "midalove":99}) # Mida
define all = GalleryItem("All", 2, "afterfannayv3g", "v0.3/good/v3g088.jpg") # Mida
define all = GalleryItem("All", 2, "v3sheknowsisa", "v0.3.1n/v31n091.jpg", {"isabellalove":99}) # Isabella
define all = GalleryItem("All", 2, "galleryScene3", "v0.3.2g/v32g060.jpg") # Zordruza
define all = GalleryItem("All", 2, "v33salazar", "v0.3.3e/v33066.jpg", {"Points":99}) # Lili
define all = GalleryItem("All", 2, "v36fannay", "v0.3.6/v36045.jpg") # Fannay + Mida

define all = GalleryItem("All", 3, "end_1_nothing_else_matters", "v0.3.6/v36112.jpg") # Aelia + Mida + Ayna + Isabella + Lili
define all = GalleryItem("All", 3, "galleryScene4", "v0.3.7/v37072.jpg") # Enainia
define all = GalleryItem("All", 3, "tisbetterthan2", "v0.3.8/v38043.jpg", {"my_path_is":"good", "midacorr":99}) # Mida + Fannay
define all = GalleryItem("All", 3, "soloingisgood2", "v0.3.8/v38081.jpg") # Mida
define all = GalleryItem("All", 3, "evilpartroomv38", "v0.3.8/v38135.jpg") # Fannay
define all = GalleryItem("All", 3, "orcbedv39", "v0.3.9/v39136.jpg") # Yotul
define all = GalleryItem("All", 3, "v4hannasex", "v0.4/v4046.jpg") # Hanna
define all = GalleryItem("All", 3, "v43somehanna", "v0.4/v4105.jpg", {"hannacorr":99, "calessapet":2}) # Calessa + Hanna

define all = GalleryItem("All", 4, "v4fuckpethall", "v0.4/v4198.jpg") # Calessa
define all = GalleryItem("All", 4, "v4fuck50room", "v0.4/v4215.jpg") # Calessa
define all = GalleryItem("All", 4, "v4runartalk", "v0.4.1/v41114.jpg") # Mida
define all = GalleryItem("All", 4, "galleryScene6", "v0.4.2/v42048.jpg") # Carilielle
define all = GalleryItem("All", 4, "v43isasex", "v0.4.3/v43109.jpg", {"isabellalove":99}) # Isabella
define all = GalleryItem("All", 4, "v43lilisex", "v0.4.3/v43135.jpg", {"lilicorr":99}) # Lili
define all = GalleryItem("All", 4, "v43zorsex", "v0.4.3/v43166.jpg") # Zor
define all = GalleryItem("All", 4, "galleryScene7", "v0.15/missions/v15mission073.jpg") # Mida

define all = GalleryItem("All", 5, "galleryScene8", "v0.18/breditalili/v18044.jpg") # Bredita, Lili
define all = GalleryItem("All", 5, "postlibrarystory", "v0.18/devil sibs/v18101.jpg") # Lili
define all = GalleryItem("All", 5, "v18midasex2", "v0.18/mcroom/v18137.jpg", {"midacorr":99, "midalove":99, "firstgoingv18":0}) # Mida
define all = GalleryItem("All", 5, "beforeGalleryScene9", "y1/1y065.jpg") # Carilielle
define all = GalleryItem("All", 5, "v44sexyotul", "v0.4.4/v44012.jpg") # Yotul
define all = GalleryItem("All", 5, "v44deadslime", "v0.4.4/v44129.jpg", {"katrionalove":99}) # Katriona
define all = GalleryItem("All", 5, "v44emiliasexpart", "v0.4.4/v44181.jpg") # Emilia
define all = GalleryItem("All", 5, "v45gooddream", "v0.4.5/v45029.jpg", {"Points":99}) # Ataegina

define all = GalleryItem("All", 6, "galleryScene10", "v0.4.5/v45112.jpg") # Anya
define all = GalleryItem("All", 6, "v45evildream", "v0.4.5/v45132.jpg", {"Points":-99}) # Lust
define all = GalleryItem("All", 6, "v45neutraldream", "v0.4.5/v45147.jpg", {"Points":0}) # Katla

default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.player_name = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("What's your name?", default='Hjard')

    $ scopeDict = {"player_name":persistent.player_name}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
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
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/modAdditions/images/button.png"
                hover Transform(im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/modAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/modAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="All"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
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
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/modAdditions/images/button.png"
                    hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)

label beforeGalleryScene9:
    menu:
        mod "Path?"
        "Good":
            $ wheretoafterslayerbath = "good"
        "Neutral":
            $ wheretoafterslayerbath = "neutral"
        "Evil":
            $ wheretoafterslayerbath = "Evil"
    jump galleryScene9
