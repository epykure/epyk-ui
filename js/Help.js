

function help(htmlObj, data, options){
    htmlObj.setAttribute("title", data);
    if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}

}