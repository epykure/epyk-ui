

function buttonCheckBox(htmlObj, data, options){
    htmlObj = $(htmlObj);
    htmlObj.empty();
    data.forEach(function(rec){
        if (rec.color == undefined) {rec.color = 'inherit'};
        var style = {'margin': 0, 'color': rec.color, 'display': 'block', 'position': 'relative', 'cursor': 'pointer'};
        if (rec.style != undefined){
            for(key in rec.style){style[key] = rec.style[key]}};
        if (rec.dsc == undefined) {rec.dsc = ''};
        if (rec.name == undefined) {rec.name = rec.value};
        var strCss = [];
        for (key in style){strCss.push(key +":"+ style[key])};
        if (rec.checked){
            var spanContent = '<span data-content="'+ rec.value +'" style="display:inline-block;float:left;margin:0"><i class="'+ options.icon + '" style="margin:2px"></i></span><p style="margin:0;padding:0" title="'+ rec.dsc +'">' + rec.name + '</p>'}
        else {
            var spanContent = '<span data-content="'+ rec.value +'" style="width:16px;display:inline-block;float:left;margin:0">&nbsp;</span><p style="margin:0" title="'+ rec.dsc +'">' + rec.name + '</p>'}
    htmlObj.append($('<label style="'+ strCss.join(";") +'">'+ spanContent +'</label>'))
    });
    htmlObj.tooltip();
    if (options.tooltip != ""){
      var tip = $('<i class="fas fa-info-circle" style="right:0" title="'+ options.tooltip +'"></i>');
      tip.tooltip();
      htmlObj.append($("<div style='width:100%%;text-align:right'></div>").append(tip))
    }
}