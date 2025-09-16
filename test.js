

function validateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	let form = event.target; // 'target' elemento que disparou o evento

	console.log(form.parameters.name);
	console.log(form.name);
	console.log(form["name"]);

};

export default validateForm;

//window.document.getElementById("")