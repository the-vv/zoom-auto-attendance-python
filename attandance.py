import sys

try:
    import pyautogui
except ModuleNotFoundError:
    print('Unable to start, Pls install pyautogui module, then restart')
    input('press enter to exit')
    sys.exit()
number = pyautogui.prompt(text='Enter your mesage to send',
                          title='Enter your message', default='')
if not number:
    if pyautogui.confirm(text='Number not enetered', title='What do you want to do?', buttons=['Continue', 'Exit']) != 'Continue':
        print('Exiting')
        sys.exit()
print('Zoom auto attendance Bot\nStarted...\nPress Ctrl + c to stop')
print('Your Number: ', number)
print('-------------------------')
try:
    printed = False
    while not pyautogui.locateOnScreen('./images/chatbox.png'):
        if not printed:
            printed = True
            print('Chatbox not found...\n Searching for chatbox')
    print('chatbox found')
    positions = []
    printed = False
    prevCount = 0
    while 1:
        position = pyautogui.locateAllOnScreen('images/from.png')
        for pos in position:
            if pos.top not in positions:
                positions.append(pos.top)
        if positions:
            if len(positions) != prevCount:
                prevCount = len(positions)
                print(len(positions), 'Attandances found')
            if len(positions) >= 5:
                print('Attandance started, Entering attandence...')
                try:
                    pyautogui.click('./images/chat.png')
                except TypeError:
                    print('Error! finding message box!!!')
                    continue
                pyautogui.write(number, interval=0.10)
                pyautogui.press('enter')
                input('Operation Success, press enter to exit')
                sys.exit()
        elif not printed:
            printed = True
            print('Waiting for annandance to start...')
except pyautogui.ImageNotFoundException:
    print('Not Found on screen')
except KeyboardInterrupt:
    print('Exiting')
    sys.exit()
