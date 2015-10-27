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

from toolium import test_cases


class SeleniumTestCase(test_cases.SeleniumTestCase):
    """Test Case base class for Selenium tests"""

    def setUp(self):
        self.set_config_directory(os.path.join(get_root_path(), 'conf'))
        self.set_output_directory(os.path.join(get_root_path(), 'output'))
        self.set_config_properties_filenames('properties.cfg', 'local-properties.cfg')
        super(SeleniumTestCase, self).setUp()


def get_root_path():
    """Returns absolute path of the project root folder

    :returns: root folder path
    """
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
