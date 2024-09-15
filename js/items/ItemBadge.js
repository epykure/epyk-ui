

function itemBadge(htmlObj, data, options){
    let item = document.createElement("DIV"); let span = document.createElement("span");
    if (typeof data !== "object"){data = {text: data, value: 0}};
    span.setAttribute('name', 'value'); span.innerHTML = data.text; item.appendChild(span);
    if(typeof data.value !== 'undefined'){
      let badge = document.createElement("span"); badge.innerHTML = data.value;
      badge.classList.add("html-item-badge");
      for(const attr in options.badge){badge.style[attr] = options.badge[attr]}; item.appendChild(badge)};
    htmlObj.appendChild(item);
}