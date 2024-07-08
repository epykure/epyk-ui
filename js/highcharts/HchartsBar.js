
function hchartsBar(data, options){
    if (data){
        let labels = []; let temp = {}; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[xDefs])){labels.push(rec[xDefs]);};
            yDefs.forEach(function(series){temp[series][rec[xDefs]] = rec[series]})
        });
        if (Array.isArray(options.xAxis)){options.xAxis[0].categories = labels;}
        else {options.xAxis.categories = labels;}
        let datasets = [];
        yDefs.forEach(function(series, i){
          let dataset = [];
          labels.forEach(function(x){
                dataset.push(temp[series][x])});
          let seriesData = {name: series, data: dataset};
          if(typeof options.commons !== 'undefined'){
              for(var attr in options.commons){seriesData[attr] = options.commons[attr]}}
          if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[series] !== 'undefined')){
              seriesData = Object.assign(seriesData, options.datasets[series])};
          if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(seriesData, i)}
          datasets.push(seriesData);
        }) ;
        options.series = datasets;
    };
    return options
}