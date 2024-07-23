

function emoji(htmlObj, data, options){
    htmlObj.innerHTML = data; setCss(htmlObj, options, true);
    if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}};
}
