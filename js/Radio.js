

function radio(htmlObj, data, options){
  htmlObj.checked = data.value;
  if(data.text !== null){
    htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
  if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}
}