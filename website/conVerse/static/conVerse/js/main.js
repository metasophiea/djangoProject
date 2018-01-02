document.write('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>');

function produce_P(innerHTML, classString){
    p = document.createElement("p");
    p.setAttribute('class',classString);
    p.innerHTML += innerHTML
    return p;
}

function dealWithData(data, element){
    // sort data by their 'position's
    data.sort(function (a, b) { return a.position - b.position; });
    data.sort();

    // push verses
    for(var a = 0; a < data.length; a++){
        text = produce_P(data[a].text, 'verse_text');
        author_screenname = produce_P(data[a].screenname, 'verse_authorScreenname');
        author_username = produce_P('('+data[a].username+')', 'verse_authorUsername');
        position = produce_P(data[a].position, 'verse_position');

        div = document.createElement("div");
            div.setAttribute('class','verse');
            div.appendChild(text);
            div.appendChild(position);
            div.appendChild(author_screenname);
            div.appendChild(author_username);
            element.appendChild(div);
    }
}