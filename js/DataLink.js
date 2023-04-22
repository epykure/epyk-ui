

function dataLink(htmlObj, data, options){
    if (options.templateMode == 'loading'){data.text = options.templateLoading(data)}
    else if (options.templateMode == 'error'){data.text = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){data.text = options.template(data)}
    var b = new Blob([data.value]); htmlObj.href = URL.createObjectURL(b);
    htmlObj.innerHTML = data.text
}