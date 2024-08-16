
function listBrackets(htmlObj, data, options){
    setCss(htmlObj, options, true); options.init = data; $(htmlObj).bracket(options)
}