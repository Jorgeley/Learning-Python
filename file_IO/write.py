import random

# always use 'try' statement to avoid problems
try:
    # it's a good idea use 'with' statement, because
    # it garantees that the file will be closed
    with open("test.txt", "a") as file:
        file.write("teste "+str(random._inst)+"\n")
except ValueError as error:
    print("an error ocurr!!!", error.message)
finally:
    pass#file.close()