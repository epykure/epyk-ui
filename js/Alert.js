

function alert(htmlObj, data, options){
    var feed = document.createElement("p");
      options.classes.forEach(function(cls){ feed.classList.add(cls) });
      if(options.showdown){
        var converter = new showdown.Converter(options.showdown); data = converter.makeHtml(data.trim())};
      if (htmlObj.style.display != 'block'){htmlObj.innerHTML = ""};
      if (options.close){
        var icon = document.createElement("i");
        icon.className = "fas fa-times"; icon.style.float = "right"; icon.style.marginRight = "2px";
        icon.style.cursor = "pointer"; icon.style.zIndex = 50; icon.style.position = "relative";
        icon.addEventListener("click", function(){feed.remove(); this.remove()} )
        htmlObj.appendChild(icon)};
      feed.innerHTML = data; htmlObj.appendChild(feed);
      var s = htmlObj.style; s.opacity = 1; htmlObj.style.display = 'block';
      if(options.time != null){
        (function fade(){(s.opacity-=.1)<0?s.display="none": setTimeout(fade, options.time)})()};
      setCss(htmlObj, options) ;
}