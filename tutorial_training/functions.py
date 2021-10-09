def say_hi(name, age):
    print("Hello " + name + "! you are " + age + " years old")


def add(num1, num2):
    return num1 + num2


def cube(num):
    return num * num * num;


say_hi(input("Enter your name : "), input("Enter your Age : "))

print(add(float(input("Enter a number : ")), float(input("Enter another number : "))))

print(cube(10))
