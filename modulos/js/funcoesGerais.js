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

}   // ; verificar se ponto e virgula faz falta.

export default VMvalidateForm;




function selectedOption(){
//Verifica qual opcao está selecionada em select tag
//Precisa ajustar para receber o select_tag e não a lista de option_tag
	select = window.document.getElementsByTagName("option");
	for (i = 0;  i < select.length ; i++) {
		if(select[i].selected){
			selected_option = select[i].value;
		}
	}
}
