class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading)+" miles on it.")
	
	def updat_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back the odometer!")
# ~ my_new_car = Car('audi','a4','2016')
# ~ print(my_new_car.get_descriptive_name())
# ~ my_new_car.read_odometer()
# ~ my_new_car.odometer_reading = 23
# ~ my_new_car.read_odometer()
# ~ my_new_car.updat_odometer(80)
# ~ my_new_car.read_odometer()
# ~ my_new_car.increment_odometer(100)
# ~ my_new_car.read_odometer()
# ~ my_new_car.updat_odometer(38)
# ~ my_new_car.increment_odometer(-1)
