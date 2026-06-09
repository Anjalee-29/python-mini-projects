import pyautogui as py
import keyboard as kbd
import time

string = input("Enter what you want to spam: \n> ")

# Countdown before starting
print("Starting in...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Spamming! Press 'q' to stop.\n")

def spammingBot(string):
    while True:
        if kbd.is_pressed('q'):
            print("Stopped.")
            break
        pyg.typewrite(string, interval=0.05)
        pyg.press("enter")
        time.sleep(2)

spammingBot(string)
