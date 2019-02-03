#
# Description:
#   Audible countdown for the Diablo 3 convention of elements (COE) ring
#
# @author:  theRealDeal
# @version: 1.0
#
# Usage:
#   start the script exactly when the desired elemental bonus damage becomes active
#
# Run:
#   python diablo3_coe_count_down.py
#
# Stop:
#   'ctrl-c' or end the process to stop the script
#
# Requirements: 
#   Python 2.7  (tested on 2.7.12)
#   <you may need to install pip>
#   pip install pypiwin32
#   pip install pyttsx
#
# Optional:
#   adjust user defined values below based on your preferences
#
# Text to Speech:
# https://pythonprogramminglanguage.com/text-to-speech/
#
# Register a hotkey in Windows:
# http://timgolden.me.uk/python/win32_how_do_i/catch_system_wide_hotkeys.html
# https://github.com/schurpf/pyhk
#
# Todo:
#   adjust volume
#   toggle mute
#   reset the elemental rotation
#   change voice
#

import time
t0= time.clock()

import pyttsx
engine = pyttsx.init()
engine.say('Hello.')
engine.runAndWait()
time.sleep(.5)
engine.say('May the luck be with you.')
engine.runAndWait()

print("Executing elements...")

##################################################################################################################
# User Defined Values
numElements = 4                 # the number of elemental rotations
elementalDuration = 4           # the number of seconds during each rotation
countDown = 3                   # starting number to count down from
notifyStart = True              # notify the start
notifyEnd = True                # state when the rotation ended
talkEarly = 0.1                 # enter the number of seconds that you want the countdown to start speaking early
##################################################################################################################

rotationLength = numElements * elementalDuration
state = countDown
rotationNumber = 0
sayStartRotationNum = 1
sayEndedRotationNum = 1

while (1):
    tCur = time.clock() + talkEarly
    elapsedTime = tCur - t0
    rotationTime = elapsedTime % rotationLength
    curRotation = int(elapsedTime / rotationLength)
    
    if curRotation == rotationNumber and rotationLength-rotationTime < state:
        engine.say( str(state) )
        engine.runAndWait()
        state = state - 1
        if state < 1:
            state = countDown
            rotationNumber = rotationNumber + 1
    
    if notifyStart and elapsedTime/rotationLength > sayStartRotationNum:
        engine.say('0')
        engine.runAndWait()
        sayStartRotationNum = sayStartRotationNum + 1
    
    if notifyEnd and curRotation == sayEndedRotationNum and (rotationTime > elementalDuration):
        engine.say('Ended.')
        engine.runAndWait()
        sayEndedRotationNum = sayEndedRotationNum + 1
        
    time.sleep(.05) # adding a delay so it doesn't busy loop
    
    
print("Script Ended")   # currently, this will never get executed.