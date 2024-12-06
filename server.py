from flask import Flask, request
from flask_cors import CORS
import communication_database as CDB

app = Flask(__name__)
CORS(app)  # Isso permite CORS para todas as rotas

'''
Cross-Origin Resource Sharing (CORS) - HTTP | MDN - MDN Web Docs
O padrão Cross-Origin Resource Sharing trabalha adicionando novos cabeçalhos HTTP
que permitem que os servidores descrevam um conjunto de origens que possuem permissão a ler uma informação usando o navegador.
'''


@app.route('/my_endpoint', methods=['POST'])
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
		response = "content/media type do not supported: "+request.headers["Content-Type"]
		print(response)

	# ------------ Executar Testes --------------------

	'''
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
	'''

	# ------------ Executar operacoes --------------------
	
	if op_type == "1" :	#login
		response = "OK"+"Hello, Flask on Railway!"
		print(name)
		print(password)
		print(op_type)

		print("???")
		CDB.start()
		print("???")


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

	
	# ------------ Resposta --------------------------
	return response
	

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 , debug=True)
