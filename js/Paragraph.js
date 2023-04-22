

function paragraph(htmlObj, data, options){
    if (options.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    if (typeof options.reset === 'undefined' || options.reset){htmlObj.innerHTML = ''};
      if (typeof data === 'string' || data instanceof String){data = data.split('\\n')};
      if(typeof data !== 'undefined'){
      data.forEach(function(line, i){
        if(options.showdown){
          var converter = new showdown.Converter(options.showdown);
          line = converter.makeHtml(line).replace("<p>", "<p style='margin:0'>")}
        var p = document.createElement('p'); p.style.margin = 0; p.innerHTML = line;
        htmlObj.appendChild(p)})}
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}

}