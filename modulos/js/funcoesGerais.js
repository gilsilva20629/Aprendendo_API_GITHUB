export function feedbackClear(){
	let feedback_user = window.document.getElementById("frm-user");
	let feedback_client = window.document.getElementById("frm-client");
	let feedback_product = window.document.getElementById("frm-product");
	feedback_user.textContent = "";
	feedback_client.textContent = "";
	feedback_product.textContent = "";
}

// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy


function validateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	feedbackClear();
	let form = event.target; // 'target' elemento que disparou o evento
	//console.log("Detalhes do evento: ", event, event.target);


	const url = "https://aprendendoapigithub-production.up.railway.app/cadastro.html";
	if (window.location.hostname == "localhost" || window.location.hostname == "127.0.0.1"){
		url = "http://127.0.0.1:5000/cadastro.html";
	}	

	let feedback_user = window.document.getElementById("frm-user");
	let feedback_client = window.document.getElementById("frm-client");
	let feedback_product = window.document.getElementById("frm-product");

	if (form.name == "form-user") {
		const user = window.document.getElementById("user").value;
		const password = window.document.getElementById("password").value;
		const tipo = window.document.getElementById("type").value;
		const op_type = window.document.getElementById("op_type_user").value;

		fetch(url, {
			method: "POST",
			headers: {
				"Access-Control-Allow-Origin": "no-cors",
				// "Access-Control-Allow-Origin": "*", // Use '*' para permitir todas as origens, se necessário
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"arg1": user,
				"arg2": password,
				"arg3": tipo,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				throw new Error('Netwok: A resposta da rede não foi boa.');
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				feedback_user.innerHTML = "O cadastro realizado com sucesso.";				
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	} else if (form.name == "form-client") {
		const name = window.document.getElementById("client").value;
		const address = window.document.getElementById("address").value;
		const contact = window.document.getElementById("contact").value;
		const op_type = window.document.getElementById("op_type_client").value;

		fetch(url, {
			method: "POST",
			headers: {
				"Access-Control-Allow-Origin": "no-cors",
        		// "Access-Control-Allow-Origin": "*", // Use '*' para permitir todas as origens, se necessário
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"arg1": name,
				"arg2": address,
				"arg3":contact,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				throw new Error('Netwok: A resposta da rede não foi boa.');
			}
			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				feedback_client.innerHTML = "O cadastro realizado com sucesso.";
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	}else if(form.name == "form-product"){
		const product_name = window.document.getElementById("product_name").value;
		const category = window.document.getElementById("category").value;
		const unit = window.document.getElementById("unit").value;
		const op_type = window.document.getElementById("op_type_product").value;

		fetch(url, {
			method: "POST",
			headers: {
				"Access-Control-Allow-Origin": "no-cors",
				// "Access-Control-Allow-Origin": "*", // Use '*' para permitir todas as origens, se necessário
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				"arg1": product_name,
				"arg2": category,
				"arg3": unit,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){ 
				throw new Error('Netwok: A resposta da rede não foi boa.');
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				feedback_product.innerHTML = "O cadastro realizado com sucesso.";
				
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	}else{

		/*
		A TRY declaração define um bloco de código a ser executado (para tentar).

		A CATCH declaração define um bloco de código para lidar com qualquer erro.

		A FINALLY instrução define um bloco de código a ser executado independentemente do resultado.

		A THROW declaração define um erro personalizado.
		

		try{	
			console.log("Nome do formulario", form.name);
		}
		catch(err){
			console.log(err.message); 	// A CATCH declaração define um bloco de código para lidar com qualquer erro.
		}
		finally{
			// A FINALLY instrução define um bloco de código a ser executado independentemente do resultado.

			// throw new Error("Esse e um erro que eu criei agora")
		}
		*/
	};
}


// declaracao "export" habilita para import via <script type="module>.
//você não pode usar a palavra-chave default mais de uma vez em um único módulo.
export default validateForm;

