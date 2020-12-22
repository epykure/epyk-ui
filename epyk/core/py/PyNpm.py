#!/usr/bin/python
# -*- coding: utf-8 -*-


try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request, ProxyHandler, build_opener, install_opener
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, ProxyHandler, build_opener, install_opener


from epyk.core.js import Imports

import subprocess
import logging
import json
import re
import os


class NpmRegisteryScore:

  def __init__(self, score):
    self.__score = score

  @property
  def final(self):
    """
    Description:
    -----------
    
    Usage:
    pkg = PyNpm.Npm().package('pivottable')
    """
    return self.__score["final"]

  @property
  def popularity(self):
    """
    Description:
    -----------


    Usage:

    """
    return self.__score['detail']['popularity']

  @property
  def maintenance(self):
    """
    Description:
    -----------
    
    Usage:

    """
    return self.__score['detail']['maintenance']


class NpmDistIntegrity:

  def __init__(self, controls):
    self.__controls = controls

  @property
  def integrity(self):
    """
    Description:
    -----------

    Usage:

    """
    return self.__controls["integrity"]

  @property
  def shasum(self):
    """
    Description:
    -----------
    """
    return self.__controls["shasum"]

  @property
  def fileCount(self):
    """
    Description:
    -----------

    Usage:

    """
    return self.__controls["fileCount"]

  @property
  def unpackedSize(self):
    """
    Description:
    -----------

    Usage:

    """
    return self.__controls["unpackedSize"]


class NpmRegistery:

  __HTTP_GITHUB_USER = "https://raw.githubusercontent.com"
  __HTTP_GITHUB = "https://api.github.com"
  __HTTP_NPM_REGISTERY = 'https://registry.npmjs.org'

  def __init__(self, package, alias):
    self._meta = package
    self._alias = alias
    self._info, self._tree = None, None

  @property
  def score(self):
    """
    Description:
    -----------
    Get the final score for the package on the NPM registry website.

    Usage:

      pkg = PyNpm.Npm().package('pivottable')
      print(pkg.score)
    """
    return self._meta["score"]['final']

  @property
  def scores(self):
    """
    Description:
    -----------

    Usage:

    """
    return NpmRegisteryScore(self._meta["score"])

  @property
  def controls(self):
    """
    Description:
    -----------

    Usage:

    """
    return NpmDistIntegrity(self.info()['dist'])

  @property
  def searchScore(self):
    """
    Description:
    -----------
    Get the score search figure on the NPM registry website.

    Usage:
    pkg = PyNpm.Npm().package('pivottable')
    print(pkg.searchScore)
    """
    return self._meta["searchScore"]

  @property
  def date(self):
    """
    Description:
    -----------
    Get the last update date of the package in NPM.

    Usage:
    pkg = PyNpm.Npm().package('pivottable')
    print(pkg.date)
    """
    return self._meta["package"]["date"]

  @property
  def keywords(self):
    """
    Description:
    -----------
    Get the list of keywords of the package in NPM.

    Usage:
    pkg = PyNpm.Npm().package('pivottable')
    print(pkg.keywords)
    """
    return self._meta["package"]["keywords"]

  @property
  def license(self):
    """
    Description:
    -----------
    Get the package license in NPM.

    Usage:

      pkg = PyNpm.Npm().package('chart.js')
      print(pkg.license)
    """
    headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    json_req = Request("%s/%s/%s/package.json" % (self.__HTTP_GITHUB_USER, self.repository.replace("https://github.com/", ""), self.version), method="GET", headers=headers)
    response = json.loads(urlopen(json_req).read())
    return response["license"]

  @property
  def description(self):
    """
    Description:
    -----------
    Get the package description in NPM.

    Usage:

    """
    return self._meta["package"]["description"]

  @property
  def scope(self):
    """
    Description:
    -----------
    Get the package scope in NPM.

    Usage:

    """
    return self._meta["package"]["scope"]

  @property
  def links(self):
    """
    Description:
    -----------
    Get the underlying package links.

    Usage:

    """
    return self._meta["package"]["links"]

  @property
  def json(self):
    """
    Description:
    -----------
    Get the full package details from the NPM website.

    Usage:

    """
    return self._meta

  @property
  def release(self):
    """
    Description:
    -----------
    Get the current package version date from the NPM website.

    Usage:

    """
    return self._meta['package']['version']

  @property
  def name(self):
    """
    Description:
    -----------
    Get the package name.

    Usage:

    """
    return self._meta['package']['name']

  def is_latest(self, verbose=True):
    """
    Description:
    -----------
    Check if the package version is the last one.

    Usage:


    Attributes:
    ----------
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    result = self.version_no == self.release
    if not result and verbose:
      scripts = self.has_cdnjs(self.release)
      is_valid = True
      for r in scripts:
        if r['code'] != 200:
          is_valid = False
      logging.warning("{} - Current: {}, Framework: {}, CDNJS: {}".format(self._alias, self.release, self.version_no, is_valid))
    return result

  def has_cdnjs(self, version=None):
    """
    Description:
    -----------
    Check if the CDNJS is available.

    Usage:

    Attributes:
    ----------
    :param version: String. Optional. The package version number (default the current release number from NPM).
    """
    version = version or self.version_no
    results = []
    for script in Imports.JS_IMPORTS[self._alias]['modules']:
      script["path"] = script["path"] % {"version": version}
      path = "%s/%s%s" % (script["cdnjs"], script["path"], script["script"])
      try:
        urlopen(path)
        results.append({"script": script["script"], 'code': 200})
      except HTTPError as e:
        results.append({"script": script["script"], 'code': e.code})

    for script in Imports.CSS_IMPORTS.get(self._alias, {}).get('modules', []):
      script["path"] = script["path"] % {"version": version}
      path = "%s/%s%s" % (script["cdnjs"], script["path"], script["script"])
      try:
        urlopen(path)
        results.append({"script": script["script"], 'code': 200})
      except HTTPError as e:
        results.append({"script": script["script"], 'code': e.code})
    return results

  @property
  def repository(self):
    """
    Description:
    -----------
    Get the package code repository path (usual Github path if available).
    If not available this will take the repository defined internally in the framework.

    Usage:

      pkg = PyNpm.Npm().package('pivottable')
      print(pkg.repository)
    """
    repo_path = self._meta['package']['links'].get('repository')
    if repo_path is None:
      repo_path = Imports.JS_IMPORTS[self._alias].get("repository")
    return repo_path

  @property
  def homepage(self):
    """
    Description:
    -----------
    Get the package homepage from the NPM definition.

    Usage:

      pkg = PyNpm.Npm().package('bootstrap')
      print(pkg.homepage)
    """
    return self._meta['package']['links']['homepage']

  def info(self, version=None):
    """
    Description:
    -----------
    Get the NPM package details.

    Usage:

      pkg = PyNpm.Npm().package('bootstrap')
      print(pkg.info())

    Attributes:
    ----------
    :param version: String. Optional. The package version number (default the current release number from NPM).
    """
    if self._info is None:
      version = version or self.version_no
      headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
      request = Request("%s/%s/%s" % (self.__HTTP_NPM_REGISTERY, self._alias, version), method="GET", headers=headers)
      self._info = json.loads(urlopen(request).read())
    return self._info

  @property
  def dependencies(self):
    """
    Description:
    -----------
    Get the package dependency packages.

    Usage:

    """
    info = self.info()
    results = {}
    for dep in ["peerDependencies", "dependencies"]:
      results.update(info.get(dep, {}))
    return results

  @property
  def version_no(self):
    """
    Description:
    -----------
    Get the package version number.

    Usage:

    """
    v = Imports.JS_IMPORTS[self._alias]['modules'][0].get("version", Imports.JS_IMPORTS[self._alias].get('version', self.release))
    return v

  @property
  def version(self):
    """
    Description:
    -----------
    Get the package version tag (it is either the version number of the version number prefixed with v).

    Usage:

    """
    prefix = Imports.JS_IMPORTS[self._alias].get("v_prefix")
    if prefix is not None:
      return "%s%s" % (prefix, self.version_no)

    return self.version_no

  @property
  def author_name(self):
    """
    Description:
    -----------
    Get the package author name defined in NPM.

    Usage:

        pkg = PyNpm.Npm().package('bootstrap')
        print(pkg.author_name)
    """
    infos = self.info()
    return infos['author']['name']

  @property
  def author_mail(self):
    """
    Description:
    -----------
    Get the email address of the package author from NPM info.

    Usage:

        pkg = PyNpm.Npm().package('bootstrap')
        print(pkg.author_mail)
    """
    infos = self.info()
    return infos['_npmUser']['email']

  def scripts(self):
    """
    Description:
    -----------
    Get the list of script used from this package in the framework.

    The framework is not using all the modules like other JavaScript framework would do.
    This framework will only import directly from a pure vanilla JavaScript implementation the various modules mandatory
    to benefit from those external packages.

    Usage:

      pkg = PyNpm.Npm().package('bootstrap')
      print(pkg.scripts())
    """
    results = []
    for script_type in [Imports.CSS_IMPORTS, Imports.JS_IMPORTS]:
      for script in script_type.get(self._alias, {}).get('modules', []):
        script["path"] = script["path"] % {"version": self.version_no}
        results.append("%s/%s%s" % (script["cdnjs"], script["path"], script["script"]))
    return results

  def get_files(self, version=None, out_path=None, update=True, verbose=True):
    """
    Description:
    -----------
    Get all the files defined from the package.json files to setup correctly the package from a nodeJs server.

    The framework will use this setup in order to ease the transition and compatibility with existing popular framework.

    Usage:


    Attributes:
    ----------
    :param version: String. Optional. The package version number (default the current release number from NPM).
    :param out_path: String. Optional. The destination path for the scripts (example the Nodejs modules path).
    :param update: Boolean. Optional. A flag to specify if the files need to be updated again.
    :param verbose: Boolean. Optional. Display warning message. Default True.
    """
    headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    json_req = Request("%s/%s/%s/package.json" % (self.__HTTP_GITHUB_USER, self.repository.replace("https://github.com/", ""), version or self.version), method="GET", headers=headers)
    try:
      response = json.loads(urlopen(json_req).read())
    except Exception as err:
      logging.warning("{} - Error getting files from {}/{}/{}/package.json".format(self._alias, self.__HTTP_GITHUB_USER, self.repository.replace("https://github.com/", ""), version or self.version))
      return None

    if "files" in response:
      regs = [re.compile(expr.replace("*", "(.*)")) for expr in response["files"]]
    else:
      regs = [re.compile("dist/(.*)")]
    if "main" in response:
      regs.append(re.compile(response["main"].replace(".js", "(.*).js")))
    for t in self.tree()["tree"]:
      if t['type'] != "blob":
        continue

      folder_map = {"tabulator-tables": 'tabulator'}
      for reg_exp in regs:
        match_reg = reg_exp.match(t["path"])
        if match_reg is not None:
          if out_path is not None:
            json_req = Request("%s/%s/%s/%s" % (self.__HTTP_GITHUB_USER, self.repository.replace("https://github.com/", ""), version or self.version, t["path"]), method="GET", headers=headers)
            req = urlopen(json_req)
            if "/" in t['path']:
              folder_path = os.path.join(out_path, folder_map.get(self._alias, self._alias), *t['path'].split("/")[:-1])
            else:
              folder_path = os.path.join(out_path, folder_map.get(self._alias, self._alias))
            if not os.path.exists(folder_path):
              os.makedirs(folder_path)
            out_file = os.path.join(folder_path, t['path'].split("/")[-1])
            if os.path.exists(out_file):
              if update:
                json_config = req.read().decode(req.info().get_content_charset())
                with open(out_file, "w", encoding="utf-8") as f:
                  f.write(json_config)
              else:
                if verbose:
                  logging.warning("{} - {} File already available".format(self._alias, t['path'].split("/")[-1]))
            else:
              json_config = req.read().decode(req.info().get_content_charset())
              with open(out_file, "w", encoding="utf-8") as f:
                f.write(json_config)
    return regs

  def tree(self, version=None):
    """
    Description:
    -----------
    Get the Github code structure. Get all the files and folder structure from the repository.

    Usage:

    Attributes:
    ----------
    :param version: String. Optional. The package version number (default the current release number from NPM).
    """
    if self._tree is None:
      version = version or self.version
      try:
        with urlopen('%s/repos/%s/git/trees/%s?recursive=1' % (self.__HTTP_GITHUB, self.repository.replace("https://github.com/", ""), version)) as response:
          self._tree = json.loads(response.read())
      except:
        logging.warning('Error get repo: %s/repos/%s/git/trees/%s?recursive=1' % (self.__HTTP_GITHUB, self.repository.replace("https://github.com/", ""), version))
        self._tree = {"tree": []}
    return self._tree


class Npm:

  __HTTP_NPM_REGISTRY = 'https://registry.npmjs.org'

  def __init__(self):
    pass

  def check(self, name, verbose=True):
    """
    Description:
    -----------
    Compare the current package version defined in the framework with the one in NPM.

    This shortcut will use the underlying is_latest package function.

    Usage:
    result = PyNpm.Npm().check('pivottable')

    Attributes:
    ----------
    :param name: String. The package alias name in NPM.
    :param verbose: Boolean. Optional. Display warning message. Default True.
    """
    pkg = self.package(name)
    if pkg is not None:
      return pkg.is_latest()

    elif verbose:
      logging.warning("{} - Missing reference".format(name))

  def meta(self, name, indent=4):
    """
    Description:
    -----------
    Get all the meta information related to the package.
    This will use json.dumps to display the output Json with all the details.

    Usage:

    Attributes:
    ----------
    :param name: String. The package alias name in NPM.
    :param indent: Integer. optional. The indent lenght.
    """
    pkg = self.package(name)
    meta = pkg._meta
    meta['info'] = pkg._info
    return json.dumps(meta, indent=indent)

  def version(self, name):
    """
    Description:
    -----------
    Get the latest version name from the npm registry.

    Usage:
    print(PyNpm.Npm().version('chart.js'))

    Attributes:
    ----------
    :param name: String. The package alias name in NPM.
    """
    headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    request = Request("%s/-/package/%s/dist-tags" % (self.__HTTP_NPM_REGISTRY, name), method="GET", headers=headers)
    return json.loads(urlopen(request).read())['latest']

  def all(self, verbose=True):
    """
    Description:
    -----------
    Check the version of all the packages currently defined in the framework.

    Usage:

    Attributes:
    ----------
    :param verbose: Boolean. Optional. Display warning message. Default True.
    """
    return {js: self.check(js, verbose) for js, js_details in Imports.JS_IMPORTS.items()}

  def search_url(self, name):
    """
    Description:
    -----------
    Return the search url for the package.

    Usage:

    Attributes:
    ----------
    :param name: String. The package alias name in NPM.
    """
    return "%s/-/v1/search?text=%s" % (self.__HTTP_NPM_REGISTRY, name)

  def package(self, name):
    """
    Description:
    -----------

    Usage:

    Attributes:
    ----------
    :param name: String. The package alias name in NPM.
    """
    headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    request = Request(self.search_url(name), method="GET", headers=headers)
    mapped_package_alias = {"sortablejs": 'sortablejs-rc'}
    for pkg in json.loads(urlopen(request).read())["objects"]:
      if pkg['package']["name"] == mapped_package_alias.get(name, name):
        return NpmRegistery(pkg, name)

  def search(self, name):
    """
    Description:
    -----------

    Usage:

    Attributes:
    ----------
    :param name: String. The package alias name in NPM.
    """
    headers = {"Content-Type": 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive'}
    request = Request(self.search_url(name), method="GET", headers=headers)
    packages = []
    for pkg in json.loads(urlopen(request).read())["objects"]:
      packages.append({"name": pkg['package']["name"], 'score': pkg['score'], 'searchScore': pkg['searchScore']})
    return packages


class Packages:

  @classmethod
  def descriptions(cls, verbose=True):
    """
    Description:
    -----------
    Get all the packages and the short description from NPM.

    Usage:

    Attributes:
    ----------
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    npm = Npm()
    results = {}
    for js, js_details in Imports.JS_IMPORTS.items():
      pkg = npm.package(js)
      if pkg is not None:
        results[js] = pkg.description
      elif verbose:
        logging.warning("{} - Missing reference".format(js))
    return results

  @classmethod
  def versions(cls, verbose=True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    npm = Npm()
    results = {}
    for js, js_details in Imports.JS_IMPORTS.items():
      pkg = npm.package(js)

  @classmethod
  def repositories(cls, verbose=True):
    """
    Description:
    -----------
    Get the repositories used to retrieve the external packages.

    This is a collaborative framework so do not hesitate to contact the author of those packages with ideas
    or even things to fix. It is important to encourage this open source community and to be part of modules
    improvements.

    Usage:

      repos = PyNpm.Packages.repositories()

    Attributes:
    ----------
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    npm = Npm()
    results = {}
    for js, js_details in Imports.JS_IMPORTS.items():
      pkg = npm.package(js)
      if pkg is not None:
        if pkg.repository is not None:
          results[js] = pkg.repository
        else:
          logging.warning("{} - Missing repository".format(js))
      elif verbose:
        logging.warning("{} - Missing reference".format(js))
    return results


def download(modules_path, update=False, verbose=True, packages=None, page=None):
  """
  Description:
  -----------

  Usage:

  Attributes:
  ----------
  :param modules_path: String. The output path for the modules.
  :param update: Boolean, Optional. Flag to specify if the files need to be uploaded again.
  :param verbose: Boolean. Optional. Display version details (default True).
  :param packages: List. Optional. A list of packages to download.
  :param page: Page. optional. Allow to filter on the required modules.
  """
  npm = Npm()
  results = {}
  if page is not None:
    packages = page.imports().requirements
  if packages is None:
    packages = Imports.JS_IMPORTS.keys()
  for pkg_alias in packages:
    pkg = npm.package(pkg_alias)
    if pkg is not None:
      pkg.get_files(out_path=modules_path, update=update, verbose=verbose)
    else:
      logging.warning("{} - Missing reference".format(pkg_alias))
  return results


def install(packages, path, node_server=False, update=False, verbose=True):
  """
  Description:
  ------------
  Install files using the npm structure is compatible.
  This will allow to run the script totally locally (without dependency on internet).

  Usage:
  -----

    PyNpm.install(['bootstrap'], r"C:\tmps\packages", update=True)


  Attributes:
  ----------
  :param packages: List. All the packages to be added to the install
  :param path: String. Optional. The install path (if node server, the folder root for /node_modules
  :param node_server: Boolean. Optional. Specify if npm from NodeJs must be used to install the package
  :param update: Boolean. Optional. Specify is the version of the package needs to be updated
  :param verbose: Boolean. Optional. Display version details (default True).
  """
  if node_server:
    if not isinstance(packages, list):
      packages = [packages]
    if update:
      subprocess.run('npm update %s' % " ".join(packages), shell=True, cwd=path)
    else:
      to_be_installed = []
      for p in packages:
        package_path = os.path.join(path, 'node_modules', p)
        if not os.path.exists(package_path):
          to_be_installed.append(p)
      if to_be_installed:
        subprocess.run('npm install %s' % " ".join(to_be_installed), shell=True, cwd=path)
        if verbose:
          logging.warning(" PYK_NPM >> All packages installed [%s]" % " ".join(to_be_installed))
      elif verbose:
        logging.warning(" PYK_NPM >> packages already installed")
  else:
    if verbose:
      if not path.endswith("node_modules"):
        logging.warning("NodeJs is using a node_modules folder.")

    for p in packages:
      if not os.path.exists(os.path.join(path, p)) or update:
        for category in [Imports.JS_IMPORTS, Imports.CSS_IMPORTS]:
          for mod in category.get(p, {}).get('modules', []):
            request = Request(Imports.script_cdnjs_path(p, mod))
            response = urlopen(request).read()
            script_path = Imports.script_npm_path(p, mod, path)
            mod_path, script = os.path.split(script_path)
            if not os.path.exists(mod_path):
              os.makedirs(mod_path)
            with open(script_path, "wb") as f:
              f.write(response)
          # Add extra ressources required by the package.
          for mod in category.get(p, {}).get('assets', []):
            request = Request(Imports.script_cdnjs_path(p, mod))
            response = urlopen(request).read()
            script_path = Imports.script_npm_path(p, mod, path)
            mod_path, script = os.path.split(script_path)
            if not os.path.exists(mod_path):
              os.makedirs(mod_path)
            with open(script_path, "wb") as f:
              f.write(response)

