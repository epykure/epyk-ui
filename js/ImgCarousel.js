

function imgCarousel(htmlObj, data, options){
    data.forEach(function(rec, i){
        var li = document.createElement('li');
        if (i == 0) {li.style.display = 'block'} else{li.style.display = 'none'};
        var img = document.createElement('img'); img.src = rec.path +'/'+ rec.image; li.appendChild(img);
        var title = document.createElement('h3'); title.innerHTML = rec.title; li.appendChild(title);
        htmlObj.appendChild(li);
        var label = document.createElement('label'); label.style.backgroundColor = options.color;
        label.style.borderRadius = '20px'; label.for = i; label.innerHTML = '&nbsp;';
        document.getElementById(htmlObj.id +'_bullets').appendChild(label)
      })
}