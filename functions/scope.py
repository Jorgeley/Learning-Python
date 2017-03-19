# be aware of scopes
def my_func():
    x = 10  # this 'x' is not the same below
    print("Value inside function:", x)

x = 20  # this 'x' is not the same above
my_func()
print("Value outside function:", x)


# objects are always passed by reference, it means that, when you call a function passing
# an object as argument, it's not a copy of the object that is passed but his reference, see:
def f(f):
    return f
g = [1,2,3]
f = f(g)
print(f is g) # True, because 'f' is reference of 'g'


# in this example, see that the objects inside the function and
# outside the function have been modified. How? Because the object 'r'
# outside the function was passed by reference when calling the function,
# it means that 'r' (inside the function) and 'r' (outside the function)
# points to the same memory address, so the function modifies the object
def references(r):
    r.append("xxx") # this 'r' object references the same address of the other 'r' object outside the function
    print("object 'r' inside function is ", r)
r = ["z","y"]
references(r)
print("object 'r' outside the function is ", r)


# if you don't want the both objects been modified, you have to create
# another one inside the function, see the same updated example above:
def references(r):
    r = ["xxx", "www"] # this is a new 'r' object
    print("object 'r' inside function is ", r)
r = ["z","y"]
references(r)
print("object 'r' outside the function is ", r)


# scopes can be:
#   local: the names exists just inside the function
#   enclosing: the names exist in any and all enclosing functions
#   global: the names exist in the entire module
#   built-in: the names exist anywhere and were defined by the python itself
# See an example:
count = 0 # this variable is global scope
def show_count():
    print("count is ", count)
def set_count(c):
    count = c # this variable is local scope
show_count() # shows 0
set_count(5)
show_count() # shows 0 again, because the 'count' variable inside the function 'set_count()' is
             # local scope, it's not the same as the global 'count' in the begining

# See the prior updated example:
count = 0 # this variable is global scope
def show_count():
    print("count is ", count)
def set_count(c):
    global count # this tells Python that this 'count' is the same prior global
    count = c
show_count() # shows 0
set_count(5)
show_count() # Now shows 5, because the 'count' variable inside the function 'set_count()' is
             # the global 'count' in the begining