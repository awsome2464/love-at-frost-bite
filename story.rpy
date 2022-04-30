label start:
    $quick_menu = False
    $renpy.music.set_volume(volume=1.0, delay=0, channel='sound')
    play sound wind
    scene bg white
    hide screen custom_main_menu
    with snowwipe_fast
    pause 1
    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene bg black
    with longdissolve
    pause 2
    $renpy.music.set_volume(volume=0.5, delay=0, channel='ambience')
    play ambience wind loop fadein 3.0
    pause 4
    play sound footsteps_snow
    pause 5
    play sound door_creak_short
    pause 1
    $renpy.music.set_volume(volume=0.1, delay=3.0, channel='ambience')
    scene bg lobby with longdissolve
    $renpy.notify(message="Resort Lobby")
    pause 1
    play music lobby
    "Well, we're here."
    "I was honestly worried that we weren't going to make it; the roads were much worse than predicted."
    "Even getting from the car to the door was a hassle; there had to have been at least a foot of snow out there!"
    "It almost makes me regret deciding to take a vacation in the winter..."
    "...but I know that she prefers this sort of atmosphere as opposed to a tropical resort."
    "Of course, that doesn't mean she's against such a thing."
    "In fact, she's the one who decided to have our honeymoon be at the beach."
    "Man...{w=0.5}\nWhat a time that was."
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    scene bg white with meddissolve
    pause 1
    $renpy.music.set_volume(volume=1.0, delay=0, channel='ambience')
    play ambience beach_ambience
    play music flashback
    scene bg beach with meddissolve
    "It may have only been a couple of years ago, but it's still a time I'll treasure always."
    "The sun was warm, the air was clean, and the breeze was just right."
    "But of course, the greatest sight of them all..."
    window hide
    pause 1
    show wife base sad smile at middle with meddissolve
    pause 1
    window show
    "...was my beautiful wife."
    window hide
    $quick_menu = True
label customize_wife:
    $renpy.block_rollback()
    show wife
    show screen change_wife
    pause

label wife_finished:
    hide screen change_wife
    show wife at left with easeinright
    $quick_menu = False
    window show
    "Are you satisfied with the wife's appearance?\nIt can not be changed later.{nw}"
    menu:
        "Are you satisfied with the wife's appearance?\nIt can not be changed later.{fast}"
        "I'm satisfied":
            jump satisfied
        "I'm not satisfied":
            window hide
            $quick_menu = True
            show wife at middle with easeinleft
            jump customize_wife

label satisfied:
    $renpy.block_rollback()
    $quick_menu = False
    window hide
    show wife at middle with easeinleft
    window show
    "She truly is just as beautiful now as she was then."
    "If only she thought the same about me..."
    c "Good afternoon, Sir!"
    stop music
    $renpy.music.set_volume(volume=0.1, delay=0, channel='ambience')
    play ambience wind
    scene bg lobby
    "A voice called out from the front desk."
    scene bg front_desk
    show clerk at left
    with dissolve
    $renpy.notify(message="Front Desk")
    play music lobby
    c "Welcome to the Triple Oak Resort!"
    c "Do you have a reservation?"
    "I gave a nod as I breathed onto my hands to warm them up."
    "Even though it was significantly warmer in here than out there, it's still taking a minute to get my blood flowing again."
    c "Alright, and what name is it under?"
label enter_surname:
    $surname = renpy.input("Enter the couple's surname.", length=20, default=surname, allow=inputCharacters)
    $surname.strip()
    if not surname:
        c "I'm sorry, Sir; I didn't get that."
        jump enter_surname
    c "The reservation is under [surname]. Is that correct?{nw}"
    menu:
        c "The reservation is under [surname]. Is that correct?{fast}"
        "That's correct.":
            jump entered_surname
        "No, that's not right.":
            c "I see. Then please tell me again."
            jump enter_surname

label entered_surname:
    c "Alright, let me see here..."
    c "Ah, yes! I see a reservation under that name here."
    c "But for security purposes, I'll need the identifications of the parties."
    "With another nod, I took out my driver's license, as well as my wife's, and handed them over to him."
    c "Alright, let's see..."

label customize_husband:
    $renpy.block_rollback()
    $customChar = "husband"
    window hide
    $quick_menu = True
    if renpy.get_screen("license"):
        hide screen license
        show screen license("husband")
    else:
        show fade with dissolve
        pause 0.5
        show screen license("husband")
        with dissolve
    pause

label enter_husband_name:
    hide fade
    $husband = renpy.input("Enter the husband's name.", length=20, default=husband, allow=inputCharacters)
    $husband.strip()
    hide screen license
    if not husband:
        $quick_menu = False
        window show
        "Come on, now; I have a name."
        jump enter_husband_name
    $quick_menu = False
    window show
    c "So you're Mr. [husband] [surname]?{nw}"
    menu:
        c "So you're Mr. [husband] [surname]?{fast}"
        "Yes, that's me.":
            jump entered_husband_name
        "No, that's not me.":
            c "Hm. Perhaps I read it wrong. Let me check again."
            jump enter_husband_name

label entered_husband_name:
    c "Very well. And your wife would be..."

label enter_wife_name:
    $wife = renpy.input("Enter the wife's name.", length=20, default=wife, allow=inputCharacters)
    $wife.strip()
    if not wife:
        "Come on, now; she has a name."
        jump enter_wife_name
    c "...Mrs. [wife] [surname]. Is that correct?{nw}"
    menu:
        c "...Mrs. [wife] [surname]. Is that correct?{fast}"
        "Yes, that's her.":
            jump entered_wife_name
        "No, that's not her.":
            c "Hm. Perhaps I read it wrong. Let me check again."
            jump enter_wife_name

label entered_wife_name:
    c "Thank you, Sir."
    "He gave me the IDs and the room key, and I accepted them with a nod."
    h "Thank you."
    play sound door_creak_short
    "I then heard the front door creak open behind me."
    "Turning around, I found the one responsible."
    $wifeTop = "coat"
    $wifeBottom = "jeans"
    scene bg lobby with dissolve
    pause 1
    $glassesFog = True
    $wifeDesign["armNumber"] = "02"
    show wife base level blank at middle with dissolve
    w "Whew! It's freezing out there!"
    h "You can say that again.{w=0.5} Were you able to find a decent parking spot?"
    $glassesFog = False
    w sad "Barely.{w=0.5} It's still quite a walk away."
    w level "Then again, maybe it just feels that way because I can barely see 3 feet in front of me."
    w mad "Probably would've helped if I had someone out here to look with me."
    h "You're the one who wanted to save time by getting checked in as soon as possible."
    w "I never said it had to be done as soon as we arrived!"
    h "Well, maybe you should've said something at the time instead of waiting until now!"
    w "I shouldn't had to have said anything, [husband]!"
    "I took a deep breath and tried to calm myself."
    "The vacation hadn't even properly begun yet; I don't want it off to a bad start."
    h "Look, we found a parking spot and we're checked in. That's all that matters right now."
    h "Let's just get our stuff up to our room and relax."
    w level "..."
    $wifeDesign["armNumber"] = "01"
    w smile "Sounds good. Just help me get the rest of the luggage from the car."
    h "Sounds like a plan."
    window hide
    pause 1
    stop music fadeout 3.0
    $renpy.music.set_volume(volume=0.5, delay=3.0, channel='ambience')
    scene bg resort_exterior
    show snowfall_bg zorder 1
    show snowfall_fg zorder 3
    with longdissolve
    pause 1
    window show
    h "Ugh...{w=0.2} This was really the closest you could've parked?"
    w "What, can you see a better spot?? {w=0.2}Or anything at all??"
    "Less than a minute later and we're already back at it again."
    "This is going to be a long week..."
    window hide
    pause 2
    play music title
    show bg intro_pan_bg
    show intro_pan
    show intro_pan_banshee:
        xalign 1.0
    with longdissolve
    pause 2
    show splashtext "Good Tales Presents" at truecenter zorder 2 with meddissolve
    pause 3
    hide splashtext with longdissolve
    pause 1
    show title at truecenter zorder 2 with longdissolve
    pause 5
    hide title with longdissolve
    pause 2
    show intro_pan_banshee:
        linear 0.15 xalign 0.0
    pause 0.15
    stop ambience
    stop music
    scene bg black
    pause 3
    $renpy.music.set_volume(volume=0.1, delay=0, channel='ambience')
    $renpy.music.set_volume(volume=1.0, delay=0, channel="music")
    play ambience wind fadein 3
    scene bg bedroom
    show snowfall_window
    with longdissolve
    $renpy.notify(message="Bedroom")
    pause 1
    window show
    h "Alright, that should be the last of them."
    show wife base smile sad at middle with dissolve
    w "Whew. That's a relief."
    play music bedroom_normal
    "Now that all the hard work was done, [wife] took off her coat and plopped down onto the bed."
    $wifeTop = "sweater"
    with dissolve
    pause 0.5
    $wifeDesign["armNumber"] = "02"
    w "Wow...{w=0.5} Talk about comfy!"
    h "You think so?"
    w level "Come on. See for yourself."
    "She lightly tapped the other side of the bed."
    "Accepting her offer, I walked to the empty side and laid down."
    h "Oh, wow!"
    w sad "Told ya!"
    h "Man, I feel like I could sleep through the whole week on this thing!"
    w level blank "Don't get too ahead of yourself.{w=0.2}\nWe can take a quick break, but then we should at least get our stuff unpacked."
    h "Alright, if you insist."
    hide wife with dissolve
    pause 0.5
    "Looking around the room, it's honestly pretty cozy."
    "The most I've ever been used to are chain hotels, which, don't get me wrong, are definitely good at making you feel like a million bucks."
    "But something about having a fireplace in your room really makes you feel like a {i}billion{/i} bucks."
    "I still think my mother-in-law was crazy to get us these reservations as an anniversary present, as she's not exactly what you'd call wealthy."
    "But she insisted that we both needed time away from it all.{w=0.2}\nAnd I guess she wasn't really wrong..."
    $wifeDesign["armNumber"] = "01"
    show wife base level blank at middle with dissolve
    w "You know, I wonder if a week is going to be enough time to really enjoy ourselves."
    h "What do you mean?"
    w sad "A week is pretty fast, especially on a vacation.{w=0.2}\nIt could be over in an instant."
    h "Well, that's all the more reason we should enjoy it while we're here."
    w raised "That's easier said than done, [husband]."
    h "Not necessarily."
    show wife casual
    "I hopped the bed and offered her my hand."
    h "Come on.{w=0.2} Let's explore the place a bit."
    w level "[husband], I just said--"
    h "We can unpack when we get back."
    w raised "And when will that be?{w=0.2} After midnight when we're totally exhausted?"
    $renpy.music.set_volume(volume=0.75, delay=3, channel="music")
    h "Now why would you automatically assume that it'll be that late?"
    $renpy.music.set_volume(volume=0.5, delay=3, channel="music")
    w mad "Did you not notice how big this place is?"
    $renpy.music.set_volume(volume=0.25, delay=3, channel="music")
    h "It's not THAT big, [wife]!"
    stop music fadeout 3
    w "You still never know!{w=0.2} I'd rather we get organized sooner rather than later!"
    play music fighting fadein 3
    h "And I'd rather we enjoy our vacation a little bit!"
    $renpy.music.set_volume(volume=0.5, delay=3, channel="music")
    w "Well, if you wanna enjoy it at this very moment, then go ahead.{w=0.2} But I'm going to stay and unpack."
    $renpy.music.set_volume(volume=0.75, delay=3, channel="music")
    h "Oh, sure. So then you can bitch about how you had to do it all by yourself, right?"
    $renpy.music.set_volume(volume=1.0, delay=3, channel="music")
    w "Oh, here we go again! Always making yourself seem like a poor little victim!"
    h "I'm not making myself a victim, I'm just calling out how fucking predictable you are!"
    w "Oh, really?{w=0.2} Well, how's THIS for fucking predictable??"
    hide wife with easeoutright
    "She then got off the bed and went towards one of her suitcases."
    h "What are you--?"
    "She grabbed it and quickly moved it towards the dresser."
    "After yanking a drawer open so fast that I'm shocked it didn't come flying out, she yanked on the suitcase zipper to get it open."
    "Once it was, she held the suitcase upside-down over the drawer, allowing all the clothing inside to fall out."
    "About half of it made it into the drawer, with the rest of it falling nearby."
    h "[wife]!"
    "Ignoring me, she tossed the suitcase onto the bed and slammed her hip into the overflowing drawer."
    "After a few hits with no noticeable closure, she turned to me with her hands on her hips."
    $wifeDesign["armNumber"] = "02"
    show wife base mad blank at middle with dissolve
    w "There! I'm unpacked! So let's go!"
    h "[wife], that--"
    window hide
    hide wife with easeoutright
    stop music fadeout 3
    play sound door_slam
    pause 4
    window show
    "I leaned against the wall and took a deep breath."
    "After a few seconds, I took a look at the mess by the dresser drawer."
    "I'm sure she'll bitch about cleaning it up later, but that's her problem."
    "Honestly, this was my biggest worry about this vacation."
    "We could go to a new location for a week if we really wanted to, but that wasn't going to change anything."
    "The bickering, the arguing, the overreactions..."
    "A new environment isn't going to make that magically go away."
    "But I guess sitting here and worrying about that shouldn't be my priority right now."
    window hide
    pause 0.5
    play sound door_creak_short
    scene bg hallway with meddissolve
    $renpy.notify(message="Hallway")
    pause 0.5
    window show
    "I couldn't see her in the halls."
    "And I have no way of knowing which direction she went towards."
    "Lovely."
    $renpy.music.set_pan(pan=-0.5, delay=0, channel='sound')
    play sound cart
    "I then heard movement around the left corner."
    "I looked and saw a maid pushing a cleaning cart."
    h "Excuse me, Miss?"
    show maid at middle with dissolve
    m "Yes, Sir?"
    h "Would you happen to have seen a woman around my age in the halls just now?"

    python:
        if wifeDesign["hairNumber"] in wifeHairLengths["short"]:
            hairLengthWText = "short"
        elif wifeDesign["hairNumber"] in wifeHairLengths["long"]:
            hairLengthWText = "long"

        if hairColorW == hairColors[0]:
            hairColorWText = "blonde"
        elif hairColorW == hairColors[1]:
            hairColorWText = "brown"
        elif hairColorW == hairColors[2]:
            hairColorWText = "black"
        elif hairColorW == hairColors[3] or hairColorW == hairColors[5]:
            hairColorWText = "red"
        elif hairColorW == hairColors[4]:
            hairColorWText = "gray"
        elif hairColorW == hairColors[6]:
            hairColorWText = "blue"
        elif hairColorW == hairColors[7]:
            hairColorWText = "purple"
        elif hairColorW == hairColors[8]:
            hairColorWText = "pink"
        elif hairColorW == hairColors[9]:
            hairColorWText = "green"

    m "Oh, does this woman have [hairLengthWText] [hairColorWText] hair?"
    h "Yes, that's her."
    m "I just passed her as I came this way.{w=0.2}\nShe was heading towards the stairs."
    h "Alright.{w=0.2} Thank you."
    hide maid with dissolve
    "I then headed towards the stairs."
    scene bg stairs with meddissolve
    $renpy.notify(message="Stairs")
    "Thankfully, we were on the highest floor, so there was only direction she could've gone."

label game_end:
    $takeScreenshot()
    return