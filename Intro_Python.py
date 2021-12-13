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
