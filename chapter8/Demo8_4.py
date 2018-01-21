# ~ def greet_users(names):
	# ~ for name in names:
		# ~ msg = "Hello, "+name.title()+"!"
		# ~ print(msg)

# ~ usename = ['haha','heihei','xixi']
# ~ greet_users(usename)
def print_models(unprint_designs,completed_models):
	"""模拟打印每个设计，直到没有未打印设计为止。
	打印每个设计后，都将移到列表completed_models中"""
	
	while unprint_designs:
		current_design = unprint_designs.pop()
		print("Print model: "+current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""显示所有打印好的模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
