#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0):
    print("siahmed walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('siahmed takes the stairs')
        if (count > 0):
            print("but siahmed's not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room():
    print("This room is full of gold.  How much does siahmed take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, siahmed's not greedy, siahmed wins!")
        exit(0)
    else:
        dead("siahmed, you greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is siahmed going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or "honey":
            dead("The bear looks at siahmed then slaps siahmed's face off.")
        elif next == "taunt" and bear_moved:
            print("The bear has moved from the door. siahmed can go through it now.")
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews siahmed's leg off.")
        elif next == "open" or "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here siahmed sees the great evil Cthulhu.")
    print("He, it, whatever stares at siahmed and siahmed goes insane.")
    print("Does siahmed flee for her life or eat her head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("siahmed is in a dark room.")
    print("There is a door to siahmed's right and left.")
    print("Which one does siahmed take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("siahmed stumbles around the room until siahmed starves.")

if __name__ == '__main__':
    main()
