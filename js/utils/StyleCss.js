
function setCss(htmlObj, options, deleteFromOptions = false){
    if(htmlObj){
        if(typeof options.css !== 'undefined'){
            for(var k in options.css){htmlObj.style[k] = options.css[k]}
        };
        if (deleteFromOptions){delete options.css}
    }
}