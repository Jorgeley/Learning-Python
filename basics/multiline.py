#this is a multi line statement sample, the "\" (slash)
#is used to keep the line without end it, in this case,
#the statement ends in line 6
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

#parenthesis (), brackets [] and braces {} can be used as well as multi line statement
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(a)

colors = ['red',
          'blue',
          'green']
print(colors)

#otherwise, we can write multiple statements in one single line using ;
a = 1; b = 2; c = 3
print(a, b, c)

#multi line strings can be built using triple quotes ''' or """, see:
b = '''multiline string with triple quotes
doesn't matter if there are more quotes
but cannot have 3 quotes \''' unless you
scape 3 quotes with \(slash)'''
print(b)
'''you can write multi line comments
with triple quotes as well'''