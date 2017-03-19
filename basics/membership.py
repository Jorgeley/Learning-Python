# membership operator is used to see if a value is part of a
# sequence (string, list, tuple, set and dictionary)
x = 'Hello world'
y = {1:'a',2:'b'}
z = [9, 'b', 0]

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output True
print('b' in z)

# Output: False, because in dictionaries
# we can only check if the index exists
print('a' in y)