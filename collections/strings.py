str = "this is a string"

# strings can be iterated, they are collections
for s in str:
    print(s)

# concatenate is simple
print(str+" in Python")

# Remember: everything in Python is an object!!!
str = "|".join(["this","will","be","concatenated"])
print(str)
print(str.split("|"))
print(str.partition("be"))
print("My name is {0} and I am {1}".format("Jorgeley",34))
print("My name is {name} and I am {age}".format(name="Jorgeley",age=34))
