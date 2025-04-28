'''
Write a Python program to get the command-line arguments
'''
import sys

print("This is the name of the script:", sys.argv[0])
print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))
