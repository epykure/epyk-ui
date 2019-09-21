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
  alias = "toMarkUp"
  params = ("data", )
  value = '''
    data = ""+data;
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
    if ((data == '') || ( data == '__' )){ data = '<br />'};
    result = data
    '''


class JsFormatNumber(object):
  """

  """
  alias = "formatNumber"
  params = ("n", "decPlaces", "thouSeparator", "decSeparator")
  value = '''
    decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 2 : decPlaces,
    decSeparator = decSeparator == undefined ? "." : decSeparator,
    thouSeparator = thouSeparator == undefined ? "," : thouSeparator,
    sign = n < 0 ? "-" : "",
    i = parseInt(n = Math.abs(+n || 0).toFixed(decPlaces)) + "",
    j = (j = i.length) > 3 ? j % 3 : 0;
    return sign + (j ? i.substr(0, j) + thouSeparator : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thouSeparator) + (decPlaces ? decSeparator + Math.abs(n - i).toFixed(decPlaces).slice(2) : "");
    '''
