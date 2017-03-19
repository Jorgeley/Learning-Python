# anonymous functions in python need to be declared with the keyword 'lambda'
#syntax:     lambda   arguments    expression
double =     lambda       x:         x * 2
# Output: 10
print(double(5))

# anonymous 'lambda' functions are useful in built-in functions (or yours)
# that requires another function as argument, see:
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# filter() function requires a function to tell how to filter the elements, so
# in this case we are using a anonymous 'lambda' function as argument
new_list = list(
            filter(
                    lambda x: (x%2 == 0), # function that tell the 'filter()' function how to do it
                    my_list # list that will be filtered
                  )
            )
# Output: [4, 6, 8, 12]
print(new_list)