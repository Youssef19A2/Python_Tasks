#!/usr/bin/python3

import os
#Write a Python program to count the number 4 in a given list.

x=[1,2,3,4,5,4,4,4,4,4,6]
print(x.count(4))

#Write a Python program to test whether a passed letter is a vowel or not.

list1=['a','e','u','i','o','A','O','U','I','E']

char=input("Please enter the vowel letter: ")

if char in list1:
    print("Vowel")
else:
    print("False")

#Write a python program to access environment variables.

current_path = os.getcwd()
print(current_path)

