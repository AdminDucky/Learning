###
import time





entries = {}

def open():
    for i, v in entries.items():
        print(f'{i}, {v}')

def specific():
    print('Please select the entry you wish to see')
    for key in entries.keys():
        print(f'{key}\n')
    
    uinput = input('> ')
    try:
        entries[uinput]
        menu()
    except:
        print('Invalid key')

def add():
    print('Please add the name of the person you wish to add')
    person = input('> ')
    print('Please enter their adress and telephone number, seperated by a comma, like this:\nCustom Street 17, +02341 21214')
    data = input('> ')
    global entries
    entries[person] = data

def menu():
    global a
    global uinput
    print("Hello! What would you like to do?")
    print("Open - See the entries\nSpecific - See a specific entry\nAdd - Add someone to the book")
    uinput = input('> ')
    print('')
    a = uinput.lower()

while True:
    menu()

    if a  == 'open':
        print('')
        time.sleep(1)
        open()

    elif a == 'specific':
        specific()

    elif a == 'add':
        add()
