

function chartSunbrust(data, options){
    var result = [{name: options.x_axis, children: []}]; var sizeTree = options.y_columns.length-1;
      data.forEach(function(rec){
        var path = []; var tmpResultLevel = result[0].children; var branchVal = 0;
        options.y_columns.forEach(function(s, i){
          var treeLevel = -1;
          tmpResultLevel.forEach(function(l, j){if(l.name == rec[s]){treeLevel = j}});
          if(i == sizeTree){
            if(treeLevel >= 0){
              tmpResultLevel[treeLevel].size += rec[options.x_axis]}
            else{tmpResultLevel.push({name: rec[s], size: rec[options.x_axis]})}
          }else{
            if(treeLevel < 0 ){
              tmpResultLevel.push({name: rec[s], children: []}); treeLevel = tmpResultLevel.length - 1};
              tmpResultLevel = tmpResultLevel[treeLevel].children}
        })}); return result
}