# Hello World

This is an example project demonstrating how to publish a python module to PyPI

## Installation
Run the following command to install:
```
You should probably:
$ virtualenv env && source ./env/bin/activate
and then
$ pip install helloworld
```

## Usage
```
from helloworld import say_hello
say_hello()
say_hello("Everybody")
```

## For developers

To install helloworld, along with the tools you need to develop and run tests, run the following in your virtualenv:
```
$ pip install -e .[dev]
```

