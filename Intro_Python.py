# Introduction to Python Programming

# Function: print
# To display our results in the console

# Example:
print(3+5)

# Arithmetic Operators

# "+" (Addition)
# Example:
3+5
# Result: 8

# "-" (Subtraction)
# Example:
7-2
# Result: 5

# "*" (Multiplication)
# Example:
7*2
# Result: 14

# "/" (Division)
# Example:
8/2
# Result: 4

# "%" (Module = The remainder after dividing)
# Example:
7%2
# Result: 1

# "**" (Exponeciation) - Important: Do not confuse with the "^", it does a different operation called "bitwise XOR"
# Example:
2**3
# Result: 8

# "//" (Integer Division - Divides and rounds down to the nearest integer)
# Example:
7//3
# Result: 2

# Variables

# Assigning one variable
x = 3

# Assigning multiple variable
x, y, z = 2, 3, 4

# The pythonic way to name variables is to use all lowercase letters and underscores to separate words

my_height = 58
my_lat = 40
my_long = 105

# Assignment Operators

x += 2 # -> x = x + 2
x -= 2 # -> x = x - 2
x *= 2 # -> x = x * 2
x /= 2 # -> x = x / 2
x %= 2 # -> x = x % 2
x //= 2 # -> x = x // 2
x **= 2 # -> x = x ** 2

# Integers and Floats

# int - for integer values
# float - for decimal or floating point values

# You can check the data type of a number with the function called "type()"
# Example:
print(type(4))
# Result: <class 'int'>

# int() - Convert a number to integer
int(4.2) # -> 4
# float() - Conver a number to float
float(4) # -> 4.0

# Be aware that float numbers use the approximation of a number.
# So you need to be careful to some operations like equalit.

# Types of errors in python:

# Exceptions: Is a problem that occurs when the code is running
# Syntax Error: Is a problem detected when Python checks the code before it runs it

# Boolean
# Bool - A boolean is a data type that can have a value of true or false

# Example:
x = 42 > 43 # -> false

# Comparison Operators

# <  -> Less than
# >  -> Greater than
# <= -> Less than or equal to
# >= -> Greater than or equal to
# == -> equal to
# != -> not equal to

# Logical Operators

# and -> evaluates if both sides are true
# or  -> evaluates if at least one side is true
# no  -> inverses a boolean type

# Example
age = 14
is_teen = age > 12 and age < 20
print(is_teen)
# Result
# True

# Example
age = 14
is_not_teen = not(age > 12 and age < 20)
print(is_teen)
# Result
# False

# String - Data type to save texts

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"

this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
# Result: Simon's skateboard is in the garage.

# Concatenation

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
# Result: John Doe

# Function len()

# The len() is a built-in Python function that returns the length of an object, like a string.
len(first_name) # -> 4

# Indexing - Notice Python uses 0 indexing

first_name[0]
# Result: "J"
first_name[1]
# Result: "o"

# Type and Type Conversion

int()   # -> To convert to an int
float() # -> To convert to a float
bool()  # -> To convert to a boolean
str()   # -> To convert to a string

# Example:

house_number = 13
street_name = "The Crescent"
town_home = "Belmont"
print(type(house_name))     # <class 'int'="">

address = str(house_number) + " " + street_name + ", " + town_name
print(address)

# String Methods

.title() # Capitalize the first letter for each word
# Example:
"john doe".title()
# Result: John Doe

.lower() # Make the string all lowercase

.upper() # Make the string all uppercase

.islower() # Check if the string is all lowercase

.isupper() # Check if the string is all uppercase

.count("arguments") # Count the number of times the argumment appears

.find("arguments") # Find the index of a argument

.format("arguments") # input some text in a string
# Example:
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
# Result: Maria loves math and statistics
