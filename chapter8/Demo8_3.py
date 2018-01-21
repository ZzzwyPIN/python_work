# ~ def get_formatted_name(first_name,last_name,middle_name=''):
	# ~ if middle_name:
		# ~ full_name = first_name+' '+middle_name+' '+last_name
	# ~ else:
		# ~ full_name = first_name+' '+last_name
	# ~ return full_name.title()

# ~ musician = get_formatted_name('jimi','hendrix')
# ~ print(musician)
# ~ musician = get_formatted_name('jimi','hendrix','lee')
# ~ print(musician)

# ~ def build_person(first_name,last_name,age=''):
	# ~ person = {'first':first_name, 'last':last_name}
	# ~ if age:
		# ~ person['age'] = age
	# ~ return person

# ~ musician = build_person('jimi','hedrix',age = 27)
# ~ print(musician)

# ~ while True:
	# ~ print("\nPlease tell me your name:")
	# ~ print("(enter 'q' at any time to quit)")
	
	# ~ f_name = input("First name: ")
	# ~ if f_name == 'q':
		# ~ break
	
	# ~ l_name = input("Last name: ")
	# ~ if l_name == 'q':
		# ~ break
	
	# ~ formatted_name = get_formatted_name(f_name,l_name)
	# ~ print("\nHello, "+formatted_name+"!")
	
def make_album(singer,name,number=''):
	album = {'Singer':singer, 'album_name':name}
	if number:
		album['number'] = number
	return album
# ~ album_info = make_album('zhouwenyue',"xingqiuzhiguang",10)
# ~ print(album_info)
		
active = True
while active:
	print("You can enter q to quit at any time.\n")
	singer_name = input("Please tell me a singer's name: ")	
	if singer_name == 'q':
		break
	
	album_name = input("Please tell me the album name: ")
	if album_name == 'q':
		break
	album_info = make_album(singer_name,album_name)
	print(album_info)
	
	
	
	
