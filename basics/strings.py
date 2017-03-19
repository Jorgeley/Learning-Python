#Strings can be delimited using single quotes or double quotes
#Strings can be accessed with slicing operator []
s = "xyz"
print(s)
print(s[2])

#multi line strings can be built using triple quotes ''' or """, see:
b = '''multiline string with triple quotes
doesn't matter if there are more quotes
but cannot have 3 quotes \''' unless you
scape 3 quotes with \(slash)'''
print(b)

#this can be done, no problem
s = 'abc'
print(s)

#this cannot be done, WE CANNOT MODIFY A SLICE OF A STRING!!!
s[2] = "d"