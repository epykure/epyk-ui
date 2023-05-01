

function fieldset(htmlObj, data, options){
    if (options.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    htmlObj.firstChild.innerHTML = data;
      if(typeof options.css !== 'undefined'){Object.keys(options.css).forEach(function(key){htmlObj.firstChild.style[key] = options.css[key]})}

}