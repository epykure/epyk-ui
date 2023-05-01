from epyk.core.js.packages import packageImport


class Auth(object):

    def __init__(self, page):
        self.page = page

    @packageImport('google-platform')
    def google_sign_in(self, client_id, scopes=['profile', 'email'], insert_button=True, debug=False):
        """
        Allows to add a google signin capability to the page
        This needs a working server to work

        Related Pages:

          https://developers.google.com/identity/sign-in/web/sign-in

        :param client_id: the google webapp client id defined here: https://console.developers.google.com/apis/credentials
        :param insert_button: choose whether the button will be inserted when this function is called or not
        :return: Epyk Obj
        """
        headers = self.page.headers
        headers.meta.custom('google-signin-scope', ' '.join(scopes))
        headers.meta.custom('google-signin-client_id', client_id)
        g_button = self.page.ui.div()
        g_button.style.no_class()
        g_button.style.clear_style()
        g_button.style.add_classes.external('g-signin2')
        g_button.attr.update({'data-onsuccess': 'onSignIn'})

        fnc_list = [self.page.js.object('profile', '''profile = googleUser.getBasicProfile()'''),
                    self.page.js.object('id_token', '''id_token = googleUser.getAuthResponse().id_token''')]
        if debug:
            fnc_list.append(self.page.js.console.log(self.page.js.getVar('id_token', 'object'), skip_data_convert=True))
        fnc_list.append(self.page.js.return_(self.page.js.getVar('id_token', 'object')))
        g_button.options.managed = insert_button
        self.page.js.registerFunction('onSignIn', fnc_list, ['googleUser'])
        return g_button

    def facebook_sign_in(self, client_id, scopes=['public_profile', 'email'], insert_button=True, graphVersion='v7.0',
                         type='login_with', debug=False):
        """

        :param client_id:
        :param insert_button:
        :param graphVersion:
        :param type:
        :param debug:
        :return:
        """
        accepted_types = ('login_with', 'continue_with')

        if type not in accepted_types:
            raise ValueError('Specified type: %s not in accepted values. Accepted values are as follows: %s' % (
            type, ', '.join(accepted_types)))

        getFbSdk = '''(function(d, s, id) {
                        var js, fjs = d.getElementsByTagName(s)[0];
                        if (d.getElementById(id)) return;
                        js = d.createElement(s); js.id = id;
                        js.src = "https://connect.facebook.net/en_US/sdk.js";
                        fjs.parentNode.insertBefore(js, fjs);
                      }(document, 'script', 'facebook-jssdk'));
                        '''

        returnFbResponse = '''function statusChangeCallback(response) {
                            return response;
                            }
                '''

        jsCheckLogin = '''function checkLoginState() {               
                        FB.getLoginStatus(function(response) {   
                          return response;
                        });
                      }
                   '''

        jsInitFnc = '''window.fbAsyncInit = function() {FB.init({
                    appId: '%s',
                    cookie: true,
                    xfbml: true,
                    version: '%s'
                    });
                };''' % (client_id, graphVersion)

        self.page.js.onReady([getFbSdk, returnFbResponse, jsCheckLogin, jsInitFnc])
        fb_button = self.page.ui.div()
        fb_button.style.no_class()
        fb_button.style.clear_style()
        fb_button.style.add_classes.external('fb-login-button')
        fb_button.attr.update(
            {'data-size': 'large', 'data-button-type': type, 'data-layout': 'default', 'data-auto-logout-link': 'true',
             'data-use-continue-as': 'false', 'data-width': '', 'onlogin': "checkLoginState();",
             'scopes': ','.join(scopes)})
