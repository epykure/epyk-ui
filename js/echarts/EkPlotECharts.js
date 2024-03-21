
function ekPlotECharts(data, options){
    let chartContext = {series: []};
    Object.assign(chartContext, options);
    delete chartContext._ek;
    if (data && data.length > 0){chartContext.series = data};
    return chartContext
}