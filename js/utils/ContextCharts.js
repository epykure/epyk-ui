

function getChartContext(options){

    if (typeof options.y_columns !== 'undefined') {options._ek.chart.y_columns = options.y_columns; delete options.y_columns;};
    if (typeof options.x_axis !== 'undefined') {options._ek.chart.x_axis = options.x_axis; delete options.x_axis;};
    if (typeof options.names !== 'undefined') {options._ek.names = options.names; delete options.names;};

    let chartContext = {};
    Object.assign(chartContext, options);
    delete chartContext._ek;
    return chartContext;
}