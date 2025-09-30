from flask import Flask, request
from flask_cors import CORS
import com_db as CDB
import user
import teste
import json


app = Flask(__name__)
CORS(app)  # Isso permite CORS para todas as rotas

'''
Cross-Origin Resource Sharing (CORS) - HTTP | MDN - MDN Web Docs
O padrão Cross-Origin Resource Sharing trabalha adicionando novos cabeçalhos HTTP
que permitem que os servidores descrevam um conjunto de origens que possuem permissão a ler uma informação usando o navegador.
'''

@app.route('/login', methods=['POST'])
def home():

	# ------------ Recepcao do request----------------
	'''
	application/x-www-form-urlencoded
	multipart/form-data
	text/plain
	text/html; charset=utf-8
	application/json
	'''

	if request.headers["Content-Type"] == "application/x-www-form-urlencoded" :
		name = request.form["name_user"]
		password = request.form["password"]
		op_type = request.form["op_type"]

	elif request.headers["Content-Type"] == "text/html; charset=utf-8" :
		name = request.form.get("name_user")
		password = request.form.get("password")
		op_type = request.form.get("op_type")

	elif request.headers["Content-Type"] == "application/json" :
		name = request.json.get("name_user")
		password = request.json.get("password")
		op_type = request.json.get("op_type")
	else:
		resposta = "content/media type do not supported: "+request.headers["Content-Type"]
		print(resposta)

	# ------------ Executar Testes --------------------

	#print(request.json)
	#teste.outhers()
	

	''' 
	print(request.method)
	print(request.status_code) 
	print(request.url)
	print(request.encoding)
	print(request.form)
	print(request.args)
	print(request.headers)
	print(request.data)
	print(request.content)
	print(request.json)
	print(request.text)
	print(request.auth)
	print(request.cookies)
	print(request.timeuot)
	print(request.params)
	print(request.body)
	'''

	# ------------ Executar operacoes --------------------
	'''
	if op_type == "1" :	#login
		r = CDB.login()
		if r :
			resposta = "OK"
		else:
			resposta = "NOK"
	elif op_type == "2" :
		pass
	elif op_type == "3" :
		pass
	elif op_type == "4" :
		pass
	elif op_type == "5" :
		pass
	elif op_type == "6" :
		pass
	else:
		pass
	'''
	
	match op_type:

		case "1": #login
			r = CDB.login(name, password)
			if r :
				resposta = "OK"

		case "2":
			pass

		case "3":
			pass

		case "4":
			pass

		case "5":
			pass

		case "6":
			pass

		case "_":
				resposta = "NOK"

	
	
	
	# ------------ Resposta --------------------------
	return resposta

@app.route("/cadastro", methods=['POST'])
def cadastro():

	# ------------ Recepcao do request----------------
	'''
	application/x-www-form-urlencoded
	multipart/form-data
	text/plain
	text/html; charset=utf-8
	application/json
	'''

	if request.headers["Content-Type"] == "application/x-www-form-urlencoded" : # Via formulario
		arg1 = request.form["arg1"]
		arg2 = request.form["arg2"]
		arg3 = request.form["arg3"]
		arg4 = request.form["arg4"]

	elif request.headers["Content-Type"] == "text/html; charset=utf-8" :
		arg1 = request.form.get("arg1")
		arg2 = request.form.get("arg2")
		arg3 = request.form.get("arg3")
		arg4 = request.form.get("arg4")

	elif request.headers["Content-Type"] == "application/json ; charset=utf-8" :
		arg1 = request.json.get("arg1")
		arg2 = request.json.get("arg2")
		arg3 = request.json.get("arg3")
		arg4 = request.json.get("arg4")

	elif request.headers["Content-Type"] == "text/plain; charset=utf-8" :
		arg1 = request.text.get("arg1")
		arg2 = request.text.get("arg2")
		arg3 = request.text.get("arg3")
		arg4 = request.text.get("arg4")

	else:
		resposta = "content/media type do not supported: "+request.headers["Content-Type"]
		print(resposta)

	# ------------ Executar Testes --------------------

	#print(request.json)
	#teste.outhers()
	

	''' 
	print(request.method)
	print(request.status_code) 
	print(request.url)
	print(request.encoding)
	print(request.form)
	print(request.args)
	print(request.headers)
	print(request.data)
	print(request.content)
	print(request.json)
	print(request.text)
	print(request.auth)
	print(request.cookies)
	print(request.timeuot)
	print(request.params)
	print(request.body)
	'''

	# ------------ Executar operacoes --------------------
	'''
	if op_type == "1" :	#login
		r = CDB.login()
		if r :
			resposta = "OK"
		else:
			resposta = "NOK"
	elif op_type == "2" :
		pass
	elif op_type == "3" :
		pass
	elif op_type == "4" :
		pass
	elif op_type == "5" :
		pass
	elif op_type == "6" :
		pass
	else:
		pass
	'''
	
	match op_type:

		case "2.1": #Cadastro de usuario.
			name = arg1
			password = arg2
			tipo =arg3

			r = CDB.cadUser(name, password, tipo)
			if r :
				resposta = "OK"

		case "2.2": # cadastro de cliente.
			name = arg1
			address = arg2
			contact = arg3

			r = CDB.cadClient(name, address, contact)
			if r :
				resposta = "OK"

		case "2.3":
			product_name = arg1
			category = arg2
			unit = arg3

			r = CDB.cadProduct(product_name, category, unit)
			if r :
				resposta = "OK"

		case "_":
				resposta = "NOK"

	return resposta


@app.route("/products", methods=["GET"])
def products():
	with open(file="./img/products.txt", mode="r", encoding="utf-8") as file: 
	# com 'with' abre e fecha o arquivo automaticamente(forma segura).
	
		#return json.dumps(file.read())
		return file.read()
	'''
	file = open("./img/products.html", "r")
	response = file.read()
	file.close()
	return response
	'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 , debug=True)  # listen all ips
	#app.run(host="127.0.0.1", port=5000 , debug=True)  # listen localhost