"""
Program: blankspace.py
Title: Blank Space
Author: Kara Jacobs
Date last modified: 05/08/2023

Description: A text-based adventure game set in outer space. An amnesiac wakes
up on an empty spaceship, and tries to figure out who they are, how they got there,
and more importantly, how to survive.
"""

# tkinter and necessary tkinter modules are imported
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import scrolledtext

# Styling for widgets
title_style = {"background": "black", "foreground":"#63C5DA", "font": "Consolas 20"} # Title page style
button_style = {"background": "#0492C2", "foreground":"white", "font": "Consolas 12"} # Buttons style
radio_style = {"background": "black", "foreground":"white", "font": "Consolas 12"} # Radiobuttons style
text_style = {"background": "black", "foreground":"#63C5DA", "font": "Consolas 12"} # Main text style
panel_style1 = {"background": "#311432", "foreground":"#00F0A8", "font": "Consolas 12"} # Style for new window
panel_style2 = {"background": "#7A4988", "foreground":"#00F0A8", "font": "Consolas 12"} # Style 2 for new window

# The root window is created, titled, and configured
root = Tk()
root.title("Blank Space")
root.geometry("800x800")
root.resizable(width=False, height=False)
root.configure(bg="black")

# Fonts are defined here
font1 = font.Font(family='Consolas', size='12') # Defines the main font style used in game 

# Game Images are loaded here. All of the images are banner header images for the story pages.
# (I didn't have time to figure out how to install PIL Pillow, so I just used tkinter's built-in 
#   PhotoImage tool. The file paths shown are how they appear on my computer, so the paths will 
#   have to be changed to wherever the Images folder path is stored on your PC.)
wakeup = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/wakeup.png")
spacepod = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/spacepod.png")
glowpanel = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/glowpanel.png")
arrows = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/arrows.png")
gameover = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/gameover.png")
doors = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/doors.png")
storeroom = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/storeroom.png")
mothbat = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/mothbat.png")
navroom = PhotoImage(file="C:/Users/Just Peachy/Desktop/Blank Space/Images/navroom.png")


# MULTIPLE LONG STORY STRINGS ARE STORED HERE
introstring = """You wake up in total darkness.

It feels like you are lying in a bed of 
chilled, semi-solid gel. This seems bizarre.

Experimentally, you try to sit up- but your head 
clunks into something hard- owch.

A low hum starts up, and suddenly- you are 
surrounded by a faint green glow. Huh. That's 
strange. It appears that your motion has activated 
something. Now that you can see, it also appears 
that you are in some sort of a metal and glass 
pod.

This all feels super weird, and you have NO idea 
how you got here. Actually, now that you think of 
it, you can't remember... anything. 

Not even your own name. 

You don't even know what you look like. 

You start panicking. 

Maybe this is all just a bad dream? Maybe if you 
go back to sleep, things will make more sense 
when you wake up?

Or maybe you should try getting out of this creepy 
coffin pod thing before you run out of air?
""" # << Scrollbox text for page2

path1 = """You close your eyes and try to fall 
asleep, but it takes a LONG time, because the
hum and the eerie green light is keeping you awake.

Eventually, finally, you drift, off, into, silent,
slumber...

When you wake up, you're still in the pod.
""" # << Scrollbox text for page3

path2 = """You push up against the glass of the pod. 
It opens easily, with a faint hiss sound as the 
pressurized seal pops open.

You climb out of the pod. All of your muscles feel 
weak and numb and tingly, and for a minute, you 
think you might collapse on the floor. But after a 
few deep breaths, the numb feeling dissipates, and 
you manage to steady yourself.

You look around yourself, trying to get a better 
view of the room you are in. It is pitch black in 
all directions. The green light from the pod is 
dim, and doesn't reach more than three feet away 
from it in any direction. This makes the pod look 
like it is the only thing that exists in the 
world, apart from you.

You blindly start walking with outstretched hands 
until you clunk into a curving wall. Your hands 
slide across the metal until you find what feels 
like buttons to a door. You press the buttons 
blindly. 

Suddenly, a dimly glowing purple panel pops out
of the wall.
""" # << Scrollbox text for page4

path3 = """You continue walking along the side of 
the curving wall, blindly searching for a door.

Suddenly, your hands feel something sharp- it's 
mangled, jagged metal. You have discovered a hole 
in the wall! It's just big enough for you to fit 
through, so you step through it, being careful not 
to cut yourself on the sharp edges.

You are now in an echoey corridor. The only reason 
you can tell it is a corridor is because there are 
two dim spots of light way back at the end of the 
corridor, casting an eerie glow.

You head towards the lights nervously, still 
unable to see your own feet.

As you get closer to the lights, you can make out 
the shapes- they are two glowing neon arrows on a 
wall, one arrow pointing left, and one arrow 
pointing right. The tunnel branches into two paths 
at this juncture. Which way do you go?
""" # << Scrollbox text for page5

path4 = """You keep walking until you come to three 
doors. Each of the doors has dimly glowing green
lighting strips outlining the edges. What secrets 
or answers could be hiding behind these doors? 
""" # << Scrollbox text for page7

path5 = """Inside Door 3, it is pitch back again.
You walk blindly for several feet, and then trip 
over something on the floor. The thing you tripped
over emits a low hum and lights up with a bright
sapphire glow- it's a Titanium KESTREL Model 9 
200 kilowatt Laser Gun!

You're stunned that you actually remember the 
exact make and model of this weapon, because you 
still can't remember ANYTHING else. Weird.

The glowing gun looks like it would make a good a 
flashlight, so you pick it up, and stand up. It 
appears that you are in a storeroom filled with 
chests and wall lockers. You try randomly opening
things, but most of the chests and lockers are 
either locked or empty.

After 15 minutes of looking, all you can find is 
a pair of broken goggles with numbers and symbols 
etched into the side of one lens, and 7 pistachio 
dragonfruit flavored ration bars.

You stuff the goggles and ration bars in your 
pockets, and step back out into corridor.

Now that you have your glow gun, you notice a 
fourth door that has no lighting strips around it. 
You try to press the open button, but the door 
stays closed.
""" # << Scrollbox text for page8

path6 = """You hold the broken goggles up to the 
door, not expecting much. Surprisingly, the door 
scans the numbers etched into the goggles, and 
then begins to glow tangerine orange. Then it 
slides open with a whirring creak.

You step into another corridor. It's dark at 
first like everything else on this ship, but 
suddenly you notice something sparkling overhead. 
It's stars! This corridor has a glass roof and 
walls, allowing you to see a fantastic view of 
outer space. The metal floor and narrow metal 
support arches along the corridor are the only 
visuals reminding you that you're still inside 
the spaceship.

The starry corridor seems to go on forever. 
Finally, you see the end of it! But suddenly, 
some of the metal floor plates in front of the 
door start shifting and clanking, and a feathery 
white creature emerges from below! It looks like 
a cross between a moth and a bat, its claws are as 
long and narrow as filet knives, and it's swooping 
right toward you!

You rapidly think up two options- you could FIGHT 
back with your laser gun, or you could throw the 
mothbat a ration bar to distract it, and then RUN!
""" # << Scrollbox text for page9


# TEXT FOR THREE POSSIBLE STORY ENDINGS ARE STORED HERE
end1 = """Oops, there was a large chunk of floor 
missing in that direction. You fall through the 
gap, plunging 700 ft until you hit cold metal.
""" # << Scrollbox text for page6

end2 = """You shoot the mothbat with all 200 
kilowatts of spectrum beam energy from your laser 
gun, but something... strange.. happens.

The mothbat turns blindingly iridescent as the ray
hits it. Somehow, it absorbed the laser energy and 
is completely uninjured! Its multicolored feathers 
are mesmerizingly beautiful and painfully bright 
to look at, and they're the last thing you'll ever 
see.

The mothbat sinks its claws into you, injecting 
you with poisonous, paralyzing venom. You hit the 
floor, and your vision goes black. 
""" # << Scrollbox text for page10

end3 = """You toss a pistachio dragonfruit ration 
bar at the mothbat. It curiously leans down to 
sniff the packaging. 

While the mothbat is distracted, you run wildly 
past it and escape through the door at the end of 
the corridor. You slam the button to shut the 
door, and, luckily, it slide shuts with no 
problem.

You use your laser gun as a flashlight again, and 
see that you are now in a room with a large sign 
on one wall saying ESCAPE PODS, and a wide cirular 
docking bay filled with metal pod harnesses. 
There's only one pod left. So that's why this 
spaceship is so empty! Everyone else must have 
abandoned ship and left you behind! 

Why were you left behind? Was it an accident? Did 
you have enemies? You're not sure, but right now, 
you don't even care. You're just excited that you 
found a way to escape this creepy ship!

You climb into the escape pod, and its 
motion-activated lights turn on. A glowing purple
viewscreen pops up, with green text asking:

"Allow autopilot? >> Y/N"
""" # << Scrollbox text for page11


# CODE FOR OPENING AND INTERACTING WITH A NEW WINDOW, WHICH IS CALLED ON PAGE 4
def new_window():
    """Opens a new window containing text entry widgets"""
    top = Toplevel() # A new window is created
    top.title("Strange Panel")

    #Frame for the panel to Enter Name and ID
    panel = LabelFrame(top, padx=120, pady=40, bg="#311432") 
    panel.pack()

    # Function to validate name input
    def lettersonly():
        """Validates name box user input to prevent entering no input or numbers, and 
        to prevent entering a name that is under 3 characters or over 40 characters.
        If input is valid, a greeting is shown."""
        namebox = name_entry.get()
        if len(namebox) == 0:
            answer1.config(text="This field cannot be empty!")
        else:
            try:
                if any(ch.isdigit() for ch in namebox):
                    answer1.config(text="Name cannot contain numbers!")
                elif len(namebox) <= 2:
                    answer1.config(text="Minimum of 3 characters required!")
                elif len(namebox) > 40:
                    answer1.config(text="Name is too long!")
                else:
                    answer1.config(text="Hello, \n" + namebox + "!\n Nice to meet you!")
            except Exception as ep:
                messagebox.showerror("error", ep)

    # Function to validate id number input
    def numbersonly():
        """Validates ID number box user input to prevent entering no input, decimals,
        symbols, or letters. If input is valid, a message is shown."""
        numbox = id_entry.get()
        try:
            int(id_entry.get())
            answer2.config(text="Your number: " + str(numbox) + " is not \nregistered in system databanks. \nYour clearance level is: 0.")
        except ValueError:
            answer2.config(text="Must enter a valid number! No decimals, \nsymbols, or letters are allowed.")

    # Label prompting user to enter their name
    name_label = Label(panel, panel_style1, text="Enter your name") 
    name_label.pack()

    # Entry box for user to enter their name
    name_entry = Entry(panel, panel_style2, width=45)
    name_entry.pack(pady=10)

    # Confirm button for name input. Calls the lettersonly() function for validation
    name_button = Button(panel, panel_style1, text="Confirm", command=lettersonly)
    name_button.pack(pady=5)

    # Text is displayed when user enters a valid or invalid name
    answer1 = Label(panel, panel_style1, text="", height=3)
    answer1.pack(pady=10)
    
    # This is just a blank space to visually separate the name entry id entry sections 
    blankspace = Label(panel, panel_style1, text="")
    blankspace.pack()

    # Label prompting user to enter their id number
    id_label = Label(panel, panel_style1, text="Enter your ID number: ")
    id_label.pack()

    # Entry box for user to enter their id number
    id_entry = Entry(panel, panel_style2)
    id_entry.pack(pady=10)

    # Confirm button for id number input. Calls the numbersonly() function for validation
    id_button = Button(panel, panel_style1, text="Confirm", command=numbersonly) 
    id_button.pack(pady=5)

    # Text is displayed when user enters a valid number or invalid input
    answer2 = Label(panel, panel_style1, text="", height=3)
    answer2.pack(pady=10)

    # Cancel button to exit the new windpw and return to the main game
    exit_top = Button(panel, panel_style1, text="Cancel", command=top.destroy)
    exit_top.pack(pady=30)


# CODE FOR STORY PAGE FRAMES IS STORED HERE
# Frames are created for holding game storyline pages
page1 = Frame(root, bg="black")
page2 = Frame(root, bg="black")
page3 = Frame(root, bg="black")
page4 = Frame(root, bg="black")
page5 = Frame(root, bg="black")
page6 = Frame(root, bg="black")
page7 = Frame(root, bg="black")
page8 = Frame(root, bg="black")
page9 = Frame(root, bg="black")
page10 = Frame(root, bg="black")
page11 = Frame(root, bg="black")
page12 = Frame(root, bg="black")

# Frames are arranged in a grid format so that they can be called with tkraise()
for frame in (page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12):
    frame.grid(row=0, column=0, sticky='news')

# A function to raise the correct frame
def raise_frame(frame):
    """Takes the user to a specified page"""
    frame.tkraise()

# First page is raised
raise_frame(page1)


# CODE TO SET RADIOBUTTONS
# The Radiobuttons on each page are all initially set at value 1
vary = IntVar() # Radiobutton variable for page 2
vary.set(1)

vary2 = IntVar() # Radiobutton variable for page 2
vary2.set(1)

vary3 = IntVar() # Radiobutton variable for page 3
vary3.set(1)

vary4 = IntVar() # Radiobutton variable for page 4
vary4.set(1)

vary5 = IntVar() # Radiobutton variable for page 7
vary5.set(1)

vary6 = IntVar() # Radiobutton variable for page 8
vary6.set(1)

vary7 = IntVar() # Radiobutton variable for page 9
vary7.set(1)


# FUNCTIONS FOR WHEN RADIOBUTTONS ARE SELECTED ARE STORED HERE
# A function to select possible story options
def continue_quest():
    """If radiobutton 1 is selected, page3 is shown.
    If radiobutton 2 is selected, page4 is shown."""
    if vary.get() == 1:
        raise_frame(page3)
    elif vary.get() == 2:
        raise_frame(page4)

def continue_quest2():
    """If radiobutton 1 is selected, a new message is shown in the scrolling textbox.
    If radiobutton 2 is selected, page4 is shown."""
    if vary2.get() == 1:
        text_area.delete("1.0", END)
        text_area.insert("1.0", "You try to fall asleep again, but it doesn't work. You're wide awake now.")
    elif vary2.get() == 2:
        raise_frame(page4)

def continue_quest3():
    """If radiobutton 1 is selected, a new window pops up asking for user input.
    If radiobutton 2 is selected, page5 is shown."""
    if vary3.get() == 1:
        new_window()
    elif vary3.get() == 2:
        raise_frame(page5)

def continue_quest4():
    """If radiobutton 1 is selected, page6 is shown.
    If radiobutton 2 is selected, page7 is shown."""
    if vary4.get() == 1:
        raise_frame(page6)
    elif vary4.get() == 2:
        raise_frame(page7)

def continue_quest5():
    """If radiobutton 1 or 2 is selected, a new message is shown in the scrolling textbox.
    If radiobutton 3 is selected, page 8 is shown."""
    if vary5.get() == 1 or vary5.get() == 2:
        text_area3.delete("1.0", END)
        text_area3.insert("1.0", "That door is locked.")
    elif vary5.get() == 3:
        raise_frame(page8)

def continue_quest6():
    """If radiobutton 1 or 2 is selected, a new message is shown in the scrolling textbox.
    If radiobutton 3 is selected, page 9 is shown."""
    if vary6.get() == 1:
        text_area4.delete("1.0", END)
        text_area4.insert("1.0", "Yikes, bad idea. The laser blast richochets off the door and walls crazily and nearly incinerates you.")
    elif vary6.get() == 2:
        text_area4.delete("1.0", END)
        text_area4.insert("1.0", "Hmm, all that accomplished was getting crumbs on the door.")
    elif vary6.get() == 3:
        raise_frame(page9)

def continue_quest7():
    """If radiobutton 1 is selected, page10 is shown.
    If radiobutton 2 is selected, page11 is shown."""
    if vary7.get() == 1:
        raise_frame(page10)
    elif vary7.get() == 2:
        raise_frame(page11)



#####################################################################
# MAIN GAME STORYLINE
# CODE FOR THE WIDGETS IN EACH FRAME IS SHOWN HERE
# THE PAGES ARE SPACED OUT WITH 3 SPACES BETWEEN EACH FOR READABILITY
#####################################################################
"""
PAGE 1 (TITLE PAGE)
This is the first page the user sees, with buttons to enter the game or exit it.
"""
# Title label for the Title Page
title_label = Label(page1, title_style, text="Blank Space \n A text-based adventure game by Kara Jacobs \n circa 2023", padx=70, pady=280)
title_label.grid(column=0, row=1, columnspan=3, rowspan=1)

# Start Game button. Uses a lambda command to bring the user to page2
start_button = Button(page1, button_style, text="Start Game >>", command=lambda: raise_frame(page2))
start_button.grid(column=1, row=2, pady=10)

# Exit Button for closing the program
exit_button = Button(page1, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=1, row=3)



"""
PAGE 2 (WAKE UP - SLEEP or EXIT POD)
The main widget layout is introduced that will be repeated in the rest of the pages.
"""
# Header image
wakeup_image = Label(page2, image=wakeup, text="A green glass hatch to a sci-fi stasis pod.")
wakeup_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)
                                                               
# Scrolling story text
text_area = scrolledtext.ScrolledText(page2, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area.grid(column=1, row=1, padx=5, pady=10)
text_area.insert("1.0", introstring)

# Radiobutton for Choice 1
choice1 = Radiobutton(page2, radio_style,text="Go back to sleep...", selectcolor="#016064", variable=vary, value=1)
choice1.grid(column=1, row=2, pady=10)

# Radiobutton for Choice 1
choice2 = Radiobutton(page2, radio_style, text="Try to push open the hatch to the pod.", selectcolor="#016064", variable=vary, value=2)
choice2.grid(column=1, row=3)

# Continue button selects the next page depending on which radiobutton is selected. Calls the continuequest() function.
continue_button = Button(page2, button_style, text="Continue >>", command=lambda: continue_quest())
continue_button.grid(column=2, row=4, padx=15, pady=20)

# Button for closing program
exit_button = Button(page2, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=4, padx=20, pady=20)



"""
PAGE 3 (SLEEP AGAIN or EXIT POD)
This page frame includes the same types of widgets as page2, arranged in the same 
way, so I didn't bother commenting each part. The main difference is that the 
Continue button calls continue_quest2() instead of continue_quest().
"""
spacepod_image = Label(page3, image=spacepod, text="A farther out side view of the stasis pod.")
spacepod_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area = scrolledtext.ScrolledText(page3, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area.grid(column=1, row=1, padx=5, pady=10)
text_area.insert("1.0", path1)

choice1 = Radiobutton(page3, radio_style, text="Try sleeping again...", selectcolor="#016064", variable=vary2, value=1)
choice1.grid(column=1, row=2, pady=10)

choice2 = Radiobutton(page3, radio_style, text="Try to push open the hatch to the pod.", selectcolor="#016064", variable=vary2, value=2)
choice2.grid(column=1, row=3)

continue_button = Button(page3, button_style, text="Continue >>", command=lambda: continue_quest2())
continue_button.grid(column=2, row=4, padx=15, pady=20)

exit_button = Button(page3, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=4, padx=20, pady=20)



"""
PAGE 4 (WALL - INTERACT WITH PANEL or SEARCH FOR EXIT)
This page also has the same widget structure as page1 and page2, except this time 
the Continue button calls continue_quest3(). Also, the Radiobutton choice1 calls 
a new window when Continue is pressed.
"""
glowpanel_image = Label(page4, image=glowpanel, text="A glowing purple viewscreen panel with static.")
glowpanel_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area2 = scrolledtext.ScrolledText(page4, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area2.grid(column=1, row=1, padx=5, pady=10)
text_area2.insert("1.0", path2)

choice1 = Radiobutton(page4, radio_style, text="Interact with panel.", selectcolor="#016064", variable=vary3, value=1)
choice1.grid(column=1, row=2, pady=10)

choice2 = Radiobutton(page4, radio_style, text="Keep searching for an exit.", selectcolor="#016064", variable=vary3, value=2)
choice2.grid(column=1, row=3)

continue_button = Button(page4, button_style, text="Continue >>", command=lambda: continue_quest3())
continue_button.grid(column=2, row=4, padx=15, pady=20)

exit_button = Button(page4, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=4, padx=20, pady=20)



"""
PAGE 5 (CORRIDOR - GO LEFT or GO RIGHT)
Same widget structure as previous page.
"""
arrows_image = Label(page5, image=arrows, text="Two purple neon arrows on a wall pointing left and right.")
arrows_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area2 = scrolledtext.ScrolledText(page5, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area2.grid(column=1, row=1, padx=5, pady=10)
text_area2.insert("1.0", path3)

choice1 = Radiobutton(page5, radio_style, text="Go Left.", selectcolor="#016064", variable=vary4, value=1)
choice1.grid(column=1, row=2, pady=10)

choice2 = Radiobutton(page5, radio_style, text="Go right.", selectcolor="#016064", variable=vary4, value=2)
choice2.grid(column=1, row=3)

continue_button = Button(page5, button_style, text="Continue >>", command=lambda: continue_quest4())
continue_button.grid(column=2, row=4, padx=15, pady=20)

exit_button = Button(page5, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=4, padx=20, pady=20)



"""
PAGE 6 (GAME OVER - FALL ENDING)
The radiobuttons and Continue button vanish, and a Restart Game button is added. 
"""
gameover_image = Label(page6, image=gameover, text="The words GAME OVER against a starry background.")
gameover_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area2 = scrolledtext.ScrolledText(page6, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area2.grid(column=1, row=1, padx=5, pady=10)
text_area2.insert("1.0", end1)

restart_button = Button(page6, button_style, text = "Restart Game?", command = lambda: raise_frame(page1))
restart_button.grid(column=1, row=3, pady=10)

exit_button = Button(page6, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=1, row=4)



"""
PAGE 7 (LOCKED DOORS)
Same standard page tructure, except with 3 Radiobutton options.
Option 3 takes you to the next page.
"""
doors_image = Label(page7, image=doors, text="Three metal doors, each one is outlined with a green glow.")
doors_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area3 = scrolledtext.ScrolledText(page7, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area3.grid(column=1, row=1, padx=5, pady=10)
text_area3.insert("1.0", path4)

choice1 = Radiobutton(page7, radio_style, text="Try opening Door 1", selectcolor="#016064", variable=vary5, value=1)
choice1.grid(column=1, row=2)

choice2 = Radiobutton(page7, radio_style, text="Try opening Door 2", selectcolor="#016064", variable=vary5, value=2)
choice2.grid(column=1, row=3)

choice3 = Radiobutton(page7, radio_style, text="Try opening Door 3", selectcolor="#016064", variable=vary5, value=3)
choice3.grid(column=1, row=4)

continue_button = Button(page7, button_style, text="Continue >>", command=lambda: continue_quest5())
continue_button.grid(column=2, row=5, padx=15, pady=10)

exit_button = Button(page7, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=5, padx=20, pady=10)



"""
PAGE 8 (STORAGE ROOM - SHOOT LOCK or RATION BARS or BROKEN GADGET)
Same widget structure as page7, also with 3 Radiobuttons.
"""
storeroom_image = Label(page8, image=storeroom, text="Closeup of a blue glowing sci-fi laser gun.")
storeroom_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area4 = scrolledtext.ScrolledText(page8, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area4.grid(column=1, row=1, padx=5, pady=10)
text_area4.insert("1.0", path5)

choice1 = Radiobutton(page8, radio_style, text="Try laser gun.", selectcolor="#016064", variable=vary6, value=1)
choice1.grid(column=1, row=2)

choice2 = Radiobutton(page8, radio_style, text="Try pistachio dragonfruit ration bar.", selectcolor="#016064", variable=vary6, value=2)
choice2.grid(column=1, row=3)

choice3 = Radiobutton(page8, radio_style, text="Try broken goggles.", selectcolor="#016064", variable=vary6, value=3)
choice3.grid(column=1, row=4)

continue_button = Button(page8, button_style, text="Continue >>", command=lambda: continue_quest6())
continue_button.grid(column=2, row=5, padx=15, pady=10)

exit_button = Button(page8, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=5, padx=20, pady=10)



"""
PAGE 9 (STARRY CORRIDOR - FIGHT ALIEN or RUN)
Same basic widget structure.
"""
starry_image = Label(page9, image=mothbat, text="A starry hallway with a moth-bat creature in it.")
starry_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area2 = scrolledtext.ScrolledText(page9, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area2.grid(column=1, row=1, padx=5, pady=10)
text_area2.insert("1.0", path6)

choice1 = Radiobutton(page9, radio_style, text="FIGHT!", selectcolor="#016064", variable=vary7, value=1)
choice1.grid(column=1, row=2, pady=10)

choice2 = Radiobutton(page9, radio_style, text="RUN!", selectcolor="#016064", variable=vary7, value=2)
choice2.grid(column=1, row=3)

continue_button = Button(page9, button_style, text="Continue >>", command=lambda: continue_quest7())
continue_button.grid(column=2, row=4, padx=15, pady=20)

exit_button = Button(page9, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=4, padx=20, pady=20)



"""
PAGE 10 (GAME OVER - MOTHBAT ENDING)
Same structure as the page6 Game Over.
"""
gameover_image = Label(page10, image=gameover, text="The words GAME OVER against a starry background.")
gameover_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area2 = scrolledtext.ScrolledText(page10, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area2.grid(column=1, row=1, padx=5, pady=10)
text_area2.insert("1.0", end2)

restart_button = Button(page10, button_style, text = "Restart Game?", command = lambda: raise_frame(page1))
restart_button.grid(column=1, row=3, pady=10)

exit_button = Button(page10, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=1, row=4)



"""
PAGE 11 (ESCAPE POD ROOM - ESCAPE SHIP)
Same basic widget structure, except only one radiobutton option is shown.
"""
navroom_image = Label(page11, image=navroom, text="A circular spaceship docking bay with a single escape pod.")
navroom_image.grid(column=0, row=0, columnspan=3, rowspan=1, padx=15, pady=20)

text_area2 = scrolledtext.ScrolledText(page11, fg="#63C5DA", bg="black", font=font1, 
        wrap = WORD, width = 50, height = 18, padx=20, pady=20)
text_area2.grid(column=1, row=1, padx=5, pady=10)
text_area2.insert("1.0", end3)

choice1 = Radiobutton(page11, radio_style, text="Allow autopilot, and escape the ship!", selectcolor="#016064")
choice1.grid(column=1, row=2, pady=10)

continue_button = Button(page11, button_style, text="Continue >>", command=lambda: raise_frame(page12))
continue_button.grid(column=2, row=4, padx=15, pady=20)

exit_button = Button(page11, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=0, row=4, padx=20, pady=20)



"""
PAGE 12 (YOU WIN!)
Finale page, includes a label saying You Win, a Restart Game Button, and an exit button.
"""
win_label = Label(page12, title_style, text="You Win!!!")
win_label.grid(column=0, row=0, columnspan=3, rowspan=1, padx=330, pady=300)

restart_button = Button(page12, button_style, text = "Restart Game?", command = lambda: raise_frame(page1))
restart_button.grid(column=1, row=3, pady=10)

exit_button = Button(page12, button_style, text = "Exit Game", command = root.destroy)
exit_button.grid(column=1, row=4)



root.mainloop()