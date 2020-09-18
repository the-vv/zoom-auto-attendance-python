import pyautogui
import sys
print('Zoom auto attendance Bot\nStarted...\nPress Ctrl + c to stop')
print('-------------------------')
while not pyautogui.locateOnScreen('images/chatbox.png'):
    print('Chatbox not found')
print('chatbox found')
positions = []
while 1:
    try:
        position = pyautogui.locateOnScreen('images/from.png')
        position = pyautogui.center(position)[1]
        if position:
            if position not in positions:
                positions.append(position)
                position = None
            print(len(positions), 'Attandances found')
            if len(positions) >= 3 :
                print('Attandance started, Entering attandence...')
                pyautogui.click('images/chat.png')
                pyautogui.write('B 45', interval=0.10)
                pyautogui.press('enter')
                x = input('Operation Success, press enter to exit')
                sys.exit()
        else:
            print('Waiting for annandance to start...')
    except pyautogui.ImageNotFoundException:
        print('NotFound')
    except KeyboardInterrupt:
        print('Exiting')
        sys.exit()

        