

function itemPeriod(htmlObj, data, options){
    if (typeof data !== "object"){data = {content: data, title: ""}};
    if(options.showdown){var converter = new showdown.Converter(options.showdown);
      converter.setOption("display", "inline-block");
      data.content = converter.makeHtml(data.content).replace("<p>", "<p style='display:inline-block;margin:0'>")};
    function hashCode(str) {
      var hash = 0; for (var i = 0; i < str.length; i++) {hash = str.charCodeAt(i) + ((hash << 5) - hash)} return hash}
    function intToRGB(i){
      var c = (i & 0x00FFFFFF).toString(16).toUpperCase(); return "00000".substring(0, 6 - c.length) + c}
    var item = document.createElement("DIV"); var title = document.createElement("DIV");
    var titleValue = document.createElement("DIV"); titleValue.innerHTML = data.title;
    titleValue.classList.add("html-item-period-title"); title.appendChild(titleValue);
    var msg = document.createElement("DIV");  msg.classList.add("html-item-period-content") ;
    title.setAttribute('name', 'value'); item.setAttribute('data-valid', true);
    if (typeof data.color === 'undefined') {data.color = "#aaaaaa"};
    var content = document.createElement("DIV"); content.innerHTML = data.content;
    msg.appendChild(title); msg.appendChild(content);
    msg.style["border-left"] = "1px solid " + data.color;
    var dFrom = document.createElement("DIV"); item.appendChild(dFrom); dFrom.innerHTML = data.from;
    dFrom.style.color = data.color; dFrom.classList.add(".html-item-period-range")
    item.appendChild(msg);
    if (typeof data.to !== 'undefined'){
      var dTo = document.createElement("DIV"); item.appendChild(dTo); dTo.innerHTML = data.to;
      dTo.style.color = data.color; dTo.classList.add(".html-item-period-range")
    };
    item.classList.add("html-item-period"); htmlObj.appendChild(item);
}