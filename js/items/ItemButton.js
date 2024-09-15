

function itemButton(htmlObj, data, options){
    if (typeof data !== "object"){data = {text: data}};
    var item = document.createElement("DIV"); item.classList.add("html-item-button");
    var text = document.createElement("div"); text.classList.add("html-item-button-text");
    text.setAttribute('name', 'value'); text.setAttribute('data-valid', false);
    text.innerHTML = data.text ; var button = document.createElement("button");
    button.classList.add("html-item-button-button");
    button.innerHTML = data.button; item.appendChild(text); item.appendChild(button);
    if(typeof data.tooltip !=='undefined'){ button.setAttribute('title', data.tooltip)}
    if(typeof data.event !=='undefined'){
      button.addEventListener("click", function() {
        var xhttp = new XMLHttpRequest();
        var event_data = {}; var event_method = 'POST';
        if(typeof data.event.data !== 'undefined'){ event_data = data.event.data}
        if(typeof data.event.method !== 'undefined'){ event_method = data.event.method}
        xhttp.open(event_method, data.event.url, true);
        xhttp.send(JSON.stringify(event_data));
      });
    };
   htmlObj.appendChild(item);
}