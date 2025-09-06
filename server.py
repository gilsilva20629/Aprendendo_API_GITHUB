from flask import Flask, request
from flask_cors import CORS
import communication_database as CDB
import user
import teste

app = Flask(__name__)
CORS(app)  # Isso permite CORS para todas as rotas

'''
Cross-Origin Resource Sharing (CORS) - HTTP | MDN - MDN Web Docs
O padrão Cross-Origin Resource Sharing trabalha adicionando novos cabeçalhos HTTP
que permitem que os servidores descrevam um conjunto de origens que possuem permissão a ler uma informação usando o navegador.
'''


@app.route('/my_endpoint', methods=['GET', 'POST'])
def home():

	# ------------ Recepcao do request----------------
	
	if request.headers["Content-Type"] == "application/x-www-form-urlencoded" :
		name = request.form["name_user"]
		password = request.form["password"]
		op_type = request.form["extra"]

	elif request.headers["Content-Type"] == "text/html; charset=utf-8" :
		name = request.form.get("name_user")
		password = request.form.get("password")
		op_type = request.form.get("extra")

	elif request.headers["Content-Type"] == "application/json" :
		name = request.json.get("name_user")
		password = request.json.get("password")
		op_type = request.json.get("extra")
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
			else:
				resposta = "NOK"

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
			pass
	
	
	# ------------ Resposta --------------------------
	return resposta
	

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 , debug=True)  #
	#app.run(host="127.0.0.1", port=5000 , debug=True)  #