"""
#Pythooon in 30 Minutes ;)
Revision Content [Fundamentals]:
print() - variables - operators - casting - if condition - loops - list - range - functions - input
"""
language = 'Python'
number = 10

print("I am learning python in 30 minutes")
print('My name is youssef')
print(language, "which I love", number, 'years of practice')
print(f'{language} which I love {number} years of practice') # format statements

"""
Declaring a variable:
    #nameOfVariable = value
"""

"""
Data type in Python: 
string (str) - integer (int) - boolean (bool) - float 
"""
# print(type(number)) => to print the data type

"""
Math operators:    
+ - / * ** // 
Operators Precedence: (1 + 1) * 2  - 5 / 4 + 3 ** 2 
() -> ** -> * -> / -> + -> - => (PEMDAS)
Comparison Op.:
< > <= >= == !=
Logical Operators:
and or not ==> && || are wrong in python
"""
print(10 // 3) #=> floor division (make implicit casting to neglect the floating points and return int)
"""
Casting:
Convert data type from type to another and have two type (Implicit / Explicit)
Implicit Casting: Interpreter itself convert to another type
Explicit Casting: Programmer convert from type to type...
"""

number = "10"
number = int(number) #=> Explicit casting
"""
Explicit Casting:
=>> int() - bool() - str() - float()
"""

# name = int("hassan") => WRONG
# print(number + 5)

number = 3
if number == 5:
    # body of condition
    print(f'number is equal to {number}')
elif number > 5:
    print(f'number bigger than  5')
else:
    print("less than")

# While loop
while number > 0:
    print("True")
    number += 1 #=> number += 1 is same as number = number + 1

# for loop
for i in range(1, 8, 2):
    print(i)



myList = ['ahmed', 'hosny', 1, 2, 3, 5.8886, True, False]
print(myList[0], myList[1])
print(myList)
print(len(myList))
for i in myList:
    print(i)
for i in range(len(myList)):
    print(myList[i])

myList.append("Add in last") # to add element in last of list
myList.pop(1) # to remove item by index
myList.remove('ahmed') # to remove item by its name
myList.clear() # delete all items in the list

myList.insert(0, 'first item') # add item add specific index
print(myList[1 : 4]) # list slicing
name = 'ali ahmed mohamed hossam'
# print(name[5 : 8])

# Functions
def greeting(name):
    #body of function
    return f'Welcome {name}'

welcome = greeting('Ahmed')
print(welcome)

name = input("Enter your name: ") # to take input from user
print(f'Welcome {name}')
"""
the default and primary type that input accept and take is STRING
You need to explicit casting to make the input taken int or float or bool
"""
number = float(input("Enter number: "))
print(number + 5)
# print(type(number))