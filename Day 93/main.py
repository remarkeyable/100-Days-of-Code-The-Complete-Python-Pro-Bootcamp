
import pyautogui

while True:
    x, y = pyautogui.position()
    pixel = pyautogui.pixel(x, y)
    print(pixel)

    # Morning
    if pixel == (83, 83, 83):
        pyautogui.press('space')
    # Night
    elif pixel == (172, 172, 172):
        pyautogui.press('space')
