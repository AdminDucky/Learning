# Simple database, made by AdminDucky to allow learning python
# I did my best on this, please make sure to leave feedback & critique and how to improve on my github
# Please note im a beginner
# https://github.com/AdminDucky/Learning


# Variables

from ast import Return
import time

level0_unlock = True # Regulates if level0_unlock can be accessed or not
administrators = ["Administrator", "AdminDucky", "Mikey", "Choppovm"]
authed_users = [administrators, "Mile", "Jack", "Bob", "Andrew"]
password = "IAmABeginner"

password_1 = "AmazingJob!"
level1_unlock = False
password_2 = "DiscordBotCoding"
level2_unlock = False
password_3 = "CodingIsHard"
level3_unlock = False

admin_pass = "ThesePasswordsAreVerySecure"

class entry:
    def __init__(self, title, date, level, author, password, entry): 
        self.title = title
        self.date = date
        self.level = level
        self.author = author
        self.password = password
        self.entry = entry

def openlevel0_unlock():
    print("Open level0_unlock?")
    open = input("")
    if open.lower() == "yes":
        level0_unlock = True
        print("Success")

if level0_unlock == False:
    openlevel0_unlock()
# Entry 1, "The Beginning"
entry_1_story = """
Hello there, wanderer. 
This is a raw, boring level0_unlock created by a random person from germany, looking forward to learn coding in Python.
This database is nothing special you see, it isn't even a database. I just made it to practice coding and learn Python more.
As you might have guessed, this is programmed in Python. I have made some entries here for you to look around.
Some are password locked (again, to allow me learning). To get the first password, visit my GitHub:
https://github.com/AdminDucky/Learning
    
    Please also leave feedback there, but please explain me how to improve/what the better solution be. Please also note that I am still a 
    beginner in coding. 
    You will get to see more passwords as you progress through this. A little minigame, per say?

Oh and, once you enter a password correctly, all entries on that level will be unlocked and accessible without password entry until you close it or reset it.
Good luck,
with kind regards,
AdminDucky
"""
entry_1 = entry("The Beginning", "04/05/2022", 0, "AdminDucky", False, entry_1_story)

def print_1():
    print(f"""
    Entry 1 "{entry_1.title}" by {entry_1.author}
    made {entry_1.date}.
    ---------------------------------------------

    {entry_1.entry}

    ---------------------------------------------
    INFORMATION

    Level {entry_1.level}
    Password Required: {entry_1.password}
    Author: {entry_1.author}
    Made on {entry_1.date}
    """
    )
##########################################################################################
############################### Entry 2, "Secrets" #######################################
##########################################################################################

entry_2_story = f"""
Welcome back, wanderer.
I see you have managed to get the password. Thank you for checking out my GitHub! You may ask yourself why I am doing this.
Well, to be honest, I don't know either. I came back from school, and I felt like programming. Sadly, I am not on the level of understanding of how to code discord bots yet.
In all essence though, I have discovered my love of coding a few weeks ago. In school, we did some experimenting on a beginner IDE where you could code with blocks.
I really like it, and since Python was said to be beginner-friendly, I decided to start learning it.
I know you might be bored of these, but since you also wish to continue, the second password is "{password_2}".
You can open files classified as Class-2 files with it. You'll have to search a little, or a lot, depending on where you look to find password-3.

With regards,
AdminDucky
"""

entry_2 = entry("Secrets", "04/05/2022", 1, "AdminDucky", True, entry_2_story)

def print_2():
    print(f"""
    Entry 2 "{entry_2.title}" by {entry_2.author}
    made {entry_2.date}.
    ---------------------------------------------

    {entry_2.entry}

    ---------------------------------------------
    INFORMATION

    Level {entry_2.level}
    Password Required: {entry_2.password}
    Author: {entry_2.author}
    Made on {entry_2.date}
    """
    )
##########################################################################################
############################# Entry 3, "Disbelief" #######################################
##########################################################################################
print("Loading.")
time.sleep(3)

entry_3_story = """
Congratulations on finding the second password, wanderer. 

Over the course of days, I have asked some friends experienced in coding discord bots. Their recommendations had a wide range of what code or decorators to use.
So for now, I have given up discord programming and am now focusing on the basic Python fundamentals. I am currently learning how to use variables and functions, as well as classes to some extent.
This level0_unlock is actually written with classes, and I use a lot of variables. My parents like the idea of me learning to code, because of course, coding brings in money, and that's something they care about a lot.
Which I can understand, since they just want to make sure I live a good life with enough money to provide for me and my future family.

Thanks for reading,
with regards,
AdminDuckyie
"""

entry_3 = entry("Disbelief", "04/05/2022", 2, "AdminDucky", True, entry_3_story)

def print_3():
    print(f"""
    Entry 3 "{entry_3.title}" by {entry_3.author}
    made {entry_3.date}.
    ---------------------------------------------

    {entry_3.entry}

    ---------------------------------------------
    INFORMATION

    Level {entry_3.level}
    Password Required: {entry_3.password}
    Author: {entry_3.author}
    Made on {entry_3.date}
    """
    )
##########################################################################################
############################# Entry 4, "Struggles" #######################################
##########################################################################################

entry_4_story = f"""
Congratulations on finding the second password, wanderer. 

Since I have started coding, I have watched a lot of tutorials, read a lot of tutorials and also did some stuff myself. I did some projects, and once of them was an old-failed version of the level0_unlock.
The old level0_unlock, which I will refer to as "level0_unlock v1", is failed project of mine. I did it when I wasn't really familiar with the syntax.
This is my second try on it, a redux, and I'll just hope it works, as a lot of effort went into this. Based on the assumption that you have read Entry 3, I wish to add something.
In class, my teacher talked to me about what I wish to do after middle school. I said that I don't know, and he recommended me to go on a high school that has mechatronics as profile.
That means building things, and then coding it. Now I can understand that you wish to proceed, which you can do with the phrase "{password_3}", but please stay.
I know reading stories might be boring, and you want to reach the glorious end already, but please do read my other stories.
I have put a lot of effort into them.

With regards,
AdminDucky
"""

entry_4 = entry("Struggles", "04/05/2022", 2, "AdminDucky", True, entry_4_story)

def print_4():
    print(f"""
    Entry 4 "{entry_4.title}" by {entry_4.author}
    made {entry_4.date}.
    ---------------------------------------------

    {entry_4.entry}

    ---------------------------------------------
    INFORMATION

    Level {entry_4.level}
    Password Required: {entry_4.password}
    Author: {entry_4.author}
    Made on {entry_4.date}
    """
    )
##########################################################################################
############################# Entry 5, "Morse Code" #######################################
##########################################################################################
print("Loading..")
time.sleep(3)

entry_5_story = f"""
Hello again.

Yes, this really is my third story on the second level, but don't worry, there really is nothing much on Level-3. I really do not have a lot to tell here.
I have once remembered a video of some japansese girl singing morse code in a high voice, and I did some research.
Countless hours of searching, I thought I'll never find it, but just as I was about to stop, I did. And turns out it's on spotify aswell.
Here is it: https://open.spotify.com/track/390P65hsMn8Dt7HJcghT6J?si=05268bbde22d42e0

Coding is hard, and I noticed that, but luckily I can type fast. When I asked my friend some questions about why certain pieces won't work, he did give me asnswers. Great friend, really.
Some other people I've asked on the other hand just spammed be with "{password_3}".

Looking for the password for the third level? Well, sadly this entry does not contain it. Or does it?

"""

entry_5 = entry("Morse Code", "04/05/2022", 2, "AdminDucky", True, entry_5_story)

def print_5():
    print(f"""
    Entry 5 "{entry_5.title}" by {entry_5.author}
    made {entry_5.date}.
    ---------------------------------------------

    {entry_5.entry}

    ---------------------------------------------
    INFORMATION

    Level {entry_5.level}
    Password Required: {entry_5.password}
    Author: {entry_5.author}
    Made on {entry_5.date}
    """
    )
##########################################################################################
############################# Entry 6, "The End" #########################################
##########################################################################################

entry_6_story = f"""
Congrats, wanderer. You are at the end now.

You have read a lot to get here, probably. Talking about entry 5, I really like that song actually. It's beautiful, and reminds me of certain things in my life.
Looking at my code, writing this piece of text I am already on line 140. I am quite proud of myself, and I just hope it will work.

Now, as we are at the end, the level0_unlock will close. Please note down the passwords, if you want to access all of my stories at a later point.

Level 1 - {password_1}
Level 2 - {password_2}
Level 3 - {password_3}

And if you really want to master the level0_unlock, and govern whether its closed or not, here's the password for that:
"{password}".

Thank you for using & testing my level0_unlock
truly, thank you
AdminDucky
"""

entry_6 = entry("The End", "04/05/2022", 3, "AdminDucky", True, entry_6_story)

def print_6():
    print(f"""
    Entry 6 "{entry_6.title}" by {entry_6.author}
    made {entry_6.date}.
    ---------------------------------------------

    {entry_6.entry}

    ---------------------------------------------
    INFORMATION

    Level {entry_6.level}
    Password Required: {entry_6.password}
    Author: {entry_6.author}
    Made on {entry_6.date}
    """
    )
##########################################################################################
############################# Code #######################################################
##########################################################################################
print("Loading...")
time.sleep(3)

def unlock(level): # function to unlock levels

    alreadyTrue = "This level is already unlocked!"
    if level == "0":
        if level0_unlock == True:
            print(alreadyTrue)

        else:
            pinput = input("Enter password: ")
            if pinput == password:
                level0_unlock = True
                print("Success")

            else:
                print("Wrong password")

    elif level == "1":
        if level1_unlock == True:
            print(alreadyTrue)

        else:
            pinput = input("Enter password: ")
            if pinput == password_1:
                level1_unlock = True
                print("Success")

    elif level == "2":
        if level2_unlock == True:
            print(alreadyTrue)

        else:
            pinput = input("Enter password: ")
            if pinput == password_2:
                level2_unlock = True

    elif level == "3":
        if level3_unlock == True:
            print(alreadyTrue)

        else:
            pinput = input("Enter password: ")
            if pinput == password_3:
                level3_unlock = True

    else:
        print("Invalid level input")

    welcome()




entries = [
    f"Entry 1, \"{entry_1.title}\"",
    f"Entry 2, \"{entry_2.title}\"",
    f"Entry 3, \"{entry_3.title}\"",
    f"Entry 4, \"{entry_4.title}\"",
    f"Entry 5, \"{entry_5.title}\"",
    f"Entry 6, \"{entry_6.title}\""
]
print("Loading up successful")

while level0_unlock == True:
    
    def welcome():

        print("Welcome to the level0_unlock.")
        action = input("What would you like to do? To see options, type \"Options\". ")

        if action.lower() == "options": # shows options
            print(f"""
            Those are the option:

            level0_unlockClose - Closes the level0_unlock
            Open - Opens an entry
            EnterPassword - Enter an password
            """)

        elif action.lower() == "level0_unlockclose": # close level0_unlock option
            confirmation = input("Do you wish to continue? (Yes/No) ")

            if confirmation.lower() == "yes":
                password_input = input("Please enter password: ")

                if password_input == password:
                    level0_unlock = False
                    print("level0_unlock successfully closed. Closing application.")
                    time.sleep(5)
                    exit()

            else:
                print("Cancelled")

        elif action.lower() == "open": # opens a file
            print(f"""
            You can choose from the following files:
            ----------------------------------------
            [{entry_1.level}] {entries[0]} 1
            [{entry_2.level}] {entries[1]} 2
            [{entry_3.level}] {entries[2]} 3
            [{entry_4.level}] {entries[3]} 4
            [{entry_5.level}] {entries[4]} 5
            [{entry_6.level}] {entries[5]} 6
            ----------------------------------------
            Format as follows:
            [Level] Entry | ID
            meaning if you wish to open entry 5, you'd need to say "5" below. Make sure you have the password for the level.
            If the entry is Level 0, then you do not need a password.
            """)

            wish = input("What file do you wish to open? ")

            if wish == "1":
                print_1()
                welcome()

            elif wish == "2":
                print_2()
                welcome()

            elif wish == "3":
                print_3()
                welcome()
            
            elif wish == "4":
                print_4()
                welcome()

            elif wish == "5":
                print_5()
                welcome()

            elif wish == "6":
                print_6()
                welcome()
            
            else:
                print("Invalid ID")
                welcome()
                
        elif action.lower() == "enterpassword":
            print(f"""
            This is the password entry terminal. These are your current level unlocks:

            Level 0 - {level0_unlock}
            Level 1 - {level1_unlock}
            Level 2 - {level2_unlock}
            Level 3 - {level3_unlock}

            Please enter the digit of the corresponding level (e. g. '0' for Level 0) below.
            """)
            unlock(input(""))
    
    welcome()
