import mysql.connector
import os                #usada para ppegar as variaveis de ambiente.
import hashlib
import user

def start():

	#obtendo variaveis locais
	#HOST = os.getenv("HOST")
	PWD = os.getenv("PWD")
	#print("Ambiente: ", PWD)


	#obtendo variaveis remotas railway.com
	MYSQLHOST = os.getenv("MYSQLHOST")
	MYSQLPORT = os.getenv("MYSQLPORT")
	MYSQLUSER = os.getenv("MYSQLUSER")
	MYSQLPASSWORD = os.getenv("MYSQLPASSWORD")
	MYSQLDATABASE = os.getenv("MYSQLDATABASE")
	DATABASE_URL = os.getenv("DATABASE_URL")

	global mydb, mycursor

	try:
		
		#if HOST != "127.0.0.1" and HOST != "localhost" :	--> não testado.
		if PWD != "/home/susan/Python/github_dir_local/Aprendendo_API_GITHUB":
			mydb = mysql.connector.connect(
				host = os.getenv("MYSQLHOST"),
				port = os.getenv("MYSQLPORT"),
				user = os.getenv("MYSQLUSER"),
				password = os.getenv("MYSQLPASSWORD"),
				database = os.getenv("MYSQLDATABASE")
			)
		else:
			mydb = mysql.connector.connect(
				host = "localhost",
				user = "root",
				password = "Nsg@2024",
				database ="db_teste01"
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
			command = command.split(";")
			print("Comandos limpos: ", command, end="\n")

			for c in command:
				mycursor.execute(c)

		except Exception as err:
			print("command extra falhou!")	

def add_user_test(user, command_x=None):
	start()

	command_extra(command_x)

	sql = "INSERT INTO user(id, name, password, tipo) VALUES(%s, %s, %s)"
	values = (user.id, user.name, user.password, user.tipo)

	#sql = "INSERT INTO user(id, name, password, `tipo`) VALUES(%s, %s, %s, %s)"
	#values = (user.id, user.name, user.password, user.tipo)

	mycursor.execute(sql, values)
	mydb.commit()
	print(mycursor.rowcount, "Record Inserted.")
	exit()

def cadUser(name, password, command_x=None):
	start()
	command_extra(command_x)

	user = User(name, password)
	sql = "INSERT INTO user(id, name, password, tipo) VALUES(%s, %s, %s, %s)"
	values = (user.id, user.name, user.password, user.tipo)

	mycursor.execute(sql, values)
	mydb.commit()
	print(mycursor.rowcount, "Record Inserted")
	exit()

def search_user(name=None, user_id=None, tipo=None, command_x=None):
	start()
	command_extra(command_x)

	n = []
	u = []
	g = []

	if name == None and user_id == None and tipo == None :
		return "Ivalid parameters!"

	else:
		#mycursor.execute(f"SELECT * FROM user WHERE name={name}")
		#results = mycursor.fetchall()

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
	
		
def list_users(command_x=None):
	start()
	command_extra(command_x)
	mycursor.execute("SELECT user_id, name, tipo FROM user")
	results = mycursor.fetchall()
	exit()
	return results

def remove(u_id, command_x=None):
	start()
	command_extra(command_x)
	mycursor.execute(f"DELETE FROM user WHERE user_id={u_id}")
	mydb.commit()
	print(mycursor.rowcount, "Record(s) Deleted.")
	exit()

def login(name, password, command_x=None):
	start()
	command_extra(command_x)

	results = search_user(name)[0]

	for r in results:
		if name in r:

			#gerar hash do password
			#h = hashlib.sha256()
			#h.update(password.encoded())
			#h.hexdigest()

			if password == (r[2])[0:16] :
				exit()
				return True
			else:
				exit()
				return False


