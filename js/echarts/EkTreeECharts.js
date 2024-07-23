
function ekTreeECharts(data, options){
    let chartContext = getChartContext(options); chartContext.series = [] ;
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
