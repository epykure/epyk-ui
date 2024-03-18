

function filterMatch(records, {rules, caseSensitive=true}){
    if(typeof records === 'undefined'){return []};
    if(!rules){return records};
    let n=[];
    records.forEach(function(e){
        var isValid = true;
        if (caseSensitive){
            for(let a in rules){if(!rules[a].includes(e[a])){isValid = false; break}};
        } else {
            for(let a in rules){if(!rules[a].toUpperCase().includes(e[a].toUpperCase())){isValid = false; break}};
        }
        if(isValid){n.push(e)}});
    return n
}
