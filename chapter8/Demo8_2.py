def describe_pet(animal_type,pet_name):
	"""显示宠物信息"""
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet('willie','dog')

describe_pet(pet_name='harry',animal_type='hamster')

def describe_pet1(pet_name,animal_type='dog'):
	"""显示宠物信息"""
	print("\nI have a "+animal_type+".")
	print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet1('willie')
describe_pet1('willie','pig')
describe_pet1(pet_name='harry',animal_type='hamster')

# ~ def describe_pet2(animal_type='dog',pet_name):#####SyntaxError: non-default argument follows default argument
	# ~ """显示宠物信息"""
	# ~ print("\nI have a "+animal_type+".")
	# ~ print("My "+animal_type+"'s name is "+pet_name.title()+".")
# ~ describe_pet2(pet_name='willie')
# ~ describe_pet()####TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'

def describe_city(name,country='China'):
	print("\n"+name.title()+" is in "+country.upper()+"!")
describe_city('hangzhou')
describe_city('newyork',country='Americ')

	

