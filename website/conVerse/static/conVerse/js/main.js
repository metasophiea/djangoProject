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

    // create table that the verses will sit in
    table = document.createElement("table");
        element.appendChild(table);
        table.setAttribute('class','mainTable');
        table.setAttribute('cellspacing',0);
        table.setAttribute('cellpadding',0);
    tbody = document.createElement("tbody");
        table.appendChild(tbody);

    // produce and push verses
    for(var a = 0; a < data.length; a++){
        tr = document.createElement("tr");
            tbody.appendChild(tr);
            tr.setAttribute('class','verse');

        td_1 = document.createElement("td");
            tr.appendChild(td_1);
            text = produce_P(data[a].text, 'verse_text');
            td_1.appendChild(text);

        td_2 = document.createElement("td");
            tr.appendChild(td_2);
            td_2.setAttribute('class','verseDetails');
            td_2.appendChild( produce_P( data[a].screenname, 'verse_authorScreenname') );
            td_2.appendChild( produce_P( '('+data[a].username+')', 'verse_authorUsername') );
            td_2.appendChild( produce_P( data[a].position, 'verse_authorPosition') );
    }
}