# -*- coding: utf-8 -*-
u"""
Copyright 2016 Telefónica Investigación y Desarrollo, S.A.U.
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

from selenium.webdriver.common.by import By

from toolium.pageelements import *
from toolium.pageobjects.page_object import PageObject


class Row(Group):
    def init_page_elements(self):
        self.last_name = Text(By.XPATH, './td[1]')
        self.first_name = Text(By.XPATH, './td[2]')
        self.email = Text(By.XPATH, './td[3]')
        self.due = Text(By.XPATH, './td[4]')
        self.web = Text(By.XPATH, './td[5]')
        self.edit = Link(By.XPATH, './/a[1]')
        self.delete = Link(By.XPATH, './/a[2]')


class Table(Group):
    def init_page_elements(self):
        self.rows = PageElements(By.XPATH, './tbody/tr', page_element_class=Row)


class TablesPageObject(PageObject):
    def init_page_elements(self):
        self.table1 = Table(By.ID, 'table1')
        self.table2 = Table(By.ID, 'table2')
