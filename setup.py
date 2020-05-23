"""
packaging module to install: python.exe -m pip install --upgrade setuptools wheel
to create the tar.gz: python.exe setup.py sdist
to create the weels: python.exe setup.py sdist bdist_wheel --universal
"""

import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def install_required():
  return [line for line in open('requirements.txt')]

setuptools.setup(
    name="epyk",
    author="epykure",
    version="1.0.10",
    author_email="smith.pyotr@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epykure/epyk-ui",
    project_urls={
        "Documentation": "http://www.epyk.io",
        "Code": "https://github.com/epykure/epyk-ui",
        "Issue tracker": "https://github.com/epykure/epyk-ui/issues"
    },
    packages=setuptools.find_packages(),
    install_requires=install_required(),
    package_data={'epyk': [os.path.join('static', 'images', '*'), os.path.join('static', 'images', 'logo', '*')]},
    entry_points={"console_scripts": ["epyk = epyk.core.cli.command_line_fncs:main"]},
    python_requires=">=2.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)