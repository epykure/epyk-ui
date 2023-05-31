

function htmlTree(htmlObj, data, options){
    if(options){htmlObj.innerHTML = '';
  if(options.is_root){window[htmlObj.id + "_data"] = data};
	if(options.is_root && options.filter_on){
      function checFiltBranch(items, branchPath, withFilter){
        items.forEach(function(item, i){
          var cloneBranchPath = [...branchPath]; cloneBranchPath.push(i);
        var filtLabel = item.label;
        if (typeof item.label === 'undefined'){filtLabel = item.value}
        if (!withFilter){
          item._meta = {visible: true};
          if(typeof item.items !== 'undefined'){checFiltBranch(item.items, cloneBranchPath, false)}}
        else{
          if(filtLabel.includes(options.filter_on)){
            var dataPoint = data[cloneBranchPath[0]]; dataPoint._meta = {visible: true};
            for (let j = 1; j < cloneBranchPath.length; j++){
              dataPoint = dataPoint.items[cloneBranchPath[j]]; dataPoint._meta = {visible: true}};
            if(typeof item.items !== 'undefined'){checFiltBranch(item.items, cloneBranchPath, false)}}
          else {
            item._meta = {visible: false};
            if(typeof item.items !== 'undefined'){checFiltBranch(item.items, cloneBranchPath, true)}}}
		  })
	  };
	  var currBranchPath = []; checFiltBranch(data, currBranchPath, true)}; options.is_root = false};
      data.forEach(function(item, i){
        if((typeof options.filter_on === 'undefined') || (options.filter_on == '') || item._meta.visible){
        var li = document.createElement("li"); var a = document.createElement("a");
        a.style["white-space"] = 'nowrap';
        if(typeof item.css !== "undefined"){for(const attr in item.css){a.style[attr] = item.css[attr]}};
        if(typeof item.items !== 'undefined'){
          var ul = document.createElement("ul");
          ul.setAttribute("data-depth", parseInt(htmlObj.getAttribute("data-depth")) + 1);
          ul.setAttribute("data-parent", item.value);
          if (!options.expanded){ul.style.display = 'none'};
          for(const attr in options.style){ul.style[attr] = options.style[attr]};
          options.builder(ul, item.items, options);
          var icon = document.createElement("i");
          icon.setAttribute("name", "item_arrow");
          for(const attr in options.icon_style){icon.style[attr] = options.icon_style[attr]};
          icon.onclick = function(){
            if (((typeof options.remote !== "undefined") && ul.children.length == 0) || (options.remoteAlways)){
              options.remote(ul, options, item.value)}
            var ulDisplay = this.parentNode.querySelector('ul').style.display;
            if(ulDisplay == 'none'){
              this.parentNode.querySelector('ul').style.display = 'block';
              icon.setAttribute("class", options.icon_open)}
            else{
              this.parentNode.querySelector('ul').style.display = 'none';
              icon.setAttribute("class", options.icon_close)}
          };
          icon.style.cursor = "pointer"; icon.style.color = "grey";
          if (options.expanded){options.icon_open.split(" ").forEach(function(s){icon.classList.add(s)})}
          else {options.icon_close.split(" ").forEach(function(s){icon.classList.add(s)})}
          var span = document.createElement("span");
          span.setAttribute("data-value", item.value);
          if(typeof item.label !== "undefined"){span.innerHTML = item.label;}
          else {span.innerHTML = item.value};
          span.setAttribute("name", "item_value");
          span.style.whiteSpace = 'nowrap';
          if(typeof options.clickNode !== "undefined"){ span.style.cursor = 'pointer';
            span.onclick = function(event){const value = span.innerText; const data = span.getAttribute("data-value");
            options.clickNode(event, value, data)}};
          if (typeof item.tooltip !== "undefined"){span.setAttribute('title', item.tooltip);};
          var badge = document.createElement("span");
          if(options.with_badge){
            badge.setAttribute("class", "badge badge-pill");
            badge.innerHTML = item.items.length;
            badge.style.padding = 0;
            badge.style.verticalAlign = "top";
            icon.appendChild(badge);
          };
          a.appendChild(icon);
          if (typeof options.with_icon !== "undefined"){
            var subIcon = document.createElement("i"); subIcon.style.marginRight = "5px";
            subIcon.setAttribute("class", item[options.with_icon]); a.appendChild(subIcon)};
          a.appendChild(span); a.appendChild(ul);
        } else {
          var span = document.createElement("span");
          span.setAttribute("data-value", item.value);
          if(typeof item.label !== "undefined"){span.innerHTML = item.label;}
          else {span.innerHTML = item.value};
          span.setAttribute("name", "item_value");
          span.style.whiteSpace = 'nowrap';
          if(item.draggable != false){
            a.setAttribute('draggable', true);
            if (typeof item._path !== "undefined"){a.setAttribute("data-path", item._path)};
            if (typeof item.tooltip !== "undefined"){a.setAttribute('title', item.tooltip);};
            a.style.cursor = 'grab';
            a.ondragstart = function(event){var value = this.innerHTML;
              var file_path = this.getAttribute("data-path");
              if (file_path === null){event.dataTransfer.setData("text", value)}
              else{ event.dataTransfer.setData("text", file_path)}}
          };
          if(typeof options.clickLeaf !== "undefined"){a.style.cursor = 'pointer';
            a.onclick = function(event){const value = a.innerText; const data = span.getAttribute("data-value");
            options.clickLeaf(event, value, data)}};
          if (typeof item.url !== "undefined"){
            a.setAttribute("target", item.target || "_blank");
            a.href = item.url}
          if (typeof options.with_icon !== "undefined"){
            var subIcon = document.createElement("i"); subIcon.style.marginRight = "5px";
            subIcon.setAttribute("class", item[options.with_icon]); a.appendChild(subIcon)};
          a.appendChild(span);
        };
        a.style.paddingLeft = 20 * (parseInt(htmlObj.getAttribute("data-depth")) - 1) + 'px';
        li.appendChild(a);
        htmlObj.appendChild(li)
        }
      })
}