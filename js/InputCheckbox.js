

function inputCheckbox(htmlObj, data, options){
    htmlObj.checked = data.value;
    if(typeof data.text !== 'undefined'){htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
    setCss(htmlObj, options);
}