
function colorsPicker(htmlObj, data, options){
    options.el = htmlObj; setCss(htmlObj, options, true);
    Coloris(options); htmlObj.value = data;
}