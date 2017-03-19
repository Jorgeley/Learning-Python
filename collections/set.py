#### Set type is automatic ordered and eliminates duplicated values
a = {5,2,3,1,4,5,4}
# printing set variable
print("a = ", a)
# data type of variable a
print(type(a))

###List type is note ordered and doesn't elimintes duplicated values
b = [5,2,3,1,4,5,4]
# printing list variable
print("b = ", b)
# data type of variable b
print(type(b))

###Tuple type is note ordered and doesn't elimintes duplicated values
c = (5,2,3,1,4,5,4)
# printing tuple variable
print("c = ", c)
# data type of variable c
print(type(c))

#Set does not support indexing, we cannot use slice operator []
#but we know that List and Tuple we can use
print(b[3])
print(c[3])
print(a[3])