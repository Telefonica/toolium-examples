Toolium Examples
================

Set of examples to learn how to use `Toolium <https://github.com/Telefonica/toolium>`_ to test web, Android or iOS
applications, in different scenarios.

Getting Started
---------------

The requirements to install Toolium are `Python 2.7 or 3.3+ <http://www.python.org>`_ and
`pip <https://pypi.python.org/pypi/pip>`_. If you use Python 2.7.9+, you don't need to install pip separately.

Clone `toolium-examples <https://github.com/Telefonica/toolium-examples>`_ repository and install requirements. It's
highly recommendable to use a virtualenv.

.. code:: console

    $ git clone git@github.com:Telefonica/toolium-examples.git
    $ pip install -r requirements.txt

Running Tests
-------------

**Web**

By default, example tests are configured to run in firefox locally, so firefox must be installed in your machine.

To run web tests:

.. code:: console

    $ nosetests tests/web

To run a single test:

.. code:: console

    $ nosetests tests/web/test_web.py:Login.test_successful_login_logout

**Android or iOS**

`Appium <http://appium.io/slate/en/master/?ruby#setting-up-appium>`_ must be installed and configured before executing
Android or iOS tests.

To run Android tests, launch Appium server, connect an Android device (or create an Android Emulator) and execute:

.. code:: console

    $ nosetests tests/android

To run iOS tests on iOS Simulator, launch Appium server in a Mac OS X and execute:

.. code:: console

    $ nosetests tests/ios
