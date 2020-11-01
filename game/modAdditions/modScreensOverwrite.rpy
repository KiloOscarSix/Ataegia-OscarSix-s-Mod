# textbutton _("Mod Options") action Show("modOptions")
# textbutton _("Oscar's Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")]

# if title == "Save":
#     text "{color=#fff}Save Name:{/color}":
#         xalign 0
#         yalign -0.005
#     input:
#         xalign 0
#         yalign 0.05
#         value VariableInputValue("save_name")

screen navigation():


    text "{size=-30}{color=#f00} V0.4.5 {/color} (All paths) {/size}":
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
            textbutton _("Oscar's Gallery") action [Show("sceneCharacterMenu"), ui.callsinnewcontext("galleryNameChange")]

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

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            if title == "Save":
                text "{color=#fff}Save Name:{/color}":
                    xalign 0
                    yalign -0.005
                input:
                    xalign 0
                    yalign 0.05
                    value VariableInputValue("save_name")


            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        if title == "Save":
                            action [SetVariable("save_name",""), get_save_name(slot)]
                        else:
                            action FileAction(slot)

                        add FileScreenshot(slot) xalign 0.5

                        key "save_delete" action FileDelete(slot)



                        vbox:
                            xalign 0.5
                            yalign 1.0
                            text FileSlotName(slot, gui.file_slot_cols * gui.file_slot_rows) + ") " + FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
