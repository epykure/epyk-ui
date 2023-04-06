
function checkButton(htmlObj, data, options){
  htmlObj.innerHTML = '';
  if (data === true || data == 'Y'){
    var i = document.createElement("i");
    i.classList.add(...options.icon_check.split(' '));
    i.style.color = options.green; i.style.marginBottom = '2px'; i.style.marginLeft = '2px';
    htmlObj.appendChild(i); htmlObj.parentNode.setAttribute('data-isChecked', true)}
  else {
    var i = document.createElement("i");
    i.classList.add(...options.icon_not_check.split(' '));
    i.style.color = options.red; i.style.marginBottom = '2px'; i.style.marginLeft = '2px';
    htmlObj.appendChild(i); htmlObj.parentNode.setAttribute('data-isChecked', false)
  }
}