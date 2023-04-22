

function text(htmlObj, data, options){
    if (options.templateMode == 'loading'){data = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
    var content = data;
      if(options && options.reset){htmlObj.innerHTML = ""};
      if(data !== ''){
        if(options && options.showdown){
          var converter = new showdown.Converter(options.showdown); content = converter.makeHtml(data)}
        if(options && (options.maxlength != undefined) && (data.length > options.maxlength)){
          content = data.slice(0, options.maxlength);
          if(options.markdown){htmlObj.innerHTML = content +"..."} else {htmlObj.innerHTML = content +"..."};
          htmlObj.title = data}
        else{
          if(options && options.markdown){htmlObj.innerHTML = content}
          else {htmlObj.innerHTML = content}}};
      if(options && typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}};
}
