init python:
    def takeScreenshot():
        """Creates screenshot of current scene before transitioning to the main menu"""
        """(It ordinarily cuts to a black BG by default)"""
        persistent.transitionScreenshot = renpy.screenshot_to_bytes((1920, 1080))
        return

# Characters
define c = Character("Clerk", image="clerk", what_prefix='"', what_suffix='"')
define h = Character("[husband]", what_prefix='"', what_suffix='"')
define m = Character("Maid", image="maid", what_prefix='"', what_suffix='"')
define w = Character("[wife]", image="wife", what_prefix='"', what_suffix='"')

# Variables
define _game_menu_screen = None

define skinColors = ["#fff6e2", "#ffefcc", "#ffe1b9", "#e4c581", "#704f33"]
define hairColors = ["#fff59d", "#5e4b3b", "#262626", "#c65d00", "#d5d5d5", "#ff0000", "#0006d0", "#a100d0", "#fec3ff", "#56cebd"]
define eyeColors = ["#5f523b", "#69b35f", "#0086e1", "#ffec00", "#ededed", "#e30000"]
define earringColors = ["#aaaaaa", "#222222", "#ffffff", "#a58a00"]
define glassesColors = ["#000000", "#b0b0b0", "#d3b600"]

default hairStylesH = ["01", "02"]
default eyeShapesH = ["01", "02"]
default pupilShapesH = ["01", "02"]
default noseShapesH = ["01", "02"]
default mouthShapesH = ["01", "02"]
default headShapesH = ["01", "02"]
default earringStylesH = ["01", "02"]
default glassesStylesH = ["01", "02"]

default hairStylesW = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
default eyeShapesW = ["01", "02", "03"]
default pupilShapesW = ["01", "02"]
default noseShapesW = ["01", "02", "03", "04", "05"]
default mouthShapesW = ["01", "02", "03", "04"]
default breastSizes = ["01", "02", "03"]
default headShapesW = ["01", "02"]
default earringStylesW = ["01", "02", "03", "04"]
default glassesStylesW = ["01", "02", "03"]

default hairColorH = hairColors[0]
default bodyColorH = skinColors[0]
default pupilColorH = eyeColors[0]
default earringColorH = earringColors[0]
default glassesColorH = glassesColors[0]

default hairColorW = hairColors[0]
default bodyColorW = skinColors[0]
default pupilColorW = eyeColors[0]
default earringColorW = earringColors[0]
default glassesColorW = glassesColors[0]

default wifeHairLengths = {"short": ["01", "02", "03", "05", "06", "10"], "long": ["04", "07", "08", "09"]}

default hairLengthWText = ""
default hairColorWText = ""

default glassesFog = False
default glassesOn = True
default husband = ""
default surname = ""
default wife = ""
default wifeBottom = "bikini"
default wifeTop = "bikini"

default husbandDesign = {"hairNumber": "01", 
"eyeballNumber": "01", 
"pupilNumber": "01", 
"headNumber": "01", 
"noseNumber": "01", 
"mouthNumber": "01", 
"earringNumber": "01", 
"glassesNumber": "01"}

default wifeDesign = {"bodyNumber": "01", 
"hairNumber": "01", 
"eyeballNumber": "01", 
"pupilNumber": "01", 
"headNumber": "01", 
"noseNumber": "01", 
"mouthNumber": "01", 
"breastNumber": "01", 
"earringNumber": "01", 
"armNumber": "01", 
"glassesNumber": "01"}

default customChar = "wife"

default nextSkin = False
default nextHead = False
default nextBreast = False
default nextHair = False
default nextHairColor = False
default nextEyeball = False
default nextPupil = False
default nextPupilColor = False
default nextNose = False
default nextGlasses = False
default nextGlassesColor = False
default nextMouth = False
default nextEarring = False
default nextEarringColor = False

default inputCharacters = "abcdefghijklmnopqrstuvwxyz -ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Transforms
transform left:
    zoom 0.95
    xalign 0.25 yalign 1.0

transform middle:
    zoom 0.95
    xalign 0.5 yalign 1.0

transform middle_close:
    zoom 1.25
    xalign 0.5 yalign 0.0

transform middle_close_shiver:
    zoom 1.25
    xalign 0.4975 yalign 0.0
    linear 0.1 xalign 0.5035
    linear 0.1 xalign 0.4975
    repeat

transform right:
    zoom 0.95
    xalign 0.75 yalign 1.0

# Transitions
define eyes_close_fast = ImageDissolve(image="eyelids.png", time=0.1, ramplen=8, reverse=True, alpha=True, time_warp=None)
define eyes_close_slow = ImageDissolve(image="eyelids.png", time=1.0, ramplen=8, reverse=True, alpha=True, time_warp=None)
define eyes_open_fast = ImageDissolve(image="eyelids.png", time=0.1, ramplen=8, reverse=False, alpha=True, time_warp=None)
define eyes_open_slow = ImageDissolve(image="eyelids.png", time=1.0, ramplen=8, reverse=False, alpha=True, time_warp=None)
define fastdissolve = Dissolve(0.25)
define longdissolve = Dissolve(3.0)
define meddissolve = Dissolve(1.5)
define snowwipe_fast = ImageDissolve(image="snowwipe.png", time=0.25, ramplen=8, reverse=False, alpha=True, time_warp=None)
define snowwipe_slow = ImageDissolve(image="snowwipe.png", time=0.5, ramplen=8, reverse=False, alpha=True, time_warp=None)

# Styles
style menu_buttons:
    color "000000"
    hover_color "#0099ff"
    insensitive_color "#8f8f8f"
    text_align 0.5

style pause_menu_buttons:
    size 70
    color "000000"
    hover_color "#0099ff"
    insensitive_color "#8f8f8f"

style quick_menu:
    color "#0099ff"
    hover_color "#000000"
    insensitive_color gui.insensitive_color
    size gui.quick_button_text_size
    font gui.interface_text_font

style splash:
    color "#ffffff"
    size 50

# Standard Images
image fade:
    "bg black"
    alpha 0.75
image good_tales = "Good Tales.png"
image intro_pan_01:
    "intro pan/01.png"
    xalign 1.0
    linear 30 xalign 0.4
image intro_pan_02:
    "intro pan/02.png"
    xalign 1.0
    linear 30 xalign 0.3
image intro_pan_03:
    "intro pan/03.png"
    xalign 1.0
    linear 30 xalign 0.2
image intro_pan_04:
    "intro pan/04.png"
    xalign 1.0
    linear 30 xalign 0.1
image intro_pan_05:
    "intro pan/05.png"
    xalign 1.0
    linear 30 xalign 0.0
image intro_pan_banshee = "intro pan/banshee.png"
image license = "license.png"
image title = "title.png"

# Backgrounds
image bg beach = "backgrounds/beach.png"
image bg black = "#000000"
image bg front_desk = "#f09d00"
image bg hallway = "#00cb67"
image bg intro_pan_bg = "#1C203C"
image bg lobby = "#ae7200"
layeredimage bg main_menu:
    always:
        "gui/main_menu.png"
    always:
        "main_menu_figure"
    always:
        "gui/main_menu_02.png"
    always:
        "snowfall_bg"
    always:
        "snowfall_fg"
    always:
        "gui/main_menu_03.png"
    always:
        "shadow_flicker"
image bg stairs = "#00cb18"
image bg resort_exterior = "#004362"
image bg white = "#ffffff"

# Animated Images
layeredimage bg bedroom_default:
    always:
        "bg intro_pan_bg"
    always:
        "snowfall_window"
    always:
        "backgrounds/bedroom_default.png"

layeredimage intro_pan:
    always:
        "intro_pan_01"
    always:
        "intro_pan_02"
    always:
        "intro_pan_03"
    always:
        "intro_pan_04"
    always:
        "intro_pan_05"

image main_menu_figure:
    "gui/main_menu_figure.png"
    yalign 0.55
    choice:
        xalign 0.0
        choice:
            pause 15
        choice:
            pause 30
        choice:
            pause 45
        linear 1 xalign 1.0
    choice:
        xalign 1.0
        choice:
            pause 15
        choice:
            pause 30
        choice:
            pause 45
        linear 1 xalign 0.0
    repeat

image shadow_flicker:
    "gui/shadow_flicker/01.png"
    choice:
        pause 0.1
    choice:
        pause 0.05
    "gui/shadow_flicker/02.png"
    choice:
        pause 0.1
    choice:
        pause 0.05
    "gui/shadow_flicker/03.png"
    choice:
        pause 0.1
    choice:
        pause 0.05
    "gui/shadow_flicker/04.png"
    choice:
        pause 0.1
    choice:
        pause 0.05
    "gui/shadow_flicker/03.png"
    choice:
        pause 0.1
    choice:
        pause 0.05
    "gui/shadow_flicker/02.png"
    choice:
        pause 0.1
    choice:
        pause 0.05
    repeat

image snowfall_bg = SnowBlossom("snow 02.png", count=300, border=5, xspeed=(0,-75), yspeed=(450,475), start=0, fast=True)
image snowfall_fg = SnowBlossom("snow 01.png", count=300, border=5, xspeed=(0,-150), yspeed=(500,575), start=0, fast=True)
image snowfall_window = SnowBlossom("snow 03.png", count=300, border=0, xspeed=(0,-150), yspeed=(500,575), start=0, fast=True)

# Text Images
image splashtext = ParameterizedText(style="splash")

# Husband Images
image husband_hair_back:
    "husband/hair back/%s.png" % husbandDesign["hairNumber"]
    matrixcolor TintMatrix(hairColorH)
image husband_head:
    "husband/head/%s.png" % husbandDesign["headNumber"]
    matrixcolor TintMatrix(bodyColorH)
image husband_eyeballs:
    "husband/eyeballs/%s.png" % husbandDesign["eyeballNumber"]
image husband_pupils:
    "husband/pupils/%s.png" % husbandDesign["pupilNumber"]
    matrixcolor TintMatrix(pupilColorH)
image husband_nose:
    "husband/nose/%s.png" % husbandDesign["noseNumber"]
    matrixcolor TintMatrix(bodyColorH)
image husband_mouth:
    "husband/mouth/%s.png" % husbandDesign["mouthNumber"]
    matrixcolor TintMatrix(bodyColorH)
image husband_hair_shadow:
    "husband/hair shadow/%s.png" % husbandDesign["hairNumber"]
    matrixcolor TintMatrix(bodyColorH)
    alpha 0.75
image husband_hair_top:
    "husband/hair top/%s.png" % husbandDesign["hairNumber"]
    matrixcolor TintMatrix(hairColorH)
image husband_eyebrows:
    "husband/eyebrows/01.png"
    matrixcolor TintMatrix(hairColorH)

# Wife Images
image wife_hair_back:
    "wife/hair back/%s.png" % wifeDesign["hairNumber"]
    matrixcolor TintMatrix(hairColorW)
image wife_body:
    "wife/body/01.png"
    matrixcolor TintMatrix(bodyColorW)
image wife_arms:
    "wife/arms/%s.png" % wifeDesign["armNumber"]
    matrixcolor TintMatrix(bodyColorW)
image breasts:
    "wife/breasts/%s.png" % wifeDesign["breastNumber"]
    matrixcolor TintMatrix(bodyColorW)
image wife_head:
    "wife/head/%s.png" % wifeDesign["headNumber"]
    matrixcolor TintMatrix(bodyColorW)
image wife_earrings:
    "wife/earrings/%s.png" % wifeDesign["earringNumber"]
    matrixcolor TintMatrix(earringColorW)
image wife_eyeballs:
    "wife/eyeballs/%s.png" % wifeDesign["eyeballNumber"]
image wife_pupils:
    "wife/pupils/%s.png" % wifeDesign["pupilNumber"]
    matrixcolor TintMatrix(pupilColorW)
image wife_nose:
    "wife/nose/%s.png" % wifeDesign["noseNumber"]
    matrixcolor TintMatrix(bodyColorW)
image wife_glasses_frames:
    "wife/glasses/%s_frames.png" % wifeDesign["glassesNumber"]
    matrixcolor TintMatrix(glassesColorW)
image wife_glasses_lenses:
    "wife/glasses/%s_lenses.png" % wifeDesign["glassesNumber"]
image wife_glasses_lenses_fog:
    "wife_glasses_lenses"
    alpha 0.8
    ease 5 alpha 0.2

image wife_mouth_blank:
    "wife/mouth/%s_blank.png" % wifeDesign["mouthNumber"]
    matrixcolor TintMatrix(bodyColorW)
image wife_mouth_smile:
    "wife/mouth/%s_smile.png" % wifeDesign["mouthNumber"]
    matrixcolor TintMatrix(bodyColorW)

image wife_hair_shadow:
    "wife/hair shadow/%s.png" % wifeDesign["hairNumber"]
    matrixcolor TintMatrix(bodyColorW)
    alpha 0.75
image wife_hair_top:
    "wife/hair top/%s.png" % wifeDesign["hairNumber"]
    matrixcolor TintMatrix(hairColorW)

image wife_eyebrows_level:
    "wife/eyebrows/01.png"
    matrixcolor TintMatrix(hairColorW)
image wife_eyebrows_sad:
    "wife/eyebrows/02.png"
    matrixcolor TintMatrix(hairColorW)
image wife_eyebrows_mad:
    "wife/eyebrows/03.png"
    matrixcolor TintMatrix(hairColorW)
image wife_eyebrows_raised:
    "wife/eyebrows/04.png"
    matrixcolor TintMatrix(hairColorW)
image wife_eyebrows_casual:
    "wife/eyebrows/05.png"
    matrixcolor TintMatrix(hairColorW)

# Wife Outfits
image wife_top_base = "wife/outfits/[wifeTop]/[wifeTop]_base.png"
image wife_bottoms = "wife/outfits/bottoms/[wifeBottom].png"
image breasts_outfit:
    "wife/outfits/[wifeTop]/breasts_%s.png" % wifeDesign["breastNumber"]
image wife_sleeves:
    "wife/outfits/[wifeTop]/sleeves_%s.png" % wifeDesign["armNumber"]

# Other Characters
image clerk = Placeholder("boy")
image maid = Placeholder("girl")

# Layered Images
layeredimage husband:
    always:
        "husband_hair_back"
    always:
        "husband_head"
    always:
        "husband_eyeballs"
    always:
        "husband_pupils"
    always:
        "husband_nose"
    always:
        "husband_mouth"
    always:
        "husband_hair_shadow"
    always:
        "husband_hair_top"
    always:
        "husband_eyebrows"

layeredimage wife:
    always:
        "wife_hair_back"
    group body:
        attribute base:
            "wife_body"
    always:
        "wife_bottoms"
    always:
        "wife_arms"
    always:
        "wife_top_base"
    always:
        "wife_sleeves"
    always:
        "breasts"
    always:
        "breasts_outfit"
    always:
        "wife_head"
    always:
        "wife_earrings"
    always:
        "wife_eyeballs"
    always:
        "wife_pupils"
    always:
        "wife_nose"
    if glassesFog:
        "wife_glasses_lenses_fog"
    elif not glassesOn:
        "wife_glasses_lenses"
        alpha 0.0
    else:
        "wife_glasses_lenses"
        alpha 0.2   
    if glassesOn:
        "wife_glasses_frames"
        alpha 1.0
    else:
        "wife_glasses_frames"
        alpha 0.0
    group mouth:
        attribute smile:
            "wife_mouth_smile"
        attribute blank:
            "wife_mouth_blank"
    always:
        "wife_hair_shadow"
    always:
        "wife_hair_top"
    group eyebrows:
        attribute sad:
            "wife_eyebrows_sad"
        attribute level:
            "wife_eyebrows_level"
        attribute mad:
            "wife_eyebrows_mad"
        attribute raised:
            "wife_eyebrows_raised"
        attribute casual:
            "wife_eyebrows_casual"

# Custom Music Channel
init python:
    renpy.music.register_channel(name="ambience", mixer="sound", loop=None, stop_on_mute=True)

# Music
define audio.bedroom_normal = "<loop 6.85>audio/music/Cruising-Back-in-Time.ogg"
define audio.fighting = "audio/music/The-Runaway_Looping.ogg"
define audio.flashback = "audio/music/Fun-Times_Looping.ogg"
define audio.lobby = "<loop 4.6>audio/music/Pride_v002.ogg"
define audio.ominous = "audio/music/Ominous-Underground-Goings-On.ogg"
define audio.spooky = "audio/music/More-Sewer-Creepers.ogg"
define audio.title = "<loop 7.8>audio/music/Another-Case-for-the-Inspector.ogg"

# Sound Effects
define audio.banshee_scream = "audio/se/banshee_scream.ogg"
define audio.beach_ambience = "audio/se/beach_ambience.ogg"
define audio.bed_spring = "audio/se/bed_spring.ogg"
define audio.cart = "audio/se/cart.ogg"
define audio.door_creak_long = "audio/se/door_creak_long.ogg"
define audio.door_creak_short = "audio/se/door_creak_short.ogg"
define audio.door_slam = "audio/se/door_slam.ogg"
define audio.footsteps_snow = "audio/se/footsteps_snow.ogg"
define audio.wind = "<loop 1>audio/se/wind.ogg"


label splashscreen:
    $persistent.splash = True
    scene bg black
    $renpy.music.set_volume(volume=0.25, delay=0.5, channel='sound')
    play sound wind loop
    show snowfall_bg zorder 1
    show snowfall_fg zorder 3
    with meddissolve
    show good_tales zorder 2 with longdissolve
    pause 2
    $renpy.music.set_volume(volume=1.0, delay=0.25, channel='sound')
    scene bg white with snowwipe_fast
    pause 0.5
    $renpy.music.set_volume(volume=0.5, delay=0.5, channel='sound')
    return

label before_main_menu:
    if renpy.music.get_playing("sound") != audio.wind:
        play sound wind loop
    if not persistent.splash:
        show expression im.Data(persistent.transitionScreenshot, "screenshot.png"):
            xalign 0.5 yalign 0.5
        $renpy.music.set_volume(volume=1.0, delay=0.25, channel='sound')
        scene bg white with snowwipe_fast
        pause 0.5
        $renpy.music.set_volume(volume=0.5, delay=0.5, channel='sound')
    else:
        scene bg white
    play music title
    scene bg main_menu with snowwipe_slow
    pause 0.5
    show title:
        xalign 0.5 yalign 0.1
    with meddissolve
    pause 1
    $persistent.splash = False
    return

label main_menu:
    hide title
    show screen custom_main_menu
    with dissolve
    pause

label random_wife_devtest:
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
    show wife
    return
