import time
import pyperclip
import pyautogui
from pywinauto.keyboard import send_keys

def check_clipboard():
    prev_content = ""
    copied = False
    while True:
        try:
            buy = pyautogui.locateCenterOnScreen('buy.png', confidence=0.7) 
            buy2 = pyautogui.locateCenterOnScreen('buy2.png', confidence=0.7) 
            redeem = pyautogui.locateCenterOnScreen('redeem.png', confidence=0.7) 
            current_content = pyperclip.paste()
            if current_content != prev_content and (buy or buy2):
                if buy:
                    pyautogui.moveTo(buy)
                else:
                    pyautogui.moveTo(buy2)

                pyautogui.click(clicks=5)
                if copied == False:
                    pyautogui.hotkey("ctrl", "v")
                    time.sleep(0.15)
                    send_keys('{ENTER}')

                    copied = True
                '''if redeem:
                    pyautogui.moveTo(redeem)
                    pyautogui.click(clicks=1)
                    time.sleep(0.1)
                    pyautogui.click(clicks=1)'''
                prev_content = current_content
                copied = False
                if buy:
                    pyautogui.moveTo(buy)
                else:
                    pyautogui.moveTo(buy2)

                pyautogui.click(clicks=2)
            time.sleep(0.1)
        except Exception as e:
            print(f"An error occurred: {e}")

check_clipboard()
