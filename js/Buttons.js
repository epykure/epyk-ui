
function buttons(htmlObj, data, options){
    htmlObj.innerHTML = "";
    if(data){
        data.forEach(function(rec, i){
            let btn = document.createElement("button");
            btn.innerHTML = rec[options.value] ;
            btn.id = htmlObj.id + "_" + i ;
            btn.onclick = function() {
                if(options.max){
                    if (options.max == 1){
                        if(btn.classList.contains(options.selected)){
                            document.querySelectorAll("div#" + htmlObj.id + " button."+ options.selected).forEach(function(d){
                                d.classList.remove(options.selected);
                            });
                        }
                        else {
                            document.querySelectorAll("div#" + htmlObj.id + " button."+ options.selected).forEach(function(d){
                                d.classList.remove(options.selected);
                            });
                            btn.classList.add(options.selected);
                        }
                    } else {
                        if(btn.classList.contains(options.selected)){ btn.classList.remove(options.selected)}
                        else if (document.querySelectorAll("div#" + htmlObj.id + " button."+ options.selected).length <  options.max){
                            btn.classList.add(options.selected);
                        }
                    }
                } else {
                    btn.classList.toggle(options.selected)
                }
            } ;

            if(typeof options.css !== 'undefined'){for(var k in options.css){btn.style[k] = options.css[k]}} ;
            if(options.classes){options.classes.forEach(function (className) {btn.classList.add(className);});}
            if(rec[options.selected]){btn.classList.add(options.selected)} ;
            if(rec[options.disabled]){btn.disabled = rec[options.disabled]} ;
            htmlObj.appendChild(btn)
        })
    }
}