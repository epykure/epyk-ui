

function paragraph(htmlObj, data, options){
    data = getDataFromTemplate(data, options); setCss(htmlObj, options, true);
    if (typeof options.reset === 'undefined' || options.reset){htmlObj.innerHTML = ''};
    if (typeof data === 'string' || data instanceof String){data = data.split('\\n')};
    if(typeof data !== 'undefined'){
      data.forEach(function(line, i){
        if(options.showdown){
          var converter = new showdown.Converter(options.showdown);
          line = converter.makeHtml(line).replace("<p>", "<p style='margin:0'>")}
        var p = document.createElement('p'); p.style.margin = 0; p.innerHTML = line;
        htmlObj.appendChild(p)})
    }
}