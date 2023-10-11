function colorFromRaw(ctx, color, border) {
  if (ctx.type !== 'data') {
    return 'transparent';
  }
  const value = ctx.raw.v;
  let alpha = (1 + Math.log(value)) / 5;
  if (border) {
    alpha += 0.5;
  }
  return Chart.helpers.color(color)
    .alpha(alpha)
    .rgbString();
};

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
          dataset.backgroundColor = function(ctx) {
              var item = ctx.dataset.data[ctx.dataIndex];
              if (item){
                    var a = item.v / (item.gs || item.s) / 2 + 0.5;
                    var colorsMaps = options.commons.backgroundColorMaps;
                    if(colorsMaps[item.g]){return colorFromRaw(ctx, colorsMaps[item.g])}
                    if(item.l === 0){return Chart.helpers.color(options.commons.colors.light).alpha(a).rgbString()}
                    if(item.l === 1){return Chart.helpers.color("white").alpha(0.3).rgbString()}
                    return colorFromRaw(ctx, Chart.helpers.color(options.commons.colors.base).alpha(a).rgbString())
                }
          }
        } else {
          dataset.borderColor = function(ctx){ return colorFromRaw(ctx, options.colors[i], true)};
          dataset.backgroundColor = function(ctx){ return colorFromRaw(ctx, options.colors[i])}
        };
        if ((typeof options.props !== 'undefined') && (typeof options.props[i] !== 'undefined')){
           for(var attr in options.props[i]){dataset[attr] = options.props[i][attr]}}
        else if(typeof options.commons !== 'undefined'){
           for(var attr in options.commons){dataset[attr] = options.commons[attr]}}
        if ((typeof options.datasets !== 'undefined') && (typeof options.datasets[i] !== 'undefined')){
          dataSet = Object.assign(dataSet, options.datasets[i])}
      })
    };
    return result
}