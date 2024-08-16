
function elapsed(htmlObj, data, options){
    setCss(htmlObj, options, true); data = getDataFromTemplate(data, options);
    var startDate = new Date(data.year, data.month-1, data.day);
    var now = new Date().getTime(); var distance = now - startDate.getTime();
    var days = Math.floor(distance / (1000 * 60 * 60 * 24)); var years = 0;
    if (days > 365){years = Math.floor(days / 365); days = days - years * 365}
    if (years > 0){htmlObj.querySelector("span[name=clock]").innerHTML = "<b>"+ years +"y, "+ days +"d </b>"}
    else {htmlObj.querySelector("span[name=clock]").innerHTML = "<b>"+ days +"d </b>"}
}