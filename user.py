import random
import hashlib
import uuid

def genarate_info_user():
	symbol = "abcdefghijklmnopqrstuvxywz0123456789_!@#$%&" # [0:25] [26:35] [36:42]
	groups = ["normal", "manager", "admin"]
	pesos = [0.9,0.08,0.02]
	name = ""
	password = ""
	group = random.choices(groups, weights=pesos, k=1)[0]

	for i in range(16):
		#generate name
		for j in random.choice(symbol[0:25]):
			name += j

		#generate password
		for j in random.choice(symbol):
			password += j
	
	
	h = hashlib.sha256()
	h.update(password.encode())
	password_hash = password + "." + h.hexdigest()
	

	return name, password_hash, group

'''
print(genarate_info_user())
name, password, group = genarate_info_user()
print(name)
print(password)
print(group)
'''


class User():

	def __init__(self, name, password, group):
		#self.id = random.randint(1,10000)
		self.id = str(uuid.uuid4())
		self.name = name
		self.password = password
		self.group = group

		
	
