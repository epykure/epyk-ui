
function label(htmlObj, data, options){
    data = getDataFromTemplate(data, options);
    if (typeof data !== "undefined"){
      if(options.showdown){var converter = new showdown.Converter(options.showdown);
        var content = converter.makeHtml(data).replace(/<\/?p[^>]*>/ig, '')} else {var content = data};
      if(options._children > 0){
        htmlObj.insertAdjacentHTML('beforeend', '<div style="display:inline-block;vertical-align:middle">'+ content +'</div>')}
      else{htmlObj.innerHTML = content};
      setCss(htmlObj, options);
   }
}