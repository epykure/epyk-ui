"""

"""


import inspect
import sys

# The columns definition factory
factory = None


def definedColumns(refresh=False):
  """

  :param refresh:

  :return:
  """
  global factory

  if factory is None or refresh:
    tmpFactory = {}
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
      if getattr(obj, 'name', None) not in [None, '__main__']:
        tmpFactory[obj.name] = obj
    # Atomic function to avoid asynchronous clashes on the server
    factory = tmpFactory
  return factory

def getEditors():
  """

  :return:
  """
  global factory
  if factory is None:
    definedColumns()
  return factory

def addColEditor(alias, pyCls):
  """

  :param alias:
  :param pyCls:

  :return:
  """
  global factory

  if factory is None:
    definedColumns()
  factory[alias] = pyCls


# --------------------------------------------------------------------------------------------------------------
#
#                                     STYLE DEFINITION FOR COLUMNS
# --------------------------------------------------------------------------------------------------------------
class EditorInput(object):
  """
  :example: {"editor": "inputParams", 'editorParams': {"refresh": True, 'emptyFirst': True}}
  """
  depsMod, depFncs = None, None
  name = "input" # The alias name
  attrs = None # Python attributes to be propagated to the Javascript definition
  jsFnc = '''
  function(cell, onRendered, success, cancel, editorParams){
      var cellValue = cell.getValue(), input = document.createElement("input");
      input.setAttribute("type", "text");
      for (var k in editorParams){input.setAttribute(k, editorParams[k])};
      if (editorParams.refresh === undefined || editorParams.refresh === true){
        input.onkeydown = function() {var key = event.keyCode || event.charCode; 
          if(key == 8 || key == 46){input.value =""; return false}}};
      if (editorParams.emptyFirst === true){   
        input.onkeypress = function() {
          if (cellValue != "" && input.value == cellValue){input.value = ""; cellValue = ""}}};
      input.style.padding = "4px"; input.style.width = "100%";
      input.style.color = "inherit";
      input.style.textAlign = "center";
      input.style.boxSizing = "border-box";
      input.value = typeof cellValue !== "undefined" ? cellValue : "";
      onRendered(function () {input.focus(); input.style.height = "100%"});
      function onChange(e) {
        if ((cellValue === null || typeof cellValue === "undefined") && input.value !== "" || input.value != cellValue) {
          success(input.value)} else {cancel()}}
      input.addEventListener("change", onChange);
      input.addEventListener("blur", onChange);
      input.addEventListener("keydown", function (e) {
        switch (e.keyCode) {
          case 13:
            if(cell.getTable().options.selectable){
              cell.getRow().deselect(); cell.getRow().toggleSelect()};
            success(input.value);
            cell.getElement().focus();
            break;

          case 27:
            cancel();
            break;
        }
      });
      if(cellValue == 'N/A'){input.style.color = "grey"; input.style.fontStyle = "italic"; 
        input.setAttribute("title", "Not Applicable"); input.setAttribute("readonly", true); return input} 
      else {return input}}
  '''


class EditorInputShortcut(object):
  """
  :example: {"editor": "inputShortcuts", 'editorParams': {"refresh": True, 'emptyFirst': True}}
  """
  depsMod, depFncs = None, None
  name = "inputShortcuts"  # The alias name
  attrs = None  # Python attributes to be propagated to the Javascript definition
  jsFnc = '''
  function(cell, onRendered, success, cancel, editorParams){
      var cellValue = cell.getValue(), input = document.createElement("input");
      input.setAttribute("type", "text");
      for (var k in editorParams){input.setAttribute(k, editorParams[k])};
      if (editorParams.refresh === undefined || editorParams.refresh === true){
        input.onkeydown = function() {var key = event.keyCode ||event.charCode; 
          if(key == 8 || key == 46){input.value ="";return false}}};
      if (editorParams.emptyFirst === true){   
        input.onkeypress = function() {
          if (cellValue != "" && input.value == cellValue){input.value = ""; cellValue = ""}}};
      input.style.padding = "4px"; input.style.width = "100%";
      input.style.color = "inherit";
      input.style.textAlign = "center";
      input.style.boxSizing = "border-box";
      input.value = typeof cellValue !== "undefined" ? cellValue : "";
      onRendered(function () {input.focus(); input.style.height = "100%"});
      function onChange(e) {
        if ((cellValue === null || typeof cellValue === "undefined") && input.value !== "" || input.value != cellValue) {
          success(input.value)} else {cancel()}}
      input.addEventListener("change", onChange);
      input.addEventListener("blur", onChange);
      input.addEventListener("keydown", function (e) {
        switch (e.keyCode) {
          case 13:
            success(input.value);
            cell.getElement().focus();
            break;

          case 27:
            cancel();
            break;

          case 66:
            success(input.value * 1000000000);
            cell.getElement().focus();
            e.stopPropagation(); e.preventDefault();
            break;

          case 75:
            success(input.value * 1000);
            cell.getElement().focus();
            e.stopPropagation(); e.preventDefault();
            break;

          case 77:
            success(input.value * 1000000);
            cell.getElement().focus();
            e.stopPropagation(); e.preventDefault();
            break;
        }
      });
      if(cellValue == 'N/A'){input.style.color = "grey"; input.style.fontStyle = "italic"; 
        input.setAttribute("title", "Not Applicable"); input.setAttribute("readonly", true); return input} 
      else {return input}}
  '''


class EditorDate(object):
  """

  """

  #
  depsMod, depFncs = ["moment"], None
  name = "date" # The alias name
  attrs = None # Python attributes to be propagated to the Javascript definition
  jsFnc = '''
    function(cell, onRendered, success, cancel, editorParams){
      var cellValue = cell.getValue(),
        input = document.createElement("input");
        input.setAttribute("type", "text");
        input.style.padding = "4px";
        input.style.color = "inherit";
        input.style.width = "100%";
        input.style.boxSizing = "border-box";
        input.value = typeof cellValue !== "undefined" ? cellValue : "";
        onRendered(function(){
          $(input).datepicker({
            onSelect: function(dateStr) {
              var dateselected = $(this).datepicker('getDate');
              var cleandate = (moment(dateselected, "YYYY-MM-DD").format("DD/MM/YYYY"));
              $(input).datepicker("destroy");
              cell.setValue(cleandate, true);
              cancel()},
           });
          input.style.height = "100%";
       }); 
       return input}
    '''


class EditorSelect(object):
  """

  """

  #
  depsMod, depFncs = None, None
  name = "select" # The alias name
  attrs = None # Python attributes to be propagated to the Javascript definition
  jsFnc = '''
    function(cell, onRendered, success, cancel, editorParams){
        var cellValue = cell.getValue(); var mappedValue = "";
        var editorItems = editorParams.default; var row = cell.getRow().getData();
        for (k in editorParams){editorItems = editorParams[k]};
        var select = document.createElement("select");
        if(Array.isArray(editorParams)){
          editorParams.forEach(function(k){
            var option = document.createElement("option"); option.text = k; option.value = k;          
            if (cellValue == k){ option.selected = true};
            option.style.color = 'black';
            select.add(option)})
        }else{
          for (k in editorParams){
            var option = document.createElement("option"); option.text = editorParams[k]; option.value = k;          
            if (cellValue == k){ option.selected = true};
            option.style.color = 'black';
            select.add(option)}
        }
        
        select.style.padding = "4px";
        select.style.width = "100%";
        select.style.color = "black";
        select.style.textAlign = "center";
        select.style.boxSizing = "border-box";
      
        onRendered(function(){select.focus(); 
          select.style.color = 'inherit'});
        select.onchange = function(){success(this.value); cell.getElement().focus()};
        select.onblur = function(){success(this.value)};
        if(cellValue == 'N/A'){input = document.createElement("input");
          input.style.padding = "4px"; input.style.width = "100%"; input.style.color = "inherit";
          input.style.textAlign = "center"; input.value = cellValue;
          input.setAttribute("type", "text"); input.style.color = "grey"; input.style.fontStyle = "italic"; 
          input.setAttribute("title", "Not Applicable"); input.setAttribute("readonly", true); return input} 
        return select;
    }'''


class EditorSelectCondition(object):
  """

  editorParams = {
    'key': '',
    'values': {
    }
  }
  """

  #
  depsMod, depFncs = None, None
  name = "selectConditions" # The alias name
  attrs = None # Python attributes to be propagated to the Javascript definition
  jsFnc = '''
    function(cell, onRendered, success, cancel, editorParams){
        var editorItems = editorParams.default; var row = cell.getRow().getData();
        for (k in editorParams.values){
          if (row[editorParams.key] == k){
            editorItems = editorParams.values[k];
            break}};
        
        var select = document.createElement("select");
        editorItems.forEach(function(r){
          var option = document.createElement("option");
          option.text = r; option.value = r;select.add(option)});
        select.style.padding = "4px";
        select.style.width = "100%";
        select.style.boxSizing = "border-box";
        select.value = cell.getValue();
        onRendered(function(){select.focus()});
        select.onchange = function(){success(this.value); cell.getElement().focus()};
        select.onblur = function(){success(this.value)};
        if(cell.getValue() == 'N/A'){return 'N/A'} 
        else{ return select}
    }'''


class EditorSelectMultiCondition(object):
  """

  editorParams = {
    'keys': [''],
    'values': {
    }
  }
  """

  #
  depsMod, depFncs = None, None
  name = "selectMultiConditions"  # The alias name
  attrs = None  # Python attributes to be propagated to the Javascript definition
  jsFnc = '''
    function(cell, onRendered, success, cancel, editorParams){
        var editorItems = editorParams.default; var row = cell.getRow().getData();
        var itemFound = false;
        for(var l=0 ;  l < editorParams.keys.length; l++) {
          for (k in editorParams.values){
            if (row[editorParams.keys[l]] == k){
              editorItems = editorParams.values[k];
              itemFound = true; break}};
          if (itemFound){break}
        }
        var select = document.createElement("select");
        editorItems.forEach(function(r){
          var option = document.createElement("option");
          option.text = r; option.value = r;select.add(option)});
        select.style.padding = "4px";
        select.style.width = "100%";
        select.style.boxSizing = "border-box";
        select.value = cell.getValue();
        onRendered(function(){select.focus()});
        select.onchange = function(){success(this.value); cell.getElement().focus()};
        select.onblur = function(){success(this.value)};
        if(cell.getValue() == 'N/A'){return 'N/A'} 
        else{ return select}
    }'''
