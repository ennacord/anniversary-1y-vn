# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#begin basic_layeredimage

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

#begin backgrounds
image urbancity = "backgrounds/medieval_path_day.jpg"
#17/05/22
image blackscreen = "backgrounds/black1.png"
image whitescreen = "backgrounds/white1.png"
image uknscreen = "backgrounds/unknown.png"

#end

define e = Character("Enna", color="#858ED1")
define m = Character("Millie", color="#FEBC87")
define ym = Character("Young Millie", color="#FEBC87")
define cm = Character("Calamillie", color="#fef187")
define r = Character("Reimu", color="#B90B4A")
define n = Character("Nina", color="#FF0000")
define l = Character("Lucie", color="#dcace3")
define el = Character("Elira", color="#95C8D8")
define ro = Character("Rosemi", color="#ff80aa")
define i = Character("Ike", color="#348EC7")
define v = Character("Vox", color="#960018")
define s = Character("Shu", color="#A660A7")
define ag = Character("Agent from Heaven", color="#ffffff")
define w = Character("Wanderer", color="#422e5a")
#17/05/22
define narrator = Character(None, kind=nvl,  color="#ffffff")
define na = Character(None, kind=nvl,  color="#ffffff", ctc="gui/3.png") #wings

# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene urbancity

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    show enna_r blinking at center
    with dissolve
    e "at the tail end of Millie's fight with Enna and friends. As Calamity Millie
    casts her world-ending spell, it seems as if the room had split in two.
    Millie escapes from her half, cackling as she takes flight,
    as the remaining members of Ethyria tend to their wounds."
    #17/05/22
    nvl show
    scene uknscreen
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    "When an unknown printer took a galley of type and scrambled it to make a type specimen book."
    na "."
    nvl clear
    "It has survived not only five centuries, but also the leap into electronic typesetting"
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
    na "."
    nvl clear
    # This ends the game.
    return
