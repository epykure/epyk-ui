
function blocktext(htmlObj, data, options){
    htmlObj.firstElementChild.innerHTML = data.title; htmlObj.lastElementChild.innerHTML = ""; let content;
    if (typeof data.text === 'string' || data.text instanceof String){
        content = data.text.split("\\n")} else {content = data.text};
    if (content){
        content.forEach(function(line){htmlObj.lastElementChild.append('<p class="py_csstext">'+ line +'</a>')})};
    if(options.showdown){var converter = new showdown.Converter(options.showdown); data.text = converter.makeHtml(data.text)}
    htmlObj.lastElementChild.innerHTML = data.text || "";
    if (data.color != undefined) {htmlObj.lastElementChild.style.color = data.color};
    if(typeof data.button != 'undefined'){
        htmlObj.querySelector("a").innerHTML = data.button.text; htmlObj.querySelector("a").setAttribute('href', data.button.url)}
}