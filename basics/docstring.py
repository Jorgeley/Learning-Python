#this is a function sample using dostring
#docstring is a function's documentation
#it must be the first statement to work
#it can be accessed by the attribute __doc__
def double(num):
    """Function to double a value"""
    return 2*num

print(double.__doc__)
print(double(5))