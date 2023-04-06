

function stateTemplate(status, htmlObj, data, options, cssStyle){
  var divLoading = htmlObj.querySelector('[name=loading]');
  if(divLoading !== nul){divLoading.remove()}
  if (status){
        var divLoading = document.createElement("div");
        divLoading.style.width = '100%'; divLoading.style.height = '100%'; divLoading.style.background = '%(background)s';
        divLoading.style.position = 'absolute'; divLoading.style.top = 0; divLoading.style.left = 0;
        divLoading.style.zIndex = %(z_index)s; divLoading.style.textAlign = 'center';
        divLoading.style.display = 'table';
        var divLoadingContainer = document.createElement("p"); divLoadingContainer.style.display = 'table-cell';
        divLoadingContainer.style.verticalAlign = 'middle';
        var divLoadingIcon = document.createElement("i"); divLoadingIcon.classList.add("fas", "fa-spinner", "fa-spin");
        divLoadingIcon.style.marginRight = "5px"; divLoadingContainer.appendChild(divLoadingIcon);
        var divLoadingContent = document.createElement("span"); divLoadingContent.innerHTML = %(label)s;
        divLoadingContainer.appendChild(divLoadingContent);
        divLoading.appendChild(divLoadingContainer); htmlObj.appendChild(divLoading)
  } else {
    window['popup_loading_%(htmlId)s'].remove(); delete window['popup_loading_%(htmlId)s'];
  }
}