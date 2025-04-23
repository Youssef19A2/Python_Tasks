'''
To install python3 --> sudo apt-get install python3 
To install python2 --> sudo apt-get install python2 
To know the version of python3 --> python3 --version
To know the version of python3 --> python3 --version

Python is an interpreter programmed language not compiler

Interpreter mean it contain compiler and bytecode and vitual machine whinch contain libarary modules
bytecode is computer object code that an interpreter converts into binary, so it can read by computer's hardware processor 

To know the assemply of file.py
1) you can write in terminal --> python3 -m dis file_name.py
2) EX:
import dis 
def sum(x,y):
    return x+y
dis.dis(sum)
print(hex(dis.opmap["LOAD_FAST"]))

To run interpreter you choose between two option:
1) python3 file_name.py
2) use shaping and change the mode to allow the user to execute 
#! /bin/python3
chmod u+x file_name.py
./file_name.py
'''

# --> for single line comment 
'''
--> for multi line comment 
'''

#To print string 
print("Hello")
print('Hello')
print('''Hello''')
print("hello mr'youssef")
print('he said hello to mr "Youssef"')

#variable 
'''
Pyhton is a dynamic language that does not need to identify the data type of variable 
in pyton we can overwrite with variable
'''
x=10
print(type(x))
x=10.20
print(type(x))
x="youssef"
print(type(x))

#variable name rule 
'''
1)variable cannot start with numbers (0-9)
2)variable cannot start with alphapets symbols like ($,%,&)
3)variable can start with underscore(_) or alphanumeric character (a-z)
4)it case sensitive (age is not Age is not AGE)
'''
#comma operator
v,y,z=1,2,3
print(v)
print(y)
print(z)
'''
                                   data types
1)numeric --> int or complex or float 
2)dictionary
3)boolen
4)set
5)seqence type --> list or tuple or string 
'''
#numeric
a=10
print(type(a))
a=12.5
print(type(a))
a=12+10J
print(type(a))
thisdic={
    "colour":"red",
    "brand":"ford"
}
print(type(thisdic))
a=[1,2,3,4,]
print(type(a))
a={1,2,2,2,2,3,4,4,4,}
print(type(a))
a=(1,2,3,4)
print(type(a))
bool=True
print(type(bool))


#task to write a python code that print your information.Full Name, Birth Year, Faculty, E-mail, Address 
print("Fullname: Youssef ahmed \nEmail: Yousifahmed36567@gmail.com\nMobilenumber: 01100168825")

u=10
p=5
print(u+p)
print(u*p)
print(u-p)
print(int(u/p))


#task to convert name into list 
name="youssef"
print(list(name))

#to take input from user 

name=input("Please Enter Your Name: ")
print("Hello " + name + "!")
age=input("Please Enter Your Age: ")
print("Your Age Is " + age +" Years Old")

#if condition 

h=10
i=3
if h is i :
    print("YES")
elif h == i :
    print("Equal")
else:
    print("NO")

#shorthand if 

print("h")if h>i else print("no") if h > i else print("hello")

#nested if 
 
n=10
o=20
if n < o:
    if o>n:
        print("No")
else:
    print("no no")

p=10
while True:
    p+=1
    print(p)
    break

r=100
for i in range(10):
    r+=1
    if r == 101:
        print("stop")
    break
else:
    print("please stop ")

name_1="Yousef"

print(name_1[::-1])
