# ~ alien_0 = {'color':'green','points':5}
# ~ print(alien_0)
# ~ print(alien_0['color'])
# ~ print("You just earned "+str(alien_0['points'])+" points!")
# ~ alien_0['x_position'] = 0
# ~ alien_0['y_position'] = 25
# ~ print(alien_0)

# ~ alien_0 = {}
# ~ alien_0['color'] = 'green'
# ~ print(alien_0['color'])
# ~ alien_0['color'] = 'yellow'
# ~ print(alien_0)

alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
print("Original x_position:" + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: "+ str(alien_0['x_position']))
print(alien_0)
del alien_0['speed']
print(alien_0)

favorite_languages = {
	'jen': 'Python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print(favorite_languages)
print("Sarah's favorite language is "+
	favorite_languages['sarah'].title()+
	".")
