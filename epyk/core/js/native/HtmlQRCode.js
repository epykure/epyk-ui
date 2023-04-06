

function htmlQRCode(htmlObj, data, options){
    htmlObj.innerHTML = "";
    window[ htmlObj.id + '_obj'] = new QRCode(htmlObj, Object.assign({'text': data}, options) );
    window[ htmlObj.id + '_obj']._el.querySelector("img").style["margin"] = 0
}