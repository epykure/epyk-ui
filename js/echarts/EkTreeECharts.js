
function ekTreeECharts(data, options){
    let chartContext = getChartContext(options); chartContext.series = [] ;
    if (!data || data.length == 0){return options}
    else {
        let xAxis = options._ek.chart.x_axis.split('/') ;
        let tree = {}; let activeBranch = {};
        data.forEach(function(row){
            activeBranch = tree;
            for (const y of xAxis) {
                let branchValue = row[y];
                if(!branchValue){break};
                if(!activeBranch[branchValue]){activeBranch[branchValue] = {}};
                activeBranch = activeBranch[branchValue];
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
                    let rec = {name: key, size: 0, value: 0, children: [], path: path.join("/")};
                    hyr.push(rec); processNode(v, rec.children, path);
                    rec.children.forEach(function(t){
                        rec.size = rec.size + t.size; rec.value = rec.value + t.value});
                }
                else {
                    path.push(key); hyr.push({name: key, size: v, value: v, path: path.join("/")})}
            });
        };
        dataSet = []; processNode(tree, dataSet, []);
        if (typeof options._ek.series !== 'undefined'){
          Object.assign(chartContext.series, options._ek.series)}
        if ((typeof options._ek.names !== 'undefined') && (typeof options._ek.names[series] !== 'undefined')){
          Object.assign(chartContext.series, options._ek.names[series])} ;
        chartContext.series = [{data: dataSet, type: options._ek.chart.type}];

        if(typeof options?._ek?.alterSeries !== 'undefined'){
            chartContext.series.forEach(function(s, i){options._ek.alterSeries(s, i)})};
        return chartContext
    }
}
