#
# from epyk.core.css import Css
# from epyk.core.css.classes import CssStyle
#
#
# cssCls = CssStyle.getCssObj('CssButtonBasic', colors={'colors': {9: 'orange'}})
# #cssCls.color('colors', -1, "orange")
# print("-------------")
# print(cssCls.getStyles()['.py_cssbuttonbasic:focus'])
# #print( CssCls().toCss({"text-align": 'right'}) )
#
# cssObj = Css.Css()
# #print(Css.Css().append(["CssBillboardTitle"]).toCss())
#
# print(cssObj.cssCls("CssDivChart", {"color": 'yellow'}).getStyles()['.py_cssdivchart']['color'])
# #print(cssObj.cssCls("CssDivChart", {"color": 'yellow'})._cssOvr)
# #print(cssObj.cssCls("CssDivChart", {"color": 'yellow'}).cssStyles['py_cssdivchart'].getStyles())
#
# # cssObj = Css.Css()
# #
# # print(cssObj.append(["CssDivChart", "CssBillboardTitle"]).toCss())
# # print(cssObj.toHtml("CssBillboardTitle"))
# # print("----------------------------------------------------")
# # print(cssObj.cssCls("CssDivChart", {"color": 'yellow'}, {'hover': {'color': 'red'}}).toCss())
# # print("----------------------------------------------------")
# #
#
# cssObj = Css.Css()
# cssObj.css('color', 'red')
# print(cssObj.getClsTag())
#
# cssObj.append(['class2', 'class1'])
# print(cssObj.getClsTag(['class1']))
#
# # create an anonymous class
# cls_name = cssObj.anonymous_cls({"color": "red"})
# print(cls_name)
# print(cssObj._cssCls)
#
# print(cssObj.colors.randColor())
# print(cssObj.colors.get('success', 0))
#
# cssObj.toCss(file_name="test", path="..\outs\css")
# # print(cssObj.toHtml())
#
