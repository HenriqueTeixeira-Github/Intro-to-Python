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

.split("sep", "maxsplit") # It splits a string into a list of evaluates
# Example:
new_str = "The cow jumped over the moon."
new_str.split()
# Result: ['The', 'cow', 'jumped', 'over', 'the', 'moon.']
new_str.split(' ', 3)
# Result: ['The', 'cow', 'jumped', 'over the moon.']

# List - Data structures are containers that organize and group data types together in different ways.
# A list is one of the most common and basic data structures in Python.

# Example
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(months[0])  # January
print(months[1])  # February
print(months[7])  # August
print(months[-1]) # December
print(months[25]) # IndexError: list index out of range

list_of_random_things = [1, 3.4, 'a string', True]

list_of_random_things[len(list_of_random_things) - 1]  # To get the last element from a list
list_of_random_things[-1]  # To get the last element from a list

# Slicing a List
print(months[6:9]) # [ 'July', 'August', 'September']
print(months[months[:6]) # ['January', 'February', 'March', 'April', 'May', 'June']
print(months[months[6:]) # ['July', 'August', 'September', 'October', 'November', 'December']

# Membership Operators

# in - Evaluates if object on left side is included in object on right side.
# noi in - Evaluates if object on left side is not included in object on right side.

# Examples:
'in' in 'this is a string' # True
'isa' in 'this is a string' # False
5 not in [1, 2, 3, 4, 6] # True
5 in [1, 2, 3, 4, 6] # False

#  List Methods

.len() # Returns how many elements are in a list.
.max() # Returns the greatest element of the list
.min() # Returns the smallest element in a list.
.sorted() # Returns a copy of a list in order from smallest to largest, leaving the list unchanged.

.join() # Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

# Example
name = "-".join(["García", "O'Kelly"])
print(name)
# Result: García-O'Kelly

.append() # Adds an element to the end of a list.

# Example
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
# Result:  ['a', 'b', 'c', 'd', 'z']

# Tuples
# Description: A tuple is another useful container. It's a data type for immutable ordered sequences of elements.

# Example:
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

#Example: Tuple unpacking (In this example the paranteses are omitted)
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
