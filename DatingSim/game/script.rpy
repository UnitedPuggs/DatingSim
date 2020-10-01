#Characters
#Roomie
define d = Character("Donnie", color="#ffffff")
#The weeaboo, Fatboy
define n = Character("Fatboy", color="#FFF000")
#Your childhood friend
define f = Character("Vanilla", color="#f3e5ab")
# The game starts here.

label start:
    scene saddleback
    "You arrive to your first day of college as an anthropology student of Saddleback College, an all boys prestigious university! You feel hope and excitement as you starting turning the page onto a new chapter of your life"
    "You head to your dorm excitedly to meet your new roommate and catch up with your childhood friend, Vanilla, who is also going to Saddleback!"

    show chernobyl with dissolve
    "\"Wow!\", you think, as this is where you'll be spending the next year of your life!"
    "You hear a knocking at the door and are surprised to see your new roommate"

    show donny with zoomin
    "???" "Hey there, you must be my new roommate."
    python:
        playerName = renpy.input("I'm Donnie, what's your name?")
        playerName = playerName.strip() or "Retard"
    #The main character
    define mc = Character("[playerName]", color="#FF0000")
    d "Wow, [playerName] is such a pretty name"

    "You hear another knock at the door and smile as you see Vanilla there waiting for you"
    show donny with moveoutright:
        xalign 0.75
        yalign 1.0
    show vanilla with zoomin:
        xalign 0.25
        yalign 1.0

    f "Hey [playerName]!! I'm so happy to see you!!! Let's meet up with a friend of mine who can give us a tour!!!!"
    "You quickly bid Donnie farewell as you're equally as quickly dragged out the door by Vanilla"
    hide vanilla
    show totallyahall with dissolve
    "You and Vanilla walk into the hall and you just take in everything with awe."

    show vanilla
    f "This place is great, I'm so excited that we both got accepted here and are going to spend the next four years together!"
    mc "Yeah! You have no idea how ready I am to tackle all those super cool anthropology courses and meet some cool dudes!"

menu:
    "Go to admissions and drop":
        jump admissions
    "Continue":
        jump cont
label admissions:
    "You dropped out!"
    return

label cont:
    "penis music"
    return
