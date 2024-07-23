
function setCss(htmlObj, options, deleteFromOptions = false){
    if(typeof options.css !== 'undefined'){
        for(var k in options.css){htmlObj.style[k] = options.css[k]}
    };
    if (deleteFromOptions){delete options.css}
}