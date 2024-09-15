
function itemLogs(htmlObj, data, options){
    var item = document.createElement("DIV"); item.classList.add("html-item-log");
    var message = document.createElement("DIV"); message.style.display = "inline-block" ;
    if (typeof data.color !== 'undefined'){item.style.borderLeftColor = data.color};
    var log = document.createElement("DIV"); log.classList.add("html-item-log-conten");
    var elapsedTime = "";
    if ((typeof data.d !== 'undefined') && (data.d != 0)){elapsedTime = data.d + "d";}
    if ((typeof data.h !== 'undefined') && (data.h != 0)){elapsedTime = elapsedTime + " "+ data.h + "h";}
    if ((typeof data.m !== 'undefined') && (data.m != 0)){elapsedTime = elapsedTime + " "+ data.m + "m";}
    if ((typeof data.s !== 'undefined') && (data.s != 0)){elapsedTime = elapsedTime + " "+ data.s + "s";}
    log.innerHTML = elapsedTime + options.label;
    if(options.click != null){
      item.style.cursor = 'pointer'; message.setAttribute('name', 'value'); message.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = message.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = Object.assign({}, {"value": message.innerHTML, "timestamp": log.innerHTML}, data);
           options.click(event, value)
           if(dataValue == 'true'){
             message.classList.remove('list_text_selected'); message.setAttribute('data-valid', false)}
           else{message.classList.add('list_text_selected'); message.setAttribute('data-valid', true)}
         }
      }
    } else {
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', true);}
    if(options.draggable != false){
      message.setAttribute('draggable', true); message.style.cursor = 'grab';
      message.ondragstart = function(event){var value = this.innerHTML; options.draggable(event, value)}
    } ;
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){message.style[key] = options.style[key] })}
    if(typeof data === 'object'){
      message.innerHTML = data.text} else { message.innerHTML = data};
    item.appendChild(log); item.appendChild(message);
   htmlObj.appendChild(item);
}