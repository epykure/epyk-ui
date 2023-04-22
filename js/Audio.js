

function audio(htmlObj, data, options){
    var source = document.createElement("source"); htmlObj.innerHTML = "";
    source.setAttribute('src', data.path +"/"+ data.audio);
    for(var key in options){
      if(key === 'autoplay'){htmlObj.autoplay = options.autoplay}
      else{source.setAttribute(key, options[key])}};
    htmlObj.appendChild(source)
}