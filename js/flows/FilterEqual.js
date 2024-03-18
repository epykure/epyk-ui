
function filterEqual(records, {key, value, caseSensitive=true}){
    if (value == ''){return records};
    let n = [];
    records.forEach(function(e){
        if (caseSensitive){if(e[key] == value){n.push(e)}}
        else {if(e[key].toUpperCase() == value.toUpperCase()){n.push(e)}}
    });
    return n
}