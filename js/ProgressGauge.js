

function progressGauge(htmlObj, data, options){
    if((Array.isArray(data)) && (data.length > 0)){data = data[0]}
    if (options.value){data = data[options.value]};
    var $bar = $(document.querySelector("#"+ htmlObj.id +" div[name='bar']"));
    var $val = $(htmlObj).find("span"); $({p:0}).animate({p:data}, {
        duration: 3000, easing: "swing",
        step: function(p) {
          $bar.css({transform: "rotate("+ (45+(p*1.8)) +"deg)"}); $val.text(p|0);
        }
      })
}