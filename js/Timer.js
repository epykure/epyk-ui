
function timer(htmlObj, data, options){
    var time = data.minutes * 60, r = htmlObj, tmp=time;
      window["time_" + htmlObj.id] = setInterval(function(){
        if(tmp < 0){
          if(typeof options.end !== 'undefined'){eval(options.end)}
          clearInterval(window["time_" + htmlObj.id])}
        if (tmp >= 0){
          var c=tmp--, m = (c/60)>>0, s=(c-m*60)+'';
          r.textContent = data.text + ' '+ m +':'+ (s.length>1?'': '0')+ s}
        tmp != 0 || (tmp=0)}, 1000)
}
