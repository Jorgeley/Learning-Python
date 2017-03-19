"""
Tuple is an ordered sequence of items same as list.
The only difference is that tuples are immutable.
Tuples once created cannot be modified.
Tuples are used to write-protect data and are usually
faster than list as it cannot change dynamically.
It is defined within parentheses () where items are separated by commas.
"""

tuple = (5, 'program', 1+3j, "a")
print(tuple)

# another way to create a tuple
tuple = 2, 5, 9, 0
print(tuple)

# tuple[1] = 'program'
print("tuple[1] = ", tuple[1])

# tuple[0:3] = (5, 'program', (1+3j))
print("tuple[0:3] = ", tuple[0:3])

# Error: Tuples cannot be modified
#tuple[0] = 10