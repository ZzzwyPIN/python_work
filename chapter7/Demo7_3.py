# ~ responses = {}
# ~ flag = True
# ~ while flag:
	# ~ name = input("\nWhat is your name? ")
	# ~ response = input("Which mountain would you like to climb someday? ")
	
	# ~ responses[name] = response
	# ~ repeat = input("Would you like to let another person respond? (yes/no) ")
	# ~ if repeat == 'no':
		# ~ flag = False
# ~ print("\n--- Poll Result ---")
# ~ for name,response in responses.items():
	# ~ print(name.title()+" would like to climb "+response.upper()+".") 
# ~ pets = ['dog','cat','pig','goldfish','cat','fuck']
# ~ print(pets)
# ~ while 'cat' in pets:
	# ~ pets.pop()
# ~ print(pets)
# ~ sandwich_orders = ['asanmingzhi','bsanmingzhi','csanmingzhi','dsanmingzhi']
# ~ finished_sandwiches = []
# ~ while sandwich_orders:
	# ~ x = sandwich_orders.pop()
	# ~ print("I need your "+x.title()+"sandwich!")
	# ~ finished_sandwiches.append(x)
# ~ for y in finished_sandwiches:
	# ~ print("Give you "+y.title()+" sandwich!")
Holiday_Poll = {}
flag = True
print("We have a poll about dream holiday place.")
while flag:
	name = input("What's your name? ")
	place = input("What's your dream holiday place? ")
	Holiday_Poll[name] = place
	
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		flag = False
print("\n--- Poll Result ---")
for name,place in Holiday_Poll.items():
	print(name.title()+"'s dream holiday place is "+place+".")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
