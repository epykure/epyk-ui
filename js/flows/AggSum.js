

function aggSum(records, {columns, attrs = null}){
    let result = {}; columns.forEach(function(c){result[c] = 0});
    records.forEach(function(v){
        columns.forEach(function(c){
            if(typeof v[c] !== 'undefined'){result[c] += v[c]}})});
    if(attrs){for(let attr in attrs){result[attr] = attrs[attr]}}; return [result]
}