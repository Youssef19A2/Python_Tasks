#!/usr/bin/python3

import webbrowser

facebook_link ="https://www.facebook.com/"
youtube_link="https://www.youtube.com"
github_link="https://github.com/login"
chatgpt_link="https://chatgpt.com/"
linkedin_link="https://www.linkedin.com/login/ar"

def firefox(url):
   browser= webbrowser.get('firefox')
   browser=webbrowser.open(url)
    
