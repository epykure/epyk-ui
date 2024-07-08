
function ekRadarECharts(data, options){
    if (typeof options.y_columns !== 'undefined') {
        options._ek.chart.y_columns = options.y_columns;
        delete options.y_columns;
    };
    if (typeof options.x_axis !== 'undefined') {
        options._ek.chart.x_axis = options.x_axis;
        delete options.x_axis;
    };
    if (typeof options.names !== 'undefined') {
        options._ek.names = options.names;
        delete options.names;
    };

    let chartContext = {series: []};
    Object.assign(chartContext, options);
    delete chartContext._ek;

    var yDefs ; var xDefs ;
    if (typeof options._ek.chart.y_columns === 'function') {
        yDefs = options._ek.chart.y_columns(data, options)} else {yDefs = options._ek.chart.y_columns} ;
    if (typeof options._ek.chart.x_axis === 'function') {
        xDefs = options._ek.chart.x_axis(data, options)} else {xDefs = options._ek.chart.x_axis} ;

    if (options._ek) {
        if (yDefs){
            yDefs.forEach(function(value){
                let dataset = {data: [], type: options._ek.chart.type, name: value};
            })
        }
    }

    if (data && data.length > 0){
        chartContext.series = []; options.series = [];
        var temp = {}; var labels = []; var uniqLabels = {};
        yDefs.forEach(function(series){temp[series] = {}});
        data.forEach(function(rec){
          yDefs.forEach(function(name){
          if(rec[name] !== undefined){
            if (!(rec[xDefs] in uniqLabels)){
              labels.push(rec[xDefs]); uniqLabels[rec[xDefs]] = true};
            temp[name][rec[xDefs]] = rec[name]}})
        });

        let dataSet = {data: [], type: options._ek.chart.type, color: options._ek.colors};
        yDefs.forEach(function(series, i){
            let values = [];
            labels.forEach(function(x){
                if (temp[series][x] == undefined){values.push(null)} else {values.push(temp[series][x])}
            });
            if (typeof options._ek.series !== 'undefined'){
              values = Object.assign(values, options._ek.series)}
            if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
              values = Object.assign(values, options._ek.names[series])};
            let dataSet = {name: series, value: values} ;
            if(typeof options?._ek?.alterSeries !== 'undefined'){options._ek.alterSeries(dataSet, i)} ;
            dataSet.data.push(dataSet);
        });
        chartContext.series.push(dataSet);
    };

    return chartContext
}