

function validateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	let form = event.target; // 'target' elemento que disparou o evento

	/*
	A TRY declaração define um bloco de código a ser executado (para tentar).

	A CATCH declaração define um bloco de código para lidar com qualquer erro.

	A FINALLY instrução define um bloco de código a ser executado independentemente do resultado.

	A THROW declaração define um erro personalizado.
	*/

	try{
		console.log(form.parameters.name);
		console.log(form.name);
		console.log(form["name"]);
	}
	catch(err){
		console.log(err.message)
	}

};

export default validateForm;

//window.document.getElementById("")