function dealWithData(data){
	for(var a = 0; a < data.length; a++){
		p = document.createElement("p");
		p.innerHTML += data[a].text;
		p.innerHTML += "<br/>";
		p.innerHTML += "- " + data[a].authorName;
		document.body.appendChild(p);
	}
}