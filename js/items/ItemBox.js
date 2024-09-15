

function itemBox(htmlObj, data, options){
    var item = document.createElement("DIV"); item.classList.add("html-item-box"); item.setAttribute('data-valid', true);
    var title = document.createElement("DIV"); title.setAttribute('name', 'value');
    item.classList.add("html-item-box-title");
    if (typeof data !== "object"){data = {text: data, title: ""}};
    if (typeof data.color !== 'undefined'){
      item.style.border = "1px solid " + data.color; title.style.color = data.color}
    title.innerHTML = data.title;
    var text = document.createElement("DIV"); text.innerHTML = data.text;
    item.appendChild(title); item.appendChild(text);
    var icons = document.createElement("DIV"); item.classList.add("html-item-box-icons");
    if(typeof data.icons !== 'undefined') {
      data.icons.forEach(function(rec){
          var icon_dom = document.createElement("I"); icon_dom.classList.add("html-item-box-icon");
          rec.icon.split(" ").forEach(function(s){icon_dom.classList.add(s)});
          if(typeof rec.color !== 'undefined'){ icon_dom.style.color = rec.color}
          if(typeof rec.tooltip !== 'undefined'){icon_dom.setAttribute('title', rec.tooltip)}
          if(rec.click != null){ icon_dom.style.cursor = 'pointer';
            icon_dom.onclick = function(event){ var value = data.title; eval(rec.click)}};
          icons.appendChild(icon_dom)})}
    item.appendChild(icons); htmlObj.appendChild(item);
}