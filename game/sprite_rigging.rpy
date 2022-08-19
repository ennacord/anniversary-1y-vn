# TODO: refactor and systematize character sprites

# TODO: Curry this
init python:
    def WhenEnnaSpeaking(*args, **kwargs):
        return WhenSpeaking("enna", *args, **kwargs)

layeredimage enna:
    always:
        "sprites/Enna1/EnnaPlaceholder.png"

    group eyes auto:
        attribute open default:
            "sprites/Enna1/Enna_Eyes_Open.png"
        attribute blinking:
            "enna_eyes_blinking"

    group mouth auto:
        attribute smile1 default:
            WhenEnnaSpeaking("enna_mouth_talking", 0.05, 
                             "sprites/Enna1/Enna_Mouth_Open.png", 1)
        attribute smile2:
            WhenEnnaSpeaking("enna_mouth_talking", 0.05, 
                             "sprites/Enna1/Enna_Mouth_Closed.png", 1)

image enna_eyes_blinking:
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

image enna_mouth_talking:
    "sprites/Enna1/Enna_Mouth_Open.png"
    0.2
    "sprites/Enna1/Enna_Mouth_Closed.png"
    0.2
    repeat

image enna_r = LayeredImageProxy("enna", Transform(zoom=0.3, xoffset=0))
#end basic_layeredimage
