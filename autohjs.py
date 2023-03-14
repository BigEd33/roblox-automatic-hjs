# Automatic Hell Jacks thing
# Move mouse to top left corner to force pyautogui to crash.

# During waiting period, click on the Roblox chatbox and let it run.
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


from num2words import num2words
from pywinauto.keyboard import send_keys
import pyautogui
from time import sleep

numbers = []
word_numbers = []

while True:
    try:
        number = int(input("Enter target number: "))
    except:
        print("That is not a valid digit, try again.")
        continue
    else:
        break


for i in range(number):
    if i == 0:
        continue
    numbers.append(i)

numbers.append(number)

for i in numbers:
    word_numbers.append(num2words(i))

print("Waiting for 5 seconds, click on an input box and don't move your mouse.")
sleep(5)

for i in word_numbers:
    chars = list(i)
    print(chars)
    for j in chars:
        if j == "-":
            continue
        sleep(0.7)
        pyautogui.write(j.upper())
        sleep(0.2)
        send_keys('{ENTER}')
        sleep(0.4)
        pyautogui.press('/')
        pyautogui.write("/e cheer")
        sleep(0.2)
        send_keys('{ENTER}')
        sleep(0.4)
        pyautogui.press('/')

