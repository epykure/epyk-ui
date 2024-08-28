
function button(htmlObj, data, options){
    data = getDataFromTemplate(data, options); htmlObj.setAttribute('data-processing', false);
    htmlObj.querySelectorAll('span[name="button-content"]')[0].innerHTML = data; setCss(htmlObj, options);
    if (options.icon){
        let icons = htmlObj.querySelectorAll('i'); if(icons){icons[0].setAttribute("class", options.icon)}};
    if (options.badge){
        let badges = htmlObj.querySelectorAll('[name="badge-value"]'); if (badges){badges[0].innerHTML = options.badge}
    };
}