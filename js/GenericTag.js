


function genericTag(htmlObj, data, options){
    if (typeof(setCss) == "function"){setCss(htmlObj, options, true)};
    if (typeof(getDataFromTemplate) == "function"){data = getDataFromTemplate(data, options)};
    if (htmlObj){htmlObj.innerHTML = data}
}