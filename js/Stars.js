

function stars(htmlObj, data, options){
  if (options.templateMode == 'loading'){
    data = options.templateLoading(data)}
  else if (options.templateMode == 'error'){
    data = options.templateError(data)}

  htmlObj.dataset.level = data;
  htmlObj.querySelectorAll("span").forEach(function(span, i){
    if (i < data){span.style.color = options.color}
    else {span.style.color = ''}})
}