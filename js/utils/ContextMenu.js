function buildContextMenu(context, menu, options){
    context.innerHTML ='';
    menu.forEach(function(item){
        let menuitem = document.createElement('div'); menuitem.innerHTML = item.title;
        menuitem.addEventListener('click', function(){eval(item.action); context.style.display = "None"});
        if (item.tooltip){menuitem.title = item.tooltip};
        if (item.icon){
            let icon = document.createElement('i'); icon.setAttribute("class", item.icon);
            icon.style.marginRight = "2px"; menuitem.prepend(icon);
        };
        context.appendChild(menuitem);
    }); context.style.left = options.left; context.style.top = options.top; context.style.display = "block" ;
    context.focus(); context.addEventListener('focusout', function(){context.style.display = "None"});
}