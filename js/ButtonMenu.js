
function buttonMenu(htmlObj, data, options){
  var panel = htmlObj.querySelector("div");
  data.forEach(function(rec){
      var href = document.createElement("a"); href.innerHTML = rec;
      Object.keys(options.css_child).forEach(function(key){href.style[key] = options.css_child[key]});

      if (options.css_cls_child != null){
        href.classList.add(...options.css_cls_child.split(" "))
      };
      panel.appendChild(href)
  })
}