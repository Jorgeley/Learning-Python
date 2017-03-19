# function is a block of reusable code, bla bla bla

# simple sample
def greet(name):
    """This function greets to
	the person passed in as
	parameter"""
    print("Hello, " + name.capitalize() + ". Good morning!")

greet("jorgeley")
greet("Goku")


# another example with 'return'
def absolute(number):
    """returns the absolute value of 'num'"""
    if number < 0:
        number *= -1
    return number

# Output: 2
print(absolute(2.99))
# Output: 4
print(absolute(-4))