


function List(htmlObj, data, options){
    htmlObj.innerHTML = "";
      data.forEach(function(item, i){
        var li = document.createElement(options.item_type); li.innerHTML = item; htmlObj.appendChild(li)})
}