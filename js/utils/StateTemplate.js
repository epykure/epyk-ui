
function hideState(htmlObj){
    var loadingObj = htmlObj.querySelector('[name="loading"]');
    if (loadingObj !== null){
            loadingObj.remove()
    }
}


function stateTemplate(status, htmlObj, data, options, cssStyle){
  if (options.templateMode == 'loading'){data = options.templateLoading(data)}
  else if (options.templateMode == 'error'){data = options.templateError(data);}
  else if (typeof options.template !== 'undefined' && data){data = options.template(data)}
  var divLoading = htmlObj.querySelector('[name=loading]');
  if(divLoading !== null){divLoading.remove()}
  if (status){
        var divLoading = document.createElement("div");
        divLoading.setAttribute("name", "loading"); divLoading.classList.add("html-state-overlay") ;
        if(typeof cssStyle !== 'undefined'){for(var k in cssStyle){divLoading.style[k] = cssStyle[k]}}
        var divLoadingContainer = document.createElement("p"); divLoadingContainer.style.display = 'table-cell';
        divLoadingContainer.style.verticalAlign = 'middle';
        var divLoadingContent = document.createElement("span"); divLoadingContent.innerHTML = data;
        divLoadingContainer.appendChild(divLoadingContent);
        htmlObj.style.position = "relative";
        divLoading.appendChild(divLoadingContainer); htmlObj.appendChild(divLoading)
  }
}