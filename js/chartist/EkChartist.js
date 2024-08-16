
function ekChartist(data, options){
    let results = {labels: [], series: []};
    if (data){
        let labels = []; let temp = {}; var yDefs; var xDefs;
        if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
        if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[xDefs])){labels.push(rec[xDefs]);}
            yDefs.forEach(function(series){
                temp[series][rec[xDefs]] = rec[series]
             })
        });
        let datasets = [];
        yDefs.forEach(function(series){
          let dataset = [];
          labels.forEach(function(x){dataset.push(temp[series][x])});
          datasets.push({name: series, data: dataset});
        })
        results.labels = labels;
        results.series = datasets;
    };
    return results
}