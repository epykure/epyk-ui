

function lastUpdated(htmlObj, data, options){
    if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data)}
    if(options._children > 0){htmlObj.appendChild(document.createTextNode(data))}
    else{if(options.icon){htmlObj.innerHTML = data + '&nbsp;&nbsp;<i class="'+ options.icon +'"></i>'} else {htmlObj.innerHTML = data}};
    htmlObj.setAttribute('data-value', data)
}