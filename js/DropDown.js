

function dropDown(htmlObj, data, options){
    if(options.clearDropDown){htmlObj.innerHTML = ""};
      data.forEach(function(rec){
        if ((rec.items != undefined) && (rec.items.length > 0)) {
          var li = document.createElement("li"); li.classList.add("dropdown"); li.style.listStyleType = 'none';
          li.style.display = 'list-item'; li.style.textAlign = '-webkit-match-parent';
          var a = document.createElement("a"); a.setAttribute('tabindex', -1);
          a.appendChild(document.createTextNode(rec.value)); options.clearDropDown = false;
          var span = document.createElement("span"); span.classList.add("caret"); a.appendChild(span);
          li.appendChild(a);
          var ul = document.createElement("ul"); ul.classList.add("submenu");
          if(typeof options.ul !== "undefined"){
            Object.keys(options.ul).forEach(function(key){ul.style[key] = options.ul[key]})}
          if(typeof options.a !== "undefined"){
            Object.keys(options.a).forEach(function(key){a.style[key] = options.a[key]})}
          options.builder(ul, rec.items, options); li.appendChild(ul); htmlObj.appendChild(li);
        } else {
          var a = document.createElement("a"); a.innerHTML = rec.value;
          if(typeof rec.url !== "undefined"){a.href= rec.url};
          if(typeof options.a !== "undefined"){
            Object.keys(options.a).forEach(function(key){a.style[key] = options.a[key]})}
          if(typeof options.clickLeaf !== "undefined"){
            a.onclick = function(event){const value = a.innerText; options.clickLeaf(event, value)}};
          var li = document.createElement("li"); li.style.listStyleType = 'none'; li.style.display = 'list-item';
          li.style.textAlign = '-webkit-match-parent'; li.appendChild(a); htmlObj.appendChild(li)}
      })
}