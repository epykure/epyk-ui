

function alert(htmlObj, data, options){
    let feed = document.createElement("p"); options.classes.forEach(function(cls){ feed.classList.add(cls)});
    if (htmlObj.style.display != 'block'){htmlObj.innerHTML = ""};
    if (options.close){
        let icon = document.createElement("i");
        icon.className = "fas fa-times"; icon.style.float = "right"; icon.style.marginRight = "2px";
        icon.style.cursor = "pointer"; icon.style.zIndex = 50; icon.style.position = "relative";
        icon.addEventListener("click", function(){feed.remove(); this.remove()})
        htmlObj.appendChild(icon)};
    feed.innerHTML = getHtmlData(data, options); htmlObj.appendChild(feed);
    let s = htmlObj.style; s.opacity = 1; htmlObj.style.display = 'block';
    if(options.time != null){(function fade(){(s.opacity-=.1)<0?s.display="none": setTimeout(fade, options.time)})()};
    setCss(htmlObj, options) ;
}