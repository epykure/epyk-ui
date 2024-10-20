

function progressCircle(htmlObj, data, options){
    if((Array.isArray(data)) && (data.length > 0)){data = data[0]}
    if (options.value){data = data[options.value]};
    htmlObj.style.setProperty('--start', htmlObj.getAttribute('aria-valuenow'));
    htmlObj.style.setProperty('--value', data); htmlObj.style.webkitAnimation = 'none';
    setTimeout(function(){htmlObj.style.webkitAnimation = '';}, 1)
}