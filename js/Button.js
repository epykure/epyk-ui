
function button(htmlObj, data, options){
    data = getDataFromTemplate(data, options);
    htmlObj.setAttribute('data-processing', false); htmlObj.innerHTML = data;
    setCss(htmlObj, options);
}