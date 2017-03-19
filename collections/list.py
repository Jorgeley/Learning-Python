'''List is an ordered sequence of items. It is one of the most used datatype
in Python and is very flexible. All the items in a list do not need to be of
the same type. Declaring a list is pretty straight forward.
Items separated by commas are enclosed within brackets [ ].'''
a = [1, 2.2, 'python',
        [9, 8.88888, 'xxx']
     ]
print(a)

#we can extract an item of the array:
print(a[2])
print(a[3][2])

#we can extract as many as we want giving a range of values in the format index:length
print(a[3][0:2])

#we can modify a specific item:
a[2] = "PYTHON"
print(a[2])