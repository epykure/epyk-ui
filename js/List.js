

function list(htmlObj, data, options){
    htmlObj.innerHTML = "";
    data.forEach(function(item, i){
        let li = document.createElement(options.item_type); li.innerHTML = item; htmlObj.appendChild(li)})
}