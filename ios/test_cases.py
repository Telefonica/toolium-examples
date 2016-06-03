# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from toolium import test_cases


class IosTestCase(test_cases.AppiumTestCase):
    """Test Case base class for iOS tests"""

    def setUp(self):
        self.config_files.set_config_properties_filenames('properties.cfg', 'ios-properties.cfg',
                                                          'local-ios-properties.cfg')
        super(IosTestCase, self).setUp()


class IosHybridTestCase(test_cases.AppiumTestCase):
    """Test Case base class for iOS tests (hybrid app)"""

    def setUp(self):
        self.config_files.set_config_properties_filenames('properties.cfg', 'ios-hybrid-properties.cfg',
                                                          'local-ios-properties.cfg')
        super(IosHybridTestCase, self).setUp()
