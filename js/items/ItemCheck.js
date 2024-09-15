

function itemCheck(htmlObj, data, options){
    var item = document.createElement("DIV"); item.classList.add("html-item-check");
    var span = document.createElement("span"); var input = document.createElement("input");
    input.setAttribute('type', 'checkbox'); input.setAttribute('name', 'input_box');
    input.classList.add("html-item-check-input");
    input.onchange = function(event){
      event.stopPropagation(); event.cancelBubble = true; span.setAttribute('data-valid', this.checked);
      var value = span.innerHTML; if(options.click != null){options.click(event, value)}};
    var span = document.createElement("label"); span.classList.add("html-item-check-label");
    if (options.text_click){
      span.style.cursor = "pointer";
      span.onclick = function(event){
        var isChecked = this.getAttribute('data-valid');
        if (isChecked == 'true'){this.setAttribute('data-valid', false); input.checked = false}
        else {this.setAttribute('data-valid', true); input.checked = true}
        var value = this.innerHTML; if(options.click != null){options.click(event, value)}
      };
    };
    span.setAttribute('data-valid', false);;
    if(typeof data === 'object'){
      if(typeof data.text !== 'undefined'){span.innerHTML = data.text} else {span.innerHTML = data.value}}
    else {span.innerHTML = data};
    if(options.checked){
      input.setAttribute('checked', options.checked); span.setAttribute('data-valid', options.checked)};
    var checkedCol = "checked";
    if (typeof options.checked_key !== 'undefined'){checkedCol = options.checked_key}
    if(data[checkedCol]){
      input.setAttribute('checked', data[checkedCol]); span.setAttribute('data-valid', data[checkedCol])};
    if (options.position == 'right'){
      span.innerHTML = ""; var labelTag = document.createElement("span"); labelTag.setAttribute('name', 'value');
      labelTag.innerHTML = data; labelTag.classList.add("html-item-check-right"); item.appendChild(labelTag);
    } else {span.setAttribute('name', 'value');};
    item.appendChild(input); item.appendChild(span); htmlObj.appendChild(item);
}