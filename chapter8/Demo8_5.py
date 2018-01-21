def make_pizza(size, *toppings):
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)

# ~ make_pizza(16, 'pepperoni')
# ~ make_pizza(12, 'mushrooms','green peppers','extra cheese')

def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
# ~ user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
# ~ print(user_profile)
