

function inputCheckbox(htmlObj, data, options){
    htmlObj.checked = data.value;
      if(typeof data.text !== 'undefined'){
        htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
}