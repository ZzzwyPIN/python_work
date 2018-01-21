# ~ Tiantian  = {'Dog':'zwy'}
# ~ xiaoxia = {'Cat':'znf'}
# ~ Heizhu = {'Pig':'wanghui'}
# ~ fama = {'mouse':'junzai'}
# ~ pets = [Tiantian,xiaoxia,Heizhu,fama]
# ~ for pet in pets:
	# ~ print(pet)
	# ~ for key,value in pet.items():
		# ~ print("This "+key.title()+" is belong to "+value.title())
# ~ favorite_places  = {
	# ~ 'Zwy':['baihu','hefei','hangzhou'],
	# ~ 'Znf':['huaibei','taiwan','xiamen','yunnan','xizang'],
	# ~ 'Tony':['Japan','tokoy','daban'],
	# ~ 'Wanghui':['bingdao','Australia','yunnan','xizang','tonglin'],
	# ~ }
# ~ for name,lists in favorite_places.items():
	# ~ print("\n"+name+"'s favorite places are:")
	# ~ for place in lists:
		# ~ print("\t"+place.title())

cities = {
	'Hefei':{'country':'China','population':'1000wan','fact':'fffff'},
	'Hongkong':{'country':'China','population':'1000wan','fact':'ddd'},
	'shanghai':{'country':'China','population':'5000wan','fact':'ewee'},
	}
for name,dic in cities.items():
	print("\n\t"+name.title()+":")
	for label,info in dic.items():
		print("\t"+label.upper()+" : "+info.title())
