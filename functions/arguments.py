# sample with default arguments
def greet(name="nobody", msg="Hi"):
    """This function greets to
	the person passed in as
	parameter, if not passed, greets 'nobody'"""
    print(msg + "," + name.capitalize() + ". Good morning!")

greet("jorgeley")
greet("goku", "Hi, I am ")
greet()
greet(msg="Hey", name="You")  # we can also specify the order of the arguments


# sample with infinite arguments
def greet(*names): # the asterix says that can be passed as many names as wee need
   """This function greets all
   the person in the names tuple."""
   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")


# be careful with default arguments, they are evaluated just once! See:
def f(a=[]):
    a.append("x")
    print(a)
f(); f(); f(); f()
# as you can see in the example above, we had 4 'x' printed but what we
# were expecting was just one because the argument 'a' supose to be always
# initiated with a empty list. BUT IT'S NOT!!! The argument it's initialized
# just once, in the 'def' moment of the declaration of the function, so, when
# we call again and again the function the 'a' list has the 'x' prior values