def compare_age(name1, age1, name2, age2):
    if age1 > age2:
        print (f"{name1} is older than {name2}")
    elif age2 > age1:
        print(f"{name2} is older than {name1}")
    else:
        print(f"{name1} and {name2} are of the same age.")
    
compare_age("johnny",6, "jon", 9)



def next_age(age):
    return age + 1

print(next_age(20) + 10) 

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))



my_global_variable = "I am global !"

def my_function():
    my_local_variable = "I am local to my_function () !"
    print(my_local_variable)
    print(my_global_variable)

def another_function():
    my_global_variable = "I am local to another function () ! "
    print(my_global_variable)


another_function()
print(my_global_variable)


def greet_person(name):
    return "Hello, " + name

greet = lambda name: "Hello, " + name

from math import factorial

print(factorial(20))

import math
print(math.gamma(9))
