label random_wife:
    python:
        bodyColor = renpy.random.choice(skinColors)
        hairColor = renpy.random.choice(hairColors)
        pupilColor = renpy.random.choice(eyeColors)
        earringColor = renpy.random.choice(earringColors)
        glassesColor = renpy.random.choice(glassesColors)
        wifeDesign["breastNumber"] = renpy.random.choice(breastSizes)
        wifeDesign["eyeballNumber"] = renpy.random.choice(eyeShapes)
        wifeDesign["hairNumber"] = renpy.random.choice(hairStyles)
        wifeDesign["mouthNumber"] = renpy.random.choice(mouthShapes)
        wifeDesign["noseNumber"] = renpy.random.choice(noseShapes)
        wifeDesign["headNumber"] = renpy.random.choice(headShapes)
        wifeDesign["pupilNumber"] = renpy.random.choice(pupilShapes)
        wifeDesign["earringNumber"] = renpy.random.choice(earringStyles)
        wifeDesign["glassesNumber"] = renpy.random.choice(glassesStyles)
    jump customize_wife

label change_skin:
    python:
        if nextSkin:
            if skinColors.index(bodyColor) == len(skinColors) - 1:
                bodyColor = skinColors[0]
            else:
                bodyColor = skinColors[skinColors.index(bodyColor) + 1]
        else:
            if skinColors.index(bodyColor) == 0:
                bodyColor = skinColors[len(skinColors) - 1]
            else:
                bodyColor = skinColors[skinColors.index(bodyColor) - 1]
    jump customize_wife

label change_head:
    python:
        if nextHead:
            if headShapes.index(wifeDesign["headNumber"]) == len(headShapes) - 1:
                wifeDesign["headNumber"] = headShapes[0]
            else:
                wifeDesign["headNumber"] = headShapes[headShapes.index(wifeDesign["headNumber"]) + 1]
        else:
            if headShapes.index(wifeDesign["headNumber"]) == 0:
                wifeDesign["headNumber"] = headShapes[len(headShapes) - 1]
            else:
                wifeDesign["headNumber"] = headShapes[headShapes.index(wifeDesign["headNumber"]) - 1]
    jump customize_wife

label change_breast:
    python:
        if nextBreast:
            if breastSizes.index(wifeDesign["breastNumber"]) == len(breastSizes) - 1:
                wifeDesign["breastNumber"] = breastSizes[0]
            else:
                wifeDesign["breastNumber"] = breastSizes[breastSizes.index(wifeDesign["breastNumber"]) + 1]
        else:
            if breastSizes.index(wifeDesign["breastNumber"]) == 0:
                wifeDesign["breastNumber"] = breastSizes[len(breastSizes) - 1]
            else:
                wifeDesign["breastNumber"] = breastSizes[breastSizes.index(wifeDesign["breastNumber"]) - 1]
    jump customize_wife

label change_hairstyle:
    python:
        if nextHair:
            if hairStyles.index(wifeDesign["hairNumber"]) == len(hairStyles) - 1:
                wifeDesign["hairNumber"] = hairStyles[0]
            else:
                wifeDesign["hairNumber"] = hairStyles[hairStyles.index(wifeDesign["hairNumber"]) + 1]
        else:
            if hairStyles.index(wifeDesign["hairNumber"]) == 0:
                wifeDesign["hairNumber"] = hairStyles[len(hairStyles) - 1]
            else:
                wifeDesign["hairNumber"] = hairStyles[hairStyles.index(wifeDesign["hairNumber"]) - 1]
    jump customize_wife

label change_hair_color:
    python:
        if nextHairColor:
            if hairColors.index(hairColor) == len(hairColors) - 1:
                hairColor = hairColors[0]
            else:
                hairColor = hairColors[hairColors.index(hairColor) + 1]
        else:
            if hairColors.index(hairColor) == 0:
                hairColor = hairColors[len(hairColors) - 1]
            else:
                hairColor = hairColors[hairColors.index(hairColor) - 1]
    jump customize_wife

label change_eyeball:
    python:
        if nextEyeball:
            if eyeShapes.index(wifeDesign["eyeballNumber"]) == len(eyeShapes) - 1:
                wifeDesign["eyeballNumber"] = eyeShapes[0]
            else:
                wifeDesign["eyeballNumber"] = eyeShapes[eyeShapes.index(wifeDesign["eyeballNumber"]) + 1]
        else:
            if eyeShapes.index(wifeDesign["eyeballNumber"]) == 0:
                wifeDesign["eyeballNumber"] = eyeShapes[len(eyeShapes) - 1]
            else:
                wifeDesign["eyeballNumber"] = eyeShapes[eyeShapes.index(wifeDesign["eyeballNumber"]) - 1]
    jump customize_wife

label change_pupil:
    python:
        if nextPupil:
            if pupilShapes.index(wifeDesign["pupilNumber"]) == len(pupilShapes) - 1:
                wifeDesign["pupilNumber"] = pupilShapes[0]
            else:
                wifeDesign["pupilNumber"] = pupilShapes[pupilShapes.index(wifeDesign["pupilNumber"]) + 1]
        else:
            if pupilShapes.index(wifeDesign["pupilNumber"]) == 0:
                wifeDesign["pupilNumber"] = pupilShapes[len(pupilShapes) - 1]
            else:
                wifeDesign["pupilNumber"] = pupilShapes[pupilShapes.index(wifeDesign["pupilNumber"]) - 1]
    jump customize_wife

label change_eye_color:
    python:
        if nextPupilColor:
            if eyeColors.index(pupilColor) == len(eyeColors) - 1:
                pupilColor = eyeColors[0]
            else:
                pupilColor = eyeColors[eyeColors.index(pupilColor) + 1]
        else:
            if eyeColors.index(pupilColor) == 0:
                pupilColor = eyeColors[len(eyeColors) - 1]
            else:
                pupilColor = eyeColors[eyeColors.index(pupilColor) - 1]
    jump customize_wife

label change_nose:
    python:
        if nextNose:
            if noseShapes.index(wifeDesign["noseNumber"]) == len(noseShapes) - 1:
                wifeDesign["noseNumber"] = noseShapes[0]
            else:
                wifeDesign["noseNumber"] = noseShapes[noseShapes.index(wifeDesign["noseNumber"]) + 1]
        else:
            if noseShapes.index(wifeDesign["noseNumber"]) == 0:
                wifeDesign["noseNumber"] = noseShapes[len(noseShapes) - 1]
            else:
                wifeDesign["noseNumber"] = noseShapes[noseShapes.index(wifeDesign["noseNumber"]) - 1]
    jump customize_wife

label change_mouth:
    python:
        if nextMouth:
            if mouthShapes.index(wifeDesign["mouthNumber"]) == len(mouthShapes) - 1:
                wifeDesign["mouthNumber"] = mouthShapes[0]
            else:
                wifeDesign["mouthNumber"] = mouthShapes[mouthShapes.index(wifeDesign["mouthNumber"]) + 1]
        else:
            if mouthShapes.index(wifeDesign["mouthNumber"]) == 0:
                wifeDesign["mouthNumber"] = mouthShapes[len(mouthShapes) - 1]
            else:
                wifeDesign["mouthNumber"] = mouthShapes[mouthShapes.index(wifeDesign["mouthNumber"]) - 1]
    jump customize_wife

label change_earring:
    python:
        if nextEarring:
            if earringStyles.index(wifeDesign["earringNumber"]) == len(earringStyles) - 1:
                wifeDesign["earringNumber"] = earringStyles[0]
            else:
                wifeDesign["earringNumber"] = earringStyles[earringStyles.index(wifeDesign["earringNumber"]) + 1]
        else:
            if earringStyles.index(wifeDesign["earringNumber"]) == 0:
                wifeDesign["earringNumber"] = earringStyles[len(earringStyles) - 1]
            else:
                wifeDesign["earringNumber"] = earringStyles[earringStyles.index(wifeDesign["earringNumber"]) - 1]
    jump customize_wife

label change_earring_color:
    python:
        if nextEarringColor:
            if earringColors.index(earringColor) == len(earringColors) - 1:
                earringColor = earringColors[0]
            else:
                earringColor = earringColors[earringColors.index(earringColor) + 1]
        else:
            if earringColors.index(earringColor) == 0:
                earringColor = earringColors[len(earringColors) - 1]
            else:
                earringColor = earringColors[earringColors.index(earringColor) - 1]
    jump customize_wife

label change_glasses:
    python:
        if nextGlasses:
            if glassesStyles.index(wifeDesign["glassesNumber"]) == len(glassesStyles) - 1:
                wifeDesign["glassesNumber"] = glassesStyles[0]
            else:
                wifeDesign["glassesNumber"] = glassesStyles[glassesStyles.index(wifeDesign["glassesNumber"]) + 1]
        else:
            if glassesStyles.index(wifeDesign["glassesNumber"]) == 0:
                wifeDesign["glassesNumber"] = glassesStyles[len(glassesStyles) - 1]
            else:
                wifeDesign["glassesNumber"] = glassesStyles[glassesStyles.index(wifeDesign["glassesNumber"]) - 1]
    jump customize_wife

label change_glasses_color:
    python:
        if nextGlassesColor:
            if glassesColors.index(glassesColor) == len(glassesColors) - 1:
                glassesColor = glassesColors[0]
            else:
                glassesColor = glassesColors[glassesColors.index(glassesColor) + 1]
        else:
            if glassesColors.index(glassesColor) == 0:
                glassesColor = glassesColors[len(glassesColors) - 1]
            else:
                glassesColor = glassesColors[glassesColors.index(glassesColor) - 1]
    jump customize_wife
