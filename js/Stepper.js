

function stepper(htmlObj, data, options){
    htmlObj.innerHTML = '';
    if (data != null){
      var width = options.svg_style.width; var height = options.svg_style.height;
      var attrs = [options.column_label, options.column_text, options.column_title, options.column_tooltip];
      var props = ['color', 'background', 'shape', 'title_color'];

      data.forEach(function(step, i){
        var li = document.createElement("LI"); li.style['margin-bottom'] = '5px'; li.style['margin-top'] = '5px';

        attrs.forEach(function(attr){if(typeof step[attr] === 'undefined'){step[attr] = ''}});
        props.forEach(function(prop){if(typeof step[prop] === 'undefined'){step[prop] = options[prop]}});

        var span = document.createElement("SPAN"); span.setAttribute('name', step[options.column_label]);
        span.setAttribute('name', 'label'); span.innerHTML = step[options.column_title];
        var div = document.createElement("DIV"); div.setAttribute('title', step.tooltip);
        div.setAttribute('name', 'svg_holder');

        for (var key in options.text_style){span.style[key] = options.text_style[key]}
        span.style.width = width +"px"; div.appendChild(span); li.appendChild(div); div.id = "svg_" + i;
        window[step.shape](div, options, step); htmlObj.appendChild(li)
      })
    }
}