



screen mcroomintro:
    imagemap:
        ground "roombg01.jpg"
        hover "roombg02.jpg"

        hotspot (742, 1, 480, 1214) clicked Jump ("introdoor")
        hotspot (1, 418, 419, 640) clicked Jump ("introbed")
        hotspot (1272, 80, 510, 710) clicked Jump ("introcloset")

init -1:
    $ v38 = 0
    $ cheaterfix = 0
    $ enemyHP = 50
    $ enemymaxHP = 50
    $ HP = 50
    $ MP = 50
    $ maxHP = 50
    $ maxMP = 50

    $ skillsum = 0

screen hpbar:
    text "[enemyname]" xalign 0.5 yalign 0.

    bar value StaticValue(1.*enemyHP/enemymaxHP):
        xalign 0.5 yalign 0.05
        xmaximum 550
        ymaximum 60
        left_bar Frame("hpfull.png", 0, 10)
        right_bar Frame("hpempty.png", 0, 10)

screen MC_bars:
    zorder 1
    vbar value StaticValue(1.*HP/maxHP):
        xalign 0.02 yalign 0.99
        xmaximum 250
        ymaximum 250
        left_bar Frame("orbhpempty.png", 0, 10)
        right_bar Frame("orbhpfull.png", 0, 10)


    vbar value StaticValue(1.*MP/maxMP):
        xalign 0.99 yalign 0.99
        xmaximum 250
        ymaximum 250
        left_bar Frame("orbmpempty.png", 0, 10)
        right_bar Frame("orbmpfull.png", 0, 10)





define n = nvl_narrator

define nar = Character("Dark Figure", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff0000", image="narface", window_left_padding=110)
image side narface = "narfacedw.png"

define MC = DynamicCharacter("player_name", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#104aa8")
define god = Character("Goddess Ataegina", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ffc70f", image="ataeface", window_left_padding=120)
image side ataeface = "ataeface.png"
define ocsav = Character("God Ocsav", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#104aa8")
define mom = Character("Mother", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#316323")
define dad = Character("Father", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#592222")
define sis = Character("Sister", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#18dbd1")


define ayna = Character("Archmage Ayna", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#974999", image="aynaface", window_left_padding=110)
image side aynaface = "aynaface.png"

define yayna = Character("Ayna", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#974959", image="yaynaface", window_left_padding=110)
image side yaynaface = "yaynaface.png"

define katarro = Character("Master Katarro", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#11eff7", image="katarroface", window_left_padding=110)
image side katarroface = "katarroface.png"

define ykatarro = Character("Katarro", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#11eff7", image="ykatarroface", window_left_padding=110)
image side ykatarroface = "ykatarroface.png"

define suntako = Character("Master Suntako", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#d36b0a", image="sunface", window_left_padding=110)
image side sunface = "sunface.png"

define Qa = Character("Mistress Qa'arra", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#18dbd1", image="qaface", window_left_padding=110)
image side qaface = "qaface.png"

define katriona = Character("Mistress Katriona", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e69dea", image="katface", window_left_padding=110)
image side katface = "katface.png"

define silvana = Character("Mistress Silvana", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#00f95b", image="silface", window_left_padding=110)
image side silface = "silface.png"

define bojay = Character("Master Bojay", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#d0e5e4", image="bojface", window_left_padding=110)
image side bojface = "bojface.png"


define mida = Character("Mida", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="midaface", window_left_padding=110)
image side midaface = "midaface.png"

define amida = Character("Mida", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="amidaface", window_left_padding=110)
image side amidaface = "amidaface.png"

define amida2 = Character("Illusion Mida", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2eee",image="amidaface", window_left_padding=110)
image side amidaface = "amidaface.png"

define tmida = Character("Mida", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="tmidaface", window_left_padding=110)
image side tmidaface = "tmidaface.png"

define koneko = Character("Koneko", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#fc05fc",image="konekoface", window_left_padding=110)
image side konekoface = "konekoface.png"

define akoneko = Character("Koneko", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#fc05fc",image="akonekoface", window_left_padding=110)
image side akonekoface = "akonekoface.png"

define kitargo = Character("Kitargo", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#592222",image="kitargoface", window_left_padding=110)
image side kitargoface = "kitargoface.png"

define jollo = Character("Jollo", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#316323")

define hatoshi = Character("Hatoshi", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#974999",image="hatoshiface", window_left_padding=110)
image side hatoshiface = "hatoshiface.png"

define fannay = Character("Fannay", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b",image="fannayface", window_left_padding=110)
image side fannayface = "fannayface.png"

define klathu = Character("Klathu", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ffffff")

define ulrich = Character("Ulrich", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#316323")

define jessica = Character("Jessica", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#553456",image="jesseface", window_left_padding=110)
image side jesseface = "jesseface.png"


define Bredita = Character("Bredita Darkheart", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#000000", image="bredface", window_left_padding=110)
image side bredface = "bredface.png"

define yBredita = Character("Bredita", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe", image="ybredface", window_left_padding=110)
image side ybredface = "ybredface.png"

define Nonen = Character("Unknown", who_outlines=[(absolute(1),"#ff00",absolute(0),absolute(0))], who_italic=True, color="#ff0000", image="face")

define demon = Character("Demon", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#000000")

define goggos = Character("Goggos", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#550000", image="gogface", window_left_padding=110)
image side gogface = "gogface.png"

define zegladar = Character("Zegladar", who_outlines=[(absolute(1),"#f0f",absolute(0),absolute(0))], who_italic=True, color="#550000", image="zegface", window_left_padding=110)
image side zegface = "zegface.png"


define fvoice = Character("Female Voice", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e88bd8", image="face")

define scl = Character("Scantily Clad Lady", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e88bd8", image="face")

define mvoice = Character("Male Voice", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#351010")


define prof = Character("Professor Rerlvam", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e804",image="revface", window_left_padding=110)
image side revface = "revface.png"

define profalter = Character("Professor Abaashi", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e804")

define profmys = Character("Professor Hishigo", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e804")

define fprof = Character("Professor Anita", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e804d5")

define sven = Character("Sven", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#351010")

define lili = Character("Liliana", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="liliface", window_left_padding=110)
image side liliface = "liliface.png"

define yisnna = Character("Yisnna the librarian", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="yisnnaface", window_left_padding=110)
image side yisnnaface = "yisnnaface.png"

define rarva = Character("Rarvayrrinth", who_outlines=[(absolute(2),"#fff",absolute(0),absolute(0))], who_italic=True, color="#000000")

define imp = Character("Imp", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e004")

define elder = Character("Village Elder", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e004")

define stman = Character("Strange Man", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#0a5519",image="stmanface", window_left_padding=110)
image side stmanface = "stmanface.png"

define enainia = Character("Princess Enainia", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#f24f4f",image="enainface", window_left_padding=110)
image side enainface = "enainface.png"

define hanna = Character("Hanna Roinestad", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="hannaface", window_left_padding=110)
image side hannaface = "hannaface.png"

define cal = Character("Calessa", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="calessaface", window_left_padding=110)
image side calessaface = "calessaface.png"


define ppl = Character("Crowd", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")
define cpt = Character("Captain", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")
define sol = Character("Soldier", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")
define sol2 = Character("Soldier 2", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7717")


define man = Character("Man", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")
define man2 = Character("Man 2", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7717")

define oldman = Character("Old man", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define sman = Character("Shady Man", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define thug = Character("Thug", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e111")

define thug2 = Character("Thug 2", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#c7ff4c")

define jack = Character("Jack the Lumberjack", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define keeper = Character("Tavern Keeper", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define karelia = Character("Karelia", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="karelface", window_left_padding=110)
image side karelface = "karelface.png"

define dwarf = Character("Dwarf", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define giselle = Character("Giselle", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="giselleface", window_left_padding=110)
image side giselleface = "giselleface.png"

define arnoldus = Character("Duke Arnoldus", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define onzanu = Character("Onzanu", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e004")

define isabella = Character("Isabella", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e4b6e8",image="isabface", window_left_padding=110)
image side isabface = "isabface.png"

define runar = Character("Lord Runar", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#4B644A",image="runarface", window_left_padding=110)
image side runarface = "runarface.png"

define guildm = Character("Guild Master", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define shop = Character("Shop Keeper", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define daug = Character("Little Girl", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e804d5")

define madam = Character("Madam Claude", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e824d5")

define emilia = Character("Emilia", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#cb2ebe",image="emiliaface", window_left_padding=110)
image side emiliaface = "emiliaface.png"

define shinji = Character("Shinji", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b")

define shipcapt = Character("Ship Captain", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e004")

define sailor = Character("Sailor", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#351010")

define adamastor = Character("Adamastor", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#550000", image="adaface", window_left_padding=110)
image side adaface = "adaface.png"

define rolf = Character("Rolf Demon Hunter", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#173f5f", image="rolfface", window_left_padding=110)
image side rolfface = "rolfface.png"

define woman = Character("Woman", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e824d5")

define katla = Character("Katla", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#974129", image="katlaface", window_left_padding=110)
image side katlaface = "katlaface.png"

define irgodon = Character("Irgodon Demon Hunter", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#e26b2b", image="irgoface", window_left_padding=110)
image side irgoface = "irgoface.png"

define vakgu = Character("Chief Vakgu", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#351010", image="vakguface", window_left_padding=110)
image side vakguface = "vakguface.png"



define chang = Character("General Chang", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#0b4f6c", image="changface", window_left_padding=110)
image side changface = "changface.png"

define yumiko = Character("Princess Yumiko", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#b70980", image="yumikoface", window_left_padding=110)
image side yumikoface = "yumikoface.png"

define tiberius = Character("Emperor Tiberius", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#b70909", image="tiberiusface", window_left_padding=110)
image side tiberiusface = "tiberiusface.png"

define aelia = Character("Aelia", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#b70982", image="aeliaface", window_left_padding=110)
image side aeliaface = "aeliaface.png"

define brutus = Character("Brutus the Behemoth", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#5e0404", image="brutusface", window_left_padding=110)
image side brutusface = "brutusface.png"

define mvamp01 = Character("Master Vampire", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#550000", image="vamp01face", window_left_padding=110)
image side vamp01face = "vamp01face.png"

define karl = Character("Karl the Fisherman", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define petra = Character("Petra", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#b70980", image="petraface", window_left_padding=110)
image side petraface = "petraface.png"

define alice = Character("Alice", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e004", image="aliceface", window_left_padding=110)
image side aliceface = "aliceface.png"

define villager = Character("Villager", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define pacu = Character("Pacuvianus", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define vampire = Character("Vampire", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#550000")

define aline = Character("Aline", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#35e004", image="alineface", window_left_padding=110)
image side alineface = "alineface.png"


define wrath = Character("Wrath", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#470202", image="wrathface", window_left_padding=110)
image side wrathface = "wrathface.png"

define pride = Character("Pride", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#001021", image="prideface", window_left_padding=110)
image side prideface = "prideface.png"

define lust = Character("Lust", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#B7074A", image="lustface", window_left_padding=110)
image side lustface = "lustface.png"

define cari = Character("Carilielle", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#B7074A", image="carilielleface", window_left_padding=110)
image side carilielleface = "carilielleface.png"

define greed = Character("Greed", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#FFAC30", image="greedface", window_left_padding=110)
image side greedface = "greedface.png"

define envy = Character("Envy", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#42D179", image="envyface", window_left_padding=110)
image side envyface = "envyface.png"

define gluttony = Character("Gluttony", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#937386", image="gluttonyface", window_left_padding=110)
image side gluttonyface = "gluttonyface.png"

define elderjit = Character("Jithak Elder", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define zordruza = Character("Queen Zordruza", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#B7074A", image="zordruzaface", window_left_padding=110)
image side zordruzaface = "zordruzaface.png"

define yzordruza = Character("Zordruza", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#B7074A", image="yzordruzaface", window_left_padding=110)
image side yzordruzaface = "yzordruzaface.png"

define ysilvana = Character("Silvana", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#00f95b", image="ysilvanaface", window_left_padding=110)
image side ysilvanaface = "ysilvanaface.png"

define darkelf = Character("Dark Elf", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define elf = Character("Elf", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define orc = Character("Orc", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#ff7777")

define orc2 = Character("Orc 2", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#127777")


define salazar = Character("Salazar", who_outlines=[(absolute(1),"#ff00",absolute(0),absolute(0))], who_italic=True, color="#ff0000", image="face")

define incubus = Character("Incubus", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#351010")

define incubus2 = Character("Incubus 2", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#312010")

define ryo = Character("Ryo Sarojini", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#fc05fc",image="ryoface", window_left_padding=110)
image side ryoface = "ryoface.png"

define yotul = Character("Yotul", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#db2ebe",image="yotulface", window_left_padding=110)
image side yotulface = "yotulface.png"

define hei = Character("Lord Heihachi", who_outlines=[(absolute(1),"#000",absolute(0),absolute(0))], who_italic=True, color="#173a5f")



define bairn = Character("Bairn", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#079E9C", image="bairnface", window_left_padding=110)
image side bairnface = "bairnface.png"

define necromancer = Character("Necromancer", who_outlines=[(absolute(1),"#ff00",absolute(0),absolute(0))], who_italic=True, color="#ff0000")

define cerea = Character("Cerea", who_outlines=[(absolute(1),"#f00",absolute(0),absolute(0))], who_italic=True, color="#B31A1A", image="cereaface", window_left_padding=110)
image side cereaface = "cereaface.png"

screen points_all:
    add "skillbar01.png"
    if Points >= 0:
        text "[Points]" xpos 55 ypos 0
    else:
        text "{color=#f00}[Points]{/color}" xpos 55 ypos 0
    text "[Destpoints]" xpos 55 ypos 92
    text "[Iluspoints]" xpos 55 ypos 200
    text "[Healpoints]" xpos 55 ypos 315
    text "[Mystpoints]" xpos 55 ypos 415
    text "[Summpoints]" xpos 55 ypos 510
    text "[Altepoints]" xpos 55 ypos 615
    text "[Necropoints]" xpos 55 ypos 710
    text "[Gold]" xpos 1720 ypos 0

screen creditscoff:
    add "system/credits.jpg"
    textbutton "Buy me a coffee" xpos 800 ypos 850 action OpenURL("https://www.buymeacoffee.com/BOTUQjCW2")

screen newpatreon:
    imagebutton auto "gui/Patreon-Logo_%s.png" xpos 700 ypos 150 action OpenURL("https://www.patreon.com/kthuliangames")

screen toggleskills:
    imagebutton auto "gui/eyeopen_%s.png" xpos 1820 ypos 80 action Show('points_allhh'), Hide('toggleskills')

screen points_allhh:

    add "skillbarmap.png"
    imagebutton auto "gui/heart_%s.png" xpos 1720 ypos 80 action Show('stats_screen')
    imagebutton auto "gui/eyeclosed_%s.png" xpos 1820 ypos 80 action Hide('points_allhh'), Show('toggleskills')
    if Points >= 3:
        text "{color=#0f0}[Points]{/color}" xpos 55 ypos 0
    elif Points >= -2 and Points <= 2:
        text "[Points]" xpos 55 ypos 0
    else:
        text "{color=#f00}[Points]{/color}" xpos 55 ypos 0
    text "[Destpoints]" xpos 55 ypos 92
    text "[Iluspoints]" xpos 55 ypos 200
    text "[Healpoints]" xpos 55 ypos 315
    text "[Mystpoints]" xpos 55 ypos 415
    text "[Summpoints]" xpos 55 ypos 510
    text "[Altepoints]" xpos 55 ypos 615
    text "[Necropoints]" xpos 55 ypos 710
    text "[Gold]" xpos 1720 ypos 0



















screen stats_screen:
    modal True

    add "girlsscreenmain.png"
    imagebutton auto "girlsbuttons/exit_%s.png" xpos 1582 ypos 993 action Hide('stats_screen')

    imagebutton auto "girlsbuttons/ayna_%s.png" xpos 13 ypos 47 action Show("screen_ayna")
    imagebutton auto "girlsbuttons/kat_%s.png" xpos 13 ypos 184 action Show('screen_katriona')
    imagebutton auto "girlsbuttons/sil_%s.png" xpos 13 ypos 320 action Show('screen_silvana')
    imagebutton auto "girlsbuttons/isa_%s.png" xpos 13 ypos 456 action Show('screen_isabella')
    imagebutton auto "girlsbuttons/mida_%s.png" xpos 13 ypos 594 action Show('screen_mida')
    imagebutton auto "girlsbuttons/lili_%s.png" xpos 13 ypos 732 action Show('screen_liliana')
    imagebutton auto "girlsbuttons/bredita_%s.png" xpos 13 ypos 870 action Show('screen_bredita')
    imagebutton auto "girlsbuttons/enainia_%s.png" xpos 1783 ypos 47 action Show('screen_enainia')
    imagebutton auto "girlsbuttons/yisnna_%s.png" xpos 1783 ypos 184 action Show('screen_yisnna')
    imagebutton auto "girlsbuttons/gise_%s.png" xpos 1783 ypos 320 action Show('screen_giselle')
    imagebutton auto "girlsbuttons/hanna_%s.png" xpos 1783 ypos 456 action Show('screen_hanna')
    imagebutton auto "girlsbuttons/karel_%s.png" xpos 1783 ypos 594 action Show('screen_karelia')
    imagebutton auto "girlsbuttons/koneko_%s.png" xpos 1783 ypos 732 action Show('screen_koneko')
    imagebutton auto "girlsbuttons/fannay_%s.png" xpos 1783 ypos 870 action Show('screen_fannay')



    text "[aynalove]" xpos 192 ypos 70
    text "[aynacorr]" xpos 340 ypos 70

    text "[katrionalove]" xpos 192 ypos 210
    text "[katrionacorr]" xpos 340 ypos 210

    text "[silvanalove]" xpos 192 ypos 350
    text "[silvanacorr]" xpos 340 ypos 350

    text "[isabellalove]" xpos 192 ypos 490
    text "[isabellacorr]" xpos 340 ypos 490

    text "[midalove]" xpos 192 ypos 620
    text "[midacorr]" xpos 340 ypos 620

    text "[lililove]" xpos 192 ypos 760
    text "[lilicorr]" xpos 340 ypos 760

    text "[breditalove]" xpos 192 ypos 900
    text "[breditacorr]" xpos 340 ypos 900



    text "[enainialove]" xpos 1545 ypos 75
    text "[enainiacorr]" xpos 1695 ypos 75

    text "[yisnalove]" xpos 1545 ypos 215
    text "[yisnacorr]" xpos 1695 ypos 215

    text "[gisellelove]" xpos 1545 ypos 355
    text "[gisellecorr]" xpos 1695 ypos 355

    text "[hannalove]" xpos 1545 ypos 495
    text "[hannacorr]" xpos 1695 ypos 495

    text "[karelialove]" xpos 1545 ypos 625
    text "[kareliacorr]" xpos 1695 ypos 625

    text "[konekolove]" xpos 1545 ypos 765
    text "[konekocorr]" xpos 1695 ypos 765

    text "[fannaylove]" xpos 1545 ypos 905
    text "[fannaycorr]" xpos 1695 ypos 905

screen stats_stats(img=None, ret=False):
    add "girlsscreenmain.png"
    if img:
        add img

    text "[aynalove]" xcenter 203 ycenter 108
    text "[aynacorr]" xcenter 350 ycenter 108

    text "[katrionalove]" xcenter 203 ycenter 245
    text "[katrionacorr]" xcenter 350 ycenter 245

    text "[silvanalove]" xcenter 203 ycenter 382
    text "[silvanacorr]" xcenter 350 ycenter 382

    text "[isabellalove]" xcenter 203 ycenter 519
    text "[isabellacorr]" xcenter 350 ycenter 519

    text "[midalove]" xcenter 203 ycenter 656
    text "[midacorr]" xcenter 350 ycenter 656

    text "[lililove]" xcenter 203 ycenter 793
    text "[lilicorr]" xcenter 350 ycenter 793

    text "[breditalove]" xcenter 203 ycenter 930
    text "[breditacorr]" xcenter 350 ycenter 930

    text "[enainialove]" xcenter 1554 ycenter 118
    text "[enainiacorr]" xcenter 1703 ycenter 118

    text "[yisnalove]" xcenter 1554 ycenter 255
    text "[yisnacorr]" xcenter 1703 ycenter 255

    text "[gisellelove]" xcenter 1554 ycenter 392
    text "[gisellecorr]" xcenter 1703 ycenter 392

    text "[hannalove]" xcenter 1554 ycenter 529
    text "[hannacorr]" xcenter 1703 ycenter 529

    text "[karelialove]" xcenter 1554 ycenter 666
    text "[kareliacorr]" xcenter 1703 ycenter 666

    text "[konekolove]" xcenter 1554 ycenter 803
    text "[konekocorr]" xcenter 1703 ycenter 803

    text "[fannaylove]" xcenter 1554 ycenter 940
    text "[fannaycorr]" xcenter 1703 ycenter 940

    imagebutton auto "girlsbuttons/ayna_%s.png" xpos 13 ypos 47 action [Show('screen_ayna'), With(dissolve)]
    imagebutton auto "girlsbuttons/kat_%s.png" xpos 13 ypos 184 action [Show('screen_katriona'), With(dissolve)]
    imagebutton auto "girlsbuttons/sil_%s.png" xpos 13 ypos 320 action [Show('screen_silvana'), With(dissolve)]
    imagebutton auto "girlsbuttons/isa_%s.png" xpos 13 ypos 456 action [Show('screen_isabella'), With(dissolve)]
    imagebutton auto "girlsbuttons/mida_%s.png" xpos 13 ypos 594 action [Show('screen_mida'), With(dissolve)]
    imagebutton auto "girlsbuttons/lili_%s.png" xpos 13 ypos 732 action [Show('screen_liliana'), With(dissolve)]
    imagebutton auto "girlsbuttons/bredita_%s.png" xpos 13 ypos 870 action [Show('screen_bredita'), With(dissolve)]
    imagebutton auto "girlsbuttons/enainia_%s.png" xpos 1783 ypos 47 action [Show('screen_enainia'), With(dissolve)]
    imagebutton auto "girlsbuttons/yisnna_%s.png" xpos 1783 ypos 184 action [Show('screen_yisnna'), With(dissolve)]
    imagebutton auto "girlsbuttons/gise_%s.png" xpos 1783 ypos 320 action [Show('screen_giselle'), With(dissolve)]
    imagebutton auto "girlsbuttons/hanna_%s.png" xpos 1783 ypos 456 action [Show('screen_hanna'), With(dissolve)]
    imagebutton auto "girlsbuttons/karel_%s.png" xpos 1783 ypos 594 action [Show('screen_karelia'), With(dissolve)]
    imagebutton auto "girlsbuttons/koneko_%s.png" xpos 1783 ypos 732 action [Show('screen_koneko'), With(dissolve)]
    imagebutton auto "girlsbuttons/fannay_%s.png" xpos 1783 ypos 870 action [Show('screen_fannay'), With(dissolve)]
    if ret:
        imagebutton auto "girlsbuttons/exit_%s.png" xpos 1300 ypos 993 action [Hide('stats_screen'), With(dissolve)]
        key "game_menu" action [Hide('stats_screen'), With(dissolve)]
    else:
        imagebutton auto "girlsbuttons/exit_%s.png" xpos 1300 ypos 993 action [Show('stats_screen'), With(dissolve)]
        key "game_menu" action [Show('stats_screen'), With(dissolve)]

screen stats_screen():
    tag stats
    modal True

    use stats_stats(ret=True)





screen screen_ayna():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenayna.png")





screen screen_katriona():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenkat.png")





screen screen_silvana():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screensil.png")





screen screen_isabella():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenisa.png")





screen screen_mida():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenmida.png")





screen screen_liliana():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenlili.png")





screen screen_bredita():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenbred.png")





screen screen_enainia():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenenai.png")





screen screen_yisnna():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenyisnna.png")





screen screen_giselle():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screengise.png")





screen screen_hanna():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenhanna.png")





screen screen_karelia():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenkarelia.png")





screen screen_koneko():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenkoneko.png")





screen screen_fannay():
    tag stats
    modal True

    use stats_stats(img="girlsbuttons/screenfannay.png")



















label start:


    $ var01 = 0


    $ var02 = 0



    $ var03 = 0
    $ var04 = 0
    $ var05 = 0
    $ var06 = 0
    $ var07 = 0
    $ var08 = 0
    $ var09 = 0
    $ var10 = 0
    $ var11 = 0
    $ var12 = 0



    $ Gold = 0
    $ Points = 0
    $ Destpoints = 0
    $ Iluspoints = 0
    $ Healpoints = 0
    $ Mystpoints = 0
    $ Summpoints = 0
    $ Altepoints = 0
    $ Necropoints = 0




    scene black
    with dissolve
    n "Are you over {color=#f00}{b}18{/b}{/color}?"

    menu:
        "Yes":
            jump beggining
        "No":

            jump endgame





label beggining:

    scene welcome
    nvl clear
    n "Welcome to Ataegina"
    n "I hope you enjoy"
    nvl clear
    n "You now have the possibility to use cheats"
    n "But I warn you"
    n "It might break the game"
    n "Do you want to use cheats?"
    nvl clear
    menu:
        "Yes":
            n "Ok... If you say so..."
            nvl clear
            menu:
                "I'm just a little bit of a cheater (All skills start at 5)":
                    $ Destpoints = 5
                    $ Iluspoints = 5
                    $ Healpoints = 5
                    $ Mystpoints = 5
                    $ Summpoints = 5
                    $ Altepoints = 5
                    $ Necropoints = 5
                    jump ataeginago
                "I Cheat a lot! (All skills start at 10 and Gold at 1000)":
                    $ Destpoints = 10
                    $ Iluspoints = 10
                    $ Healpoints = 10
                    $ Mystpoints = 10
                    $ Summpoints = 10
                    $ Altepoints = 10
                    $ Necropoints = 10
                    $ Gold = 1000
                    jump ataeginago
                "I'm a nice guy but a cheater (Skills start at 5 and Alignment at 10)":
                    $ Destpoints = 5
                    $ Iluspoints = 5
                    $ Healpoints = 5
                    $ Mystpoints = 5
                    $ Summpoints = 5
                    $ Altepoints = 5
                    $ Necropoints = 5
                    $ Points = 10
                    jump ataeginago
                "I'm evil and I cheat (Skills start at 5 and Alignment at -10)":
                    $ Destpoints = 5
                    $ Iluspoints = 5
                    $ Healpoints = 5
                    $ Mystpoints = 5
                    $ Summpoints = 5
                    $ Altepoints = 5
                    $ Necropoints = 5
                    $ Points = -10
                    jump ataeginago
        "No":


            n "Great! let's start the game then!"
            nvl clear
            jump ataeginago


label ataeginago:
    stop music fadeout 4.0

    scene black
    nvl clear

    n "You are sleeping"
    n "A strange dream inhabits your sleep"
    n "Sweat covers your body"
    n "You Feel like something bad is about to happen"
    nvl clear
    fvoice "Time to wake up"

    scene black01
    with dissolve
    fvoice "If you don't wake up now"
    scene black02
    with dissolve
    fvoice "You will die..."
    fvoice "Like all your family and friends"
    nvl clear
    n "That last sentence..."
    n "You wake up in terror"
    nvl clear
    scene windowintro01
    with dissolve
    n "Attracted by the light from the window"
    nvl clear
    n "You try to reason with your mind"
    nvl clear
    scene windowintro02
    with dissolve
    n "You know it was a dream"
    nvl clear
    n "But at the same time it felt so real..."
    nvl clear
    n "Before you could calm yourself"
    nvl clear
    play sound "sounds/battle01.mp3"
    n "You hear a lot of noise outside"

    nvl clear
    scene windowintro
    with dissolve

    ppl "AHHHH"
    ppl "Arghh"
    n "Confused"
    nvl clear
    n "Wondering if you really are awake"
    nvl clear
    ppl "Oh my God!!! Run!!"
    ppl "They are killing everyone"
    ppl "AHHH"
    ppl "We must fight for our lives!!"
    n "This must still be a dream"
    nvl clear
    n "You decide to look through the window"
    nvl clear

    scene streetslay01
    with dissolve
    n "You are shocked to see a mass invasion at your doorstep"
    n "Soldiers killing everything that moves"
    n "You look at a specific one that looks like the captain"

    scene streetcpt01
    with dissolve
    cpt "Kill them all!"
    scene streetcpt02
    with dissolve
    cpt "I want no prisoners!!"
    cpt "Well.... take only women.... So we can have some fun later"
    cpt "AHAHAHAHA"
    nvl clear
    n "You feel the Captain staring at you"
    scene streetcpt03
    with dissolve
    nvl clear
    n "You feel a chill run through your body"
    cpt "Hey look boys"
    scene streetcpt04
    with dissolve
    cpt "We seem to have an audience"
    cpt "You know what to do"
    sol "But it's just a child"
    cpt "And???"
    scene streetcpt05
    with dissolve
    sol "Very well sir"
    nvl clear
    n "As you hear this, you leave the window in panic"

    scene roombg01
    with dissolve
    nvl clear
    n "You need to find a way to escape, you need to do something!!"
    n "Fast!!!!"
    nvl clear


    call screen mcroomintro

label introbed:
    scene roombg01
    n "You think about getting under the bed"
    n "But what would that do?"
    n "They will find you anyway"
    n "Before you could do anything else"
    jump introparents


label introcloset:
    scene roombg01
    n "Should you get in the closet?"
    n "Maybe the best option"
    n "But they surely will look inside"
    n "Before you could do anything else"
    jump introparents

label introdoor:
    scene roombg01
    n "Yes, you should get the hell out"
    n "It's the smartest thing to do"
    n "But what about your family?"
    n "Just as you are about to leave"
    jump introparents

label introparents:
    scene roombg01
    nvl clear
    dad "Hurry get inside"
    n "Your family enters your room"
    scene roomfam01
    with dissolve
    mom "Oh my God... they are coming"
    sis "We must fight them"
    dad "You all try to escape through the window"
    dad "I will try to hold them here"
    mom "No!!!"
    mom "I know what that means"
    sis "Please father come with us"
    dad "There is no other way"
    dad "Leave NOW!!"
    scene roomfam02
    with dissolve
    nvl clear
    n "You try to say something"
    n "But the words won't come out"
    mom "Let's go"
    mom "I love you dear"
    mom "Goodbye"
    scene streetfam01
    with dissolve
    nvl clear
    n "When you come to your senses"
    n "You are on the street"
    n "You see your mother and your sister"
    n "Running in front of you"
    mom "Come on run"
    sis "What is going to happen to us mom?"
    mom "We will get out of this"
    nvl clear
    n "As she finishes that sentence"
    nvl clear
    scene streetfam02
    with dissolve
    n "Some of the soldiers appeared"
    nvl clear
    cpt "Well well"
    cpt "Look what we got here"
    cpt "Hmmm, I'm going to have so much fun"
    cpt "Take the girls to my carriage!"
    sol "Very well sir"
    scene streetfam03
    with dissolve
    scene streetfam03
    with hpunch
    mom "Noooo"
    sis "Ahrgh.."
    mom "Leave her alone"
    cpt "Ahahaha"
    n "You see the soldiers taking your mother and sister"
    n "Leaving you alone with the captain"
    scene cptvsmc
    with dissolve
    cpt "Ahahaha"
    cpt "Now it's just you and me"
    cpt "I'm going to kill you now"
    cpt "And then I'm going to fuck your mother and sister"
    nvl clear
    n "Feeling scared and angry"
    n "Knowing it's the end of the line for you..."
    n "You can't stop thinking about your family"
    nvl clear
    scene cptvsmc01
    with dissolve
    cpt "Let's get this over with"
    cpt "I have some pussy to destroy"
    cpt "Ahahaha"
    cpt "Prepare to die"

    scene atamc
    with dissolve
    fvoice "Are you going to let him kill you?"
    stop sound
    n "Everything went silent"
    n "This voice again?"
    fvoice "And rape your family??"
    fvoice "You need to do something!"
    fvoice "N O W !!"
    scene cptvsmc01
    with dissolve
    nvl clear
    n "As soon as the mysterious woman disappeared"
    n "An extremely angry feeling strikes you"
    n "You start losing control of your body"
    n "You feel something pushing you"
    n "In the next moment it's like you're seeing yourself"
    n "In the third person"
    nvl clear
    scene cptvsmc02
    with dissolve
    cpt "What is this?"
    cpt "What are you doing?"
    cpt "Put me down"
    scene cptvsmc03
    with dissolve
    n "The only thing you can do now is watch"
    n "Anger... Pain... Rage..."
    n "You are no longer in control of your own body"
    nvl clear
    cpt "Arghh..."
    scene cptvsmc04
    with dissolve
    n "An immense power surrounds you"
    n "You feel your opponent disintegrate in front of you"
    cpt "...."
    nvl clear
    scene black
    n "And then you faint"
    nvl clear
    scene meanwhile
    with dissolve
    scene meanwhile
    with dissolve
    scene mages001
    with dissolve
    ayna "What an amazing power"
    ayna "I have to do something"
    ayna "This is impossible"
    scene mages002
    with dissolve
    katarro "Did you feel that Archmage?"
    ayna "Yes...."
    ayna "It's amazing..."
    katarro "What should we do?"
    scene mages003
    with dissolve
    ayna "Take Mistress Katriona with you"
    ayna "Go get that boy!"
    katarro "Very well"
    ayna "I've instructed her to go with you"
    ayna "Use your teleport ability to bring him over"
    ayna "Mistress Katriona will take care of his wounds"
    n "The next moment this little guy"
    n "was near Mistress Katriona"
    nvl clear
    scene mages004
    with dissolve
    katriona "Yeah yeah... it always has to be me..."
    katarro "But I..."
    katriona "I know, little guy... Archmage Ayna told me"
    katarro "If you could sense what I and the Archmage sensed"
    katarro "You wouldn't be joking"
    scene mages005
    with dissolve
    katriona "Yes... I know...."
    katriona "What are we waiting for then?"
    katriona "Let's go!"
    n "In a split second Master Katarro teleported them"
    nvl clear
    scene mages006
    with dissolve
    play sound "sounds/burning.mp3"
    katriona "Wow"
    katriona "What the hell happened here?"
    katarro "Look at the body count"
    katriona "There seem to be no survivors"
    katriona "Can you sense anyone?"
    katarro "Yes, over there"
    katriona "It's a kid!"
    n "Mistress Katriona held you"
    nvl clear
    scene mages007
    with dissolve
    n "And started using her healing abilities"
    nvl clear
    katriona "He's almost dead"
    katriona "Take us back right now!"
    katarro "Right!"
    n "Master Katarro put his hand on"
    n "Mistress Katriona's shoulder"
    stop sound
    nvl clear
    scene mages008
    with dissolve
    scene mages009
    with dissolve
    scene mages010
    with dissolve


    scene black
    n "Some time later"
    nvl clear
    ayna "So, how is he?"
    katriona "He's stable now"
    n "What is this? are you hearing voices now?"
    n "Women’s voices?"
    nvl clear
    ayna "Do you need my help with his recovery?"
    katriona "I don't think so"
    katriona "He should be waking up soon"
    n "With these words you start opening your eyes"
    nvl clear
    scene a001
    with dissolve
    scene a002
    with dissolve
    scene a003
    with dissolve
    scene a004
    with dissolve
    ayna "That's good to hear"
    ayna "I need to know what happened"
    scene a005
    with dissolve
    nvl clear
    n "You look up, so you can put faces to the voices you hear"
    scene a006
    with dissolve
    n "You see two ladies talking about you"
    katriona "Hey, look who's awake"
    scene a007
    with dissolve
    ayna "Hello there"
    katriona "Hi kid"
    nvl clear
    n "You want to answer but you are so confused"
    katriona "Cat got your tongue?"
    scene a008
    with dissolve
    ayna "He seems confused, let's start with an easy one"
    ayna "What is your name?"
    nvl clear
    n "You panic, because you can't remember"
    n "You don't know your name? Really?"
    ayna "He seems to have some kind of memory problem"
    ayna "Don't worry"
    nvl clear
    n "A feeling of peace and energy starts to envelop you"
    scene a009
    with dissolve
    play sound "sounds/spell01.mp3"
    scene a010
    with dissolve
    scene a011
    with dissolve
    scene a012
    with dissolve
    stop sound
    ayna "There... calm down"
    scene a008
    with dissolve
    ayna "If you don't remember your name"
    ayna "You can always choose a cool one"
    ayna "So... What do you want to be called?"
    nvl clear


    $ player_name = renpy.input("What's your name?",default='Hjard')

    if player_name == "":
        $ player_name="Hjard"

    MC "I... call me [MC]"
    scene a008
    with dissolve

    ayna "Very well"
    ayna "You shall be called [MC] from now on"
    MC "Thank you"
    MC "Now tell me"
    MC "Where am I?"
    MC "Who are you?"
    MC "And..."
    scene a008
    with dissolve

    ayna "Well I'll try to answer all your questions"
    ayna "But first, tell me"
    ayna "What is the last thing you remember?"
    MC "I... don't know..."
    MC "I just woke up here"
    scene a007
    with dissolve

    ayna "So you don't remember the attack?"
    MC "I... no... I don't remember being attacked"
    katriona "Oh great... how do we find out what happened now?"
    ayna "Do you remember what you were doing before coming here?"
    MC "I... don't think so..."
    MC "I can't remember anything"
    scene a008
    with dissolve
    ayna "Well, you should rest"
    ayna "We will talk again later"
    scene a013
    with dissolve

    ayna "Take good care of him"
    katriona "Yeah Yeah...Sure..."
    scene a014
    with dissolve
    ayna "Bye... You'll be fine in her hands"
    nvl clear
    n "She leaves the room"
    n "And in a joking voice she said"
    scene a016
    with dissolve
    ayna "Don't you go hurting [MC] now, hehehe"
    katriona "Sure sure..."
    scene a015
    with dissolve
    katriona "So let's put you to sleep..."
    katriona "Ahaha, that sounded like a threat"
    scene a016a
    with dissolve
    katriona "Here you go... Sweet dreams"

    scene a017
    with dissolve
    play sound "sounds/spell01.mp3"
    scene a018
    with dissolve
    scene a019
    with dissolve
    scene a020
    with dissolve
    scene a021
    with dissolve
    scene a022
    with dissolve
    scene a023

    with dissolve
    nvl clear
    n "Her powers surround you"
    n "You feel so relaxed that you fall asleep"
    n "Almost instantly"
    nvl clear
    katriona "That should do it"
    play music "<loop 0.0>epic.mp3" fadein 10.0
    scene black

    with dissolve
    mom "Hey [MC] are you sleeping again?"
    MC "What?"
    mom "Go outside and play with your sister"
    MC "Mother? I..."
    mom "I want no excuses"
    mom "Go on now"
    play sound "sounds/beat.mp3"
    cpt "You should listen to your mom"
    scene a024
    with hpunch
    scene a024
    with hpunch
    MC "Wha..."
    scene a025
    with dissolve

    mom "Who are you?"
    cpt "Let's have some fun"
    mom "What are you doing....?"
    scene a026
    with dissolve

    mom "Stop it!"
    cpt "Ahahaha"
    cpt "Such a beauty"
    mom "Ahhhh!!"
    MC "Stop this!!!"
    nvl clear
    n "A familiar voice speaks to you"
    fvoice "Calm down..."
    scene black01
    with dissolve

    fvoice "This is just a dream"
    scene black02
    with dissolve
    fvoice "None of this is really happening"
    fvoice "It's all in your head"
    stop sound
    MC "I... do I know you?"
    MC "And these people?"

    fvoice "Calm down..."
    fvoice "I'm here to help you"
    fvoice "Like I've always been"
    fvoice "If you let me"
    fvoice "I will take you out of this nightmare"
    fvoice "If you don't..."
    fvoice "I will leave right now"
    fvoice "And you will stay in this dream"
    nvl clear
    scene black
    n "This is the first choice in the game"
    n "Know that choices will change"
    n "How the game will progress"
    nvl clear
    n "Your Alignment will change"
    n "Towards good or evil"
    n "Depending on your choices"
    nvl clear
    n "Your alignment right now is zero"
    n "That means you are a neutral character"
    n "More points mean you are a good person"
    n "If you have like -100 points"
    n "You are bad to the bone xD"
    nvl clear
    scene white
    show screen points_all

    "Before we continue"
    "That bar at the left"

    "Will show your stats"
    show arrowalig
    "This is your alignment"
    hide arrowalig
    show arrowdest
    "This is your Battlemagic skill"
    hide arrowdest
    show arrowilu
    "This is your Illusion skill"
    hide arrowilu
    show arrowheal
    "This is your Healing skill"
    hide arrowheal
    show arrowmyst
    "This is your Mysticism skill"
    hide arrowmyst
    show arrowsumm
    "This is your Summoning skill"
    hide arrowsumm
    show arrowalt
    "This is your Alteration skill"
    hide arrowalt
    show arrownecro
    "This is your Necromancer skill"
    hide arrownecro
    "The one with the coins up there is your gold"
    "And that's it"
    "Don't worry about it for now"
    "Let's continue"

    hide screen points_all
    scene black
    n "You were left with a choice"
    n "I will help on this one"
    n "If you choose to keep on in this dream"
    n "Something bad will happen to your mother"
    nvl clear
    n "You gain alignment towards evil"
    n "Otherwise"
    nvl clear
    n "The woman that is talking to you"
    n "Will take you to a nice dream"
    n "You will gain alignment towards good"
    nvl clear
    n "Remember"
    n "Your choices will change the gameplay"
    nvl clear
    scene black02
    with dissolve
    fvoice "So... will you come with me?"
    menu:
        "Yes, take me out of this nightmare[abgreen] [abalignment]":
            $ Points += 1
            $ cheaterfix = 1
            nvl clear
            n "You now have [Points] point"
            n "That's still considered neutral"
            n "But it's a start to Goodness"
            stop music fadeout 10.0
            nvl clear
            jump sweetdream
        "No, I don't want to go with you[abred] [abnoalignment]":

            $ Points -= 1

            nvl clear
            n "You now have [Points] point"
            n "That's still considered neutral"
            n "But it's the first step to Villainy"
            stop music fadeout 10.0
            nvl clear
            jump nightmare

label splashscreen:

    scene warning
    $ renpy.pause(3, hard=True)

    scene kthulian
    $ renpy.pause(1, hard=True)
    play sound "sounds/intro.mp3"
    show text "{color=#f00}{b}Kthulian Games{/b}{/color}" with dissolve
    $ renpy.pause(1, hard=True)

    hide text with dissolve
    $ renpy.pause(1, hard=True)
    play sound "sounds/intro.mp3"
    show text "{color=#f00}{b}Presents{/b}{/color}" with dissolve
    $ renpy.pause(1, hard=True)

    hide text with dissolve
    with Pause(1)



    return
label endgame:



    return

init:
    define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }
