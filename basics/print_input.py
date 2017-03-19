print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,'*')
# Output: 1*2*3*4

print(1,2,3,4,'#','&')
# Output: 1#2#3#4&

#remember: strings are objects, so you can use their methods and
#attributes, see the 'format()' and 'upper()' methods below
x = 5; y = 10
print('the value of x is {} and y is {}'.upper().format(x,y))

#the braces {} are the placeholders and can indicate the index
print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

print('Hello {name}, {greeting}'.format(greeting = 'Good morning', name = 'John'))

#inputing
num = input('Enter a number: ')
print(num)