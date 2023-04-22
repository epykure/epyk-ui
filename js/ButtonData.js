

function buttonData(htmlObj, data, options){
    htmlObj.setAttribute("data-content", JSON.stringify(data));
    htmlObj.setAttribute("title", ""+ data.length + " row loaded: " + (new Date()).toISOString().slice(0, 19).replace("T", " "));
    if(data.length > 0){htmlObj.style.visibility = "visible"}
}