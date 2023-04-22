

function breadcrumb(htmlObj, data, options){
  htmlObj.innerHTML = "";
  if(typeof data === "undefined"){htmlObj.style["height"] = 0;}
  else{
    if(data.length == 0){htmlObj.style["height"] = 0}
    else{
      htmlObj.style["height"] = options.height + "px";
      var text = document.createTextNode(options.delimiter); htmlObj.appendChild(text)
      data.forEach(function(rec, i){
        if(typeof rec.type !== 'undefined'){
          if(rec.type == "dots"){var text = document.createTextNode("... "); htmlObj.appendChild(text)}}
        else{
          if (rec.selected){
            var aHref = document.createElement("span"); aHref.innerHTML = rec.text}
          else{
            var aHref = document.createElement("a"); aHref.setAttribute('href', rec.url);
            aHref.innerHTML = rec.text}
          Object.keys(options.style).forEach(function(key){aHref.style[key] = options.style[key]});
          if (rec.selected){
            Object.keys(options.style_selected).forEach(
              function(key){aHref.style[key] = options.style_selected[key]});
          }
          htmlObj.appendChild(aHref)}
        var text = document.createTextNode(options.delimiter);
        if (i < data.length-1){htmlObj.appendChild(text)}
  })}}
}