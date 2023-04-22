

function highlights(htmlObj, data, options){
    if (options.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    if(typeof data === 'undefined'){htmlObj.remove()}
      else {
        if(options.reset){htmlObj.querySelector('div[name=content]').innerHTML = ""};
        if(options.showdown){var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data)}
        htmlObj.querySelector('div[name=content]').innerHTML = data}
}