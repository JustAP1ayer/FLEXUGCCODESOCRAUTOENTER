import time
import os

try:
    import pyperclip
    import pyautogui
    from pywinauto.keyboard import send_keys
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install opencv-python")
    os.system("pip install pyperclip")
    os.system("pip install pywinauto")

def check_clipboard():
    prev_content = ""
    copied = False
    
    while True:
        try:
            buy_button = pyautogui.locateCenterOnScreen('buy.png', confidence=0.7) 
            buy_button_alt = pyautogui.locateCenterOnScreen('buy2.png', confidence=0.7) 
            # redeem_button = pyautogui.locateCenterOnScreen('redeem.png', confidence=0.7) 
            current_content = pyperclip.paste()

            if current_content != prev_content and (buy_button or buy_button_alt):
                button_to_click = buy_button if buy_button else buy_button_alt
                pyautogui.moveTo(button_to_click)
                pyautogui.click(clicks=5)

                if not copied:
                    pyautogui.hotkey("ctrl", "v")
                    time.sleep(0.15)
                    send_keys('{ENTER}')
                    copied = True

                prev_content = current_content
                copied = False

                pyautogui.moveTo(button_to_click)
                pyautogui.click(clicks=2)

            time.sleep(0.1)

        except Exception as e:
            print(f"An error occurred: {e}")

check_clipboard()
