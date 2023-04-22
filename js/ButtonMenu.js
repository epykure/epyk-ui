
function buttonMenu(htmlObj, data, options){
  var panel = htmlObj.querySelector("div");
  data.forEach(function(rec){
  var href = document.createElement("a"); href.innerHTML = rec;
  Object.keys(options).forEach(function(key){href.style[key] = options[key]});
  panel.appendChild(href)})
}