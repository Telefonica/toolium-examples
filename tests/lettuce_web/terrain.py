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

import os

from lettuce import after, before, world

from toolium.config_files import ConfigFiles
from toolium.lettuce.terrain import (setup_driver as toolium_setup_driver, teardown_driver as toolium_teardown_driver,
                                     teardown_driver_all as toolium_teardown_driver_all)


@before.each_scenario
def setup_driver(scenario):
    """Scenario initialization

    :param scenario: running scenario
    """
    config_files = ConfigFiles()
    config_files.set_config_directory(os.path.join(get_root_path(), 'conf'))
    config_files.set_output_directory(os.path.join(get_root_path(), 'output'))
    config_files.set_config_properties_filenames('properties.cfg', 'local-properties.cfg')
    world.config_files = config_files
    toolium_setup_driver(scenario)


@after.each_scenario
def teardown_driver(scenario):
    """Clean method that will be executed after each scenario

    :param scenario: running scenario
    """
    toolium_teardown_driver(scenario)


@after.all
def teardown_driver_all(total):
    """Clean method that will be executed after all features are finished

    :param total: results of executed features
    """
    toolium_teardown_driver_all(total)


def get_root_path():
    """Returns absolute path of the project root folder

    :returns: root folder path
    """
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
