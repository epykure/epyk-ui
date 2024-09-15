
function listItems(htmlObj, data, options){
  htmlObj.innerHTML = "";
  data.forEach(function(item, i){
    if(options.showdown){var converter = new showdown.Converter(options.showdown);
      converter.setOption("display", "inline-block"); var content = item;
      if(typeof item.content !== 'undefined'){content = item.content}
      else if(typeof item.text !== 'undefined'){content = item.text};
      var content = converter.makeHtml(content).replace("<p>", "<p style='display:inline-block;margin:0'>")};
    let li = document.createElement("li");
    if (options.items_class){li.classList.add(options.items_class)};
    Object.keys(options.li_style).forEach(function(key){li.style[key] = options.li_style[key]});
    if(typeof item.type === 'undefined'){let subItem = window[options.items_type](li, item, options);}
    else{let subItem = window[item.type](li, item, options)};
    if(typeof item.tooltip !== 'undefined'){
      var info = document.createElement("i");
      info.classList.add(...options.info_icon.split(" ")); info.setAttribute('title', item.tooltip);
      close.classList.add("html-items-info"); info.setAttribute('data-html', true);
      info.setAttribute('data-placement', 'right'); info.setAttribute('data-toggle', 'tooltip');
      li.style.position = "relative"; li.lastChild.style.display = 'inline-block'; li.appendChild(info);
    };
    if(options.delete){
      var close = document.createElement("i"); close.classList.add(...options.delete_icon.split(" "));
      close.classList.add("html-items-close"); close.onclick = function(event){this.parentNode.remove()};
      li.style.position = "relative";
      for (const [key, value] of Object.entries(options.delete_position)){
        close.style[key] = value}
      li.lastChild.style.display = 'inline-block'; li.appendChild(close)}
    htmlObj.appendChild(li)})
}