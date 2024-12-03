"""
    - Display a message
    - Concatenate strings
    - Recognize errors message such as Synthax error, Indendation error, etc.
    - input function
    - comment 
    - count the caracters in string
    - variables
"""

print("Hello World!")

first_name = 'Jean'
last_name= 'Aime'

print('my full name is :'+ first_name + " " + last_name)

# input function
age = input("Enter your age: ")

print("Your age is " + age + " years old")

print("hello " + input("enter your name: "))


# len function
name = "Jean Aime"
print("The length of the string is " + str(len(name)))


# variables
x = 10
y = 20
z = x + y
print('z is ' + str(z))

# switch a value of two variables
a = 2
b = 3

c = a
a = b
b = c

# or
#a, b = b, a

print('a :', a)
print('b :', b)

