'''
Using “Pyautogui” to open Emails and change Emails from unread to read
'''
import pyautogui
from time import sleep
import webbrowser

#open gmail inbox
url="https://mail.google.com/mail/u/0/?hl=ar#inbox"
webbrowser.open(url)
sleep(5)

try:
    #to selct all 
    pyautogui.moveTo(x=284,y=228,duration=0.5)
    sleep(2)        
    pyautogui.click()
    sleep(2)
    #to mark as read
    pyautogui.moveTo(x=492,y=231,duration=0.5)
    sleep(2)
    pyautogui.click()
    #to delete all
    pyautogui.moveTo(x=433,y=228,duration=0.5)
    sleep(2)
    pyautogui.click()
except :
    print("not fount")
