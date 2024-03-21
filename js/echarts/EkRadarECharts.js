
function ekRadarECharts(data, options){
    let chartContext = {series: []};
    Object.assign(chartContext, options);
    delete chartContext._ek;

    if (options._ek) {
        if (options._ek.chart.y_columns){
            options._ek.chart.y_columns.forEach(function(value){
                let dataset = {data: [], type: options._ek.chart.type, name: value};
            })
        }
    }

    if (data && data.length > 0){
        chartContext.series = []; options.series = [];
        var temp = {}; var labels = []; var uniqLabels = {};
        options._ek.chart.y_columns.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          options._ek.chart.y_columns.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[options._ek.chart.x_axis] in uniqLabels)){
              labels.push(rec[options._ek.chart.x_axis]); uniqLabels[rec[options._ek.chart.x_axis]] = true};
            temp[name][rec[options._ek.chart.x_axis]] = rec[name]}})
        });

        let dataSet = {data: [], type: options._ek.chart.type, color: options._ek.colors};
        options._ek.chart.y_columns.forEach(function(series, i){
            let values = [];
            labels.forEach(function(x){
                if (temp[series][x] == undefined){values.push(null)} else {values.push(temp[series][x])}
            });
            if (typeof options._ek.series !== 'undefined'){
              values = Object.assign(values, options._ek.series)}
            if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
              values = Object.assign(values, options._ek.names[series])}
            dataSet.data.push({name: series, value: values});
        })
        chartContext.series.push(dataSet);
    };

    return chartContext
}