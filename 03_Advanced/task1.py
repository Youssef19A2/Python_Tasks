'''
Using PyAutoGUI 
- To open vscode 
- install clangd from extension
- install c++ testmate from extension
- install c++ helper from extension
- install cmake from extension
- install cmake tools from extension
'''
import pyautogui
from time import sleep

#Open terminal
pyautogui.hotkey('ctrl', 'shift', '~')
sleep(2)
#open vs code
pyautogui.write('code', interval=0.1)
pyautogui.press('enter')
sleep(5)
#open extenxion
pyautogui.hotkey('ctrl','shift','x')
sleep(2)
#install clang
pyautogui.write('clangd', interval=0.1)
sleep(2)
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(x=156,y=181,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=590 ,y=227 , duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
#clear
pyautogui.moveTo(x=165,y=121,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.hotkey('ctrl','a')
sleep(2)
pyautogui.press('backspace')
sleep(2)
#install c++ testmate
pyautogui.write('c++ testmate', interval=0.1)
sleep(2)
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(x=156,y=181,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=588,y=231,duration=0.5)
sleep(2)
pyautogui.click()
#clear
pyautogui.moveTo(x=165,y=121,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.hotkey('ctrl','a')
sleep(2)
pyautogui.press('backspace')
sleep(2)
#install c++ helper
pyautogui.write('c++ helper', interval=0.1)
sleep(2)
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(x=156,y=181,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=588,y=231,duration=0.5)
sleep(2)
pyautogui.click()
#clear
pyautogui.moveTo(x=165,y=121,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.hotkey('ctrl','a')
sleep(2)
pyautogui.press('backspace')
sleep(2)
#install cmake
pyautogui.write('cmake', interval=0.1)
sleep(2)
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(x=158,y=330,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=588,y=231,duration=0.5)
sleep(2)
pyautogui.click()
#clear
pyautogui.moveTo(x=165,y=121,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.hotkey('ctrl','a')
sleep(2)
pyautogui.press('backspace')
sleep(2)
#install cmake tools
pyautogui.write('cmake tools', interval=0.1)
sleep(2)
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(x=156,y=181,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.moveTo(x=588,y=231,duration=0.5)
sleep(2)
pyautogui.click()
#clear
pyautogui.moveTo(x=165,y=121,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.hotkey('ctrl','a')
sleep(2)
pyautogui.press('backspace')
sleep(2)

#tell me the code is end
pyautogui.moveTo(x=18,y=331,duration=0.5)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.hotkey('ctrl', 'shift', '~')
sleep(2)
pyautogui.write("echo Finshed Mr yousef",interval=0.1)
pyautogui.press('enter')
