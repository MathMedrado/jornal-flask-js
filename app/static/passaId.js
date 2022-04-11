function passaId(id){
    fetch("/deletar-prod",{ method: "POST", 
        body: JSON.stringify({ resp: id }),
    
	}).then((_res) => {
		window.location.href = "/";
	});
}