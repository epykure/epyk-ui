

function highlights(htmlObj, data, options){
    data = getDataFromTemplate(data, options);
    if(typeof data === 'undefined'){htmlObj.remove()}
    else {
        if(options.reset){htmlObj.querySelector('div[name=content]').innerHTML = ""};
        htmlObj.querySelector('div[name=content]').innerHTML = getHtmlData(data, options)
    }
}