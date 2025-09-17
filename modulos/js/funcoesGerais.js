function VMvalidateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	let form = event.target; // 'target' elemento que disparou o evento
	console.log(event, event.target, typeof event.target )
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

export default VMvalidateForm;

//window.document.getElementById("")