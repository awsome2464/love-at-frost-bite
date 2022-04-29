label random_husband:
    python:
        bodyColorH = renpy.random.choice(skinColors)
        hairColorH = renpy.random.choice(hairColors)
        pupilColorH = renpy.random.choice(eyeColors)
        earringColorH = renpy.random.choice(earringColors)
        glassesColorH = renpy.random.choice(glassesColors)
        husbandDesign["eyeballNumber"] = renpy.random.choice(eyeShapesH)
        husbandDesign["hairNumber"] = renpy.random.choice(hairStylesH)
        husbandDesign["mouthNumber"] = renpy.random.choice(mouthShapesH)
        husbandDesign["noseNumber"] = renpy.random.choice(noseShapesH)
        husbandDesign["headNumber"] = renpy.random.choice(headShapesH)
        husbandDesign["pupilNumber"] = renpy.random.choice(pupilShapesH)
        husbandDesign["earringNumber"] = renpy.random.choice(earringStylesH)
        husbandDesign["glassesNumber"] = renpy.random.choice(glassesStylesH)
    jump customize_husband

label random_wife:
    python:
        bodyColorW = renpy.random.choice(skinColors)
        hairColorW = renpy.random.choice(hairColors)
        pupilColorW = renpy.random.choice(eyeColors)
        earringColorW = renpy.random.choice(earringColors)
        glassesColorW = renpy.random.choice(glassesColors)
        wifeDesign["breastNumber"] = renpy.random.choice(breastSizes)
        wifeDesign["eyeballNumber"] = renpy.random.choice(eyeShapesW)
        wifeDesign["hairNumber"] = renpy.random.choice(hairStylesW)
        wifeDesign["mouthNumber"] = renpy.random.choice(mouthShapesW)
        wifeDesign["noseNumber"] = renpy.random.choice(noseShapesW)
        wifeDesign["headNumber"] = renpy.random.choice(headShapesW)
        wifeDesign["pupilNumber"] = renpy.random.choice(pupilShapesW)
        wifeDesign["earringNumber"] = renpy.random.choice(earringStylesW)
        wifeDesign["glassesNumber"] = renpy.random.choice(glassesStylesW)
    jump customize_wife


label change_skin:
    python:
        if customChar == "wife":
            bodyColor = bodyColorW
        elif customChar == "husband":
            bodyColor = bodyColorH

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

        if customChar == "wife":
            bodyColorW = bodyColor
            renpy.jump("customize_wife")
        elif customChar == "husband":
            bodyColorH = bodyColor
            renpy.jump("customize_husband")


label change_head:
    python:
        if customChar == "wife":
            headShapes = headShapesW
            charDesign = wifeDesign
        elif customChar == "husband":
            headShapes = headShapesH
            charDesign = husbandDesign

        if nextHead:
            if headShapes.index(charDesign["headNumber"]) == len(headShapes) - 1:
                charDesign["headNumber"] = headShapes[0]
            else:
                charDesign["headNumber"] = headShapes[headShapes.index(charDesign["headNumber"]) + 1]
        else:
            if headShapes.index(wifeDesign["headNumber"]) == 0:
                charDesign["headNumber"] = headShapes[len(headShapes) - 1]
            else:
                charDesign["headNumber"] = headShapes[headShapes.index(charDesign["headNumber"]) - 1]

        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")


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
        if customChar == "wife":
            hairStyles = hairStylesW
            charDesign = wifeDesign
        elif customChar == "husband":
            hairStyles = hairStylesH
            charDesign = husbandDesign

        if nextHair:
            if hairStyles.index(charDesign["hairNumber"]) == len(hairStyles) - 1:
                charDesign["hairNumber"] = hairStyles[0]
            else:
                charDesign["hairNumber"] = hairStyles[hairStyles.index(charDesign["hairNumber"]) + 1]
        else:
            if hairStyles.index(charDesign["hairNumber"]) == 0:
                charDesign["hairNumber"] = hairStyles[len(hairStyles) - 1]
            else:
                charDesign["hairNumber"] = hairStyles[hairStyles.index(charDesign["hairNumber"]) - 1]
    
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")

label change_hair_color:
    python:
        if customChar == "wife":
            hairColor = hairColorW
        elif customChar == "husband":
            hairColor = hairColorH

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
    
        if customChar == "wife":
            hairColorW = hairColor
            renpy.jump("customize_wife")
        elif customChar == "husband":
            hairColorH = hairColor
            renpy.jump("customize_husband")

label change_eyeball:
    python:
        if customChar == "wife":
            eyeShapes = eyeShapesW
            charDesign = wifeDesign
        elif customChar == "husband":
            eyeShapes = eyeShapesH
            charDesign = husbandDesign

        if nextEyeball:
            if eyeShapes.index(charDesign["eyeballNumber"]) == len(eyeShapes) - 1:
                charDesign["eyeballNumber"] = eyeShapes[0]
            else:
                charDesign["eyeballNumber"] = eyeShapes[eyeShapes.index(charDesign["eyeballNumber"]) + 1]
        else:
            if eyeShapes.index(charDesign["eyeballNumber"]) == 0:
                charDesign["eyeballNumber"] = eyeShapes[len(eyeShapes) - 1]
            else:
                charDesign["eyeballNumber"] = eyeShapes[eyeShapes.index(charDesign["eyeballNumber"]) - 1]
    
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")

label change_pupil:
    python:
        if customChar == "wife":
            pupilShapes = pupilShapesW
            charDesign = wifeDesign
        elif customChar == "husband":
            pupilShapes = pupilShapesH
            charDesign = husbandDesign

        if nextPupil:
            if pupilShapes.index(charDesign["pupilNumber"]) == len(pupilShapes) - 1:
                charDesign["pupilNumber"] = pupilShapes[0]
            else:
                charDesign["pupilNumber"] = pupilShapesW[pupilShapes.index(charDesign["pupilNumber"]) + 1]
        else:
            if pupilShapes.index(charDesign["pupilNumber"]) == 0:
                charDesign["pupilNumber"] = pupilShapes[len(pupilShapes) - 1]
            else:
                charDesign["pupilNumber"] = pupilShapes[pupilShapes.index(charDesign["pupilNumber"]) - 1]
    
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")

label change_eye_color:
    python:
        if customChar == "wife":
            pupilColor = pupilColorW
        elif customChar == "husband":
            pupilColor = pupilColorH

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
    
        if customChar == "wife":
            pupilColorW = pupilColor
            renpy.jump("customize_wife")
        elif customChar == "husband":
            pupilColorH = pupilColor
            renpy.jump("customize_husband")

label change_nose:
    python:
        if customChar == "wife":
            noseShapes = noseShapesW
            charDesign = wifeDesign
        elif customChar == "husband":
            noseShapes = noseShapesH
            charDesign = husbandDesign

        if nextNose:
            if noseShapes.index(charDesign["noseNumber"]) == len(noseShapes) - 1:
                charDesign["noseNumber"] = noseShapes[0]
            else:
                charDesign["noseNumber"] = noseShapes[noseShapes.index(charDesign["noseNumber"]) + 1]
        else:
            if noseShapes.index(charDesign["noseNumber"]) == 0:
                wifeDesign["noseNumber"] = noseShapes[len(noseShapes) - 1]
            else:
                charDesign["noseNumber"] = noseShapes[noseShapes.index(charDesign["noseNumber"]) - 1]
    
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")

label change_mouth:
    python:
        if customChar == "wife":
            mouthShapes = mouthShapesW
            charDesign = wifeDesign
        elif customChar == "husband":
            mouthShapes = mouthShapesH
            charDesign = husbandDesign

        if nextMouth:
            if mouthShapes.index(charDesign["mouthNumber"]) == len(mouthShapes) - 1:
                charDesign["mouthNumber"] = mouthShapes[0]
            else:
                charDesign["mouthNumber"] = mouthShapes[mouthShapes.index(charDesign["mouthNumber"]) + 1]
        else:
            if mouthShapes.index(charDesign["mouthNumber"]) == 0:
                charDesign["mouthNumber"] = mouthShapes[len(mouthShapes) - 1]
            else:
                charDesign["mouthNumber"] = mouthShapes[mouthShapes.index(charDesign["mouthNumber"]) - 1]
    
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")

label change_earring:
    python:
        if customChar == "wife":
            earringStyles = earringStylesW
            charDesign = wifeDesign
        elif customChar == "husband":
            earringStyles = earringStylesH
            charDesign = husbandDesign

        if nextEarring:
            if earringStyles.index(charDesign["earringNumber"]) == len(earringStyles) - 1:
                charDesign["earringNumber"] = earringStyles[0]
            else:
                charDesign["earringNumber"] = earringStyles[earringStyles.index(charDesign["earringNumber"]) + 1]
        else:
            if earringStyles.index(charDesign["earringNumber"]) == 0:
                charDesign["earringNumber"] = earringStyles[len(earringStyles) - 1]
            else:
                charDesign["earringNumber"] = earringStyles[earringStyles.index(charDesign["earringNumber"]) - 1]
        
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")

label change_earring_color:
    python:
        if customChar == "wife":
            earringColor = earringColorW
        elif customChar == "husband":
            earringColor = earringColorH

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
    
        if customChar == "wife":
            earringColorW = earringColor
            renpy.jump("customize_wife")
        elif customChar == "husband":
            earringColorH = earringColor
            renpy.jump("customize_husband")


label change_glasses:
    python:
        if customChar == "wife":
            glassesStyles = glassesStylesW
            charDesign = wifeDesign
        elif customChar == "husband":
            glassesStyles = glassesStylesH
            charDesign = husbandDesign

        if nextGlasses:
            if glassesStyles.index(charDesign["glassesNumber"]) == len(glassesStyles) - 1:
                charDesign["glassesNumber"] = glassesStyles[0]
            else:
                charDesign["glassesNumber"] = glassesStyles[glassesStyles.index(charDesign["glassesNumber"]) + 1]
        else:
            if glassesStyles.index(charDesign["glassesNumber"]) == 0:
                charDesign["glassesNumber"] = glassesStyles[len(glassesStyles) - 1]
            else:
                charDesign["glassesNumber"] = glassesStyles[glassesStyles.index(charDesign["glassesNumber"]) - 1]
    
        if customChar == "wife":
            renpy.jump("customize_wife")
        elif customChar == "husband":
            renpy.jump("customize_husband")


label change_glasses_color:
    python:
        if customChar == "wife":
            glassesColor = glassesColorW
        elif customChar == "husband":
            glassesColor = glassesColorH

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
    
        if customChar == "wife":
            glassesColorW = glassesColor
            renpy.jump("customize_wife")
        elif customChar == "husband":
            glassesColorH = glassesColor
            renpy.jump("customize_husband")
