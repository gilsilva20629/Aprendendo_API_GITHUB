

function validateForm(event){
	event.preventDefault();	// Impede o envio imediato do formulário.
	let form = event.target;

	console.log(form.name);
	console.log(form["name"]);

};

export default validateForm;

//window.document.getElementById("")