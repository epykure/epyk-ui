

function upandDown(htmlObj, data, options){
    htmlObj = htmlObj.querySelector("#" + htmlObj.id + "_content");
    if(typeof data === 'number'){data = {value: data, previous: data}};
    var delta = data.value - data.previous; htmlObj.innerHTML = "";
    if(data.previous == 0) {var relMove = 'N/A'}
    else{var relMove = 100 * ((data.value - data.previous) / data.previous)};
    if(data.digits == undefined){data.digits = 0};
    var span = document.createElement("span"); span.innerHTML = data.label || options.label; htmlObj.appendChild(span);
    var valueElt = document.createElement('span'); valueElt.setAttribute('style', 'padding:5px');
    valueElt.innerHTML = accounting.formatNumber(data.value, options.digits, options.thousand_sep, options.decimal_sep);
    htmlObj.appendChild(valueElt); var deltaElt = document.createElement('span');
    var relMoveElt = document.createElement('span'); var icon = document.createElement('i');
    if (delta < 0){
      deltaElt.innerHTML = "(+"+ accounting.formatNumber(delta, options.digits, options.thousand_sep, options.decimal_sep) +")";
      relMoveElt.innerHTML = "("+ accounting.formatNumber(relMove, options.digits_percent, options.thousand_sep, options.decimal_sep) +"%)";
      deltaElt.style["color"] = options.red; relMoveElt.style["color"] = options.red;
      icon.className = options.icon_down;
      icon.style["transform"] = "rotate(-"+ options.rotate + "deg)";
      icon.style["color"] = options.red;
    } else{
      deltaElt.innerHTML = "(+"+ accounting.formatNumber(delta, options.digits, options.thousand_sep, options.decimal_sep) +")";
      deltaElt.style["color"] = options.green; relMoveElt.style["color"] = options.green;
      relMoveElt.innerHTML = "("+ accounting.formatNumber(relMove, options.digits_percent, options.thousand_sep, options.decimal_sep) +"%)";
      icon.className = options.icon_up;
      icon.style["transform"] = "rotate("+ options.rotate + "deg)";
      icon.style["color"] = options.green;
    };
    relMoveElt.style["font-size"] = options.font_size;
    deltaElt.style["font-size"] = options.font_size;
    icon.style["font-size"] = options.font_size;
    Object.keys(options.css_stats).forEach(function(attr){
      relMoveElt.style[attr] = options.css_stats[attr]; deltaElt.style[attr] = options.css_stats[attr];
      icon.style[attr] = options.css_stats[attr]});
    htmlObj.appendChild(deltaElt); htmlObj.appendChild(relMoveElt); htmlObj.appendChild(icon);
    Object.keys(options.css).forEach(function(attr){htmlObj.style[attr] = options.css[attr]})
}