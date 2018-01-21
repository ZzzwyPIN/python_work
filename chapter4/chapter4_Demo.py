animals = ['cat','dog','monkey','elephant']
for animal in animals:
	print(animal)
	print("A "+animal.title()+" would be a great friend.\n")
print("We should be friendly to this animals!")
for value in range(1,6):
	print(value)
numbers = list(range(1,10,2))
print(numbers)
squares = []
for value in range(1,11):
	# ~ square = value**2
	squares.append(value**2)
	
print(squares)
print(min(squares))
print(sum(squares))

squares2 = [value**2 for value in range(1,11)]
print(squares2)

for value in range(1,21):
	print(value)

num = list(range(1,1000001))
print(min(num))
print(max(num))
print(sum(num))
num3 = [value*3 for value in range(1,11)]
for x in num3:
	print(x)
num4 = []
for x in range(3,31,3):
	num4.append(x)
print(num4)
num5 = [value**3 for value in range(1,11)]
for num in num5:
	print(num)
plays = ['a','b','c','d','e']
print("Three items from the middle of the list are:")
for play in plays[1:4]:
	print(play)
# ~ print(plays[-2:])
# ~ print("Here are the last three in the plays:")
# ~ for play in plays[-3:]:
	# ~ print(play)
# ~ plays2 = plays[:]
# ~ plays.append('g')
# ~ plays2.append('f')
# ~ print(plays)
# ~ print(plays2)

# ~ yuanzu
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# ~ dimensions[0] = 250 #TypeError: 'tuple' object does not support item assignment

















