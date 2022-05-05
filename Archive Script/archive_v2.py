# https://github.com/AdminDucky/Learning
import time

user = input("Who are you? ")
active = True
level = 0 
L1 = "GitHub"
L2 = "Discord Robots"
L3 = "Coding Is Hard"

termination = 100 # If counter reaches this number, terminal will terminate
counter = 0 # Goes up +1 every time something is done

# Valid levels:
# Level-0 | Public, not password secured
# Level-1 | Standard, members only
# Level-2 | Authorised only (password)
# Level-3 | Administrators only

administrators = [
    "AdminDucky",
    "Mikey",
    "Choppovm"
]

members = [
    administrators,
    "Meaxis",
    "Janiqz",
    "Patata",
    "Meli"
]

class entry:
    def __init__(self, ID, title, author, level, content):
        
        self.ID = ID
        self.title = title
        self.author = author
        self.level = level
        self.content = content


entry1_content = """
Hello there, wanderer. 
This is a raw, archive created by a random person from germany, looking forward to learn coding in Python.
This database is nothing special you see, it isn't even a database. I just made it to practice coding and learn Python more.
As you might have guessed, this is programmed in Python. I have made some entries here for you to look around.
Some are password locked (again, to allow me learning). To get the first password, visit my \"{L1}\":
https://github.com/AdminDucky/Learning, or find out where I've hidden it within this text.
    
    Please also leave feedback there, but please explain me how to improve/what the better solution be. Please also note that I am still a 
    beginner in coding. 
    You will get to see more passwords as you progress through this. A little minigame, per say?

Oh and, once you enter a password correctly, all entries on that level will be unlocked and accessible without password entry until you close it or reset it.
Good luck,
with kind regards,
AdminDucky
"""

entry1 = entry(1, "The Beginning", "AdminDuckyie", 0, entry1_content) # Entry 1

def print_entry1(user, clearance):

    print(f"Loading Entry {entry1.ID}, \"{entry1.title}\"")
    print(f"""
        
        Greetings, {user}, Level-{clearance}.
        ------------------------------------------
        Loading
        Loading.
        Loading..
        Loading...
        ------------------------------------------

        Entry {entry1.ID} "{entry1.title}"
        ----
        {entry1.content}
        ----
        By {entry1.author}
    """)



entry2_content = f"""
Welcome back, wanderer.
I see you have managed to get the password. Thank you for checking out my GitHub! You may ask yourself why I am doing this.
Well, to be honest, I don't know either. I came back from school, and I felt like programming. Sadly, I am not on the level of understanding of how to code discord bots yet.
In all essence though, I have discovered my love of coding a few weeks ago. In school, we did some experimenting on a beginner IDE where you could code with blocks.
I really like it, and since Python was said to be beginner-friendly, I decided to start learning it.
I know you might be bored of these, but since you also wish to continue, the second password is "{L2}".
You can open files classified as Class-2 files with it. You'll have to search a little, or a lot, depending on where you look to find password-3.

With regards,
AdminDucky
"""

entry2 = entry(2, "Secrets", "AdminDuckyie", 1, entry2_content) # Entry 2

def print_entry2(user, clearance):

    print(f"Loading Entry {entry2.id}, \"{entry2.title}\"")
    print(f"""
        
        Greetings, {user}, Level-{clearance}.
        ------------------------------------------
        Loading
        Loading.
        Loading..
        Loading...
        ------------------------------------------

        Entry {entry2.ID} "{entry2.title}"
        ----
        {entry2.content}
        ----
        By {entry2.author}
    """)




entry3_content = """
Congratulations on finding the second password, wanderer. 

Over the course of days, I have asked some friends experienced in coding discord bots. Their recommendations had a wide range of what code or decorators to use.
So for now, I have given up discord programming and am now focusing on the basic Python fundamentals. I am currently learning how to use variables and functions, as well as classes to some extent.
This level0_unlock is actually written with classes, and I use a lot of variables. My parents like the idea of me learning to code, because of course, coding brings in money, and that's something they care about a lot.
Which I can understand, since they just want to make sure I live a good life with enough money to provide for me and my future family.

Thanks for reading,
with regards,
AdminDuckyie
"""

entry3 = entry(3, "Coding", "AdminDuckyie", 2, entry3_content) # Entry 3

def print_entry3(user, clearance):

    print(f"Loading Entry {entry3.ID}, \"{entry3.title}\"")
    print(f"""
        
        Greetings, {user}, Level-{clearance}.
        ------------------------------------------
        Loading
        Loading.
        Loading..
        Loading...
        ------------------------------------------

        Entry {entry3.ID} "{entry3.title}"
        ----
        {entry3.content}
        ----
        By {entry3.author}
    """)




entry4_content = f"""
Congratulations on finding the second password, wanderer. 

Since I have started coding, I have watched a lot of tutorials, read a lot of tutorials and also did some stuff myself. I did some projects, and once of them was an old-failed version of the archive.
The old archive, which I will refer to as "archive v1", is failed project of mine. I did it when I wasn't really familiar with the syntax.
This is my second try on it, a redux, and I'll just hope it works, as a lot of effort went into this. Based on the assumption that you have read Entry 3, I wish to add something.
In class, my teacher talked to me about what I wish to do after middle school. I said that I don't know, and he recommended me to go on a high school that has mechatronics as profile.
That means building things, and then coding it. Now I can understand that you wish to proceed, which you can do with the phrase "{L3}", but please stay.
I know reading stories might be boring, and you want to reach the glorious end already, but please do read my other stories.
I have put a lot of effort into them.

With regards,
AdminDucky
"""

entry4 = entry(4, "Struggles", "AdminDuckyie", 2, entry4_content) # Entry 4

def print_entry4(user, clearance):

    print(f"Loading Entry {entry4.ID}, \"{entry4.title}\"")
    print(f"""
        
        Greetings, {user}, Level-{clearance}.
        ------------------------------------------
        Loading
        Loading.
        Loading..
        Loading...
        ------------------------------------------

        Entry {entry4.ID} "{entry4.title}"
        ----
        {entry4.content}
        ----
        By {entry4.author}
    """)


entry5_content = """
Hello again.

Yes, this really is my third story on the second level, but don't worry, there really is nothing much on Level-3. I really do not have a lot to tell here.
I have once remembered a video of some japansese girl singing morse code in a high voice, and I did some research.
Countless hours of searching, I thought I'll never find it, but just as I was about to stop, I did. And turns out it's on spotify aswell.
Here is it: https://open.spotify.com/track/390P65hsMn8Dt7HJcghT6J?si=05268bbde22d42e0

Coding is hard, and I noticed that, but luckily I can type fast. When I asked my friend some questions about why certain pieces won't work, he did give me asnswers. Great friend, really.
Some other people I've asked on the other hand just spammed be with "{L3}".

Looking for the password for the third level? Well, sadly this entry does not contain it. Or does it?
"""

entry5 = entry(5, "Memories", "AdminDuckyie", 2, entry5_content) # Entry 5

def print_entry5(user, clearance):

    print(f"Loading Entry {entry5.ID}, \"{entry5.title}\"")
    print(f"""
        
        Greetings, {user}, Level-{clearance}.
        ------------------------------------------
        Loading
        Loading.
        Loading..
        Loading...
        ------------------------------------------

        Entry {entry5.ID} "{entry5.title}"
        ----
        {entry5.content}
        ----
        By {entry5.author}
    """)



entry6_content = f"""
Congrats, wanderer. You are at the end now.

You have read a lot to get here, probably. Talking about entry 5, I really like that song actually. It's beautiful, and reminds me of certain things in my life.
Looking at my code, writing this piece of text I am already on line 140. I am quite proud of myself, and I just hope it will work.

Now, as we are at the end, the archive will close. Please note down the passwords, if you want to access all of my stories at a later point.

Level 1 - {L1}
Level 2 - {L2}
Level 3 - {L3}

Thank you for using & testing my archive
truly, thank you
AdminDucky
"""

entry6 = entry(6, "Memories", "AdminDuckyie", 3, entry6_content) # Entry 6

def print_entry6(user, clearance):

    print(f"Loading Entry {entry6.ID}, \"{entry6.title}\"")
    print(f"""
        
        Greetings, {user}, Level-{clearance}.
        ------------------------------------------
        Loading
        Loading.
        Loading..
        Loading...
        ------------------------------------------

        Entry {entry6.ID} "{entry6.title}"
        ----
        {entry6.content}
        ----
        By {entry6.author}
    """)


##########################################################################################################
####################################   ___|  _ \  __ \  ____| ############################################
#################################### |     |   | |   | __|    ############################################
#################################### |     |   | |   | |      ############################################
#################################### \____|\___/ ____/ _____| ############################################
##########################################################################################################

def welcome():
    print("Please choose one of the following options:\n\nOpen - Open a file\nClose - Close the archive\nChange - Change your level\nReset - Sets your level to 0\nInformation - views information")
    global user_input
    user_input = input("")
    if user_input.lower() == "open":
        open()
    elif user_input.lower() == "close":
        close()

    elif user_input.lower() == "change":
        change()

    elif user_input.lower() == "information":
        info()

    else:
        print("Invalid keyword")

def change():
    print(f"""
    This is the clearance change pannel. Your current level is '{level}'. To change, please select the number of one of the levels below:

    Level 1 - Confidential
    Level 2 - Secret
    Level 3 - Wow okay
    
    To change to Level 0, type "reset" in the menu.
    To cancel, type 'cancel'.
    """)
    changeinput = input("")
    if changeinput.lower() == "cancel":
        print("Successfully cancelled")
    elif changeinput == "1":
        def changeto_l1():
            print("Commencing changing level to Level-1. Please enter password below.\nIf password is wrong, procedure will be cancelled.")
            changeinput = input("")
            if changeinput == L1:
                print("Correct password, changing level")
                level = 1
                if level == 1:
                    print("Changing level successful")
                else:
                    print("Something went wrong, terminal will terminate.")
                    exit()
        changeto_l1()

    elif changeinput == "2":
        def changeto_l2():
            print("Commencing changing level to Level-3. Please enter password below.\nIf password is wrong, procedure will be cancelled.")
            changeinput = input("")
            if changeinput == L2:
                print("Correct password, changing level")
                level = 2
                if level == 2:
                    print("Changing level successful")
                else:
                    print("Something went wrong, terminal will terminate.")
                    exit()
        changeto_l2()

    elif changeinput == "3":
        def changeto_l3():
            print("Commencing changing level to Level-3. Please enter password below.\nIf password is wrong, procedure will be cancelled.")
            changeinput = input("")
            if changeinput == L3:
                print("Correct password, changing level")
                level = 3
                if level == 3:
                    print("Changing level successful")
                else:
                    print("Something went wrong, terminal will terminate.")
                    exit()
        changeto_l3()

def reset():
    print("You are about to reset the archive. Your clearance level will be wiped. Type your username (case insensitive) below to confirm reset.")
    changeinput = input("Enter your username to confirm reset. ")
    print("Reset confirmed. Resetting terminal.")
    
    def reset_procedure():
        print("Reset confirmed. Resetting terminal.")
        print("Loading")
        time.sleep(1)
        print("Loading.")
        time.sleep(1)
        print("Loading..")
        time.sleep(3)
        print("Loading...")
        time.sleep(5)
        level = 0
    
    if changeinput == user:
        reset_procedure()
        if level == 0:
            print(f"Procedure successful. You are now at Level-{level}.")
            print("Redirecting to menu")
        
        else:
            print("Something went wrong with the reset procedure. The terminal will terminate itself.")
            time.sleep(5)
            exit()

    else:
        print("Wrong username, please run \"information\" in the menu to see your username.")
    
def close():
    print("Are you sure you wish to close the archive? Type yes to confirm.")
    user_inputc = input("")
    if user_inputc.lower() == "yes":
        exit()
    else:
        print("Cancelled.")

def open():
        print(f"""
        ----------------------------
        [ID] | Title | Clearance
        [{entry1.ID}] | {entry1.title} | {entry1.level}
        [{entry2.ID}] | {entry2.title} | {entry2.level}
        [{entry3.ID}] | {entry3.title} | {entry3.level}
        [{entry4.ID}] | {entry4.title} | {entry4.level}
        [{entry5.ID}] | {entry5.title} | {entry5.level}
        [{entry6.ID}] | {entry6.title} | {entry6.level}
        ----------------------------
        Respond with the ID of the file you wish to open.
        """)
        user_input = input("")

        if user_input == "1":
            if level >= entry1.level:
                print_entry1(user, level)
                
            else:
                print("Insufficient clearance")
                return
        
        if user_input == "2":
            if level >= entry2.level:
                print_entry2(user, level)
                return
            else:
                print("Insufficient clearance")
                return

        if user_input == "3":
            if level >= entry3.level:
                print_entry3(user, level)
                return
            else:
                print("Insufficient clearance")
                return

        if user_input == "4":
            if level >= entry4.level:
                print_entry4(user, level)
                return
            else:
                print("Insufficient clearance")
                return

        if user_input == "5":
            if level >= entry5.level:
                print_entry5(user, level)
                return
            else:
                print("Insufficient clearance")
                return

        if user_input == "6":
            if level >= entry6.level:
                print_entry6(user, level)
                return
            else:
                print("Insufficient clearance")
                return

def info():
    print("Loading information")
    time.sleep(2)
    print(f"""
    USER INFORMATION
    ----------------
    Level {level} user, {user}
    Action Counter: {counter}
    
    Archive terminating in {termination - counter} actions.
    ----------------
    """)

while True:
    welcome()
    if counter == termination:
        break
