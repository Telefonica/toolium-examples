Toolium Examples
================

Set of examples to learn how to use `Toolium <https://github.com/Telefonica/toolium>`_ to test web, Android or iOS
applications, in different scenarios.

Getting Started
---------------

Clone `toolium-examples <https://github.com/Telefonica/toolium-examples>`_ repository and install requirements. It's
highly recommendable to use a virtualenv.

.. code:: console

    $ git clone git@github.com:Telefonica/toolium-examples.git
    $ cd toolium-examples
    $ pip install -r requirements.txt

Running Tests
-------------

Each folder contains a sample project to test web, Android or iOS applications using nose2, behave or pytest to execute
them.

Running web tests using Selenium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, web tests are configured to run in chrome locally, so chrome must be installed in your machine.
Selenium 4 will download chrome driver automatically when tests are executed.

**/web_behave**

To run behave web tests:

.. code:: console

    $ behave web_behave

**/web_pytest**

To run web tests with pytest:

.. code:: console

    $ cd web_pytest
    $ python -m pytest

**/web_nose2**

To run web tests with nose2:

.. code:: console

    $ python -m nose2 web_nose2

These web tests can also be executed with pytest:

.. code:: console

    $ cd web_nose2
    $ python -m pytest

Running web tests using Playwright
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**/web_playwright**

To run playwright web tests:

.. code:: console

    $ cd web_playwright
    # Run playwright test integrated with pytest
    $ python -m pytest tests/test_web_playwright_pytest.py --headed --browser chromium
    # Run playwright test using sync library mode
    $ python -m pytest tests/test_web_playwright_library_sync.py --headed
    # Run playwright test using async library mode
    $ python tests/test_web_playwright_library_async.py

Running mobile tests
~~~~~~~~~~~~~~~~~~~~

By default, mobile tests are configured to run against a local Appium server, so
`Appium <https://appium.github.io/appium/docs/en/2.0>`_ must be installed, configured and started before
executing tests.

**/android_behave**

Android tests need an Android Emulator or a plugged Android device.

To run behave Android tests:

.. code:: console

    $ behave android_behave

**/ios_behave**

iOS tests are configured to run on iOS Simulator.

To run behave iOS tests:

.. code:: console

    $ behave ios_behave

**/mobile_behave**

This folder contains a behave test that could be executed either in Android or iOS depending on *TOOLIUM_CONFIG_ENVIRONMENT*
behave user property.

To run behave test in Android:

.. code:: console

    $ behave mobile_behave -D TOOLIUM_CONFIG_ENVIRONMENT=android

To run behave test in iOS:

.. code:: console

    $ behave mobile_behave -D TOOLIUM_CONFIG_ENVIRONMENT=ios

**/web_behave**

The same `/web_behave` tests already run in a browser could also be executed in an Android or iOS
device using different configuration files per environment.

To run behave web tests in an Android device:

.. code:: console

    $ behave web_behave/features/login.feature -D TOOLIUM_CONFIG_ENVIRONMENT=android

To run behave web tests in an iOS device:

.. code:: console

    $ behave web_behave/features/login.feature -D TOOLIUM_CONFIG_ENVIRONMENT=ios

**/android_nose2**

To run Android tests with nose2:

.. code:: console

    $ python -m nose2 android_nose2

**/ios_nose2**

To run iOS tests with nose2:

.. code:: console

    $ python -m nose2 ios_nose2

Contributing
------------

If you want to collaborate in Toolium-examples development, feel free of `forking it <https://github.com/Telefonica/toolium-examples>`_
and asking for a pull request.

Finally, before accepting your contribution, we need you to sign our
`Contributor License Agreement <https://raw.githubusercontent.com/telefonicaid/Licensing/master/ContributionPolicy.txt>`_
and send it to ruben.gonzalezalonso@telefonica.com.
