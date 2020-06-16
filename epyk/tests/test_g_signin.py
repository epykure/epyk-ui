from epyk.core.Page import Report
rptObj = Report()




rptObj.auth.google_sign_in('739797595806-8kb4iili6br2gt00h5uhuugkvjhlq4ho.apps.googleusercontent.com', insert_button=True, debug=True)
print(rptObj.outs.html_file(path=r"C:\Users\nelso\Desktop", name='g_signin'))
