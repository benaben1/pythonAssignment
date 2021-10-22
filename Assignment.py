# 1a
# displaying values
x = 8
y = 2
print("x:" + str(x) + ", y:" + str(y))

# 1b
# multiplication
print("x*y=" + str(x * y))

# 1c
# exponential
print("x**y=" + str(x ** y))

# 1d
# division
print("x/y=" + str(x / y))

# 1e
#  Floor division
print("x//y=" + str(x // y))

# 1f
# dividing a value by zero
y = 0
z = (x / y) if y != 0 else 0  # created another variable z
print("x/0=" + str(z))

# 2a
# User Input
name = input("Enter your name:")
print("And " + name + " is my name.")

# 2b
# displaying values
name = "Bena"
address = "Kireka"
telphone = "0757389094"
print("Wow! good to know you dear, my name is " + name + ", i stay in " + address + " and " + telphone + "is my "
                                                                                                         "contact.")
# 3a
# User Input
userName = input("Enter user Name: ")
userAge = input("Enter user Age: ")
print("Hello!\nYou have successfully entered your details.\nUser Name: " + userName + "\nUser Age: " + userAge)

# 3b
# Finding the birth year
current_year = 2021
birth_year = 2021 - int(userAge)
print("birth_year is " + str(birth_year))

# 4
# Area of a circle
r = input("Enter radius ")
s = int(r)**2  # created another variable s
PI = int(3.14)
Area = PI * s
print("Area of the circle is " + str(Area))

# 5a
'''
A Python script is a collection of commands in a file designed to be executed like a program
'''

# 5b  what goes on behind the scenes when your computer runs a Python Program.
'''
1. At first step python program is written in text editor or IDE (integrated development environment). Then 
programmer saved this source code to a file with .py extension. This file is called script file. 

2. After writing source code, programmer uses compiler to interpret the source code to byte code

3. Python virtual machine then translate this byte code into instructions that can interact with operating system of 
computer. 

4. Operating system then execute these instructions.'''