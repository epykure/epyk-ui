

function slideShow(htmlObj, data, options){
    if(typeof window[ htmlObj.id + '_obj'] !== 'undefined') {window[ htmlObj.id + '_obj'].destroy();}
      window[ htmlObj.id + '_obj'] = tns(options)
}