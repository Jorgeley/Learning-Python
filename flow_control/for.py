# For is used to loop a code as many times as we need
# it's recommended in cases when we know exactly how
# many times we need to execute a code, in collections for example

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum += val

# Output: The sum is 48
print("The sum is", sum)

# 'for' can have an 'else' statement that specify
# what to do when there's no more elements, see:
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# we can iterate strings as well
string = 'abcd'
for s in string:
    print(s)

# we can use 'break' statement to exit a flow_control if necessary
string = 'abcd'
for s in string:
    print(s)
    if s == 'c':
        print('exiting')
        break

# we can use 'continue' statement to skip an iteration, it
# doesn't finish the flow_control as 'break', just stop executing
# the code below 'continue' and goes to the next iteration
for s in string:
    if s == 'c':
        print('skiping')
        continue
    print(s)