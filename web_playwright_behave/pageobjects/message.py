# -*- coding: utf-8 -*-
u"""
Copyright 2024 Telefónica Innovación Digital, S.L.
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

from toolium.pageelements import Text
from toolium.pageobjects.playwright_page_object import PlaywrightPageObject


class MessagePageObject(PlaywrightPageObject):
    def init_page_elements(self):
        self.message = Text(By.ID, 'flash')

    async def get_message(self):
        """ Get first line of actual message

        :returns: str with message
        """
        # TODO: update toolium page objects to use playwright
        text = await self.page.locator('#flash').text_content()
        return text.splitlines()[1]
        # return self.message.wait_until_visible(2).text.splitlines()[0]