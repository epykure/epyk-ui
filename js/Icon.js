

function Icon(htmlObj, data, options){
    if (typeof data !== 'undefined'){
      htmlObj.classList = []; data.split(' ').forEach(function(cls){htmlObj.classList.add(cls)});
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlObj.style[k] = options.css[k]}}}
}