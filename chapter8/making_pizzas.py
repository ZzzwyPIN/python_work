# ~ from Demo8_5 import make_pizza as mp

# ~ make_pizza(16,'pepperoni')
# ~ mp(14,'rushrooms','green peppers','extra cheese')

# ~ import Demo8_5 as D

# ~ D.make_pizza(16,'pepperoni')

from Demo8_5 import *
make_pizza(16,'pepperoni')
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
for key,value in user_profile.items():
	print("\n"+key.title()+": "+value)
