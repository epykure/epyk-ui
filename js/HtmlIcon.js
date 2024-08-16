

function htmlIcon(htmlObj, data, options){
    if (typeof data !== 'undefined'){
      htmlObj.classList = []; data.split(' ').forEach(function(cls){htmlObj.classList.add(cls)});
      setCss(htmlObj, options, true);
    }
}