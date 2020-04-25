# <span class="fas fa-spinner fa-spin" style="padding:auto;margin:auto;font-size:65px;"></span>

STATIC_PAGE = '''
<!DOCTYPE html>
<html lang="en" style="height:100%%">
<head>
%(header)s
%(jsImports)s
%(cssImports)s
<style>
%(cssStyle)s
</style>
</head>
%(body)s
<script>
%(jsFrgs)s
</script>
</html>
'''

JUPYTER = '''
<head>
<style>
    %(cssStyle)s
</style>
%(cssImports)s
%(jsImports)s
</head>
<body>
%(content)s
<script>
require.config({ paths:%(req_config)s});
$(document).ready(function() {
  %(jsFrgs)s
})
</script>
<body>
'''
