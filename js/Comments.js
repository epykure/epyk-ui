
function comments(htmlObj, data, options){
    if (data != null){
          let comments;
          if(!Array.isArray(data)){let now = new Date();
            comments = [{text: data, time: moment(now).format(options.timestamp_format)}];
          } else {comments = data}
          comments.forEach(function(comment){
            if (typeof comment !== "object"){
                comment = {text: comment, time: moment((new Date())).format(options.timestamp_format)}};
            let feed = document.createElement("p"); feed.classList.add(options.feed);
            if(options.showdown){
              let converter = new showdown.Converter(options.showdown);
              comment.text = converter.makeHtml(comment.text.trim())};
            feed.innerHTML = comment.text; htmlObj.querySelector("div").prepend(feed);
            let dateNews = document.createElement("p"); dateNews.classList.add(options.timestamp) ;
            dateNews.innerHTML = comment.time; htmlObj.querySelector("div").prepend(dateNews);
          }); document.getElementById(htmlObj.id  + "_counter").innerHTML = data.length ;
    }
}