#converting int to float
print(float(5))

#converting float to int
print(int(5.9999))

#it's also possible to convert strings to numbers
#if there're no literal characters, see:
print(float('123.99'))

#converting List type to Set
a = [2.2, 1, 'python', 0]
print("a=",a)
print("object 'a' is a original ",type(a))
b = set(a)
print("b=",b)
print("object 'b' is a converted",type(b))

#converting List type to Tuple
c = tuple(a)
print("c=",c)
print("object 'c' is a converted",type(c))

d = dict([
        ['d','ddd'],#to be converted has to be
        [1,99]      #pairs in the format key,value
    ])
print("d=",d)
print("object 'd' is a converted",type(d))

#trying to convert List type to Dictrionary, but results an error
#because the list must have pairs
#d = dict(a)
#print d
#print type(d)

#this converstion results an error because . is a literal
#print int('123.99')