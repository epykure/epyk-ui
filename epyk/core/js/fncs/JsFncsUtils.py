"""

"""


class JsColSum(object):
  """
  Get the result only on the selected column. This function will return a dictionary with the column name and the sum
  """
  alias = "sum(Column)"
  params = ("column", )
  value = '''
    var value = 0;
    data.forEach( function(rec) {if (rec[column] !== undefined) { value += rec[column]; }})
    result = {label: column, value: value};
  '''


class JsColStats(object):
  """
  Get the result only on the selected column. This function will return a dictionary with the column name and the sum
  """
  alias = "stats(Column)"
  params = ("column", )
  value = '''
    var value = 0; var countVals = 0;
    data.forEach( function(rec) {if (rec[column] !== undefined) { value += rec[column]; countVals ++; }})
    result = {label: column, value: value, count: countVals, average: value/countVals};
  '''


class JsMarkUp(object):
  """

  """
  alias = "toMarkUp"
  value = '''
    data = data.replace(/\*\*(.*?)\*\*/g, "<b>$1</b>");
    data = data.replace(/\*\*\*(.*?)\*\*\*/g, "<b><i>$1</i></b>");
    data = data.replace(/\*(.*?)\*/g, "<i>$1</i>");
    data = data.replace(/__(.*?)__/g, "<u>$1</u>");
    data = data.replace(/~~(.*?)~~/g, "<i>$1</i>");
    data = data.replace(/--(.*?)--/g, "<del>$1</del>");
    data = data.replace(/<<(.*?)>>/g, "<a href='$1'>Link</a>");
    data = data.replace(/\!\((.*?)\)/g, "<i class='$1'></i>");
    data = data.replace(/\[(.*?)\]\(https\\\:(.*?)\)/g, "<a href='$2' target='_blank'>$1</a>");
    data = data.replace(/\[(.*?)\]\(http\\\:(.*?)\)/g, "<a href='$2' target='_blank'>$1</a>");
    data = data.replace(/\[(.*?)\]\((.*?)\)/g, "<a href='$2'>$1</a>");
    if ( (data == '') || ( data == '__' ) ) { data = '<br />'; }
    result = data ;
    '''

