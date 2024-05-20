
function label(htmlObj, data, options){
    if (options?.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options?.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options?.template !== 'undefined' && data){data = options.template(data)}
    if (typeof data !== "undefined"){
      if(options.showdown){var converter = new showdown.Converter(options.showdown);
        var content = converter.makeHtml(data).replace(/<\/?p[^>]*>/ig, '')} else {var content = data};
      if(options._children > 0){
        htmlObj.insertAdjacentHTML('beforeend', '<div style="display:inline-block;vertical-align:middle">'+ content +'</div>')}
      else{htmlObj.innerHTML = content};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}}
}