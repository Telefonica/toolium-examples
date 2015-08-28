Selenium Python
===============

Example python project to start using Selenium WebDriver for testing api, web and mobile applications 
using requests, selenium and appium tools

Requirements
------------

Python 2.7.10 (http://www.python.org)

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
easy_install pillow
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

Browser configuration
---------------------

Chrome: download driver from http://chromedriver.storage.googleapis.com/index.html

Explorer: download driver from http://selenium-release.storage.googleapis.com/index.html 

Edge: download driver from https://www.microsoft.com/en-us/download/details.aspx?id=48212

PhantomJS: download driver from http://phantomjs.org/download.html
