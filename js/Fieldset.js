

function fieldset(htmlObj, data, options){
    data = getDataFromTemplate(data, options);
    htmlObj.firstChild.innerHTML = data;
    setCss(htmlObj.firstChild, options, true);
}