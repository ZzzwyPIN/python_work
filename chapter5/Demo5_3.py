age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age > 65:
	price = 5
print("Your admission cost is $" + str(price) +".")

alien_color = 'yellow'
if alien_color == 'green':
	print("You have got 5 points!")
elif alien_color == 'red':
	print("You have got 10 points!")
elif alien_color == 'yellow':
	print("You have got 15 points!")

favorite_fruits = ['apple','bananas','orange']
if 'bananas' in favorite_fruits: 
	print("You really like bananas!")
