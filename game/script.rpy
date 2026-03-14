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

        "No, solve this case now":
            jump living

label living:
    "The next day I woke up and went to the apartment of the victim."
    "I found that there were 2 suspects, the cook and the husband."

    show chef
    show man
    menu: 
        "Who should we interrogate first?":
        "The cook":
            jump cook
        "The husband":
            jump man


label cook:
    show cook

    menu: 
        "What should we ask the cook?":
            "Where were you last night?"
                "I was at home, I was cooking dinner for sir and mam."

            "Did you have any arguments with the victime?":
                "No, I have been working for them for more thn 5 years, we had no problems at all."
    return

label man:
    show man

    menu:
        "What should we ask the husband?":
            "Where were you last night?"
                "I was at my office"
return
