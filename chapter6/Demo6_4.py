# ~ alien_0 = {'color':'green', 'points':5}
# ~ alien_1 = {'color':'yellow', 'points':10}
# ~ alien_2 = {'color':'red', 'points':15}
# ~ aliens = [alien_0,alien_1,alien_2]
# ~ for alien in aliens:
	# ~ print(alien)

# ~ aliens = []
# ~ for alien_number in range(30):
	# ~ new_alien = {'color':'green', 'point':5, 'speed':'slow'}
	# ~ aliens.append(new_alien)
# ~ for alien in aliens[:5]:
	# ~ print(alien)
# ~ print("...")

# ~ print("Total number of aliens: "+str(len(aliens)))

# ~ for alien in aliens[:3]:
	# ~ if alien['color'] == 'green':
		# ~ alien['color'] = 'yellow'
		# ~ alien['speed'] = 'medium'
		# ~ alien['points'] = 10
		
# ~ for alien in aliens[:5]:
	# ~ print(alien)
# ~ print("...")

# ~ print("Total number of aliens: "+str(len(aliens)))
# ~ favorite_languages = {
	# ~ 'jen': ['python','C'],
	# ~ 'sarah': ['c'],
	# ~ 'edward': ['ruby','go'],
	# ~ 'phil': ['python','haskell'],
	# ~ }
# ~ for name,languages in favorite_languages.items():
	# ~ if len(languages)>1:
		# ~ print("\n"+name.title()+"'s favorite languages are:")
		# ~ for language in languages:
			# ~ print("\t"+language.title())
	# ~ else:
		# ~ print("\n"+name.title()+"'s favorite languages is:\n\t"+languages[0].title())

users = {
	'aeinstein':{
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},
	
	'murie':{
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},
	}
for usename,userinfo in users.items():
	print("\nUsername: "+usename)
	full_name = userinfo['first']+" "+userinfo['last']
	location = userinfo['location']
	
	print("\tFull name: "+full_name.title())
	print("\tLocation: "+location.title())	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

