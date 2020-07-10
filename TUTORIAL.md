# Packages in Python and PyPI 
Based on link: https://www.youtube.com/watch?v=GIF3LaRqgXo

## Some setup notes
```
You will want to git init 
You will want to virtualenv env  (or a python3 -m venv env )
```

## Make a package

```
Create example code src/helloworld.py

def say_hello(name=None):
  if name is None:
    return "Hello, World!"
  else:
    return f"Hello, {name}!"

Add a ./setup.py:

from setuptools import setup

setup(
  name='helloworld',
  version='0.0.1',
  description='Say hello!',
  py_modules=["helloworld"],
  package_dir={'': 'src'},
)

Notes:
  name : this is what you pip install
  version: 0.0.x implies unstable
  py_modules: list of modules imported

Gives us:

setup.py
src
 |--- helloworld.py

```

## Build the package
```
$ pip install wheel
$ python setup.py bdist_wheel

Note that: copying src/helloworld.py --> build/lib

It will create dist/helloworld-0.0.1-py3-non-any.whl

Resulting structure:

build
 |-- bdist_macosx-10.11-x86_64   <-- YMMV
 |-- lib
 |    |-- helloworld.py
 |
 |-- dist
 |    |-- helloworld-0.0.1-py3-none-any.whl
 | 
 |-- setup.py
 |-- src
      |-- helloworld.egg-info
      |    |-- dependency_links.txt
      |    |-- PKG-INFO
      |    |-- SOURCES.txt
      |    |-- top_level.txt
      |
      |-- helloworld.py


Notes:
  Ignore this:  bdist_macosx-10.11-x86_64
```

## Install it locally
```
$ pip install -e .

Note: -e essentially links to code you are working on
      run this whenever you change setup.py

```

## Manually testing 
```
$ python
>>> from helloworld import say_hello

>>> say_hello()
'Hello, World!'

>>> say_hello("Everybody")
'Hello, Everybody!'

Note: this is a working package
```

## Housekeeping
```
Need a .gitignore ; can use https://www.toptal.com/developers/gitignore
Need a LICENSE.txt, https://choosealicense.com/
Need to add some classifiers to setup.py ; see: https://pypi.org/classifiers for list, apply the usefull ones:

setup(
...
classifiers=[
    "Programming Langauge :: Python :: 3",
    "Programming Langauge :: Python :: 3.6",
    "Programming Langauge :: Python :: 3.7",
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    "Operationing System :: OS Independent",
  ],
)

Some documentation; either ReStructedText .rst or MarkDown .md
 .rst - Pythonic, Powerful, Can use Sphinx
 .md - more widespread, simpler, can use MkDocs


Create a README.md file.

  Hello World
  
  This is an example project demonstrating how to publish a python module to PyPI

  ...
  ## Installation
  Run the following command to install:
  
    pip install helloworld
  
  ## Usage
  
  from helloworld import say_hello
  say_hello()
  say_hello("Everybody")

```

### Add to setup.py

```
from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
...
  long_description=long_description,
  long_description_content_type="text/markdown",
)

```

### Add dependencies (if needed, example):
```
setup(
  ...
  install_requires = [
      "blessings ~= 1.7",
  ],
)

```
### Since changed setup.py, retest:
```
$ pip install -e .

```

#### testing with pytest
```
First, lets add dev dependencies to setup.py

setup(
  ...
  extras_require = {
    "dev": [
      "pytest>=3.7",
    ],
  },
)

If you have a setup.py, you don't really need a requirements.txt anymore.

Update the README.md

For developers...

To install helloworld, along with the tools you need to develop and run tests, run the following in your virtualenv:
  $ pip install -e .[dev]

Difference is, install_requires should be for production, least specific versions.
extras_require is for optional for dev/testing - make it more specific.

what about requirements.txt - thats for specific installations on production servers with specific versions.

So rerun:
  $ pip install -e .[dev]

Ok, finally can add some tests:

test_helloworld.py

from helloworld import say_hello

def test_helloworld_no_params():
  assert say_hello() == "Hello, World!"

def test_helloworld_with_param():
  assert say_hello("Everyone") == "Hello, Everyone!"

And test:

$ pytest
```

### Source distribution
```
$ python setup.py sdist
some errors/warnings:
warning: check: missing required meta-data: url
warning: check: missing required meta-data: either (author and author_email) or (maintainer and maintainer_email) must be supplied
...
Creating tar archive

Add in:

setup(
  ...
  url="https://github.com/blah/blah",
  author="First Last",
  author_email="first.last@email_provider.com",
)

Re-run tests
Re-run python setup.py sdist
Have a look at what is inside the tar:
$ tar tzf dist/helloworld-0.0.1.tar.gz

By default, its not including LICENSE.txt or test_helloworld.py

In order to include these missing files, a Manifest is needed.
Use tool:

$ pip install check-manifest  # add to dev deps ?
$ check-manifest --create
$ git add MANIFEST.in

Have a look at it.

And rebuild sdist again.
```

NOTE: from this point on I have not tested.

### and publish:
```
$ python setup.py bdist_wheel sdist
$ ls dist/

$ pip install twine

$ twine upload dist/<star>

```

### Productionize it

#### Testing with tox

```
tox.ini

[tox]
envlist = py36,py37

[testenv]
deps = pytest
commands = pytest


$ pip install tox   # add to dev deps?
$ tox
...

:)

```

### Final thoughts
```
$ pip install cookiecutter
$ cookiecutter gh:ionelmc/cookiecutter-pylibrary
... asks you questions ...
... etc etc ...
```

