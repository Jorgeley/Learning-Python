# while executes a block of code as long as his condition is true
# it's recommended in cases when we don't know exactly how many
# times we need to execute a flow_control
n = 10
sum = 0
i = 1

while i <= n:
    sum += i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

# like 'for' flow_control, while can have 'else' too
counter = 0
while counter < 3:
    print("Inside flow_control")
    counter = counter + 1
else:
    print("Inside else")

# like 'for' flow_control, while can have 'break' to exit the flow_control
while sum>0:
    sum -= 5
    if sum <= 30:
        break
print('sum is',sum)