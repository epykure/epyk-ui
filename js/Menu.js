

function menu(htmlObj, data, options){
  var jqHtmlObj = jQuery(htmlObj); if (options.clearDropDown) {jqHtmlObj.empty()};
  var isRoot =  options.isRoot; if(typeof isRoot === 'undefined'){isRoot = true}
  data.forEach(function(rec){
    if (rec.items != undefined) {
      var li = $('<li></li>'); var div = $('<div>'+ rec.value +'</div>');
      li.append(div); var ul = $('<ul aria-hidden="true"></ul>');
      options.clearDropDown = false; options.isRoot = false;
      options.builder(ul, rec.items, options); li.append(ul); jqHtmlObj.append(li);
    } else {
      var div = $('<div>'+ rec.value +'</div>').css({"width": '150px'}); var li = $('<li></li>');
      li.append(div); jqHtmlObj.append(li)};
  }); if(isRoot){jqHtmlObj.menu(options)}
}