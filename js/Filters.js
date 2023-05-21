

function filters(htmlObj, data, options){
    var panel = htmlObj.querySelector('[name=panel]'); panel.innerHTML = '';
  if (typeof data !== 'undefined'){
  data.forEach(function(val){
    if(typeof val === 'string'){
      val = {name: options.category, category: options.category, value: val, disabled: false, fixed: false} }
    else{
      if(val.category === undefined){
        if(val.name === undefined) {val.category = options.category} else {val.category = val.name}}
      if(val.name === undefined){ val.name = val.category}};
    chipAdd(panel, val, options)})}
}