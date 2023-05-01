

function Switch(htmlObj, data, options){
    if (data.off == data.checked){
        htmlObj.querySelector("input").checked = false; htmlObj.querySelector("p").innerHTML = data.off}
      else {htmlObj.querySelector("input").checked = true; htmlObj.querySelector("p").innerHTML = data.on};
      window[htmlObj.getAttribute('id') +"_data"] = data
}