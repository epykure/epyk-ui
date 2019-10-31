# <span class="fas fa-spinner fa-spin" style="padding:auto;margin:auto;font-size:65px;"></span>

STATIC_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
%(header)s
%(jsImports)s
%(cssImports)s
<style>
%(cssStyle)s
</style>
</head>

<body>
  <div id="page_content" style="%(cssContainer)s">
  %(content)s
  </div>
</body>

<script>
%(jsFrgs)s
</script>

</html>
'''

JUPYTER = '''
<!DOCTYPE html>
<HTML>
<style>
    %(cssStyle)s
</style>
%(cssImports)s
%(jsImports)s

%(content)s
<script>
    %(jsFrgs)s
</script>
</HTML>
'''

DATA = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Cache-control" content="no-cache">
<meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0"/>
{{ favicon|safe }}

<title>{{ title }}</title>
{{ cssImports|safe }}
{{ jsImports|safe }}

<style>
{{ cssStyle|safe }}
</style>

<script>
{{ jsGlobal|safe }}

$(document).ready(function() {var main_t0 = performance.now(); {{ jsDocumentReady|safe }}; console.log('|Total||'+ (performance.now()-main_t0))});

window.onload = function() { {{ jsWindowLoad|safe }} };

$(window).bind("pageshow", function(event) {$("div[name='loading']").hide()});

$(window).on('beforeunload', function(){
    if (typeof NO_UNLOAD === 'undefined') {$("div[name='loading']").show()}
    else {
        if (NO_UNLOAD == true) {NO_UNLOAD=false;}
        else { $("div[name='loading']").show()}}
});
</script>

</head>
<body onclick="$('#popup').hide()">

<div id="page_content">
{{ content|safe }}
</div>

<div id="popup_loading_back" name="loading" style="display:none;">&nbsp;</div>

<div id="popup_loading" name="loading" style="display:none;">
    <img src="/static/images/loading.gif">
    <div style="font-size:15px;font-style:italic;font-family:Calibri;color:#838383">Please wait</div>
</div>
<br />
<footer class="footer" style="bottom:0;display:block;margin:0;padding:0" id="footer">
  <div style="width:100%%;margin:0;padding:0">
    <span style="float:left"></span>
    <span style="float:right"><a class='py_cssstandardlinks' onclick="window['NO_UNLOAD'] = true; " href="mailto:{{mailTo|safe}}">Contact Us</a></span>
  </div>
  <div>
      <span style="display:inline-block;text-align:justify;width:100%%;margin-bottom:15px;margin-top:20px"></span>
  </div>
</footer>
</body>
</html>
'''