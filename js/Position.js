

function position(htmlObj, data, options){
    htmlObj.innerHTML = "";
    var prevCursor = 0; var content = ""+ data; var shift = 0;
    if (options.digits === true){ shift = content.indexOf(".") + 1; }
    if (typeof options.positions !== 'undefined'){
      const keys = Object.keys(options.positions).sort();
      keys.forEach(function(k){
        var cursor = parseInt(k) + shift;
        var span = document.createElement("span");
        span.innerHTML = content.slice(prevCursor, cursor);
        span.style.display = "inline-block";
        htmlObj.appendChild(span);

        var span2 = document.createElement("span");
        span2.innerHTML = content.slice(cursor, cursor+1);
        span2.style.display = "inline-block";
        Object.keys(options.positions[k]).forEach(function(key){
            span2.style[key] = options.positions[k][key]});
        htmlObj.appendChild(span2);
        prevCursor = cursor+1;
      });
      if (content.length > prevCursor){
        var span = document.createElement("span");
        span.innerHTML = content.slice(prevCursor, content.length);
        span.style.display = "inline-block";
        htmlObj.appendChild(span)}
    }
}