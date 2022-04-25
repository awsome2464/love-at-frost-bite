label start:
    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene bg black
    hide screen custom_main_menu
    with longdissolve
    pause 2
    $renpy.music.set_volume(volume=0.5, delay=0, channel='ambience')
    play ambience wind loop fadein 3.0
    pause 4
    play sound footsteps_snow
    pause 5
    play sound door_creak_short
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
    "Man...{w=0.5} What a time that was."
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
    show wife base sad smile bikini_top bikini_bottom at middle with dissolve
    pause 1
    window show
    "...was my beautiful wife."
    window hide
label customize_wife:
    $renpy.block_rollback()
    show wife
    show screen change_wife
    pause

label wife_finished:
    hide screen change_wife
    show wife at left with easeinright
    window show
    "Are you satisfied with the wife's appearance?\nIt can not be changed later.{nw}"
    menu:
        "Are you satisfied with the wife's appearance?\nIt can not be changed later.{fast}"
        "I'm satisfied":
            jump satisfied
        "I'm not satisfied":
            window hide
            show wife at middle with easeinleft
            jump customize_wife

label satisfied:
    $renpy.block_rollback()
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
    show clerk at middle
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

label enter_husband_name:
    $husband = renpy.input("Enter the husband's name.", length=20, default=husband, allow=inputCharacters)
    $husband.strip()
    if not husband:
        "Come on, now; I have a name."
        jump enter_husband_name
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
    scene bg lobby with dissolve
    pause 1
    show wife base level blank coat_base coat_breasts coat_sleeves jeans at middle with dissolve
    w "Whew! It's freezing out there!"
    h "You can say that again.{w=0.5} Were you able to find a decent parking spot?"
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
    show splashtext "Good Tales Presents" at truecenter zorder 2 with meddissolve
    pause 3
    hide splashtext with longdissolve
    pause 1
    show title at truecenter zorder 2 with longdissolve
    show bg black with meddissolve
    pause 3
    stop ambience fadeout 3
    scene bg black with longdissolve
    pause 2
    $takeScreenshot()
    return