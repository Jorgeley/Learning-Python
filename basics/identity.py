# identty operator 'is' used to see if value and type is the same
x1 = 5
y1 = 5
z1 = '5'
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
tuple1 = (1,2,3)
tuple2 = (1,2,3)
set1 = {1,2,3}
set2 = {1,2,3}

# Output: False
print(x1 is not y1)

# Output false because z1 is string
print(x1 is z1)

# Output: True
print(x2 is y2)

# Output: False, because lists can be changed
print(x3 is y3)
print(tuple1 is tuple2)
print(set1 is set2)