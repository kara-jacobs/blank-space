"""
Program: blankspace.py
Title: Blank Space
Author: Kara Jacobs
Date last modified: 04/28/2023

Description: A text-based adventure game set in outer space. An amnesiac wakes
upon an empty spaceship, and tries to figure out who they are, how they got there,
and more importantly, how to survive.

Variables:
    
"""

from tkinter import *
root = Tk()
root.title(“Blank Space”)

#time and random are imported for future use
import time
import random

#Title page
title_page = Label(root, text="Blank Space: A text-based adventure game by Kara Jacobs, circa 2023”

#The introduction module
def intro():	
    String = """You wake up in total darkness.

    It feels like you are lying in a bed of chilled, semi-solid gel. This seems bizarre.

    Experimentally, you try to sit up- but your head clunks into something hard- owch.

    A low hum starts up, and suddenly- you are surrounded by a faint green glow. Huh.
    That’s strange. It appears that your motion has activated something. Now that you
    can see, it also appears that you are in some sort of a metal and glass pod.

    This all feels super weird, and you have NO idea how you got here. Actually, now
    that you think of it, you can’t remember… anything. Not even your own name. You
    don’t even know what you look like. You start panicking. 

    Maybe this is all just a bad dream? Maybe if you go back to sleep, things will make
    more sense when you wake up?

    Or maybe you should try getting out of this creepy coffin pod thing before you run
    out of air?"""

#This creates a small delay before each line of the intro is printed, for dramatic effect
    for line in string.splitlines():
        print(line)
        time.sleep(0.5)
    return


#Radio buttons for user choices
choice1 = Radiobutton(root, text="Go back to sleep...", fg="white", bg="black", command = option1)
choice2 = Radiobutton(root, text = "Try to push open the hatch to the pod.", fg="white", bg ="black", command = option 1)

#Continue button which the user can only select after choosing a story path option.  
continue = Button(root, text="Continue")


#A while loop to cycle through possible story options will be created here
def options1():
	while 

 option1 =
    """You close your eyes and try to fall asleep, but it takes a LONG time, because the
    hum and the eerie green light is keeping you awake.

    Eventually, finally, you drift, off, into, silent, slumber…

    When you wake up, you’re still in the pod."""

option2 =
    """You push up against the glass of the pod. It opens easily, with a faint hiss sound as
    the pressurized seal pops open.

    You climb out of the pod. All of your muscles feel weak and numb and tingly, and for a
    minute, you think you might collapse on the floor. But after a few deep breaths, the
    numb feeling dissipates, and you manage to steady yourself.

    You look around yourself, trying to get a better view of the room you are in. It is pitch
    black in all directions. The green light from the pod is dim, and doesn’t reach more than
    three feet away from it in any direction. This makes the pod look like it is the only thing
    that exists in the world, apart from you."""

root.mainloop()
