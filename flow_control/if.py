# If the number is positive, we print an appropriate message
# be careful with indention! remember there are not {} to
# indicate start and end of the block, instead use indention
num = 0
if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is a negative number")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

# BE CAREFUL WITH INDENTION!!!
#if num < 0:
#print "this will result an error because isn't indented!"