# IMPORTANT: when an object calls a method always the object itself is
# passed as argument, so in the above example 'ob.func()' is the same
# as 'MyClass.func(ob)'

class MyClass:
    '''this is my class'''
    a = 10
    def func(self):
		print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()