
function trafficLight(htmlObj, data, options){
    if(data === false){htmlObj.firstChild.style.backgroundColor = options.red}
    else if (data === true){htmlObj.firstChild.style.backgroundColor = options.green}
    else if (data === null){htmlObj.firstChild.style.backgroundColor = options.orange}
    else {htmlObj.firstChild.style.backgroundColor = data}
}