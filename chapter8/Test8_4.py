magicans = ['haha','xixi','hehe','hiahia']
def print_magicans_name(names):
	print("\n")
	for name in names:
		print("\t"+name.title())
	
new_magicans = []

def make_great(names):
	while names:
		name ="the Great " + names.pop()
		new_magicans.append(name)

		
# ~ print_magicans_name(magicans)
make_great(magicans[:])
print_magicans_name(magicans)
print_magicans_name(new_magicans)

