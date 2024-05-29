
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
            if(rec[options.title]){btn.setAttribute("title", rec[options.title])} ;
            if(options.selection && (options.selection.includes(rec[options.value]))){
                btn.classList.add(options.selected)} ;
            if(rec[options.style]){
                if(typeof rec[options.style] === "object"){
                    for(var k in rec[options.style]){btn.style[k] = rec[options.style][k]}
                }
                else {rec[options.style].split(" ").forEach(function (className) {btn.classList.add(className);})}
            } ;
            if(rec[options.attributes]){
                for(var k in rec[options.attributes]){btn.setAttribute(k, rec[options.attributes][k])}} ;
            htmlObj.appendChild(btn)
        })
    }
}