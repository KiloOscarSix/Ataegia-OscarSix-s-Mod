init python:
    modGame = "{}".format(config.name)
    modGameLink = "https://www.patreon.com/OscarSix"

screen navigation():

    text "{size=-30}{color=#f00} V0.4.3 {/color} (All paths) {/size}":
        xpos 1900
        ypos 30

    imagebutton auto "gui/kofi_%s.png" xalign 1.00 yalign 1.00 action OpenURL("https://www.buymeacoffee.com/BOTUQjCW2")
    imagebutton auto "gui/gjolt_%s.png" xalign 0.879 yalign 0.9999 action OpenURL("https://gamejolt.com/games/ataegina/511466")
    imagebutton auto "gui/subscribestar_%s.png" xalign 0.751 yalign 1.00 action OpenURL("https://subscribestar.adult/kthulian-games")
    imagebutton auto "gui/patreon_%s.png" xalign 0.622 yalign 1.00 action OpenURL("https://www.patreon.com/kthuliangames")

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 1.0
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start("oscarUpdateAlert")

        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Options") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Oscar's Gallery") action [Show("sceneGalleryMenu"), ui.callsinnewcontext("galleryNameChange")]

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Visit Us") action OpenURL("http://www.kthuliangames.rf.gd")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)

screen modOutOfDate:
    modal True
    zorder 100
    add "#23272a"

    vbox:
        xcenter 0.5
        ycenter 0.5
        spacing 50

        text "{size=64}A new version of {b}Oscar's [modGame] Mod{/b} is now available.\nClick the Download Now button to download the new update." text_align 0.5 xcenter 0.5 ycenter 0.5
        hbox:
            spacing 100
            xcenter 0.5

            textbutton "Download Now":
                action OpenURL("{}".format(modGameLink))
            textbutton "Ask Me Later":
                action Return()

label oscarUpdateAlert:
    if updateChecker():
        call screen modOutOfDate

    jump start
