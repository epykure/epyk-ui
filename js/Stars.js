

function stars(htmlObj, data, options){
  if (options.templateMode == 'loading'){
    data = options.templateLoading(data)}
  else if (options.templateMode == 'error'){
    data = options.templateError(data)}
  htmlObj.dataset.level = data;
  htmlObj.querySelectorAll("span").forEach(function(span, i){
    if (options.tail && (i < data)){span.style.color = options.colors[i]}
    else if (!options.tail && (i == (data-1))){span.style.color = options.colors[i]}
    else {span.style.color = ''}})
}