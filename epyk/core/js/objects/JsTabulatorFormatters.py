"""

"""


import inspect
import sys

# The columns definition factory
factory = None


def definedFormats(refresh=False):
  """

  :param refresh:
  :return:
  """
  global factory

  if factory is None or refresh:
    tmpFactory = {}
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
      if getattr(obj, 'alias', None) not in [None, '__main__']:
        tmpFactory[obj.alias] = obj
    # Atomic function to avoid asynchronous clashes on the server
    factory = tmpFactory
  return factory

def getFormatters():
  """

  :return:
  """
  global factory

  if factory is None:
    definedFormats()
  return factory

def addColFormatter(alias, pyCls):
  """

  :param alias:
  :param pyCls:

  :return:
  """
  global factory

  if factory is None:
    definedFormats()
  factory[alias] = pyCls


# --------------------------------------------------------------------------------------------------------------
#
#                                     STYLE DEFINITION FOR COLUMNS
# --------------------------------------------------------------------------------------------------------------
class TabulatorColStyleUrl(object):
  """

  """
  depsMod, depFncs = None, None
  alias = 'url'
  _dflts = {'target': '_blank'}
  jsCreatedCell = '''
    var row = cell.getRow().getData(); var url = '%(url)s';
    result =  "<a href='"+ url +"' target='%(target)s'>" + cell.getValue() + "</a>"'''


class TabulatorColStyleNumber(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  alias = 'number'
  _dflts = {'digits': 0, 'threshold': 0, 'red': 'red', 'white': 'white', 'css': {}}
  jsCreatedCell = '''
    if (cell.getValue() < %(threshold)s) {$(cell.getElement()).css({'color': '%(red)s'})}
    else {$(cell.getElement()).css({'color': '%(white)s'})};
    $(cell.getElement()).css(%(css)s);
    result = parseFloat(cell.getValue()).formatMoney(%(digits)s, ',', '.')'''


class TabulatorColStyleNumberFactor(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  alias = 'factor'
  _dflts = {'digits': 0, 'threshold': 0, 'red': 'red', 'white': 'white', 'css': {}}
  jsCreatedCell = '''
    if (cell.getValue() < %(threshold)s) {$(cell.getElement()).css({'color': '%(red)s'})}
    else {$(cell.getElement()).css({'color': '%(white)s'})};
    $(cell.getElement()).css(%(css)s); var cellVal = parseFloat(cell.getValue()) / %(factor)s;
    result = cellVal.formatMoney(%(digits)s, ',', '.')'''


class TabulatorColStyleNumberReporting(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  alias = 'number-reporting'
  _dflts = {'digits': 0, 'threshold': 0, 'red': 'red', 'white': 'white', 'css': {}}
  jsCreatedCell = '''
    $(cell.getElement()).css({'color': '%(white)s'});
    if (cell.getValue() < %(threshold)s){
      var val = -1 * parseFloat(cell.getValue());
      result = "("+ val.formatMoney(%(digits)s, ',', '.') + ")"}
    else {result = parseFloat(cell.getValue()).formatMoney(%(digits)s, ',', '.')};
    $(cell.getElement()).css(%(css)s)'''


class TabulatorColStyleOverride(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()

  The variable resetOvrs will reset the row, hence the previous initial value will be re defined.

  Example:
    {'title': 'Order', 'formatters': ['number', 'override'], 'editor': 'input'}
  """
  depsMod, depFncs = None, None
  alias = 'override'
  #  'key': '"solver"', 'values': '["Strike", "Notional"]' #000099
  _dflts = {'digits': 0, 'color': '#81abef', 'background': 'inherit', 'key': 'null', 'values': '[]', 'timer': 'null'}
  jsCreatedCell = '''
    var jqCell = $(cell.getElement());
    var rowData = cell.getRow().getData();
    if(%(key)s !== null) {
      if (%(values)s.indexOf(cell.getRow().getData()[%(key)s]) > -1){
        if ((jqCell.data('init') === undefined) || rowData.resetOvrs){jqCell.data('init', cell.getValue())};
        if(jqCell.data('init') != cell.getValue()){jqCell.css({'color': '%(color)s', 'background': '%(background)s'})}
      }
      else{jqCell.css({'color': 'inherit', 'background': 'inherit'})};
      if (%(timer)s !== null){setTimeout(function(){jqCell.css({'color': 'inherit'})}, %(timer)s)}
    } else {
      if ((jqCell.data('init') === undefined) || rowData.resetOvrs){jqCell.data('init', cell.getValue())};
      if(jqCell.data('init') != cell.getValue()){
        jqCell.css({'color': '%(color)s', 'background': '%(background)s'});
        if (%(timer)s !== null){setTimeout(function(){jqCell.css({'color': 'inherit'})}, %(timer)s * 1000)}}
    }'''


class TabulatorColStylePassword(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  alias = 'password'
  _dflts = {}
  jsCreatedCell = '''
    if (cell.getValue() === undefined){result = ""}
    else{result = cell.getValue().replace(/./g, '*')}
    '''


class TabulatorColIcon(object):
  """

  """
  depsMod, depFncs = None, None
  alias = 'icon'
  reqJs = ['font-awesome']
  _dflts = {'displayVal': 'null', 'css': {}}
  jsCreatedCell = '''
    if(%(displayVal)s !== null){
      if (cell.getValue() == %(displayVal)s){
        $(cell.getElement()).css(%(css)s);
        return "<i class='%(icon)s'></i>"}
      else {result = ""}
    } else {
      $(cell.getElement()).css(%(css)s);
      result = "<i class='%(icon)s'></i>"}
    '''


class TabulatorColTick(object):
  depsMod, depFncs = None, None
  alias = 'ticks'
  reqJs = ['font-awesome']
  _dflts = {'css': {}, 'valid': 'true', 'wrong': 'false', 'success': '#3bb194', 'failure': '#C00000',
            'true': 'fas fa-check', 'false': 'fas fa-times', 'clickable': 'true'}
  jsCreatedCell = '''
    if (%(clickable)s){ $(cell.getElement()).css("cursor", "pointer")};
    if (cell.getValue() === %(wrong)s){result = "<i style='color:%(failure)s' class='%(false)s'></i>"}
    else if(cell.getValue() === %(valid)s) { result = "<i style='color:%(success)s' class='%(true)s'></i>"}
    else { result = "" }
    '''


class TabulatorColStyleAge(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  reqJs = ['d3']
  alias = 'age'
  _dflts = {'background': 'white', 'red': 'red', 'steps': 100, 'factor': 100, 'column': 'age'}
  jsCreatedCell = '''
    var row = cell.getRow().getData();
    var column = cell.getColumn().getField() + '.%(column)s';
    if(row[column] !== undefined){
      var colorFnc = d3.scaleLinear().domain([1, %(steps)s]).range([d3.rgb('%(background)s'), d3.rgb('%(red)s')]);
      cell.getElement().style.background = colorFnc(%(factor)s * row[column]);
      if(row[column] > 0.5){cell.getElement().style.color = 'white'}
    } '''


class TabulatorColStyleQuality(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  reqJs = ['d3']
  alias = 'quality'
  _dflts = {'background': 'white', 'red': 'red', 'steps': 100, 'factor': 100, 'column': 'age'}
  jsCreatedCell = '''
    var row = cell.getRow().getData();
    var column = cell.getColumn().getField() + '.%(column)s';
    if(row[column] !== undefined){
      var colorFnc = d3.scaleLinear().domain([1, %(steps)s]).range([d3.rgb('%(background)s'), d3.rgb('%(red)s')]);
      cell.getElement().style.border  = '1px solid '+  colorFnc(%(factor)s * row[column])
    } '''


class TabulatorColStyleControl(object):
  """

  to get the column name cell.getColumn().getField()
  to get the row cell.getRow().getData()
  cell.getOldValue()
  """
  depsMod, depFncs = None, None
  alias = 'control'
  _dflts = {'css': {}, 'red': 'red', 'green': 'green', 'yellow': 'yellow', 'size': 15}
  jsCreatedCell = '''
    var cellData = cell.getValue(); var mainDiv = $('<div style="padding:auto"></div>'); var iDiv = $('<div></div>');
    iDiv.css({"width": "%(size)spx", "height": "%(size)spx", "border-radius": "10px", "margin": "auto", "display": "inline-block", "vertical-align": "middle"});
    if ((typeof cellData.val === 'undefined') || (cellData.val == null)){iDiv.css({"background": "%(yellow)s"})}
    else if (cellData.val){iDiv.css({"background": "%(green)s"})}
    else {iDiv.css({"background": "%(red)s"})};
    if (typeof cellData.title != 'undefined'){iDiv.attr("title", cellData.title)}; 
    if (typeof cellData.text != 'undefined'){mainDiv.append("<span style='vertical-align:middle;display:inline-block;margin-right:10px'>"+ cellData.text +"</span>")}; 
    iDiv.css(%(css)s); mainDiv.append(iDiv); result = mainDiv.get(0)'''
