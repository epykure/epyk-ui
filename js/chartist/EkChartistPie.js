
function ekChartistPie(data, options){
    let results = {labels: [], series: []};
    if (data){
        let labels = []; let temp = {};
        options.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
            if (!labels.includes(rec[options.x_axis])){labels.push(rec[options.x_axis]);}
            options.y_columns.forEach(function(series){
                temp[series][rec[options.x_axis]] = rec[series]
             })
        });
        let datasets = [];
        options.y_columns.forEach(function(series){
          let dataset = [];
          labels.forEach(function(x){dataset.push(temp[series][x])});
          datasets.push(dataset);
        })
        results.labels = labels;
        results.series = datasets[0];
    };
    return results
}