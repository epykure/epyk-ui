
function getDataFromTemplate(data, options){
    let content = data ;
    if (options.templateMode == 'loading'){content = options.templateLoading(data)}
    else if (options.templateMode == 'error'){content = options.templateError(data)}
    else if (typeof options.template !== 'undefined' && data){content = options.template(data)}
    return content;
}