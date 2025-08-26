import mysql.connector
import os

def start():

	MYSQLHOST = os.getenv("MYSQLHOST")
	MYSQLPORT = os.getenv("MYSQLPORT")
	MYSQLUSER = os.getenv("MYSQLUSER")
	MYSQLPASSWORD = os.getenv("MYSQLPASSWORD")
	MYSQLDATABASE = os.getenv("MYSQLDATABASE")
	DATABASE_URL = os.getenv("DATABASE_URL")

	global mydb, mycursor

	try:
		mydb = mysql.connector.connect(
			host = os.getenv("MYSQLHOST"),
			#host = "localhost",
			port = os.getenv("MYSQLPORT"),
			user = os.getenv("MYSQLUSER"),
			#user = "root"
			password = os.getenv("MYSQLPASSWORD"),
			#password = "Nsg@2024"
			database = os.getenv("MYSQLDATABASE")
			)
	except Exception as err:
		print(err, type(err))
		return "Erro: Não foi possivel conectar ao database!"
	
	mycursor = mydb.cursor()

	return "Connected in BD..."

	'''
	mycursor.execute("SHOW TABLES")
	mycursor.execute("DROP TABLE usuario")
	results = mycursor.fetchall()
	print(results)
	
	# Exibir os resultados
	print(":----- via 'for' -----:")
	for linha in results:
		print(linha)

	# Fechar a conexão
	mycursor.close()
	mydb.close()

	#mydb.commit()
	'''


def quit():
	mycursor.close()
	mydb.close()

def exit():
	mycursor.close()
	mydb.close()

def command_extra(command=None):
	if command!=None :

		command = command.replace("\\", "")
		command = command.replace("\t", "")
		command = command.replace("\n", "")

		try:
			print("Testando split: ", command.split(";"), end="\n")

			for c in command.split(";"):
				mycursor.execute(c)

		except Exception as err:
			print("command extra falhou!")
			

def add_user(user, command_x=None):
	start()

	command_extra(command_x)

	sql = "INSERT INTO user(id, name, password, tipo) VALUES(%s, %s, %s, %s)"
	values = (user.id, user.name, user.password, user.tipo)

	#sql = "INSERT INTO user(id, name, password, `tipo`) VALUES(%s, %s, %s, %s)"
	#values = (user.id, user.name, user.password, user.tipo)

	mycursor.execute(sql, values)
	mydb.commit()
	print(mycursor.rowcount, "Record Inserted.")
	exit()

'''
###########################################
def search_user(name=None, user_id=None, tipo=None, command_extra=None):
	start()
	command_extra(command_extra)

	n = []
	u = []
	g = []

	if name == None and user_id == None and tipo == None :
		return "Ivalid parameters!"

	else:
		mycursor.execute("SELECT * FROM user")
		results = mycursor.fetchall()

		#print(results, type(results))

		#for i in results:
		#	print(i)

		#for i in mycursor:, type(results
		#	print(i[1], i[4], i[3], type(i[1]), type(i[4]), type(i[3]))

		
		if name is not None:
			#print(f"name: __________ __________ __________ {name}")
			for i in results:
				if name in i[1] :
					#print(i)
					n.append(i)
		
		if user_id is not None:
			#print(f"user_id: __________ __________ __________ {user_id}")
			for i in results:
				if user_id == i[4] :
					#print(i)
					u.append(i)
		
		if tipo is not None:
			#print(f"tipo: __________ __________ __________ {tipo}")
			for i in results:
				if tipo == i[3] :
					#print(i)
					g.append(i)	
	exit()
	return n, u, g	


		
def list_users(command_extra=None):
	start()
	command_extra(command_extra)
	mycursor.execute("SELECT user_id, name, `tipo` FROM user")
	results = mycursor.fetchall()
	exit()
	return results

def remove(u_id, command_extra=None):
	start()
	command_extra(command_extra)
	mycursor.execute(f"DELETE FROM user WHERE user_id={u_id}")
	mydb.commit()
	print(mycursor.rowcount, "Record(s) Deleted.")
	exit()

def login(name, password, command_extra=None):
	start()
	command_extra(command_extra)
	flag = True
	results = search_user(name)[0]

	for r in results:
		if name in r:
			if password == (r[2])[0:16] :
				exit()
				return flag
			else:
				flag = False
				exit()
				return flag
		
'''