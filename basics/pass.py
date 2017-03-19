# pass is used when we know that we have to implement something but
# we don't know how at the moment (we know that it happens sometimes)
# It's like to tell the compiler something as:
# 'Dear compiler, I don't know what to do here at the moment, but I know
# that I'll have to, later I'll think about, just don't give me an error ok?
#           sincerely Me'
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass # if we left a 'for' without body would result an error, so we use 'pass'

# same with functions or whatever block of code
def function(args):
    pass

class example:
    pass