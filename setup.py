
from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='helloworld',
  version='0.0.1',
  description='Say hello!',
  py_modules=["helloworld"],
  package_dir={'': 'src'},
  classifiers=[
    "Programming Langauge :: Python :: 3",
    "Programming Langauge :: Python :: 3.6",
    "Programming Langauge :: Python :: 3.7",
    "License :: OSI Approved :: MIT ",
    "Operationing System :: OS Independent",
  ],
  long_description=long_description,
  long_description_content_type="text/markdown",
  install_requires = [
    
  ],
  extras_require = {
    "dev": [
      "pytest>=3.7",
      "check-manifest",
    ],
  },
  entry_points = {
    "console_scripts" :[
      "helloworld = helloworld:say_hello",
    ]
  },
  url="https://github.com/steve1281/helloworld_package",
  author="Steven V Falcigno",
  author_email="steve1281@hotmail.com",
)

