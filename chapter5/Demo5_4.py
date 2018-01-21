request_toppings = ['mushrooms','green peppers','extra cheese']
for request_topping in request_toppings:
	if request_topping == 'green peppers':
		print("Sorry,we are out of our green pappers!")
	else:
		print("Adding "+request_topping+".")
print("\nFinished making your pizza!")


String1 = []
if String1:
	for s in String1:
		print("T")
else:
	print("Are you sure you want a plain pizza?")
	
available_toppings = ['mushrooms','green peppers','olives','pepperoni','pineapple','extra cheese']
request_toppings1 = ['mushrooms','french fries','extra cheese']
for request_topping in request_toppings1:
	if request_topping in available_toppings:
		print("Adding "+request_topping+".")
	else:
		print("Sorry,we dont have "+request_topping+".")
print("\nFinished making your pizza!")
