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
    $ cd toolium-examples
    $ pip install -r requirements.txt

Running Tests
-------------

Each folder contains a sample project to test web, Android or iOS applications using nose, behave or lettuce to execute
them.

By default, web tests are configured to run in firefox locally, so firefox must be installed in your machine.

And mobile tests are configured to run against a local Appium server, so
`Appium <http://appium.io/slate/en/master/?ruby#setting-up-appium>`_ must be installed, configured and started before
executing tests. iOS tests are configured to run on iOS Simulator and Android tests need an Android Emulator or a
plugged Android device.

**web**

To run web tests with nose:

.. code:: console

    $ nosetests web

**android**

To run Android tests with nose:

.. code:: console

    $ nosetests android

**ios**

To run iOS tests with nose:

.. code:: console

    $ nosetests ios

**web_behave**

To run behave web tests:

.. code:: console

    $ behave web_behave

The same web tests could be executed in an Android or iOS device using different configuration files per environment.
To run behave web tests in an Android device:

.. code:: console

    $ behave web_behave/features/login.feature -D env=android

To run behave web tests in an iOS device:

.. code:: console

    $ behave web_behave/features/login.feature -D env=ios

**android_behave**

To run behave Android tests:

.. code:: console

    $ behave android_behave

**ios_behave**

To run behave iOS tests:

.. code:: console

    $ behave ios_behave

**mobile_behave**

This folder contains a behave test that could be executed either in Android or iOS depending on *env* behave user
property.

To run behave test in Android:

.. code:: console

    $ behave mobile_behave -D env=android

To run behave test in iOS:

.. code:: console

    $ behave mobile_behave -D env=ios

**web_lettuce**

To run lettuce web tests:

.. code:: console

    $ lettuce web_lettuce

Note: lettuce works only in Python 2
