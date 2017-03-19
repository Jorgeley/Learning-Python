# we can have nested functions: functions inside functions
def print_msg(msg):
    def printer(): # this is the nested function
        print(msg)
    printer()
print_msg("Hello")


# closures: it's a returned function 'jailed' inside other function
def print_msg(msg):
    def printer():
        print(msg)
    return printer  # returning the function
another = print_msg("Hello")
another()

# another good example of closures
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))