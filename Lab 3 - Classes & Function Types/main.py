"""
Content : Functions, Lambda Functions, Generator Functions (Yield), Exceptions, Classes
"""


# Functions
#------------------------------#
def printStatments():
    #body
    print("Welcome to Lab 3 :)")
    print("Content : Functions, Lambda Functions, Yield, Exceptions, Classes")
    print("Now We are in functions")

# printStatments()
#------------------------------#
def sumNumbers(num1, num2):
    return num1 + num2

result = sumNumbers(1, 2)
# print(result)
#------------------------------#
def moreThanOne(num1, num2):
    condition = num1 > num2
    sum = num1 + num2
    minus = num1 - num2
    return condition, sum, minus

# con, sum, minus = moreThanOne(1, 2)
# print(f"The condition is {con}, the summation is {sum} and the sub is {minus}")
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# print(moreThanOne(n1, n2), type(moreThanOne(n1, n2)))
#------------------------------#
def defaultParams(college = "CS"):
    return "My college is " + college

# print(defaultParams())
# print(defaultParams("Computer & Information Science"))
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
# Lambda Expression
# Syntax => x = lambda arguments: ONE expression

perimeter = lambda side: side * 4
# print(perimeter(5))

sum = lambda a, b: a + b * 2
# print(sum(1, 2))

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
# Generator Functions (Yield)

def func():
    yield "Hello from 1"
    yield "Taking Break..."
    yield "I'm about ending"

result = func()
# print(next(result))
# print(next(result))


# for x in func():
#     print(x)

myList = [1, 2, 3]
generator = (i + 1 for i in myList)

# 1st Loop <<<
# for res in generator:
#     print(res)
#
# # 2nd Loop <<<
# for res in generator:
#     print(res)

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
# Exceptions
try:
    print(x)
except: #Error called => NameError
    print("Something went wrong :(")

#------------------------------------------#

try:
    x = int(input("Please enter a number: "))
except:
    print("Please enter a number should be integer")
finally:
    print("I will always run")
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

# Classes
class Person:
    haveHead = True
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
    def greeting(self):
        return "Hello " + self.name
    def setID(self, id): # att.setter
        self.id = id
    def getID(self): # att. getter
        return self.id

# p1 = Person('ali', 'SWE', 1)
# print(p1.name)
# print(p1.greeting())
# print(p1.haveHead)
# p1.setID("51024")
# print(p1.getID())
# p1.college = "CS"



#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

# Hands on #

class Solution:
    # with declarative functions
    def recursive(self, n):
        # base condition
        if n == 0:
            return 1
        else:
            return self.recursive(n - 1) + 100

    # with lambda exp.
    rec = lambda self, n: 1 if n == 0 else self.rec(n - 1) + 100  # => Ternary Operator -> True if condition else False

sol = Solution()
n = int(input("Enter a number: "))
# print(sol.recursive(n))
# print(sol.rec(n))

