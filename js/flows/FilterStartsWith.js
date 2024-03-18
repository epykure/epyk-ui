
function filterStartsWiths(records, {key, value, caseSensitive=true}){
    let n=[];
    records.forEach(function(e){
        if (caseSensitive){if(e[key].startsWith(value)){n.push(e)}}
        else {if(e[key].toUpperCase().startsWith(value.toUpperCase())){n.push(e)}}
     });
    return n
}
