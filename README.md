Selenium Python
===============

Example Python project to start using Selenium WebDriver

Requirements
------------

Python 2.7.4 (http://www.python.org)

distribute 0.6.36 (https://pypi.python.org/pypi/distribute)

pip 1.3.1 (https://pypi.python.org/pypi/pip)

Installation
------------

Configure a virtual environment with the required packages:

```
make venv
```

or 

```
virtualenv ENV
source ENV/bin/activate
pip install --upgrade -r requirements.txt
```

The following packages will be installed:
  * selenium-tid-python (https://pdihub.hi.inet/QA/selenium-tid-python)
  * selenium (http://docs.seleniumhq.org/)
  * nose (https://pypi.python.org/pypi/nose/)

Running tests
-------------

Run all tests with:

```
make test
```

or 

```
nosetests tests
```

Run a singular test with:

```
nosetests tests.test_register_user
```

Running examples
----------------

Run all example tests with:

```
make example
```

Android examples require Appium and Android Emulator

Browser configuration
---------------------

Chrome: download driver from http://code.google.com/p/chromedriver/downloads/list

Explorer: download driver from http://code.google.com/p/selenium/downloads/list

PhantomJS: download driver from http://phantomjs.org/download.html
