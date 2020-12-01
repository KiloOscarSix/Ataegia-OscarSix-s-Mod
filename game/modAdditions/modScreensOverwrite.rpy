screen navigation():


    text "{size=-30}{color=#f00} V0.4.6 {/color} (All paths) {/size}":
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
            textbutton _("Start") action Start()

        else:
            textbutton _("Mod Options") action Show("modOptions")

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Oscar's Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()


        textbutton _("Visit Us") action OpenURL("http://www.kthuliangames.rf.gd")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)

screen save():

    tag menu

    use file_slots(_("Save"))

    vbox:
        align(0.28, 0.185)
        text "{color=#fff}Save Name:{/color}"
        input:
            yalign 0.05
            value VariableInputValue("save_name")
