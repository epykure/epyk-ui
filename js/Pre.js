


function pre(htmlObj, data, options){
    setCss(htmlObj, options, true);
    if (options.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    if(options.showdown){var converter = new showdown.Converter(options.showdown);
      htmlObj.innerHTML = converter.makeHtml(data)} else {htmlObj.innerHTML = data}
}