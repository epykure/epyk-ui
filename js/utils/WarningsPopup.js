

function signOffModal(e, callbacks, attrs){
    const popup = document.createElement("div");
    popup.innerHTML = attrs.text ? attrs.text : "Are you sure you want to proceed?";
    popup.setAttribute("tabindex", "0");
    popup.setAttribute("class", "warning-model");
    popup.style.boxShadow = 'rgba(99, 99, 99, 0.2) 0px 2px 8px 0px';
    popup.style.width = 'auto';
    popup.style.padding = '2px 5px';
    popup.style.position = 'absolute';
    popup.style.top = 15 + e.clientY + window.pageYOffset + "px";
    popup.style.left = e.clientX + window.pageXOffset + "px";
    const validate = document.createElement("span");
    validate.style.color = '#006100';
    validate.style.cursor = 'pointer';
    validate.style.margin = '0 5px';
    validate.innerHTML = attrs.validate ? attrs.validate : "&#10003;Yes";
    validate.addEventListener("click", callbacks);
    validate.setAttribute("tabindex", "0");
    const cancel = document.createElement("span");
    cancel.style.color = '#9C0006';
    cancel.style.cursor = 'pointer';
    cancel.style.margin = '0 5px';
    cancel.innerHTML = attrs.cancel ? attrs.cancel : "&#x2718;No";
    cancel.setAttribute("tabindex", "0");
    popup.appendChild(cancel);
    popup.appendChild(validate);
    document.body.appendChild(popup);
    function fOut(event){if(popup.contains(event.relatedTarget)) {return ;}; popup.remove();}
    popup.focus(); popup.addEventListener("focusout", fOut);
    validate.addEventListener("click", function(){popup.removeEventListener("focusout", fOut); popup.remove()});
    cancel.addEventListener("click", function(){popup.removeEventListener("focusout", fOut); popup.remove()});
}