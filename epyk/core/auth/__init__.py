from epyk.core.js.packages import packageImport


class Auth(object):


    def __init__(self, report):
        self._report = report

    @packageImport('google-platform')
    def google_sign_in(self, client_id, scopes=['profile', 'email'], insert_button=False, debug=False):
        """
        Description:
        -------------
        Allows to add a google signin capability to the page
        This needs a working server to work

        Related Pages:

            https://developers.google.com/identity/sign-in/web/sign-in

        :param client_id: the google webapp client id defined here: https://console.developers.google.com/apis/credentials
        :param insert_button: choose whether the button will be inserted when this function is called or not
        :return: Epyk Obj
        """

        headers = self._report.headers
        headers.meta.custom('google-signin-scope', ' '.join(scopes))
        headers.meta.custom('google-signin-client_id', client_id)
        g_button = self._report.ui.div()
        g_button.style.no_class()
        g_button.style.clear_style()
        g_button.style.add_classes.external('g-signin2')
        g_button.attr.update({'data-onsuccess': 'onSignIn'})

        fnc_list = [self._report.js.object('profile', '''profile = googleUser.getBasicProfile()'''),
                    self._report.js.object('id_token', '''id_token = googleUser.getAuthResponse().id_token''')]
        if debug:
            fnc_list.append(self._report.js.console.log(self._report.js.getVar('id_token', 'object'), skip_data_convert=True))
        fnc_list.append(self._report.js.return_(self._report.js.getVar('id_token', 'object')))
        g_button.options.managed = insert_button
        self._report.js.registerFunction('onSignIn', fnc_list, ['googleUser'])
        return g_button


