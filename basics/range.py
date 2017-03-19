# Output: range(0, 9)
print(range(10)) # 10 is the quantity of numbers, default inits from 0

# Output: [2, 3, 4, 5, 6, 7]
print(range(2, 8)) # here we specified to init from 2

# Output: [2, 5, 8, 11, 14, 17]
print(range(2, 20, 3)) # here we specified to init from 2 until 20 steping in 3

# range can be used to iterate elements as well, see:
genres = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genres)):
	print("I like", genres[i])
# ofcourse this would be more easy using 'in' membership operator, see:
for genre in genres:
	print("I like", genre)