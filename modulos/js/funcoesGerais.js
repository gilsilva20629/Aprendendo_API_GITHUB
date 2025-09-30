function feedbackClear(){
	let feedback_user = window.document.getElementById("frm-user");
	feedback_user.textContent = "";
	let feedback_client = window.document.getElementById("frm-client");
	feedback_client.textContent = "";
	let feedback_product = window.document.getElementById("frm-product");
	feedback_product.textContent = "";
}


// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy


function VMvalidateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	feedbackClear();
	let form = event.target; // 'target' elemento que disparou o evento
	console.log("Detalhes do evento: ", event, event.target, typeof event.target );
	let url = "http://127.0.0.1:5000/cadastro";

	if (form.name == "form-user") {
		const user = form.input["name='user'"].value;
		const password = form.input["name='password'"].value;
		const type = form.input["name='type'"].value;
		const op_type = form.input["name='op_type'"].value;


		fetch(url, {
			method: "POST",
			header: {
				"Acess-Control-Allow-Origin": "no-cors",
				"Content-Type": "aplication/json"
			},
			body: JSON.stringify({
				"arg1": user,
				"arg2": password,
				"arg3": type,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				window.alert(response.text());
				feedback_user.innerHTML = "O cadastro falhou tente novamente!";
				throw new Error('RESPOSTA_REDE: Falhou.');
			}else{
				feedback_user.innerHTML = "O cadastro realizado com sucesso.";
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				// Fazer algo!
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	} else if (form.name == "form-client") {
		const name = form.input["name='nome'"].value;
		const address = form.input["name='address'"].value;
		const contact = form.input["name='contact'"].value;
		const op_type = form.input["name='op_type'"].value;


		fetch(url, {
			method: "POST",
			header: {
				"Acess-Control-Allow-Origin": "no-cors",
				"Content-Type": "aplication/json"
			},
			body: JSON.stringify({
				"arg1": name,
				"arg2": address,
				"arg3": contact,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				window.alert(response.text());
				feedback_client.innerHTML = "O cadastro falhou tente novamente!"
				throw new Error('RESPOSTA_REDE: Falhou.');
			}else{
				feedback_client.innerHTML = "O cadastro realizado com sucesso."
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				// Fazer algo!
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	}else if(form.name == "form-product"){
		const product_name = form.input["name='product-name'"].value;
		const address = form.input["name='category'"].value;
		const contact = form.input["name='unit'"].value;
		const op_type = form.input["name='op_type'"].value;


		fetch(url, {
			method: "POST",
			header: {
				"Acess-Control-Allow-Origin": "no-cors",
				"Content-Type": "aplication/json"
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
				window.alert(response.text());
				feedback_product.innerHTML = "O cadastro falhou tente novamente!"
				throw new Error('RESPOSTA_REDE: Falhou.');
			}else{
				feedback_product.innerHTML = "O cadastro realizado com sucesso."
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				// Fazer algo!
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
		*/

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
	};
}; 



// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy
// javascript import falha caregado pelo protocolo file:// devido a CORS policy


function validateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	feedbackClear();
	let form = event.target; // 'target' elemento que disparou o evento
	console.log("Detalhes do evento: ", event, event.target, typeof event.target );
	let url = "http://127.0.0.1:5000/cadastro";

	if (form.name == "form-user") {
		const user = form.input["name='user'"].value;
		const password = form.input["name='password'"].value;
		const type = form.input["name='type'"].value;
		const op_type = form.input["name='op_type'"].value;


		fetch(url, {
			method: "POST",
			header: {
				"Acess-Control-Allow-Origin": "no-cors",
				"Content-Type": "aplication/json"
			},
			body: JSON.stringify({
				"arg1": user,
				"arg2": password,
				"arg3": type,
				"arg4": op_type
			})
		})
		.then(response => {
			if(!response.ok){
				window.alert(response.text());
				feedback_user.innerHTML = "O cadastro falhou tente novamente!";
				throw new Error('RESPOSTA_REDE: Falhou.');
			}else{
				feedback_user.innerHTML = "O cadastro realizado com sucesso.";
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				// Fazer algo!
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	} else if (form.name == "form-client") {
		const name = form.input["name='nome'"].value;
		const address = form.input["name='address'"].value;
		const contact = form.input["name='contact'"].value;
		const op_type = form.input["name='op_type'"].value;


		fetch(url, {
			method: "POST",
			header: {
				"Acess-Control-Allow-Origin": "no-cors",
				"Content-Type": "aplication/json"
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
				window.alert(response.text());
				feedback_client.innerHTML = "O cadastro falhou tente novamente!"
				throw new Error('RESPOSTA_REDE: Falhou.');
			}else{
				feedback_client.innerHTML = "O cadastro realizado com sucesso."
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				// Fazer algo!
			}
		})
		.catch(error => {
			console.log("Log de erro: ", error, typeof error);
		});

	}else if(form.name == "form-product"){
		const product_name = form.input["name='product-name'"].value;
		const address = form.input["name='category'"].value;
		const contact = form.input["name='unit'"].value;
		const op_type = form.input["name='op_type'"].value;


		fetch(url, {
			method: "POST",
			header: {
				"Acess-Control-Allow-Origin": "no-cors",
				"Content-Type": "aplication/json"
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
				window.alert(response.text());
				feedback_product.innerHTML = "O cadastro falhou tente novamente!"
				throw new Error('RESPOSTA_REDE: Falhou.');
			}else{
				feedback_product.innerHTML = "O cadastro realizado com sucesso."
			}

			return response.text();  // ou response.json() se a resposta for JSON.
		})
		.then(dados => {
			window.alert(dados);
			if(dados == "OK"){
				// Fazer algo!
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
		*/

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
	};
}; 


// habilita para import via script type="module.
export default validateForm;
export default VMvalidateForm;
export default feedbackClear;
