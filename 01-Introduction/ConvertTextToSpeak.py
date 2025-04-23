#!/bin/usr/python3
from gtts import gTTS
import vlc
import time

myobj = gTTS(text='صباح الخير يا كبير', lang='ar', slow=False)
myobj.save("Welcome.mp3")  

p = vlc.MediaPlayer("Welcome.mp3")
p.play()

time.sleep(1)

while p.is_playing():
    pass
