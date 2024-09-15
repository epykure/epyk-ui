

function itemText(htmlObj, data, options){
    let item = document.createElement("DIV");
    if(options.click != null){
      item.style.cursor = 'pointer'; item.setAttribute('name', 'value'); item.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = item.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = this.innerHTML; options.click(event, value);
           if(dataValue == 'true'){
             item.classList.remove('list_text_selected'); item.setAttribute('data-valid', false)}
           else{item.classList.add('list_text_selected'); item.setAttribute('data-valid', true) }
         }
      }
    } else {
      item.setAttribute('name', 'value'); item.setAttribute('data-valid', true);};
    if(options.draggable != false){
      item.setAttribute('draggable', true); item.style.cursor = 'grab';
      item.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}
    };
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){item.style[key] = options.style[key] })};
    if(typeof data === 'object'){
      if(typeof data.style !== 'undefined'){
        Object.keys(data.style).forEach(function(key){item.style[key] = data.style[key] })};
      item.innerHTML = data.text} else {item.innerHTML = data};
   htmlObj.appendChild(item);
}