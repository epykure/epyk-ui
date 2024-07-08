
function ekTreeECharts(data, options){
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

    let chartContext = {series: {type: options._ek.chart.type}, name: options._ek.chart.x_axis};
    Object.assign(chartContext, options);
    delete chartContext._ek;

    if (!data || data.length == 0){return options}
    else {
        let tree = {}; let activeBranch = {};
        data.forEach(function(row){
            activeBranch = tree ;
            for (const y of options._ek.chart.x_axis.split('/')) {
                if(!row[y]){break}

                if(!activeBranch[row[y]]){activeBranch[row[y]] = {}};
                activeBranch = activeBranch[row[y]];
            };
            options._ek.chart.y_columns.forEach(function(name){
                if (row[name]){
                    if (activeBranch[name]){activeBranch[name] += row[name]}
                    else {activeBranch[name] = row[name]}
                }
            })
        });
        function processNode(branch, hyr, path){
            Object.keys(branch).forEach(function(key) {
                let v = branch[key];
                if (typeof v === 'object'){
                    path.push(key);
                    let rec = {name: key, children: [], path: path.join("/")};
                    hyr.push(rec); processNode(v, rec.children, path)}
                else {path.push(key); hyr.push({name: options._ek.chart.x_axis, value: v, path: path.join("/")})}
            });
        };
        dataSet = []; processNode(tree, dataSet, []);

        if (typeof options._ek.series !== 'undefined'){
          Object.assign(chartContext.series, options._ek.series)}
        if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
          Object.assign(chartContext.series, options._ek.names[series])} ;
        chartContext.series.data = dataSet;
        return chartContext
    }
}
