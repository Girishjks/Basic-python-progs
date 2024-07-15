data = 50
try: 
	data = data/0
except ZeroDivisionError: 
	print('Cannot divide by 0 ', end = '') 
else: 
	print('Division successful ', end = '') 

try: 
	data = data/5
except: 
	print('Inside except block ', end = '') 
else: 
	print('GFG', end = '') 
