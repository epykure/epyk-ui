

function apBubble(data, options){
    if(data.python){
         result = {series: [], labels: data.labels};
         data.datasets.forEach(function(dataset, i){
           if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors[i]};
           if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors[i]};
           if(typeof dataset.hoverBackgroundColor === "undefined"){
             dataset.hoverBackgroundColor = options.background_colors[i]};
           if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)}
           dataset.name = data.series[i];
           if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataset, i)}
           result.series.push(dataset) })
       } else{
         var temp = {}; var labels = []; var uniqLabels = {}; var yDefs; var xDefs;
         if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
         if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
         yDefs.forEach(function(series){temp[series] = {}});
         data.forEach(function(rec){
           yDefs.forEach(function(name){
           if(rec[name] !== undefined){
             if (!(rec[xDefs] in uniqLabels)){labels.push(rec[xDefs]);
             uniqLabels[rec[xDefs]] = true};
             temp[name][rec[xDefs]] = rec[name]}})
         });
         result = {series: [], type: options.chart.type };
         yDefs.forEach(function(series, i){
             dataSet = {label: series, data: [], color: options.colors[i], type: options.chart.type, borderWidth: 2, backgroundColor: 'rgb(255, 99, 132)'};
             if ((typeof options.attrs !== 'undefined') && (typeof options.attrs[series] !== 'undefined')){
               for(var attr in options.attrs[series]){dataSet[attr] = options.attrs[series][attr]}}
             else if(typeof options.commons !== 'undefined'){
               for(var attr in options.commons){dataSet[attr] = options.commons[attr]}}
             labels.forEach(function(x){
                 if (typeof temp[series][x] === "undefined"){dataSet.data.push(null)}
                 else {dataSet.data.push({x: x, r: 100, y: temp[series][x]})}});
             if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSet, i)}
           result.series.push(dataSet)})
       }; return result;
}