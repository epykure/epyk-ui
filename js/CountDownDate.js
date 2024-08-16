

function countDownDate(htmlObj, data, options){
      setCss(htmlObj, options, true);
      var endDate = new Date(data.year, data.month-1, data.day, data.hour, data.minute, data.second);
      var now = new Date().getTime(); var distance = endDate.getTime() - now;
      if(distance < 0){distance = -distance}
      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);
      var dtString = [];
      if(days > 0){dtString.push(days +"d")}
      if(hours > 0){dtString.push(hours +"h")}
      if(minutes > 0){dtString.push(minutes +"m")}
      if(seconds > 0){dtString.push(seconds +"s")}
      htmlObj.querySelector("span[name=dt_time]").innerHTML = dtString.join(" ");
      if ((distance < 0) && (options.delete)){
        if(typeof options.end !== 'undefined'){eval(options.end)}
        htmlObj.remove(); if (options.reload){location.reload()}
        clearInterval(window[htmlObj.id +"_interval"])
      }
}