'''
Dictionary type seens like a Set type, but instead of Set, Dictionary has indexing
'''
d = {1:'value', 'key':2, 0:99, "a":"aaa"}
print(d)
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error, this index doesn't exist
#print("d[2] = ", d[2]);