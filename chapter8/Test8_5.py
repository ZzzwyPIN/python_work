def make_car(manufacturer,model,**other_infos):
	car_information = {}
	car_information['manufacturer_name'] = manufacturer
	car_information['model_name'] = model
	for key,value in other_infos.items():
		car_information[key] = value
	return car_information

car = make_car('subaru','outback',color='blue',tow_pack=True)
print(car)

