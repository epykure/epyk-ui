"""
All those components are a bit special as they would require to work properly:
  - A server in order to interact dynamically
  - A database source

This can definition be configured but by default it is using the ones of the server.
"""

import json
import datetime

from epyk.core.html import Html

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsText

from epyk.core.js.Imports import requires
sqlalchemy = requires("sqlalchemy", reason='Missing Package', install='sqlalchemy', source_script=__file__)


# -------------------------------------------------------------------------------------------------------------------
#                                               DATABASE SCHEMA
#
def scripts_chat():
  return [sqlalchemy.Column('script_chat_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
          sqlalchemy.Column('report_name', sqlalchemy.String, nullable=False),
          sqlalchemy.Column('script_name', sqlalchemy.String, nullable=False),
          sqlalchemy.Column('message', sqlalchemy.Text, nullable=False),
          sqlalchemy.Column('usr_name', sqlalchemy.String, nullable=False),
          sqlalchemy.Column('html_code', sqlalchemy.String, nullable=False),
          sqlalchemy.Column('lst_mod_dt', sqlalchemy.DateTime, nullable=False, default=datetime.datetime.utcnow())]


def system_comments():
  return [sqlalchemy.Column('com_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('environment', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('report', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('htmlCode', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('username', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('visibility', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('comment', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('pmts', sqlalchemy.String),
    sqlalchemy.Column('lst_mod_dt', sqlalchemy.DateTime, default=datetime.datetime.utcnow(), nullable=True)]


def system_comments_replies():
  return [sqlalchemy.Column('reply_id', sqlalchemy.Integer, autoincrement=True, primary_key=True),
    sqlalchemy.Column('master_com_id', sqlalchemy.String),
    sqlalchemy.Column('environment', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('report', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('htmlCode', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('username', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('visibility', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('comment', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('pmts', sqlalchemy.String),
    sqlalchemy.Column('lst_mod_dt', sqlalchemy.DateTime, default=datetime.datetime.utcnow(), nullable=True)]


def system_user_comments():
  return [sqlalchemy.Column('auth_com_id', sqlalchemy.Integer, autoincrement=True, primary_key=True),
    sqlalchemy.Column('com_id', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('auth_name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('lst_mod_dt', sqlalchemy.DateTime, default=datetime.datetime.utcnow(), nullable=True)]


class Comments(Html.Html):
  name = 'Comment'
  requirements = ('jquery-scrollbar', )
  # _grpCls = CssGrpClsText.CssClassComment

  def __init__(self, report, htmlCode, recordset, title, pmts, db_service, width, height, httpCodes, readonly, profile):
    if httpCodes is None:
      self.httpCodeStr = ''
    else:
      self.httpCodeStr = '#%s' % '#'.join([report.http[code] for code in httpCodes])
    com_table = 'system_comments'
    reply_table = 'system_comments_replies'
    self.privacy = 'public' if not db_service else db_service.get('privacy', 'public')
    self.code = htmlCode
    super(Comments, self).__init__(report, recordset, css_attrs={"width": width, "height": height}, code=htmlCode, profile=profile)
    self.css({"clear": 'both', "display": "inline-block", 'margin': '5px 0', 'padding': '0'})
    self.pmts, self._height, self.readonly = pmts, "%s%s" % (height[0], height[1]), readonly
    self.add_title(title, options={'content_table': False})
    if db_service is not None:
      if 'db' not in db_service:
        raise Exception('The db keyword needs to be defined with a proper epyk db Object (report.db.public)')

      com_table = db_service.get('com_table', 'system_comments')
      reply_table = db_service.get('reply_table', 'system_comments_replies')
      db_service['db'].table_create(com_table, system_comments())
      db_service['db'].table_create(reply_table, system_comments_replies())
      db_service['db'].table_create(db_service.get('user_coms', 'system_user_comments'), system_user_comments())
      db = db_service['db']
    else:
      db_service = {}
      db = self._report.data.db.public
      db.table_create(com_table, system_comments())
      db.table_create(reply_table, system_comments_replies())
      db.table_create(db_service.get('user_coms', 'system_user_comments'), system_user_comments())
    # Bind the database services associated to this component
    db_service.setdefault('service', '%s/comment/add' % self._report._urlsApp['report'])
    db_service.setdefault('reply_service', '%s/comment/reply' % self._report._urlsApp['report'])
    self.com_table = com_table
    self.reply_table = reply_table
    self.db_service = db_service
    for rec in db.select([com_table]).where([db.column(com_table, 'environment') == self._report.run.report_name,
                                             db.column(com_table, 'report') == self._report.run.script_name,
                                             db.column(com_table, 'htmlCode') == '%s%s' % (self.code, self.httpCodeStr)]).order_by(db.asc(db.column(com_table, 'lst_mod_dt'))).fetch():
      com_replies = []
      for reply in db.select([reply_table]).where([db.column(reply_table, 'environment') == self._report.run.report_name,
                                             db.column(reply_table, 'report') == self._report.run.script_name,
                                             db.column(reply_table, 'master_com_id') == rec['com_id'],
                                             db.column(reply_table, 'htmlCode') == '%s%s' % (self.code, self.httpCodeStr)]).order_by(db.asc(db.column(reply_table, 'lst_mod_dt'))).fetch():
        com_replies.append(dict(reply))
      recordset.append({'id': rec['com_id'], 'value': rec['comment'], 'user': rec['username'], 'time': datetime.date.strftime(rec['lst_mod_dt'], '%Y-%m-%d %H:%M:%S'), 'replies': com_replies, 'nb_replies': len(com_replies)})

  @property
  def jqId(self): return "$('#%s_comms')" % self.htmlId

  @property
  def val(self): return "$(this).val()"

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''htmlObj.empty();
      data.forEach(function(rec){addComment(htmlObj, rec.value, rec.user, rec.time, rec.replies, rec.nb_replies, rec.id)});
      $('.scroll_content').mCustomScrollbar()''', 'Javascript Object builder')

  def save(self):
    if self._report.run.current_user != 'local':
      data = ''' 'env': "%s" , 'report': "%s", 'htmlCode': "%s", "table_name" : "%s",
              'username': "%s", 'visibility': "%s", 'val': %s, 'path': JSON.stringify('%s'), 'httpCodes': "%s", 'timestamp': timeStamp ''' % (self._report.run.report_name, self._report.run.script_name,
                                                                              self.code, self.com_table, self._report.run.current_user, self.privacy, self.val,
                                                                              self._report.run.local_path, self.httpCodeStr)
      return self._report.jsPost(self.db_service['service'], data, isPyData=False)

    return ''

  def saveReply(self):
    if self._report.run.current_user != 'local':
      data = ''' 'env': "%s" , 'report': "%s", 'htmlCode': "%s", "table_name" : "%s",
              'username': "%s", 'visibility': "%s", 'val': %s, 'path': JSON.stringify('%s'), 'httpCodes': "%s", 'master_com_id': parentId ''' % (self._report.run.report_name, self._report.run.script_name,
                                                                              self.code, self.reply_table, self._report.run.current_user, self.privacy, self.val,
                                                                              self._report.run.local_path, self.httpCodeStr)
      return self._report.jsPost(self.db_service['reply_service'], data, isPyData=False)

    return ''

  def jsAdd(self, jsData='data', jsDataKey=None, isPyData=False, pmts=None, jsParse=False):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData)
    return "addComment(%s, %s, '%s', Today())" % (self.jqId, jsData, self._report.user)

  def __str__(self):
    self._report.jsOnLoadFnc.add("$('#%(htmlId)s_text').on('keypress', function (e) {if(e.which === 13){var timeStamp = new Date().getTime(); %(save)s; addComment($('#%(htmlId)s_comms'), $(this).val(), '%(user)s', Today(), [], 0, '%(user)s_' + timeStamp); $(this).val('')}})" % {'save': self.save(), 'htmlId': self.htmlId, 'user': self._report.run.current_user})
    self.addGlobalFnc('replyComment(htmlObj, user, parentId)', '''$('.comments_reply_inputs').remove(); 
    var inputReply = $('<input class="comments_reply_inputs" style="display:block;margin-left:20px" id=' + htmlObj.attr("id") + '_text type="text" placeholder="Add Reply" />');
    htmlObj.append(inputReply);
    inputReply.on('keypress', function (e) {if(e.which === 13){%(saveReply)s; addReply(htmlObj, $('#%(htmlId)s_comms'), $(this).val(), '%(user)s', Today()); $(this).remove()}})''' % {'saveReply': self.saveReply(), 'htmlId': self.htmlId, 'user': self._report.run.current_user})
    self.addGlobalFnc('addComment(htmlObj, data, user, timeStamp, replies, nbReplies, comId)', r'''
      var countComs = parseInt($('#'+ htmlObj.attr('id') + '_count').text()) + 1 + nbReplies; 
      var div = $("<div style='margin:5px;padding:0;text-align:left'>");
      div.append("<p style='margin:0;padding:0;display:inline-block;color:%(color)s;font-weight:bold'>"+ user +"</p>");
      div.append("<p style='margin:0;padding:0;display:inline-block;margin-left:10px;color:%(grey)s'>"+ timeStamp +"</p>");
      var replyCount = $("<p style='margin:0;padding:0;display:inline-block;margin-left:10px;color:%(color)s;font-weight:bold'> Replies: </p><p id=" + comId + "_nbRep style='display:inline-block;margin-left:5px;color:%(color)s;font-weight:bold'> "+ 0 +"</p>");
      div.append(replyCount);
      var button = $("<button id=" + comId + "_button style='margin:0;padding:0;display:inline-block;margin-left:10px;color:#3bb194;background:none;border:none'> Reply </button>");
      div.append(button);
      var commentTxt = $("<p id=" + comId +" style='margin:0 5px 20px 5px;padding:0;text-align:left'>"+ data +"</p>");
      htmlObj.prepend(commentTxt);
      button.on('click', function(e) {replyComment(commentTxt, user, comId);});
      htmlObj.prepend(div); 
      replies.forEach(function(rec) {addReply(commentTxt, $('#%(htmlId)s_comms'), rec.comment, rec.username, rec.lst_mod_dt)});
      $('#'+ htmlObj.attr('id') +'_count').text(countComs)''' % {'htmlId': self.htmlId, r'color': self._report.theme.greys[-1], 'grey': self._report.theme.greys[6]})
    self.addGlobalFnc('addReply(htmlObj, parentObj, data, user, timeStamp)', '''
      var replyCount = parseInt($('#'+ $.escapeSelector(htmlObj.attr('id')) + '_nbRep').text()) + 1;
      if (replyCount == 1) 
      {
        htmlObj.append("<div id=" + htmlObj.attr('id') + "_replies></div>");
      }
      var div = $("<div style='margin-left:20px;padding:0;text-align:left'>");
      div.append("<p style='margin:0;padding:0;display:inline-block;color:%(color)s;font-weight:bold'>"+ user +"</p>");
      div.append("<p style='margin:0;padding:0;display:inline-block;margin-left:10px;color:%(grey)s'>Replied At:</p>");
      div.append("<p style='margin:0;padding:0;display:inline-block;margin-left:10px;color:%(grey)s'>"+ timeStamp +"</p>");
      $("#" + $.escapeSelector(htmlObj.attr('id')) + "_replies").prepend("<p style='margin:0 5px 20px 20px;padding:0;text-align:left'>"+ data +"</p>");
      $("#" + $.escapeSelector(htmlObj.attr('id')) + "_replies").prepend(div);
      var countTotalComs = parseInt($('#'+ parentObj.attr('id') + '_count').text()) + 1;
      $('#'+ parentObj.attr('id') +'_count').text(countTotalComs);
      $('#'+ $.escapeSelector(htmlObj.attr('id')) + '_nbRep').text(replyCount);
    ''' % {'color': self._report.theme.greys[-1], 'grey': self._report.theme.greys[6]})
    inputTag = ''
    if not self.readonly:
      inputTag = '<input spellcheck=”false” style="display:block" id="%s_text" type="text" placeholder="Add public comment" />' % self.htmlId
    return '''
      <div %(attr)s>
        <span><p style="display:inline-block;margin:0;padding:0;cursor:pointer" id="%(htmlId)s_comms_count">0</p> Comments <i style="margin:0 5px 0 20px;cursor:pointer;display:inline-block" class="fas fa-sort-amount-up"></i>Sort by</span>
        %(inputTag)s
        <div class='scroll_content' style="margin:0;padding:5px 0;height:%(height)s;overflow:auto">
          <div id="%(htmlId)s_comms"></div>
        </div>
      </div>
      ''' % {'attr': self.get_attrs(pyClassNames=self.defined), 'htmlId': self.htmlId, 'height': self._height,
             'inputTag': inputTag}


class Chat(Html.Html):
  name = 'Chat'
  requirements = ('jquery-scrollbar', )
  # _grpCls = CssGrpClsText.CssClassComment

  def __init__(self, report, htmlCode, title, pmts, dbService, width, height, httpCodes, readonly, profile, chatOptions):
    self.readonly, self._height = readonly, "%s%s" % (height[0], height[1])
    if chatOptions is None:
      chatOptions = {}
    self.chatOptions = chatOptions
    if httpCodes is None:
      self.httpCodeStr = ''
    else:
      self.httpCodeStr = '#%s' % '#'.join([report.http[code] for code in httpCodes])
    # Get the database service
    db = report.data.db.public
    db.table_create("scripts_chat", scripts_chat())
    recordSet = []
    for rec in db.select("scripts_chat").where([db.column("scripts_chat", 'lst_mod_dt') > datetime.datetime.utcnow().date()]).records:
      rec["time"] = str(rec["lst_mod_dt"]).split(".")[0]
      recordSet.append(rec)
    self.privacy = 'public' if not dbService else dbService.get('privacy', 'public')
    super(Chat, self).__init__(report, recordSet, css_attrs={"width": width}, code=htmlCode, profile=profile)
    # Add internal HTML components
    self.add_title(title, options={'content_table': False})
    self._report.jsImports.add('socket.io')
    self._report.jsOnLoadFnc.add("var socket = io.connect('%s')" % self._report.run.url_root)
    self._report.jsOnLoadFnc.add("socket.on('message_%s_%s_%s', function(data) {%s})" % (
      self._report.run.report_name, self._report.run.script_name, self.htmlId, self.jsAppend()))

  @property
  def jqId(self): return "$('#%s_comms')" % self.htmlId

  @property
  def val(self): return "$(this).val()"

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''htmlObj.empty();
      data.forEach(function(rec){addChatMessage(htmlObj, rec.message, rec.usr_name, rec.time, true)});
      htmlObj.prepend("<hr style='background:%(color)s;margin:10px 10px 0 10px'/>");
      $('.scroll_content').mCustomScrollbar()''' % {'color': self._report.theme.greys[5]}, 'Javascript Object builder')

  def jsAppend(self, jsData='data', jsDataKey=None, isPyData=False, pmts=None, jsParse=False):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData)
    return "addChatMessage(%(jqId)s, %(data)s.text, %(data)s.user, Today(), false)" % {"jqId": self.jqId, "data": jsData}

  def __str__(self):
    self._report.jsOnLoadFnc.add('''
      $('#%(htmlId)s_text').on('keypress', function (e) {if(e.which === 13){
        var timeStamp = new Date().getTime(); var content = $(this).val();
        var data = {user: '%(user)s', text: content, timestamp: timeStamp, ext_system: %(chatOptions)s};
        %(postMessage)s; $(this).val('')}})
      ''' % {'htmlId': self.htmlId, 'user': self._report.run.current_user, 'chatOptions': json.dumps(self.chatOptions),
             "postMessage": self._report.jsPost('%s/socket/%s/%s/%s' % (self._report._urlsApp['index'].replace("/index", ""), self.htmlId, self._report.run.report_name, self._report.run.script_name))})
    self.addGlobalFnc('addChatMessage(htmlObj, data, user, timeStamp, oldMsg)', r'''
      var div = $("<div style='margin:5px;padding:0;text-align:left'>");
      var color = "%(color)s"; if(oldMsg){color = "%(grey)s"};
      div.append("<p style='margin:0;padding:0;display:inline-block;color:"+ color +";font-weight:bold'>"+ user +"</p>");
      div.append("<p style='margin:0;padding:0;display:inline-block;margin-left:10px;color:%(grey)s'>"+ timeStamp +"</p>");
      var commentTxt = $("<p style='margin:0 5px 20px 5px;padding:0;color:"+ color +";text-align:left'>"+ data +"</p>");
      htmlObj.prepend(commentTxt); htmlObj.prepend(div)''' % {'htmlId': self.htmlId, 'color': self._report.theme.greys[-1], 'grey': self._report.theme.greys[6]})
    inputTag = ''
    if not self.readonly:
      inputTag = '<input spellcheck="false" style="display:block" id="%s_text" type="text" placeholder="Write a message" />' % self.htmlId
    return '''
      <div %(attr)s>
        <span><p style="display:inline-block;margin:0;padding:0;cursor:pointer" id="%(htmlId)s_comms_count">0</p> Comments <i style="margin:0 5px 0 20px;cursor:pointer;display:inline-block" class="fas fa-sort-amount-up"></i>Sort by</span>
        %(inputTag)s
        <div class='scroll_content' style="margin:0;padding:5px 0;height:%(height)s;overflow:auto">
          <div id="%(htmlId)s_comms"></div>
        </div>
      </div>
      ''' % {'attr': self.get_attrs(pyClassNames=self.defined), 'htmlId': self.htmlId, 'height': self._height,
             'inputTag': inputTag}

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document): pass
  def to_xls(self, workbook, worksheet, cursor): pass
  def to_ppt(self, workbook, worksheet, cursor): pass


class Bot(Html.Html):
  """

  Three main states for the bot:
    - Message
    - Question
    - Advice / Information

  """
  name = 'Bot'

  def __init__(self, report, htmlCode, name, pmts, dbService, width, height, httpCodes, profile, botOptions):
    super(Bot, self).__init__(report, [], css_attrs={"width": width}, code=htmlCode, profile=profile)
    self.css({"position": 'fixed', "bottom": 0, 'margin': '10px', 'background': self._report.theme.greys[0],
              "right": 0, "display": "block", "padding": "5px", 'border': "1px solid %s" % self._report.theme.success[1],
              "z-index": 200})
    self.name, self.height = name, height

  def __str__(self):
    self.addGlobalFnc('addBotMessage(htmlObj)', '''
      htmlObj.empty();
      var text = jQuery('<textarea type=\\"text\\" style=\\"width:100%%;height:%(height)spx\\" spellcheck=\\"false\\"></textarea>');
      htmlObj.append(text)''' % {"height": self.height[0] - 55})
    self.addGlobalFnc('addBotAdvices(htmlObj, message)', '''
      htmlObj.empty();
      var text = jQuery('<div>'+ message +'</div>');
      htmlObj.append(text)''' % {"height": self.height[0] - 55})
    self.addGlobalFnc('addBotQuestion(htmlObj, message, answers)', '''
      htmlObj.empty();
      var text = jQuery('<div>'+ message +'</div>');
      htmlObj.append(text)''' % {"height": self.height[0] - 55})
    # onclick="addBotMessage(jQuery('#content_bot'))"
    return '''
       <div %(attr)s>
          <p style="font-size:18px;width:100%%;margin:0;display:block">
            <i class="far fa-comments" style="font-size:12px;float:left;margin-right:5px"></i>
            <span onclick="addBotAdvices(jQuery('#content_bot'), 'text')" style="font-size:12px;cursor:pointer;float:left">%(name)s</span>
            <i onclick="jQuery('#content_bot').empty()" class="far fa-minus-square" style="font-size:12px;float:right;cursor:pointer"></i>
          </p>
          <div id="content_bot" style="clear:both;display:block"></div>
       </div>   
    ''' % {'attr': self.get_attrs(), "name": self.name, "height": self.height[0] - 55}

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document): pass
  def to_xls(self, workbook, worksheet, cursor): pass
  def to_ppt(self, workbook, worksheet, cursor): pass


class Alert(Html.Html):
  requirements = ('bootstrap', )
  name = 'Alert'
  marginTop = 90

  def __init__(self, report, title, value, category, width, height, close_button=False,
               background_color=None, color='black', htmlCode=None, dataSrc=None, profile=False):
    super(Alert, self).__init__(report, {'title': title, 'value': value, 'closure': close_button},
                                css_attrs={"width": width, 'height': height}, code=htmlCode, profile=profile)
    self.close_button = close_button
    self.attr["class"].add('alert')
    self.attr["class"].add('alert-%s' % category.lower())
    heightSpace = 70 if self.close_button else 10
    self._jsStyles = {'class': ['alert', 'alert-%s' % category.lower()], "css": {'position': 'fixed', 'z-index': '290', 'right': '5px',
                      'width': '%s%s' % (width[0], width[1]), 'height': "%s%s" % (height[0], height[1]),
                      'color': color,
                      'top': '%spx' % (self.marginTop + (report._props["ui"]["notifications"]["count"] - 1) * heightSpace)}}
    if background_color is not None:
      self._jsStyles['background'] = background_color
    self.css(self._jsStyles["css"])
    if self.close_button:
      self._jsStyles['class'] += ['alert-dismissable']
      self.style.addCls('alert-dismissable')

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' 
      if (htmlObj.length == 0){htmlObj = $("<div class='"+ jsStyles.class.join(" ") +"'></div>"); htmlObj.css(jsStyles.css); $('body').append(htmlObj)}
      htmlObj.empty();
      if((data.closure) || (data.closure == undefined)){htmlObj.append('<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>')}
      htmlObj.append('<strong>'+ data.title +'!</strong>&nbsp;'+ data.value)''')

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.pyStyle)


class News(Html.Html):
  name = 'News'
  requirements = ('jqueryui', )

  def __init__(self, report, title, value, label, link_script, icon, width, height, htmlCode, profile):
    super(News, self).__init__(report, value, css_attrs={"width": width, 'height': height}, code=htmlCode, profile=profile)
    self.css({"padding": '5px', "display": 'none', 'position': 'fixed', 'border': '1px solid %s' % self._report.theme.success[1],
              "background": self._report.theme.greys[0], 'bottom': '20px', 'right': '20px'})
    # Add internal HTML component to the new feed
    self.add_label(label)
    self.add_title(title, options={'content_table': False})
    self.add_link(link_script, position="after")

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, "htmlObj.find('p#content').html(data)")

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsStyles=None, jsFnc=None):
    js_data = super(News, self).jsGenerate(jsData, jsDataKey, isPyData, jsParse, jsStyles, jsFnc)
    return "%(js_data)s;%(jqId)s.show().delay(1000);%(jqId)s.fadeOut(1000)" % {"js_data": js_data, "jqId": self.jqId}

  def __str__(self):
    return "<div %s><p id='content'></p></div>" % self.get_attrs(pyClassNames=self.pyStyle)
