"""
packaging module to install: python.exe -m pip install --upgrade setuptools wheel
to create the tar.gz: python.exe setup.py sdist
to create the weels: python.exe setup.py sdist bdist_wheel --universal
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def install_required():
  return [line for line in open('requirements.txt')]

setuptools.setup(
    name="epyk",
    author="epykure",
    version="1.00.00",
    author_email="smith.pyotr@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epykure/epyk-ui",
    packages=setuptools.find_packages(),
    install_requires=install_required(),
    python_requires=">=2.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)