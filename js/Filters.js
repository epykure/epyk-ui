function addChip(panel, record, options){
    if(typeof(record.category !== "undefined")){options.category = record.category}
    var div = document.createElement("div");
    for (var key in options.item_css){div.style[key] = options.item_css[key]};
    div.setAttribute('data-category', record.category);
    if(typeof(record.css !== "undefined")){for (var key in record.css){ div.style[key] = record.css[key]}};
    var content = document.createElement("span");
    for (var key in options.value_css){ content.style[key] = options.value_css[key]};
    content.setAttribute('name', 'chip_value'); content.innerHTML = record.value;
    if(options.visible){var p = document.createElement("p");
      for (var key in options.category_css){p.style[key] = options.category_css[key]};
      p.innerHTML = record.name; div.appendChild(p)} ;
    div.appendChild(content);
    if(!record.fixed && options.delete){
      var icon = document.createElement("span"); icon.innerHTML = "&#215;";
      for (var key in options.icon_css){icon.style[key] = options.icon_css[key] };
      icon.addEventListener('click', function(){eval(options.delete)});
      div.appendChild(icon)}
    if(typeof options.draggable !== 'undefined'){
      div.setAttribute('draggable', true); div.style.cursor = 'grab';
      div.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}
    }; panel.appendChild(div);
}

function filters(htmlObj, data, options){
  let panel = htmlObj.querySelector('[name=panel]'); panel.innerHTML = '';
  if (typeof data !== 'undefined'){
      data.forEach(function(val){
        if(typeof val === 'string'){
          val = {name: options.category, category: options.category, value: val, disabled: false, fixed: false}}
        else{
          if(val.category === undefined){
            if(val.name === undefined) {val.category = options.category} else {val.category = val.name}}
          if(val.name === undefined){val.name = val.category}};
        addChip(panel, val, options)})};
  const maxHeight = options.max_height;
  if(maxHeight > 0){
      panel.style.maxHeight = ""+ maxHeight + "px"; panel.style.overflow = "hidden" ;
      var div = document.createElement("div"); div.classList.add("html-filters-showAll"); div.innerHTML = options.show_all;
      div.addEventListener("click", function(event){
        var targetElement = event.target || event.srcElement;
        if (targetElement.innerHTML != options.reduce){panel.style.maxHeight = null; targetElement.innerHTML = options.reduce}
        else {panel.style.maxHeight = ""+ maxHeight + "px"; targetElement.innerHTML = options.show_all}});
      panel.appendChild(div)
    }
}
