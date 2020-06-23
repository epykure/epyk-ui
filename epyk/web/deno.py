
import os


class Deno(object):

  def __init__(self, app_path, name=None):
    self._app_path, self._app_name = app_path, name
    self._route, self._fmw_modules = None, None
    self._page = None

  def router(self, target_path):
    """
    Description:
    ------------
    Create a simple router file for your different views on your server.

    Attributes:
    ----------
    :param target_path: String. The target path where the views are stored
    """
    router_path = os.path.join(self._app_path, "server.ts")
    with open(router_path, "w") as f:
      f.write('''
import { serve } from 'https://deno.land/std/http/server.ts';
import { readFileStr } from 'https://deno.land/std/fs/read_file_str.ts';

const server = serve({ port: 3000 });
for await (const req of server) {
  // Read the url
  const url = req.url;
  const params = req.url.split("?");
  if (params.length >= 2) {
    const search_params = new URLSearchParams(params[1]);
    console.log(search_params.get('refresh'));
  }
  
  const text = await readFileStr('./%s/'+ url.substr(1) +'.html');
  req.respond({ body: text });    
}''' % target_path)

  def launcher(self, app_name, target_path):
    """
    Description:
    ------------
    Create a single launcher for the application.

    Attributes:
    ----------
    :param app_name: String. The deno path (This should contain the deno.exe file)
    :param target_path: String. The target path for the views
    """
    out_path = os.path.join(self._app_path, "launchers")
    if not os.path.exists(out_path):
      os.makedirs(out_path)
    router_path = os.path.join(out_path, "launcher_%s.ts" % app_name)
    with open(os.path.join(self._app_path, "run_%s.bat" % app_name), "w") as f:
      f.write("deno.exe run --allow-net --allow-read ./launchers/launcher_%s.ts" % app_name)
    with open(router_path, "w") as f:
      f.write('''
import { serve } from 'https://deno.land/std/http/server.ts';
import { readFileStr } from 'https://deno.land/std/fs/read_file_str.ts';

const server = serve({ port: 3000 });
for await (const req of server) {
  // Read the url
  const url = req.url;
  const params = req.url.split("?");
  if (params.length >= 2) {
    const search_params = new URLSearchParams(params[1]);
    console.log(search_params.get('refresh'));
  }

  const text = await readFileStr('../%s/%s.html');
  req.respond({ body: text });    
} ''' % (target_path, app_name))

  def page(self, selector=None, name=None, report=None, auto_route=False, target_folder="apps"):
    """
    Description:
    ------------
    Publish a new application on the deno server.
    This will create a static rich HTML file.

    Attributes:
    ----------
    :param selector:
    :param name:
    :param report:
    :param auto_route:
    :param target_folder:
    """
    self._report = report
    self.target_folder = target_folder
    self.name = name
    self.selector = selector
    self.auto_route = auto_route

  def publish(self):
    """
    Description:
    ------------

    """
    out_path = os.path.join(self._app_path, self.target_folder)
    if not os.path.exists(out_path):
      os.makedirs(out_path)
    self._report.outs.html_file(path=out_path, name=self.name)
    if self.auto_route:
      self.launcher(self.name, out_path)
