try:
    with open("test.txt") as file:
        for line in file:
            print(line)
except ValueError as error:
    print("an error ocurrs!!!", error.message)
finally:
    file.close()