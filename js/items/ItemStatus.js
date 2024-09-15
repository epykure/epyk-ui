

function itemStatus(htmlObj, data, options){
    var item = document.createElement("DIV"); item.classList.add("html-item-status");
    var message = document.createElement("DIV"); message.classList.add("html-item-status-info");
    var log = document.createElement("DIV");
    if(typeof data.color !== 'undefined'){
        log.classList.add("html-item-status-log-color"); log.style.background = data.color} ;
    log.classList.add("html-item-status-log");
    if(options.click != null){
      item.style.cursor = 'pointer'; message.setAttribute('name', 'value'); message.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = message.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = Object.assign({}, {"value": message.innerHTML, "status": log.innerHTML});
           options.click(event, value)
           if(dataValue == 'true'){
             message.classList.remove('list_text_selected'); message.setAttribute('data-valid', false)}
           else{message.classList.add('list_text_selected'); message.setAttribute('data-valid', true) }
        }
      }
    } else { message.setAttribute('name', 'value'); message.setAttribute('data-valid', true);}
    if(options.draggable != false){
      message.setAttribute('draggable', true); message.style.cursor = 'grab';
      message.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}}
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){message.style[key] = options.style[key] })}
    if(typeof data === 'object'){ message.innerHTML = data.text} else { message.innerHTML = data };
    if(typeof data.color !== 'undefined'){ message.style.borderLeft = "1px solid "+ data.color;}
    item.appendChild(log); item.appendChild(message); htmlObj.appendChild(item);
}