"""
packaging module to install: python.exe -m pip install --upgrade setuptools wheel
to create the tar.gz: python.exe setup.py sdist
to create the wheels: python.exe setup.py sdist bdist_wheel --universal
"""
import setuptools
import os


with open("README.md", "r") as fh:
    long_description = fh.read()


with open("epyk/_version.py", "w") as fp:
  fp.write("__version__ = '%s'" % os.environ["VERSION"])


def install_required():
  return [line for line in open('requirements.txt')]


def get_pkg_data() -> dict:
  """

  :return:
  """
  pkg_data = {
    'epyk': [
      os.path.join('static', 'images', '*'),
      os.path.join('static', 'images', 'logo', '*')
  ]}
  folders = set()
  for fd in os.walk(r"epyk\core\js\native"):
    if fd[2]:
      folders.add(os.path.join(fd[0].replace("epyk\\", ""), "*.js"))
  pkg_data['epyk'].extend(list(folders))
  return pkg_data


setuptools.setup(
    name="epyk",
    author="epykure",
    version=os.environ["VERSION"],
    author_email="smith.pyotr@gmail.com",
    description="A simple way to create rich interactive websites and dashboards compatible with modern web frameworks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epykure/epyk-ui",
    project_urls={
        "Documentation": "http://www.epyk.io",
        "Code": "https://github.com/epykure/epyk-ui",
        "Issue tracker": "https://github.com/epykure/epyk-ui/issues"
    },
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=install_required(),
    package_data=get_pkg_data(),
    entry_points={"console_scripts": [
      "epyk = epyk.core.cli.cli_export:main",   # For common quick page transformation
      "epyk_project = epyk.core.cli.cli_project:main",   # For project structure
      "epyk_npm = epyk.core.cli.cli_npm:main",   # For Import management
    ]},
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)