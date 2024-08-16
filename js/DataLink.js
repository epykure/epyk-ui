

function dataLink(htmlObj, data, options){
    setCss(htmlObj, options, true); data = getDataFromTemplate(data, options);
    var b = new Blob([data.value]); htmlObj.href = URL.createObjectURL(b);
    htmlObj.innerHTML = data.text
}