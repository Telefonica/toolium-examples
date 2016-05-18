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

from toolium.behave.environment import (before_all as toolium_before_all, before_scenario as toolium_before_scenario,
                                        after_scenario as toolium_after_scenario, after_all as toolium_after_all)


def before_all(context):
    """Initialization method that will be executed before the test execution

    :param context: behave context
    """
    toolium_before_all(context)


def before_scenario(context, scenario):
    """Scenario initialization

    :param context: behave context
    :param scenario: running scenario
    """
    toolium_before_scenario(context, scenario)


def after_scenario(context, scenario):
    """Clean method that will be executed after each scenario

    :param context: behave context
    :param scenario: running scenario
    """
    toolium_after_scenario(context, scenario)


def after_all(context):
    """Clean method that will be executed after all features are finished

    :param context: behave context
    """
    toolium_after_all(context)
