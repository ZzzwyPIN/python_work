# ~ class Dog():
	# ~ """一次模拟小狗的简单尝试。"""
	
	# ~ def __init__(self,name,age):
		# ~ """初始化属性name和age"""
		# ~ self.name = name
		# ~ self.age = age
	
	# ~ def sit(self):
		# ~ print(self.name.title()+" is now sitting!")
	
	# ~ def roll_over(self):
		# ~ """模拟小狗被命令打滚"""
		# ~ print(self.name.title()+" rolled over!")
		
# ~ my_dog = Dog('willie',6)
# ~ my_dog.sit()
# ~ print(my_dog.name)
# ~ your_dog = Dog('znf',3)
# ~ your_dog.roll_over()

class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("This restaurant's name is: "+self.restaurant_name+".")
		print("It's cuisine type is: "+self.cuisine_type+".")
		
	def open_restaurant(self):
		print(self.restaurant_name+" is opening now!")
	
	def increment_number_served(self,number):
		if number >= 0:
			self.number_served += number
		else:
			print("You can't roll back the number!")
		print("We have served "+str(self.number_served)+" people!")
		
# ~ restaurant = Restaurant('磬苑宾馆','hotel')
# ~ restaurant.open_restaurant()
# ~ restaurant.describe_restaurant()
# ~ restaurant.increment_number_served(20)
# ~ restaurant.increment_number_served(12)
