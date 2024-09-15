
function itemIcon(htmlObj, data, options){
    var item = document.createElement("DIV"); var icon = document.createElement("I");
    if (typeof data !== "object"){data = {text: data}};
    if(data.icon){data.icon.split(" ").forEach(function(s){icon.classList.add(s)})}
    else if(options.icon) {options.icon.split(" ").forEach(function(s){icon.classList.add(s)}) }
    icon.classList.add("html-item-icon"); var span = document.createElement("span");
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', true);
    if(typeof data === 'object'){span.innerHTML = data.text} else {span.innerHTML = data};
    if(options.click != null){ item.style.cursor = 'pointer';
      item.onclick = function(event){ var value = span.innerHTML; options.click(event, value)}};
    item.appendChild(icon); item.appendChild(span);
    htmlObj.appendChild(item);
}