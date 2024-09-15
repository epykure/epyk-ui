

function itemLink(htmlObj, data, options){
    var item = document.createElement("div"); var link = document.createElement("a");
    if (typeof data !== "object"){data = {text: data}};
    item.classList.add("html-item-link"); link.setAttribute('name', 'value'); link.setAttribute('data-valid', false);
    link.innerHTML = data.text; if(typeof data.url !== 'undefined'){link.href = data.url} else {link.href = '#'};
    if(typeof data.target !== "undefined"){link.target = data.target}
    if(typeof data.icon !== 'undefined'){
      var iconItem = document.createElement("i"); iconItem.setAttribute("class", data.icon);
      iconItem.classList.add("html-item-link-icon"); item.appendChild(iconItem)};
    item.appendChild(link);
    if(typeof data.dsc !== "undefined"){
      var dsc = document.createElement("div"); dsc.classList.add("html-item-link-dsc");
      dsc.innerHTML = data.dsc; item.appendChild(dsc)};
    if(typeof data.image !== "undefined"){
      var img = document.createElement("img"); dsc.classList.add("html-item-link-image");
      img.setAttribute('src', data.image); link.prepend(img)} ;
   htmlObj.appendChild(item);
}