# ~ prompt = "\nTell me something, and I will repeat it back to you:"
# ~ prompt += "\nEnter 'quit' to end the program."
# ~ message = ""
# ~ while message != 'quit':
	# ~ message = input(prompt)
	# ~ if message != 'quit':
		# ~ print(message)
# ~ active = True
# ~ while active:
	# ~ message = input(prompt)
	# ~ if message == 'quit':
		# ~ active = False
	# ~ else:
		# ~ print(message)
# ~ prompt = "\nPlease enter the name of a city you have visit:"
# ~ prompt += "\n(Enter 'quit' when you are finished.)"

# ~ while True:
	# ~ city = input(prompt)
	# ~ if city == 'quit':
		# ~ break
	# ~ else:
		# ~ print("I'd love to go to "+city.title()+"!")
		
# ~ current_number = 0
# ~ while current_number < 10:
	# ~ current_number += 1
	# ~ if current_number % 2 == 0:
		# ~ continue  #会调到循环起始位置。
		
	# ~ print(current_number)	
# ~ x = 1
# ~ while x<5:
	# ~ print(x)

prompt = "How old are you? "
active = True
while active:
	age = input(prompt)
	if age == 'quit':
		# ~ break
		active = False
		continue
	age = int(age)
	if age < 3:
		print("You are free!\n")
	elif age >= 3 and age <=12:
		print("You should pay 10$!\n")
	elif age > 12:
		print("You should pay 15$!\n")

	
	
	
	
	
	
	
	
	
	
