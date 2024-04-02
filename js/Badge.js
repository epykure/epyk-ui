

function badge(htmlObj, data, options){
    let badgeContent = htmlObj.querySelector("[name='badge-value']")
    badgeContent.innerHTML = data;
    if (!options.show_empty){
        if(!data) {htmlObj.style.display = 'None'}
        else {htmlObj.style.display = ''}
    }
    if(typeof options.css !== 'undefined'){for(var k in options.css){badgeContent.style[k] = options.css[k]}}
}