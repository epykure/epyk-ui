

function chartSunbrust(data, options){
    var yDefs; var xDefs;
    if (typeof options.y_columns === 'function') {yDefs = options.y_columns(data, options)} else {yDefs = options.y_columns} ;
    if (typeof options.x_axis === 'function') {xDefs = options.x_axis(data, options)} else {xDefs = options.x_axis} ;
    var result = [{name: xDefs, children: []}]; var sizeTree = yDefs.length-1;
      data.forEach(function(rec){
        var path = []; var tmpResultLevel = result[0].children; var branchVal = 0;
        yDefs.forEach(function(s, i){
          var treeLevel = -1;
          tmpResultLevel.forEach(function(l, j){if(l.name == rec[s]){treeLevel = j}});
          if(i == sizeTree){
            if(treeLevel >= 0){
              tmpResultLevel[treeLevel].size += rec[xDefs]}
            else{tmpResultLevel.push({name: rec[s], size: rec[xDefs]})}
          }else{
            if(treeLevel < 0 ){
              tmpResultLevel.push({name: rec[s], children: []}); treeLevel = tmpResultLevel.length - 1};
              tmpResultLevel = tmpResultLevel[treeLevel].children}
        })}); return result
}