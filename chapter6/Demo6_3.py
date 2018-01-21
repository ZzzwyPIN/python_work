favorite_languages = {
	'jen': 'Python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'Python',
	}
# ~ for key,value in favorite_languages.items():
	# ~ print(key.title() + "'s favorite language is " +
	# ~ value.title() + ".")
# ~ for name in favorite_languages.keys():
	# ~ print(name.title())
# ~ for name in sorted(favorite_languages.keys()):
	# ~ print(name.title()+",thank you for taking the poll.")
# ~ for language in set(favorite_languages.values()):
	# ~ print(language.title())
nameArray = ['zwy','smith','sarah','zne','phil']
for name in favorite_languages.keys():
	if name in nameArray:
		print(name.title()+",thank you!")
	else:
		print(name.title()+",please jion us!")
