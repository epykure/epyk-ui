
function trafficLight(htmlObj, data, options){
    let tf = htmlObj.firstChild;
    if (!tf){tf = htmlObj};
    if(data === false){
        tf.setAttribute("data-status", options.red); tf.style.backgroundColor = options.red}
    else if (data === true){
        tf.setAttribute("data-status", options.green); tf.style.backgroundColor = options.green}
    else if (data === null){
        tf.setAttribute("data-status", options.orange); tf.style.backgroundColor = options.orange}
    else {
        tf.setAttribute("data-status", data); tf.style.backgroundColor = data}
}