#!/usr/bin/python3
from pytube import YouTube

url = input("Please Enter the url if video: ")

# السطر ده هو المهم - بيشيل أي حاجة بعد علامة ؟ أو &
url = url.split('?')[0].split('&')[0]

YouTube(url).streams.filter(progressive=True, file_extension='mp4').first().download()
