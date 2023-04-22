

function chartTreeMap(data, options){
    if(data.python){
      result = {datasets: [], labels: data.labels};
      data.datasets.forEach(function(dataset, i){
        if(typeof dataset.backgroundColor === "undefined"){dataset.backgroundColor = options.background_colors};
        if(typeof dataset.borderColor === "undefined"){dataset.borderColor = options.colors};
        if(typeof dataset.hoverBackgroundColor === "undefined"){
          dataset.hoverBackgroundColor = options.background_colors};
        if(typeof options.commons !== "undefined"){Object.assign(dataset, options.commons)};
        result.datasets.push(dataset)})
    } else {
      result = {datasets: [], labels: []};
      result.datasets.push({
        tree: data, key: options.y_columns[0], groups: options.groups, labels: {display: true}});
      result.datasets.forEach(function(dataset, i){
        if (options.commons.backgroundColorMaps){
          dataset.backgroundColor = function(ctx) {var item = ctx.dataset.data[ctx.dataIndex];
              if (item){
                var a = item.v / (item.gs || item.s) / 2 + 0.5;
                var colorsMaps = options.commons.backgroundColorMaps; if(colorsMaps[item.g]){return colorsMaps[item.g]}
                if(item.l === 0){return Chart.helpers.color(options.commons.colors.light).alpha(a).rgbString()}
                if(item.l === 1){return Chart.helpers.color("white").alpha(0.3).rgbString()}
                else{return Chart.helpers.color(options.commons.colors.base).alpha(a).rgbString()}}}
        } else {
          dataset.backgroundColor = options.colors[i];
        }
      })
    }; return result
}