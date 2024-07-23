

function badge(htmlObj, data, options){
    let badgeContent = htmlObj.querySelector("[name='badge-value']"); badgeContent.innerHTML = data;
    if (!options.show_empty){if(!data) {htmlObj.style.display = 'None'} else {htmlObj.style.display = ''}};
    setCss(htmlObj, options);
}