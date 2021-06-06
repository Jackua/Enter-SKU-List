import pyautogui
import tkinter
import time

try:
    skuList = list(tkinter.Tk().clipboard_get().split())
except:
    pass

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.click()

for i in range(len(skuList)):
    pyautogui.write(skuList[i])
    pyautogui.press('enter')
    time.sleep(1)
