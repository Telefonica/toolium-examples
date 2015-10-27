Toolium template
================

Base project to start using toolium for your testing automation projects

Requirements
------------

Python 2.7.10 (http://www.python.org)

Installation
------------

Configure a virtual environment with the required packages:

::

    virtualenv ENV
    source ENV/bin/activate
    pip install -r requirements.txt

The following packages will be installed:

- toolium (https://github.com/Telefonica/toolium)
- requests (http://docs.python-requests.org)
- selenium (http://docs.seleniumhq.org/)
- Appium-Python-Client (https://github.com/appium/python-client)
- nose (https://pypi.python.org/pypi/nose/)
- lettuce (http://lettuce.it) *not installed by default, see requirements.txt*

Running tests
-------------

Run all tests with:
::

    nosetests tests

Run a singular test with:
::

    nosetests tests.test_register_user

Browser configuration
---------------------

Configure browser property in [Browser] section of properties.cfg file

Valid values are: firefox, chrome, iexplore, edge, safari, opera, phantomjs,
iphone, android
::

    browser: firefox

Firefox:

- No extra configuration is needed

Chrome:

- Download chromedriver\_*.zip from
  http://chromedriver.storage.googleapis.com/index.html
- Unzip file and save the executable in a local folder
- Configure driver path in [Browser] section of properties.cfg file
::

    chromedriver_path: C:\Drivers\chromedriver.exe

Explorer:

- Download IEDriverServer\_Win32\_*.zip from
  http://selenium-release.storage.googleapis.com/index.html
- Use always Win32 version, because x64 version is very slow
- Unzip file and save the executable in a local folder
- Configure driver path in [Browser] section of properties.cfg file
::

    explorerdriver_path: C:\Drivers\IEDriverServer.exe

Edge:

- Download MicrosoftWebDriver.msi from
  https://www.microsoft.com/en-us/download/details.aspx?id=48212
- Install MicrosoftWebDriver.msi
- Configure driver path in [Browser] section of properties.cfg file
::

    edgedriver_path: C:\Drivers\MicrosoftWebDriver.exe

PhantomJS:

- Download phantomjs-*.zip from http://phantomjs.org/download.html
- Unzip file and save the executable in a local folder
- Configure driver path in [Browser] section of properties.cfg file
::

    phantomdriver_path: C:\Drivers\phantomjs.exe
