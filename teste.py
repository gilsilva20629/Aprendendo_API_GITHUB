def teste_subprocess():
	import subprocess
	#import sys
	#print(sys.path, end="\n\n")

	diretorio_alvo = "/home/susan/Python/mini_projetos/loja/login_auth"
	comando = ["python3","-m","login_auth.server_app"]
	output_terminal = subprocess.run(comando, cwd=diretorio_alvo, capture_output=True, text=True) 


	#print(output_terminal, type(output_terminal))
	print("Codigo de retorno:", output_terminal.returncode)
	print("stdout:", output_terminal.stdout)
	print("stderr:", output_terminal.stderr)


def teste_user():
	from cad_user import user
	from database import communication_database as CDB
	
	for i in range(10):
		name, password, group = user.genarate_info_user()

		u = user.User(name, password, group)

		CDB.add_user(u)
		

	#CDB.search_user("wkwllo", 89, "admin")

	#CDB.remove(71)

	#print(user.list())


def teste_request():
	from flask import Flask, request, redirect, url_for

	#: Os dados do formulário (para requisições POST).
	print("_______________________________________________________")
	for i, j in request.form.items():
		print(i, j)

	for x in request.form.values():
	    print("values:", x)

	for z in request.form.keys():
	    print("keys:", z)


	print("--> request.form: ", request.form, end="\n\n")       #: Os dados do formulário (para requisições POST).
	print("--> request.args: ", request.args, end="\n\n")             #: Os parâmetros da query string (para requisições GET).
	print("--> request.method: ", request.method, end="\n\n")         #: O método HTTP usado (GET, POST, etc.).
	print("--> request.url: ", request.url, end="\n\n")               #: A URL completa da requisição.
	print("--> request.headrs: ", request.headers, end="\n\n")        #: Os cabeçalhos da requisição.
	print("--> request.data: ", request.data, end="\n\n")             #: O corpo da requisição (para dados não estruturados).
	#print("--> request.json: ", request.json, end="\n\n")             #: O corpo da requisição, se for JSON.
	print("_______________________________________________________")

	nome = request.form.get('name_user')
	print("server side:", nome, type(nome))
	senha = request.form.get('password')
	print("server side:", senha, type(senha))
	op_type = request.form.get("extra")
	print("server side:", op_type, type(op_type))

	
	#print("fecth status:", request.status_code)
	print("fecth method:", request.method)
	#print("fecth encoding:", request.encoding)
	print("fecth url:", request.url)
	print("fecth args:", request.args)
	print("fecth headers:", request.headers)
	print("fecth data:", request.data)
	print("fecth json:", request.json)
	#print("fecth text:", request.text)
	#print("fecth content:", request.content)
	print("fecth path:", request.path)
	print("fecth form:", request.form)
	#print("fecth raw:", request.raw)

	print(request.json.get('name_user'))
	print(request.json.get('password'))
	print(request.json.get('extra'))

def outhers():
	import user
	import communication_database as CDB

	cmd_x = "DROP TABLE usuario;CREATE TABLE usuario(	\
	id varchar(36),	\
	name varchar(16),	\
	password varchar(81),	\
	user_id int NOT NULL PRIMARY KEY AUTO_INCREMENT \
	);"

	for i in range(10):
		name, password, group = user.genarate_info_user()
		u = user.User(name,password, group)
		response = CDB.add_user(u, cmd_x)
		cmd_x = None


if __name__ == "__main__":
	pass