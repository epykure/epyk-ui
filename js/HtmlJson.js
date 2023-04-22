

function htmlJson(htmlObj, data, options){
    window[htmlObj.id + '_obj'] = new JSONFormatter(data, options.open, options.opts); htmlObj.innerHTML = '';
    htmlObj.appendChild(window[ htmlObj.id + '_obj'].render())
}