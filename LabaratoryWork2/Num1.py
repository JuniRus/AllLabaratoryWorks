def greet(name):
    print("Hello, " + name + "!")

def square(number):
    return number**2

def max_of_two(x, y):
    if x > y:
        return  x
    else:
        return  y

greet("Пётр")
print(square(25))
print(max_of_two(47, 29))