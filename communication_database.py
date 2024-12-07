import mysql.connector
import os

def start():

	global mydb, DATABASE_URL

	DATABASE_URL = os.getenv("DATABASE_URL")
	print(DATABASE_URL)
	print("MYSQLHOST:", type(os.getenv("MySQL.MYSQLHOST")))
	print("MYSQLPORT:", type(os.getenv("MySQL.MYSQLPORT")))
	print("MYSQLUSER:", type(os.getenv("MySQL.MYSQLUSER")))
	print("MYSQLPASSWORD:", type(os.getenv("MySQL.MYSQLPASSWORD")))
	print("MySQLDATABASE:", type(os.getenv("MySQL.MySQLDATABASE")))


	#mydb = mysql.connector.connect(DATABASE_URL)
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
		return "erro: deu merda!"
	

	global mycursor

	mycursor = mydb.cursor()
	mycursor.execute("SHOW TABLES")
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


	return "OK"+" Hello, Flask on Railway!"












































'''
#######################################################################################
def add_user(user):
	start()

	sql = "INSERT INTO user(id, name, password, `group`) VALUES(%s, %s, %s, %s)"
	values = (user.id, user.name, user.password, user.group)

	mycursor.execute(sql, values)
	mydb.commit()
	print(mycursor.rowcount, "Record Inserted.")


def search_user(name=None, user_id=None, group=None):
	start()

	n = []
	u = []
	g = []

	if name == None and user_id == None and group == None :
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
		
		if group is not None:
			#print(f"group: __________ __________ __________ {group}")
			for i in results:
				if group == i[3] :
					#print(i)
					g.append(i)	
	
	return n, u, g	


		
def list_users():
	start()
	mycursor.execute("SELECT user_id, name, `group` FROM user")
	results = mycursor.fetchall()
	return results

def remove(u_id):
	start()
	mycursor.execute(f"DELETE FROM user WHERE user_id={u_id}")
	mydb.commit()
	print(mycursor.rowcount, "Record(s) Deleted.")

def login(name, password):
	start()
	flag = True
	results = search_user(name)[0]

	for r in results:
		if name in r:
			if password == (r[2])[0:16] :
				return flag
			else:
				flag = False
				return flag
		
'''