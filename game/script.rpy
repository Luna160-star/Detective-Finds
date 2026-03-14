# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default progression_points = 0
    # choose character colours

define a = Character("Detective")
define b = Character("Cook")
define c = Character ("Husband")



image 1:
    "images/1.jpg"
    zoom 1

image 2:
    "images/2.jpg"
    zoom 1

image tove:
    "images/tove.jpg"
    zoom 1

image living:
    "images/living.jpg"
    zoom 1

image chef:
    "images/chef.png"
    zoom 1

image detective:
    "images/detective.png"
    zoom 1

image man:
    "images/man.png"
    zoom 1

label start:

    scene 1
    "Hi, Help me solve this case, I am a detective and I need your help!"


    
    scene 2
    "Oh, another case, I wonder what this is about"
    "It's already very late, I will work on this case tomorrow."
   
    show detective
    menu:
        "What should we do now?"
        "Yes, solve this case tomorrow":
            jump living

        "No, solve this case now":
            jump living
return
