﻿init python:
    def takeScreenshot():
        """Creates screenshot of current scene before transitioning to the main menu"""
        """(It ordinarily cuts to a black BG by default)"""
        persistent.transitionScreenshot = renpy.screenshot_to_bytes((1920, 1080))
        return

# Characters
define c = Character("Clerk", image="clerk", what_prefix='"', what_suffix='"')
define h = Character("[husband]", what_prefix='"', what_suffix='"')
define w = Character("[wife]", image="wife", what_prefix='"', what_suffix='"')

# Variables
define _game_menu_screen = None

define skinColors = ["#fff6e2", "#ffefcc", "#ffe1b9", "#e4c581", "#704f33"]
define hairColors = ["#fff59d", "#5e4b3b", "#262626", "#c65d00", "#d5d5d5", "#ff0000", "#0006d0", "#a100d0", "#fec3ff", "#56cebd"]
define eyeColors = ["#5f523b", "#69b35f", "#0086e1", "#ffec00", "#ededed", "#e30000"]
define earringColors = ["#aaaaaa", "#222222", "#ffffff", "#a58a00"]
define glassesColors = ["#000000", "#b0b0b0", "#d3b600"]
default bodyTypes = ["01"]
default hairStyles = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
default eyeShapes = ["01", "02", "03"]
default pupilShapes = ["01", "02"]
default noseShapes = ["01", "02", "03", "04", "05"]
default mouthShapes = ["01", "02", "03"]
default breastSizes = ["01", "02", "03"]
default headShapes = ["01", "02"]
default earringStyles = ["01", "02", "03", "04"]
default glassesStyles = ["01", "02", "03"]

default hairColor = hairColors[0]
default bodyColor = skinColors[0]
default pupilColor = eyeColors[0]
default earringColor = earringColors[0]
default glassesColor = glassesColors[0]
default wife = ""
default husband = ""
default surname = ""

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
transform middle:
    zoom 0.95
    xalign 0.5 yalign 1.0

transform left:
    zoom 0.95
    xalign 0.25 yalign 1.0

# Transitions
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
image good_tales = "Good Tales.png"
image title = "title.png"

# Backgrounds
image bg beach = "backgrounds/beach.png"
image bg black = "#000000"
image bg fade:
    "bg black"
    alpha 0.75
image bg front_desk = "#f09d00"
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
image bg resort_exterior = "#004362"
image bg white = "#ffffff"

# Animated Images
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

# Text Images
image splashtext = ParameterizedText(style="splash")

# Wife Images
image hair_back:
    "wife/hair back/%s.png" % wifeDesign["hairNumber"]
    matrixcolor TintMatrix(hairColor)
image body:
    "wife/body/%s.png" % wifeDesign["bodyNumber"]
    matrixcolor TintMatrix(bodyColor)
image arms:
    "wife/arms/%s.png" % wifeDesign["armNumber"]
    matrixcolor TintMatrix(bodyColor)
image breasts:
    "wife/breasts/%s.png" % wifeDesign["breastNumber"]
    matrixcolor TintMatrix(bodyColor)
image head:
    "wife/head/%s.png" % wifeDesign["headNumber"]
    matrixcolor TintMatrix(bodyColor)
image earrings:
    "wife/earrings/%s.png" % wifeDesign["earringNumber"]
    matrixcolor TintMatrix(earringColor)
image eyeballs:
    "wife/eyeballs/%s.png" % wifeDesign["eyeballNumber"]
image pupils:
    "wife/pupils/%s.png" % wifeDesign["pupilNumber"]
    matrixcolor TintMatrix(pupilColor)
image nose:
    "wife/nose/%s.png" % wifeDesign["noseNumber"]
    matrixcolor TintMatrix(bodyColor)
image glasses_frames:
    "wife/glasses/%s_frames.png" % wifeDesign["glassesNumber"]
    matrixcolor TintMatrix(glassesColor)
image glasses_lenses:
    "wife/glasses/%s_lenses.png" % wifeDesign["glassesNumber"]

image mouth_blank:
    "wife/mouth/%s_blank.png" % wifeDesign["mouthNumber"]
    matrixcolor TintMatrix(bodyColor)
image mouth_smile:
    "wife/mouth/%s_smile.png" % wifeDesign["mouthNumber"]
    matrixcolor TintMatrix(bodyColor)

image hair_shadow:
    "wife/hair shadow/%s.png" % wifeDesign["hairNumber"]
    matrixcolor TintMatrix(bodyColor)
    alpha 0.75
image hair_top:
    "wife/hair top/%s.png" % wifeDesign["hairNumber"]
    matrixcolor TintMatrix(hairColor)

image eyebrows_level:
    "wife/eyebrows/01.png"
    matrixcolor TintMatrix(hairColor)
image eyebrows_sad:
    "wife/eyebrows/02.png"
    matrixcolor TintMatrix(hairColor)
image eyebrows_mad:
    "wife/eyebrows/03.png"
    matrixcolor TintMatrix(hairColor)

image bikini_bottom = "wife/outfits/bikini/bottom.png"
layeredimage bikini_top:
    if wifeDesign["breastNumber"] == "01":
        "wife/outfits/bikini/top_small.png"
    elif wifeDesign["breastNumber"] == "02":
        "wife/outfits/bikini/top_medium.png"
    elif wifeDesign["breastNumber"] == "03":
        "wife/outfits/bikini/top_large.png"

image coat_base = "wife/outfits/coat/coat_base.png"
image jeans = "wife/outfits/coat/jeans.png"
layeredimage coat_breasts:
    if wifeDesign["breastNumber"] == "01":
        "wife/outfits/coat/breasts_small.png"
    elif wifeDesign["breastNumber"] == "02":
        "wife/outfits/coat/breasts_medium.png"
    elif wifeDesign["breastNumber"] == "03":
        "wife/outfits/coat/breasts_large.png"
image coat_sleeves = "wife/outfits/coat/sleeves_01.png"

image clerk = Placeholder("boy")

layeredimage wife:
    always:
        "hair_back"
    group body:
        attribute base:
            "body"
    group bottoms:
        attribute bikini_bottom:
            "bikini_bottom"
        attribute jeans:
            "jeans"
    always:
        "arms"
    group tops:
        attribute coat_base:
            "coat_base"
    group sleeves:
        attribute coat_sleeves:
            "coat_sleeves"
    always:
        "breasts"
    group tops_breasts:
        attribute bikini_top:
            "bikini_top"
        attribute coat_breasts:
            "coat_breasts"
    always:
        "head"
    always:
        "earrings"
    always:
        "eyeballs"
    always:
        "pupils"
    always:
        "nose"
    always:
        "glasses_lenses"
    always:
        "glasses_frames"
    group mouth:
        attribute smile:
            "mouth_smile"
        attribute blank:
            "mouth_blank"
    always:
        "hair_shadow"
    always:
        "hair_top"
    group eyebrows:
        attribute sad:
            "eyebrows_sad"
        attribute level:
            "eyebrows_level"
        attribute mad:
            "eyebrows_mad"

# Custom Music Channel
init python:
    renpy.music.register_channel(name="ambience", mixer="sound", loop=None, stop_on_mute=True)

# Music
define audio.flashback = "audio/music/Fun-Times_Looping.ogg"
define audio.lobby = "<loop 4.6>audio/music/Pride_v002.ogg"
define audio.ominous = "audio/music/Ominous-Underground-Goings-On.ogg"
define audio.spooky = "audio/music/More Sewer Creepers_Looping.ogg"
define audio.title = "<loop 7.8>audio/music/Another-Case-for-the-Inspector.ogg"

# Sound Effects
define audio.beach_ambience = "audio/se/beach_ambience.ogg"
define audio.door_creak_long = "audio/se/door_creak_long.ogg"
define audio.door_creak_short = "audio/se/door_creak_short.ogg"
define audio.footsteps_snow = "audio/se/footsteps_snow.ogg"
define audio.wind = "audio/se/wind.ogg"


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
    if renpy.music.get_playing("sound") != "audio/se/wind.ogg":
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
