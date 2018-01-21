# ~ from Demo9_1 import Restaurant
# ~ class IceCreamStand(Restaurant ):
	# ~ def __init__(self,restaurant_name,cuisine_type):
		# ~ super().__init__(restaurant_name,cuisine_type)
		# ~ self.flavors = []
	
	# ~ def set_flavor_list(self,*flists):
		# ~ for flist in flists:
			# ~ self.flavors.append(flist)
	
	# ~ def show_flavors(self):
		# ~ print("The flavors lists are: ")
		# ~ print(self.flavors)

# ~ my_IceCream = IceCreamStand('qingyuan','IceCream store')
# ~ my_IceCream.set_flavor_list('qiaokeli','xiangcao','caomei')
# ~ my_IceCream.show_flavors()
# ~ from collections import OrderedDict

# ~ favorite_languages = OrderedDict()

# ~ favorite_languages['edward'] = 'ruby'
# ~ favorite_languages['jen'] = 'Python'
# ~ favorite_languages['phli'] = 'java'
# ~ favorite_languages['sarach'] = 'c'


# ~ for name,language in favorite_languages.items():
	# ~ print(name.title()+"'s favorite language is "+
		# ~ language.title()+".")

from random import randint
class Die():
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		print("\t"+str(randint(1,self.sides)))
		
# ~ my_die_6 = Die()
# ~ for num in range(1,7):
	# ~ my_die_6.roll_die() 

my_die_10 = Die(10)
for num in range(1,11):
	my_die_10.roll_die()



















