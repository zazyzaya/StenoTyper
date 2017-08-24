# Stenotyper
#   ____ ____ ____ ____ __ ____ ____ ____ ____ ____
#  /q S /w T /e P/ r H|t * |y F \u P \i L \o T \p D\
#  |   |____|____|____|    |____|____|____|____|____|
#  |   |    |    |    |    |    |    |    |    |    |
#  \a S\ s K\ d W\ f R|g * |h R /j B /k G /l S /; Z/
#   \___\____\____\___|____|___/____/____/____/___/
#               |    |    |    |    |
#               \c A |v O | b E| n U/
#                \___|____|____|___/
# 
# * Lowercase = qwerty 
#   Uppercase = Steno

from pynput import keyboard

keysDown = []
letterMapping = [ ('a','S'), ('q','S'), ('w','T'), ('s','K'), ('e', 'P'), ('d','W'), ('r','H'), ('f', 'R'),                             # Initial 
                  ('c', 'A'), ('v', 'O'), ('g','*'), ('t','*'), ('b', 'E'), ('n', 'U'),                                                 # Vowels
                  ('y', 'F'), ('h','R'), ('u', 'P'), ('j', 'B'), ('i', 'L'), ('k', 'G'), ('o', 'T'), ('l', 'S'), ('p', 'D'), (';', 'Z') # Final
                ]   

def addToPressedKeys(key):
    global keysDown
    try:
        letter = key.char
        if letter not in keysDown:
            keysDown.append(letter)
    
    except (AttributeError):
        return False

def printKeys(key):
    global keysDown
    try:
        key.char    # Test if input is a special char or not
    except (AttributeError):
        return False

    if keysDown == []:
        return True # Exit without doing anything

    strToPrint = ''
    for mappedKey in letterMapping:
        if mappedKey[0] in keysDown:
            strToPrint += mappedKey[1]
        else:
            strToPrint += ' '

    print(strToPrint)
    keysDown = []

print(''' ================================================================== 
/ Welcome to stenotyper! The worst way to take notes in the world! \\
\\                   To quit, hit escape                            / 
 ==================================================================

''')

with keyboard.Listener(on_release=printKeys, on_press=addToPressedKeys) as listener:
    listener.join()
