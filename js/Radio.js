

function radio(htmlObj, data, options){
  htmlObj.checked = data.value;
  if(data.text !== null){
    htmlObj.parentNode.insertBefore(document.createTextNode(data.text), htmlObj.nextSibling)};
  setCss(htmlObj, options) ;
}