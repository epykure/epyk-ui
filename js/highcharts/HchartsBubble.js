
function hchartsBubble(data, options){
    if (data){
        let labels = []; let temp = {}; let dataset = []; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[xDefs])){labels.push(rec[xDefs]);};
            yDefs.forEach(function(series){
                if (options.rDim){temp[series][rec[xDefs]] = {y: rec[series], x: rec[xDefs], z: rec[options.rDim[0]]}}
                else {temp[series][rec[xDefs]] = {y: rec[series], x: rec[xDefs], z: 2}}
             })
        });
        let datasets = [];
        yDefs.forEach(function(series, i){
          let dataset = [];
          labels.forEach(function(x){dataset.push(temp[series][x])});
          let seriesData = {name: series, data: dataset};
          if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(seriesData, i)}
          datasets.push(seriesData);
        });
        options.series = datasets;
    };
    return options
}