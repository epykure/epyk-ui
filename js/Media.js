

function media(htmlObj, data, options){
    var source = document.createElement("source"); htmlObj.innerHTML = "";
    source.setAttribute('src', data.path +"/"+ data.video);
    for(var key in options){
      if(key === 'autoplay'){htmlObj.autoplay = options.autoplay}
      else{source.setAttribute(key, options[key])}};
    htmlObj.appendChild(source)
}
