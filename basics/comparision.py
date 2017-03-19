x = 10
y = 12

# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)


# we can use logical operators 'and', 'or' and 'not'. Examples:

#x is greater than 0 but not greater than y, so result is False
print('x > y and x > 0?', x>y and x>0)
#x is greater than 0 and lower than y, so result is True
print('x < y and x > 0?', x<y and x>0)
#x is greater than 0, if one is true no matter the others, so result is True
print('x > y or x > 0?', x>y or x>0)