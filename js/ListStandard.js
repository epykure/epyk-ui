

function listStandard(htmlObj, data, options){
    htmlObj.innerHTML = ""; setCss(htmlObj, options, true);
    data.forEach(function(item, i){
       if (typeof item !== "object"){item = {text: item}};
        let li = document.createElement(options.item_type); li.innerHTML = item.text;
        if (options.items_class){li.classList.add(options.items_class)};
        if(options.categories){
            for (const [key, value] of Object.entries(options.categories)) {
              if (item[key]){li.classList.add(value)}}};
        htmlObj.appendChild(li)})
}