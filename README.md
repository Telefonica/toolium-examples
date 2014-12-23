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
  * seleniumtid (https://pdihub.hi.inet/QA/selenium-tid-python)
  * requests (http://docs.python-requests.org)
  * selenium (http://docs.seleniumhq.org/)
  * Appium-Python-Client (https://github.com/appium/python-client)
  * nose (https://pypi.python.org/pypi/nose/)
  * lettuce (http://lettuce.it) -> not installed by default, see requirements.txt

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

or

```
nosetests examples
```

The Android examples require that Appium Server and Android Emulator are started at localhost

Running lettuce examples
------------------------

Run lettuce example tests with:

```
lettuce examples
```

Browser configuration
---------------------

Chrome: download driver from http://code.google.com/p/chromedriver/downloads/list

Explorer: download driver from http://code.google.com/p/selenium/downloads/list

PhantomJS: download driver from http://phantomjs.org/download.html
