"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two input integers."""
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    """Multiply the two inputs together."""
    product = num1 * num2
    return product

def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""
    quotient = num1/num2
    return quotient

def square(num1):
    """Return the square of the input."""
    squared = num1**2
    return squared

def cube(num1):
    """Return the cube of the input."""
    cubed = num1**3
    return cubed

def power(num1, num2):
    """Raise num1 to the power of num and return the value."""
    exp = num1**num2
    return exp

def mod(num1, num2):
    """Return the remainder of num / num2."""
    modulo = num1%num2
    return modulo

# sum = add(1, 2)
# print sum

# difference = subtract(5,10)
# print difference

# product = multiply(3, 5)
# print product

# quotient = divide(10,5)
# print quotient

# squared = square(3)
# print squared

# cubed = cube(4)
# print cubed

# exp = power(6, 2)
# print exp

# modulo = mod(9,4)
# print modulo