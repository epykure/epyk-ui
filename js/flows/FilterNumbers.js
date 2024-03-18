

function filterNumbers(records, {key, value, type, strict=true}){
    let n = [];
    if (type == "sup"){
        if (strict){records.forEach(function(e){if(e[key] > value){n.push(e)}})}
        else {records.forEach(function(e){if(e[key] >= value){n.push(e)}})}
    }
    if (type == "inf"){
        if (strict){records.forEach(function(e){if(e[key] < value){n.push(e)}})}
        else {records.forEach(function(e){if(e[key] <= value){n.push(e)}})}
    }
    return n
}