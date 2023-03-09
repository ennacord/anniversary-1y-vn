# The script of the game goes in this file.

# TODO: refactor and systematize character sprites
layeredimage enna:
    always:
        "sprites/Enna1/EnnaPlaceholder.png"
    group eyes auto:
        attribute open default:
            "sprites/Enna1/Enna_Eyes_Open.png"
        attribute blinking:
            "blinking"

image blinking:

    "sprites/Enna1/Enna_Eyes_Open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "sprites/Enna1/Enna_Eyes_Closed.png"
    .1
    repeat
image enna_r = LayeredImageProxy("enna", Transform(zoom=0.3, xoffset=0))
#end basic_layeredimage

label start:
    call ch1_part1 from _start_enter_ch1
    #menu:
    #    "Choose a demo"
    #    "Initial demo":
    #        call initial_demo from _call_initial_demo
    #"end of demo"

    return
