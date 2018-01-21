# ~ import Demo9_2 as D9
from Demo9_2 import Car
class ElecticCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()
	# ~ def describe_battery(self):
		# ~ print("This car has a "+str(self.battery_size)+"-kWh battery.")

class Battery():
	def __init__(self,battery_size=70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size
	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-kWh battery.")
	
my_tesla = ElecticCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


