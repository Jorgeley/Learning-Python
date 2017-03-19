# recursive function sample:
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))

# the same example above with for
def factorial(number):
    """factoring a number"""
    f = 1
    for n in range(1,number+1):
        f *= n
    return f

n = 5
print("Factoria of ",n," is ",factorial(n))