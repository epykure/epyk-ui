

function highlights(htmlObj, data, options){
    data = getDataFromTemplate(data, options);
    if(typeof data === 'undefined'){htmlObj.remove()}
      else {
        if(options.reset){htmlObj.querySelector('div[name=content]').innerHTML = ""};
        if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data)}
        htmlObj.querySelector('div[name=content]').innerHTML = data}
}