# -*- coding: utf-8 -*-

u"""
(c) Copyright 2015 Telefónica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefónica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefónica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
"""

import os

from seleniumtid import test_cases


class SeleniumTestCase(test_cases.SeleniumTestCase):
    """Test Case base class for Selenium tests"""

    def setUp(self):
        os.environ['Files_properties'] = '{};{}'.format(get_config_file_path('properties.cfg'),
                                                        get_config_file_path('local-properties.cfg'))
        os.environ['Files_logging'] = get_config_file_path('logging.conf')
        os.environ['Files_log_filename'] = os.path.join(get_root_path(), 'selenium.log')
        os.environ['Files_output_path'] = os.path.join(get_root_path(), 'dist')
        super(SeleniumTestCase, self).setUp()


def get_root_path():
    """Returns absolute path of the project root folder

    :returns: root folder path
    """
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_config_file_path(filename):
    """Returns absolute path of a configuration file

    :param filename: config file name
    :returns: config file path
    """
    return os.path.join(get_root_path(), 'conf', filename)
