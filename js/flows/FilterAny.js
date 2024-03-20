

function filterAny(records, {value, keys=null, caseSensitive=false}){
    if (value == ''){return r};
    if (!caseSensitive){value = value.toUpperCase()};
    let n = [];
    records.forEach(function(e){
      if (keys){
        for(const k in keys){
          if (!caseSensitive){if(String(e[k]).toUpperCase().includes(v)){n.push(e); break;}}
          else {if(e[k].includes(v)){n.push(e); break;}}}}
      else {
        for(const k in e){
          if (!caseSensitive){if(String(e[k]).toUpperCase().includes(v)){n.push(e); break;}}
          else {if(e[k].includes(v)){n.push(e); break;}}
        }
      }
    });
    return n
}