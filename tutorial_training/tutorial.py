print("|\\")
print("| \\")
print("|  \\")
print("|   \\")
print("|    \\")
print("|_____\\")

print("Name : John")
print("Age : 35")

character_name = "John"
character_age = "35"
print("Name : " + character_name)
print("Age : " + character_age)

character_name = "Mike"
character_age = "30"
print("Name : " + character_name)
print("Age : " + character_age)

# data types
character_name = "Tom"  # String
character_age = 30  # Number
height = 6.5  # Number
is_male = True  # Boolean

# String Operations
print("Arun\nKumar")  # new line
print("Arun\"Kumar")  # escape sequence
phrase = "AK is Awesome"
print(phrase)
print(phrase + " And Cool")  # concatenation
print(phrase.lower())  # change to lower case
print(phrase.upper())  # change to upper case
print(phrase.isupper())  # check upper case
print(phrase.islower())  # check lower case
print(len(phrase))  # Find Length
print(phrase[6])  # get char from string
# print(phrase.index("Äwe"))  # get index of character
print(phrase.replace("Awesome", "Cool"))

# Working with Numbers
print(2)
print(2.03545)
print(-2.03545)
print(2 + 10.332)  # Addition
print(34 - 324)  # Subtraction
print(3 * 10)  # Multiplication
print(30 / 34)  # division
print(34 // 3)  # floor division
print(30 % 34)  # modulus for remainder
my_num = 5
print("My Number : " + str(my_num))  # python wont allow number to string concatenation so we have to use str method
print(abs(-3))  # to get absolute value
print(pow(3, 2))  # power method
print(max(10, 40))  # to get max of numbers
print(min(10, 40))  # to get min of numbers
print(round(3.45))  # rounding up numbers

from math import *

print(floor(3.45))  # rounding up floor
print(ceil(3.45))  # rounding up ceil
print(sqrt(4))  # returns square root

# Getting input from users
name = input("Enter your Name : ")
age = input("Enter your age : ")
print("Hello " + name + "! your age is " + age)

# Building A Basic Calculator
num1 = int(input("Enter a number"))  # input is always a string use int to convert to integer
num2 = float(input("Enter another number"))  # input is always a string use float
result = num1 + num2
print("Result" + str(result))
