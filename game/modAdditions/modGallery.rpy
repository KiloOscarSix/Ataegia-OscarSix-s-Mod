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
            self.thumbnail = os.path.join("/images/", "{}".format(thumbnail))
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

default galleryPageNumber = 1
default scopeDict = {}

define galleryMenu = [
["Mida", "/images/v0.15/init/v015011.jpg"],
["Lili", "/images/v0.15/init/v015096.jpg"],
["Ayna", "/images/v0.15/init/v015090.jpg"],
["Isabella", "/images/v0.2.1/v021045.jpg"],
["Katriona", "/images/v0.15/init/v015094.jpg"],
["Bredita", "/images/Bredita/bredita003.jpg"],
["Fannay", "/images/v0.15/init/v015018.jpg"],
["Other", "/images/v0.4.2/v42112.jpg"],
]

define Mida = GalleryItem("Mida", 1, "yourroomv3e", "v0.3/evil/v3e095.jpg", {"afteralinepart":1, "midaown":0, "midalove":99}) # Mida
define Mida = GalleryItem("Mida", 1, "afterfannayv3g", "v0.3/good/v3g088.jpg") # Mida
define Mida = GalleryItem("Mida", 1, "v36fannay", "v0.3.6/v36045.jpg") # Fannay + Mida
define Mida = GalleryItem("Mida", 1, "end_1_nothing_else_matters", "v0.3.6/v36112.jpg") # Aelia + Mida + Ayna + Isabella + Lili
define Mida = GalleryItem("Mida", 1, "tisbetterthan2", "v0.3.8/v38043.jpg", {"my_path_is":"good", "midacorr":99}) # Mida + Fannay
define Mida = GalleryItem("Mida", 1, "soloingisgood2", "v0.3.8/v38081.jpg") # Mida
define Mida = GalleryItem("Mida", 1, "v4runartalk", "v0.4.1/v41114.jpg") # Mida
define Mida = GalleryItem("Mida", 1, "galleryScene7", "v0.15/missions/v15mission073.jpg") # Mida
define Mida = GalleryItem("Mida", 2, "v18midasex2", "v0.18/mcroom/v18137.jpg", {"midacorr":99, "midalove":99, "firstgoingv18":0}) # Mida
define Mida = GalleryItem("Mida", 2, "galleryScene11", "v0.4.6/v46147.jpg")
define Mida = GalleryItem("Mida", 2, "v47sexmidakoneko", "v0.4.7/v47180.jpg")


define Liliana = GalleryItem("Lili", 1, "sunbanglili001", "suntakolili/sunlili020.jpg") # Lili
define Liliana = GalleryItem("Lili", 1, "v33salazar", "v0.3.3e/v33066.jpg", {"Points":99}) # Lili
define Liliana = GalleryItem("Lili", 1, "end_1_nothing_else_matters", "v0.3.6/v36112.jpg") # Aelia + Mida + Ayna + Isabella + Lili
define Liliana = GalleryItem("Lili", 1, "v43lilisex", "v0.4.3/v43135.jpg", {"lilicorr":99}) # Lili
define Liliana = GalleryItem("Lili", 1, "galleryScene8", "v0.18/breditalili/v18044.jpg") # Bredita, Lili
define Liliana = GalleryItem("Lili", 1, "postlibrarystory", "v0.18/devil sibs/v18101.jpg") # Lili
define LilianaFannay = GalleryItem("Lili", 1, "v47partyfannaylili", "v0.4.7/v47227.jpg")


define Ayna = GalleryItem("Ayna", 1, "keepbath", "bath001/aynabath013.jpg") # Katriona + Ayna
define Ayna = GalleryItem("Ayna", 1, "sweetdream", "Dreams/heaven017.jpg") # Ayna + Katriona
define Ayna = GalleryItem("Ayna", 1, "v25", "v0.2.5/v25154.jpg") # Bredita + Ayna
define Ayna = GalleryItem("Ayna", 1, "end_1_nothing_else_matters", "v0.3.6/v36112.jpg") # Aelia + Mida + Ayna + Isabella + Lili
define Ayna = GalleryItem("Ayna", 1, "galleryScene10", "v0.4.5/v45112.jpg") # Ayna
define AynaKatriona = GalleryItem("Other", 3, "v47afterallparty", "v0.4.7/v47259.jpg")

define isabella = GalleryItem("Isabella", 1, "v026neutralpart2", "v0.2.6np/v26n137.jpg", {"isabellalove":99, "Points":99}) # Isabella
define isabella = GalleryItem("Isabella", 1, "v3sheknowsisa", "v0.3.1n/v31n091.jpg", {"isabellalove":99}) # Isabella
define isabella = GalleryItem("Isabella", 1, "end_1_nothing_else_matters", "v0.3.6/v36112.jpg") # Aelia + Mida + Ayna + Isabella + Lili
define isabella = GalleryItem("Isabella", 1, "v43isasex", "v0.4.3/v43109.jpg", {"isabellalove":99}) # Isabella

define Katriona = GalleryItem("Katriona", 1, "keepbath", "bath001/aynabath013.jpg") # Katriona + Ayna
define Katriona = GalleryItem("Katriona", 1, "sweetdream", "Dreams/heaven017.jpg") # Ayna + Katriona
define Katriona = GalleryItem("Katriona", 1, "v44deadslime", "v0.4.4/v44129.jpg", {"katrionalove":99}) # Katriona
define AynaKatriona = GalleryItem("Other", 3, "v47afterallparty", "v0.4.7/v47259.jpg")

define bredita = GalleryItem("Bredita", 1, "galleryScene1", "Bredita/bredita018.jpg") # Bredita
define bredita = GalleryItem("Bredita", 1, "v25", "v0.2.5/v25154.jpg") # Bredita + Ayna
define bredita = GalleryItem("Bredita", 1, "galleryScene8", "v0.18/breditalili/v18044.jpg") # Bredita, Lili

define Fannay = GalleryItem("Fannay", 1, "v36fannay", "v0.3.6/v36045.jpg") # Fannay + Mida
define Fannay = GalleryItem("Fannay", 1, "tisbetterthan2", "v0.3.8/v38043.jpg", {"my_path_is":"good", "midacorr":99}) # Mida + Fannay
define Fannay = GalleryItem("Fannay", 1, "evilpartroomv38", "v0.3.8/v38135.jpg") # Fannay
define Fannay = GalleryItem("Fannay", 1, "v46fannayscene", "v0.4.6/v46102.jpg")
define LilianaFannay = GalleryItem("Lili", 1, "v47partyfannaylili", "v0.4.7/v47227.jpg")


define Giselle = GalleryItem("Other", 1, "fuckgisellev2", "v0.2/2stage/v2137.jpg", {"helparnoldus":0})
define Emilia = GalleryItem("Other", 1, "emiliasexpart", "v0.2.1/v021033.jpg")
define Yumiko = GalleryItem("Other", 1, "v026", "v0.2.6A/v26a009.jpg")
define Vampire = GalleryItem("Other", 1, "galleryScene2", "v0.2.6np/v26n102.jpg")
define Zordruza = GalleryItem("Other", 1, "galleryScene3", "v0.3.2g/v32g060.jpg")
define Enainia = GalleryItem("Other", 1, "galleryScene4", "v0.3.7/v37072.jpg")
define Yotul = GalleryItem("Other", 1, "orcbedv39", "v0.3.9/v39136.jpg")
define Hanna = GalleryItem("Other", 1, "v4hannasex", "v0.4/v4046.jpg")
define CalessaHanna = GalleryItem("Other", 2, "v43somehanna", "v0.4/v4105.jpg", {"hannacorr":99, "calessapet":2})
define Calessa = GalleryItem("Other", 2, "v4fuckpethall", "v0.4/v4198.jpg")
define Calessa = GalleryItem("Other", 2, "v4fuck50room", "v0.4/v4215.jpg")
define Carilielle = GalleryItem("Other", 2, "galleryScene6", "v0.4.2/v42048.jpg")
define Zor = GalleryItem("Other", 2, "v43zorsex", "v0.4.3/v43166.jpg")
define Carilielle = GalleryItem("Other", 2, "beforeGalleryScene9", "y1/1y065.jpg")
define Yotul = GalleryItem("Other", 2, "v44sexyotul", "v0.4.4/v44012.jpg")
define Emilia = GalleryItem("Other", 2, "v44emiliasexpart", "v0.4.4/v44181.jpg")
define Ataegina = GalleryItem("Other", 3, "v45gooddream", "v0.4.5/v45029.jpg", {"Points":99})
define Lust = GalleryItem("Other", 3, "v45evildream", "v0.4.5/v45132.jpg", {"Points":-99})
define Katla = GalleryItem("Other", 3, "v45neutraldream", "v0.4.5/v45147.jpg", {"Points":0})

label galleryNameChange:
    default persistent.player_name = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("What's your name?", default='Hjard')

    $ scopeDict = {"player_name":persistent.player_name}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action Function(galleryDecreasePageNumber)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)