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

Running web tests
~~~~~~~~~~~~~~~~~

By default, web tests are configured to run in chrome locally, so chrome must be installed in your machine.
Selenium 4 will download chrome driver automatically when tests are executed.

**/web**

To run web tests with nose2, excluding skipped tests:

.. code:: console

    $ nose2 web

**/web_pytest**

To run web tests with pytest:

.. code:: console

    $ cd web_pytest
    $ python -m pytest

**/web_behave**

To run behave web tests:

.. code:: console

    $ behave web_behave

Running mobile tests
~~~~~~~~~~~~~~~~~~~

By default, mobile tests are configured to run against a local Appium server, so
`Appium <https://appium.github.io/appium/docs/en/2.0>`_ must be installed, configured and started before
executing tests.

**/android**

Android tests need an Android Emulator or a plugged Android device.

To run Android tests with nose2:

.. code:: console

    $ nose2 android

**/ios**

iOS tests are configured to run on iOS Simulator.

To run iOS tests with nose2:

.. code:: console

    $ nose2 ios

**/android_behave**

To run behave Android tests:

.. code:: console

    $ behave android_behave

**/ios_behave**

To run behave iOS tests:

.. code:: console

    $ behave ios_behave

**/mobile_behave**

This folder contains a behave test that could be executed either in Android or iOS depending on *Config_environment*
behave user property.

To run behave test in Android:

.. code:: console

    $ behave mobile_behave -D Config_environment=android

To run behave test in iOS:

.. code:: console

    $ behave mobile_behave -D Config_environment=ios

**/web_behave**

The same `/web_behave` tests already run in a browser could also be executed in an Android or iOS
device using different configuration files per environment.

To run behave web tests in an Android device:

.. code:: console

    $ behave web_behave/features/login.feature -D Config_environment=android

To run behave web tests in an iOS device:

.. code:: console

    $ behave web_behave/features/login.feature -D Config_environment=ios

Contributing
------------

If you want to collaborate in Toolium-examples development, feel free of `forking it <https://github.com/Telefonica/toolium-examples>`_
and asking for a pull request.

Finally, before accepting your contribution, we need you to sign our
`Contributor License Agreement <https://raw.githubusercontent.com/telefonicaid/Licensing/master/ContributionPolicy.txt>`_
and send it to ruben.gonzalezalonso@telefonica.com.
