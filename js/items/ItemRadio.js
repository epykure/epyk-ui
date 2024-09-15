

function itemRadio(htmlObj, data, options){
    var item = document.createElement("DIV"); item.classList.add("html-item-radio");
    var span = document.createElement("span"); var input = document.createElement("input");
    input.setAttribute('type', 'radio'); input.setAttribute('name', options.group);
    input.classList.add("html-item-radio-input");
    input.onclick = function(event){
        var value = span.innerHTML;
        if (input.checked && (span.getAttribute('data-valid') == 'true')){
          input.checked = false; span.setAttribute('data-valid', false)}
        else{
          this.parentNode.parentNode.parentNode.querySelectorAll('[name=value]').forEach(
            function(node){node.setAttribute('data-valid', false)});
          if(options.click != null){options.click(event, value)};
          span.setAttribute('data-valid', input.checked)
        }
    };
    if (options.text_click){
      span.style.cursor = "pointer";
      span.onclick = function(event){
          var value = span.innerHTML;
          if (this.getAttribute('data-valid') == 'true'){
            input.checked = false; this.setAttribute('data-valid', false)
          } else {
            this.parentNode.parentNode.parentNode.querySelectorAll('[name=value]').forEach(
              function(node){node.setAttribute('data-valid', false)});
            if(options.click != null){options.click(event, value)};
            this.setAttribute('data-valid', true); input.checked = true;
          }
      };
    };
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', false);
    span.classList.add("html-item-radio-label");
    if(typeof data === 'object'){
      if(typeof data.text !== 'undefined'){span.innerHTML = data.text} else {span.innerHTML = data.value};
      var checkedCol = "checked";
      if (typeof options.checked_key !== 'undefined'){checkedCol = options.checked_key};
      if(data[checkedCol]){
        input.setAttribute('checked', data[checkedCol]); span.setAttribute('data-valid', data[checkedCol]);
      }
    } else { span.innerHTML = data};
     item.appendChild(input); item.appendChild(span);
   htmlObj.appendChild(item);
}