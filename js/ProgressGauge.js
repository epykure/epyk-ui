

function progressGauge(htmlObj, data, options){
    if((Array.isArray(data)) && (data.length > 0)){data = data[0]}
    if(options.value){data = data[options.value]};
    htmlObj.innerHTML = "" ;

    let progOverFlow = document.createElement("div"); progOverFlow.classList.add("html-prog-flow") ;
    progOverFlow.style.width = options.width ; progOverFlow.style.height = options.height ;
    progOverFlow.style.marginBottom = - parseFloat(options.width) / 4 + "px" ;

    let progBar = document.createElement("div"); progBar.classList.add("html-prog-bar") ;
    let heightVal = parseFloat(options.height); progBar.style.width = options.width;
    progBar.style.height = 2 * heightVal + options.height.replace('' + heightVal, '');
    progBar.setAttribute("name", "bar") ;
    let progSpan = document.createElement("span"); progSpan.classList.add("html-prog-text") ;

    progOverFlow.appendChild(progBar); htmlObj.appendChild(progOverFlow); htmlObj.appendChild(progSpan);
    let progSymbol = document.createTextNode(options.symbol); htmlObj.appendChild(progSymbol);

    let $bar = $(progBar); let $val = $(progSpan); $({p:0}).animate({p:data}, {
        duration: 3000, easing: "swing",
        step: function(p) {$bar.css({transform: "rotate("+ (45+(p*1.8)) +"deg)"}); $val.text(p|0)}
    })
}