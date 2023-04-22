

function Emoji(htmlObj, data, options){
    htmlObj.innerHTML = data;
    if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}

}
