

function skillBar(htmlObj, data, options){
    var table = htmlObj.querySelector("table"); table.innerHTML = "";
      var thead = document.createElement("thead"); var tbody = document.createElement("tbody");
      tbody.style["box-sizing"] = "border-box";
      table.appendChild(thead); table.appendChild(tbody);
      data.forEach(function(rec, i){
        var tooltip = "";
        if (typeof rec.tooltip !== "undefined"){var tooltip = rec.tooltip};
        if (typeof rec.url !== "undefined") {
          var content = document.createElement("a"); content.href =  rec.url}
        else {
          var content = document.createElement("span")};
        content.innerHTML = rec[options.value].toFixed(options.digits) + "%";
        content.style.whiteSpace = "nowrap";
        var tr = document.createElement("tr");
        tr.style.width = options.width + "px"; tr.title = tooltip;
        var col = document.createElement("td");
        col.style.textAlign = "right"; col.style.padding = "0 5px";
        var p = document.createElement("span"); p.innerHTML = rec[options.label];
        col.appendChild(p); tr.appendChild(col);
        var row = document.createElement("td");
        row.style["box-sizing"] = "border-box";
        row.style.width = "100%";
        var div = document.createElement("div");
        div.style.width = rec[options.value].toFixed(options.digits) + "%";
        if( rec[options.value].toFixed(options.digits) > options.thresholds[1]){ div.style.backgroundColor = options.success}
        else if(rec[options.value].toFixed(options.digits) > options.thresholds[0]) {div.style.backgroundColor = options.warning}
        else {div.style.backgroundColor = options.danger}
        div.style.fontSize = "10px"; div.style.lineHeight = options.height ?? "20px"; div.style.verticalAlign = "middle%";
        div.style.display = "block"; div.style.paddingLeft = "5px";
        if(options && typeof options.css !== 'undefined'){for(var k in options.css){div.style[k] = options.css[k]}};
        if (options.percentage){div.appendChild(content)}
        else { div.innerHTML = "&nbsp;"; div.title = rec[options.value].toFixed(options.digits) + "%" }
        row.appendChild(div); tr.appendChild(row);
        tbody.appendChild(tr)
      })
}