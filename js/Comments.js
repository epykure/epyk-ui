

function comments(htmlObj, data, options){
    if (data != null){
          var comments;
          if(!Array.isArray(data)){ var now = new Date();
            comments = [{text: data, time: moment(now).format('YYYY-MM-DD HH:mm:ss')}];
          } else {comments = data}
          comments.forEach(function(comment){
            var feed = document.createElement("p"); feed.style.margin = "0 0 5px 0";
            if(options.showdown){var converter = new showdown.Converter(options.showdown);
            comment.text = converter.makeHtml(comment.text.trim())};
            feed.innerHTML = comment.text; htmlObj.querySelector("div").prepend(feed);

            var dateNews = document.createElement("p");
            dateNews.style.margin = 0;
            dateNews.style.fontWeight = 'bold';
            dateNews.innerHTML = comment.time;
            htmlObj.querySelector("div").prepend(dateNews);
          })
        }
}