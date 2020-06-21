from epyk.core.Page import Report
rptObj = Report()




rptObj.auth.facebook_sign_in('1553869208115832', insert_button=True, debug=True)
print(rptObj.outs.html_file(path=r"C:\Users\nelso\Desktop", name='fb_signin'))
