# Screens
screen change_wife():
    modal True
    frame:
        xalign 1.0 yalign 0.5
        xysize(400, 1080)
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            vbox:
                xalign 0.5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    vbox:
                        xalign 0.5
                        text "Body" xalign 0.5 yalign 0.5
                        null height 2
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextSkin", False), Jump("change_skin")]
                            text "Skin Color" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextSkin", True), Jump("change_skin")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextHead", False), Jump("change_head")]
                            text "Head Shape" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextHead", True), Jump("change_head")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextBreast", False), Jump("change_breast")]
                            text "Breast Size" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextBreast", True), Jump("change_breast")]
                null height 5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    vbox:
                        xalign 0.5
                        text "Hair" xalign 0.5 yalign 0.5
                        null height 10
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextHair", False), Jump("change_hairstyle")]
                            text "Hairstyle" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextHair", True), Jump("change_hairstyle")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextHairColor", False), Jump("change_hair_color")]
                            text "Hair Color" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextHairColor", True), Jump("change_hair_color")]
                null height 5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    vbox:
                        xalign 0.5
                        text "Eyes" xalign 0.5 yalign 0.5
                        null height 10
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextEyeball", False), Jump("change_eyeball")]
                            text "Eye Shape" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextEyeball", True), Jump("change_eyeball")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextPupil", False), Jump("change_pupil")]
                            text "Pupil Style" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextPupil", True), Jump("change_pupil")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextPupilColor", False), Jump("change_eye_color")]
                            text "Eye Color" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextPupilColor", True), Jump("change_eye_color")]
                null height 5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    vbox:
                        xalign 0.5
                        text "Nose" xalign 0.5 yalign 0.5
                        null height 10
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextNose", False), Jump("change_nose")]
                            text "Nose Shape" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextNose", True), Jump("change_nose")]
                null height 5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    vbox:
                        xalign 0.5
                        text "Mouth" xalign 0.5 yalign 0.5
                        null height 10
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextMouth", False), Jump("change_mouth")]
                            text "Mouth Shape" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextMouth", True), Jump("change_mouth")]
                null height 5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    vbox:
                        xalign 0.5
                        text "Jewelry" xalign 0.5 yalign 0.5
                        null height 10
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextEarring", False), Jump("change_earring")]
                            text "Earring Style" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextEarring", True), Jump("change_earring")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextEarringColor", False), Jump("change_earring_color")]
                            text "Earring Color" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextEarringColor", True), Jump("change_earring_color")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextGlasses", False), Jump("change_glasses")]
                            text "Glasses Style" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextGlasses", True), Jump("change_glasses")]
                        null height 5
                        hbox:
                            xalign 0.5 yalign 0.5
                            textbutton "<" yalign 0.5 action [SetVariable("nextGlassesColor", False), Jump("change_glasses_color")]
                            text "Glasses Color" yalign 0.5
                            textbutton ">" yalign 0.5 action [SetVariable("nextGlassesColor", True), Jump("change_glasses_color")]
                null height 5
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    textbutton "Random" xalign 0.5 yalign 0.5 action Jump("random_wife")
                null height 10
                frame:
                    background None
                    xpadding 25
                    xalign 0.5 yalign 0.5
                    textbutton "Finished" xalign 0.5 yalign 0.5 action Jump("wife_finished")

screen change_husband():
    modal True
    frame:
        background None
        xysize(875, 570)
        xalign 0.79 yalign 0.63
        vbox:
            xalign 0.5 yalign 0.5
            text "Face" xalign 0.5 yalign 0.5
            null height 5
            vbox:
                xalign 0.5
                hbox:
                    xalign 0.5
                    textbutton "<" yalign 0.5 action [SetVariable("nextSkin", False), Jump("change_skin")]
                    text "Skin Color" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextSkin", True), Jump("change_skin")]
                    null width 10
                    textbutton "<" yalign 0.5 action [SetVariable("nextNose", False), Jump("change_head")]
                    text "Head Shape" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextNose", True), Jump("change_head")]
                hbox:
                    xalign 0.5
                    textbutton "<" yalign 0.5 action [SetVariable("nextNose", False), Jump("change_nose")]
                    text "Nose Shape" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextNose", True), Jump("change_nose")]
                    null width 10
                    textbutton "<" yalign 0.5 action [SetVariable("nextMouth", False), Jump("change_mouth")]
                    text "Mouth Shape" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextMouth", True), Jump("change_mouth")]
            null height 30
            vbox:
                xalign 0.5
                text "Eyes" xalign 0.5 yalign 0.5
                null height 5
                hbox:
                    xalign 0.5
                    textbutton "<" yalign 0.5 action [SetVariable("nextEyeball", False), Jump("change_eyeball")]
                    text "Eye Shape" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextEyeball", True), Jump("change_eyeball")]
                    null width 10
                    textbutton "<" yalign 0.5 action [SetVariable("nextPupil", False), Jump("change_pupil")]
                    text "Pupil Style" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextPupil", True), Jump("change_pupil")]
                    null width 10
                    textbutton "<" yalign 0.5 action [SetVariable("nextPupilColor", False), Jump("change_eye_color")]
                    text "Eye Color" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextPupilColor", True), Jump("change_eye_color")]
            null height 30
            vbox:
                xalign 0.5
                text "Hair" xalign 0.5 yalign 0.5
                null height 5
                hbox:
                    textbutton "<" yalign 0.5 action [SetVariable("nextHair", False), Jump("change_hairstyle")]
                    text "Hairstyle" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextHair", True), Jump("change_hairstyle")]
                    null width 10
                    textbutton "<" yalign 0.5 action [SetVariable("nextHairColor", False), Jump("change_hair_color")]
                    text "Hair Color" yalign 0.5
                    textbutton ">" yalign 0.5 action [SetVariable("nextHairColor", True), Jump("change_hair_color")]

    textbutton "Random" xalign 0.45 yalign 0.85 action Jump("random_husband")
    textbutton "Finished" xalign 0.9 yalign 0.85 action [Hide("license"), Jump("enter_husband_name")]


screen license(spouse):
    modal True
    add "license" xalign 0.5 yalign 0.5
    add spouse:
        xysize(600,600)
        xalign 0.15 yalign 0.59
    if spouse == "husband":
        use change_husband

screen custom_main_menu():
    tag mm
    modal True
    add "title" xalign 0.5 yalign 0.1
    hbox:
        xalign 0.5 yalign 0.83
        spacing 1
        imagebutton auto "gui/menu_buttons/start_%s.png" xalign 0.5 yalign 0.5 action Start()
        imagebutton auto "gui/menu_buttons/load_%s.png"  xalign 0.5 yalign 0.5 action ShowMenu("file_slots")
        imagebutton auto "gui/menu_buttons/options_%s.png" xalign 0.5 yalign 0.5 action ShowMenu("preferences")
        imagebutton auto "gui/menu_buttons/extras_%s.png" xalign 0.5 yalign 0.5 action NullAction()
        imagebutton auto "gui/menu_buttons/quit_%s.png" action Quit(confirm=not main_menu)
    text "©2022 Good Tales" xalign 0.99 yalign 0.99

