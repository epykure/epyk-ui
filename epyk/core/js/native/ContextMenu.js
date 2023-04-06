

function contextMenu(htmlObj, data, options){
    var contextMenu = htmlObj.querySelector('ul'); contextMenu.innerHTML = '';
      data.forEach(function(rec){
        var li = document.createElement("li"); var item = document.createElement("DIV");
        item.innerHTML = rec; li.appendChild(item)})
      contextMenu.appendChild(li)
}