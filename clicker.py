import pyautogui
import os
print('Zoom auto attendance Bot\nStarted...\nPress Ctrl + c to stop')
print('-------------------------')
while 1:
    try:
        if pyautogui.locateOnScreen('images/from.png'):
            print('Attandance started, Entering attandence...')
            pyautogui.click('images/chat.png')
            pyautogui.write('B 45', interval=0.10)
            pyautogui.press('enter')
            x = input('Operation Success, press enter to exit')
            os.exit()
        else:
            print('Checking for attandance...')
    except KeyboardInterrupt:
        print('Exiting')
        os.exit()

        