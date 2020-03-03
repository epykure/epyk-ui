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
%(body)s
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
